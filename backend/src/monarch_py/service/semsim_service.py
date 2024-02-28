from typing import List, Any
import requests

from pydantic import BaseModel

from monarch_py.datamodels.model import TermSetPairwiseSimilarity, SemsimSearchResult
from monarch_py.interfaces.entity_interface import EntityInterface


class SemsimianService(BaseModel):
    """A class that makes HTTP requests to the semsimian_server."""
    semsim_server_port: int
    semsim_server_host: str
    entity_implementation: Any # TODO: should be EntityInterface

    def convert_tsps_data(self, data):
        """Convert to a format that can be coerced into a TermSetPairwiseSimilarity model

        FIXME: currently, the response returned from semsimian_server doesn't
        100% match the TermSetPairwiseSimilarity model, so we perform some
        transformations below. once it does, we can remove all the code below
        and just return TermSetPairwiseSimilarity(**data)
        """
        # remove these similarity maps and fold them into the _best_matches dicts
        object_best_matches_similarity_map = self._convert_nans(data.pop("object_best_matches_similarity_map"))
        subject_best_matches_similarity_map = self._convert_nans(data.pop("subject_best_matches_similarity_map"))
        converted_data = {
            **data,
            **{
                # flatten the nested termset dicts
                "subject_termset": {k: v for d in data["subject_termset"] for k, v in d.items()},
                "object_termset": {k: v for d in data["object_termset"] for k, v in d.items()},
                "subject_best_matches": {
                    k: {**v, "similarity": subject_best_matches_similarity_map[k]}
                    for k, v in data["subject_best_matches"].items()
                },
                "object_best_matches": {
                    k: {**v, "similarity": object_best_matches_similarity_map[k]}
                    for k, v in data["object_best_matches"].items()
                },
            },
        }
        return converted_data

    def compare(self, subjects: List[str], objects: List[str]):
        host = f"http://{self.semsim_server_host}:{self.semsim_server_port}"
        path = f"compare/{','.join(subjects)}/{','.join(objects)}"
        url = f"{host}/{path}"

        print(f"Fetching {url}...")
        response = requests.get(url=url)
        data = response.json()
        results = self.convert_tsps_data(data)
        return TermSetPairwiseSimilarity(**results)

    def multi_compare(self, subjects: List[str], object_sets: List[List[str]]) -> List[TermSetPairwiseSimilarity]:
        compare_results = [self.compare(subjects, object_set) for object_set in object_sets]
        # TODO: probably should be sorted
        return compare_results


    def search(self, termset: List[str], prefix: str, limit: int):
        host = f"http://{self.semsim_server_host}:{self.semsim_server_port}"
        path = f"search/{','.join(termset)}/{prefix}?limit={limit}"
        url = f"{host}/{path}"

        print(f"Fetching {url}...")
        response = requests.get(url=url)
        data = response.json()
        results = [
            SemsimSearchResult(
                subject=self.entity_implementation.get_entity(i[2], extra=False),
                score=i[0],
                similarity=self.convert_tsps_data(i[1])
            )
            for i in data
        ]

        return results

    @staticmethod
    def _convert_nans(input_dict, to_value=None):
        """
        Given an input dict of the form {<term>: {<field>: <value>, ...}}
        converts any <value> of 'NaN' to None.
        """
        for k, v in input_dict.items():
            for ik, iv in v.items():
                if iv == "NaN":
                    input_dict[k][ik] = None

        return input_dict