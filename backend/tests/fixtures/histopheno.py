import pytest


@pytest.fixture
def histopheno():
    return {
        "id": "MONDO:0020121",
        "items": [
            {"label": "musculature", "count": 1677, "id": "HP:0003011"},
            {"label": "nervous_system", "count": 1071, "id": "HP:0000707"},
            {"label": "head_neck", "count": 577, "id": "HP:0000152"},
            {"label": "skeletal_system", "count": 471, "id": "HP:0000924"},
            {"label": "eye", "count": 287, "id": "HP:0000478"},
            {"label": "metabolism_homeostasis", "count": 213, "id": "HP:0001939"},
            {"label": "cardiovascular_system", "count": 177, "id": "HP:0001626"},
            {"label": "blood", "count": 175, "id": "HP:0001871"},
            {"label": "connective_tissue", "count": 161, "id": "HP:0003549"},
            {"label": "respiratory", "count": 150, "id": "HP:0002086"},
            {"label": "neoplasm", "count": 148, "id": "HP:0002664"},
            {"label": "digestive_system", "count": 142, "id": "HP:0025031"},
            {"label": "integument", "count": 47, "id": "HP:0001574"},
            {"label": "genitourinary_system", "count": 44, "id": "HP:0000119"},
            {"label": "growth", "count": 32, "id": "HP:0001507"},
            {"label": "ear", "count": 28, "id": "HP:0000598"},
            {"label": "endocrine", "count": 25, "id": "HP:0000818"},
            {"label": "immune_system", "count": 22, "id": "HP:0002715"},
            {"label": "prenatal_or_birth", "count": 21, "id": "HP:0001197"},
            {"label": "breast", "count": 1, "id": "HP:0000769"},
        ],
    }
