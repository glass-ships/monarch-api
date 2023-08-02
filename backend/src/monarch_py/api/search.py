from typing import List, Union

from fastapi import APIRouter, Query  # , Depends
from monarch_py.api.config import solr
from monarch_py.datamodels.model import SearchResults

router = APIRouter(
    tags=["search"],
    responses={404: {"description": "Not Found"}},
)


@router.get("/search")
async def search(
    q: str = "*:*",
    category: Union[List[str], None] = Query(default=None),
    taxon: Union[List[str], None] = Query(default=None),
    offset: int = 0,
    limit: int = 20,
) -> SearchResults:
    """Search for entities by label, with optional filters

    Args:
        q (str, optional): TODO. Defaults to "*:*".
        category (str, optional): TODO. Defaults to None.
        taxon (str, optional): TODO. Defaults to None.
        offset (int, optional): Offset for pagination. Defaults to 0.
        limit (int, optional): Limit results. Defaults to 20.

    Returns:
        EntityResults
    """
    facet_fields = ["category", "in_taxon_label"]
    response = solr.search(
        q=q,
        category=category,
        in_taxon_label=taxon,
        facet_fields=facet_fields,
        offset=offset,
        limit=limit,
    )

    return response


@router.get("/autocomplete")
async def autocomplete(q: str) -> SearchResults:
    """Autocomplete for entities by label

    Args:
        q (str): Query string to autocomplete against

    Returns:
        SearchResults
    """
    response = solr.autocomplete(q=q)
    return response