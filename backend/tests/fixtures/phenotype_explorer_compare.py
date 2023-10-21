import pytest


@pytest.fixture
def phenotype_explorer_compare():
    return {
        "subject_termset": {
            "MP:0002169": {"id": "MP:0002169", "label": "no abnormal phenotype detected (MPO)"},
            "MP:0010771": {"id": "MP:0010771", "label": "integument phenotype (MPO)"},
        },
        "object_termset": {"HP:0004325": {"id": "HP:0004325", "label": "Decreased body weight (HPO)"}},
        "subject_best_matches": {
            "MP:0002169": {
                "match_source": "MP:0002169",
                "match_source_label": "no abnormal phenotype detected (MPO)",
                "match_target": "HP:0004325",
                "match_target_label": "Decreased body weight (HPO)",
                "score": 1.5616002210519475,
                "match_subsumer": None,
                "match_subsumer_label": None,
                "similarity": {
                    "subject_id": "MP:0002169",
                    "subject_label": None,
                    "subject_source": None,
                    "object_id": "HP:0004325",
                    "object_label": None,
                    "object_source": None,
                    "ancestor_id": "UPHENO:0001003",
                    "ancestor_label": "",
                    "ancestor_source": None,
                    "object_information_content": None,
                    "subject_information_content": None,
                    "ancestor_information_content": 1.5616002210519475,
                    "jaccard_similarity": 0.16216216216216217,
                    "cosine_similarity": None,
                    "dice_similarity": None,
                    "phenodigm_score": 0.5032220864376823,
                },
            },
            "MP:0010771": {
                "match_source": "MP:0010771",
                "match_source_label": "integument phenotype (MPO)",
                "match_target": "HP:0004325",
                "match_target_label": "Decreased body weight (HPO)",
                "score": 2.2728188647181566,
                "match_subsumer": None,
                "match_subsumer_label": None,
                "similarity": {
                    "subject_id": "MP:0010771",
                    "subject_label": None,
                    "subject_source": None,
                    "object_id": "HP:0004325",
                    "object_label": None,
                    "object_source": None,
                    "ancestor_id": "UBERON:0000468",
                    "ancestor_label": "",
                    "ancestor_source": None,
                    "object_information_content": None,
                    "subject_information_content": None,
                    "ancestor_information_content": 2.2728188647181566,
                    "jaccard_similarity": 0.325,
                    "cosine_similarity": None,
                    "dice_similarity": None,
                    "phenodigm_score": 0.8594568814276845,
                },
            },
        },
        "object_best_matches": {
            "HP:0004325": {
                "match_source": "HP:0004325",
                "match_source_label": "Decreased body weight (HPO)",
                "match_target": "MP:0010771",
                "match_target_label": "integument phenotype (MPO)",
                "score": 2.2728188647181566,
                "match_subsumer": None,
                "match_subsumer_label": None,
                "similarity": {
                    "subject_id": "HP:0004325",
                    "subject_label": None,
                    "subject_source": None,
                    "object_id": "MP:0010771",
                    "object_label": None,
                    "object_source": None,
                    "ancestor_id": "UBERON:0000468",
                    "ancestor_label": "",
                    "ancestor_source": None,
                    "object_information_content": None,
                    "subject_information_content": None,
                    "ancestor_information_content": 2.2728188647181566,
                    "jaccard_similarity": 0.325,
                    "cosine_similarity": None,
                    "dice_similarity": None,
                    "phenodigm_score": 0.8594568814276845,
                },
            }
        },
        "average_score": 2.0950142038016044,
        "best_score": 2.2728188647181566,
        "metric": "ancestor_information_content",
    }
