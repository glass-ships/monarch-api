import pytest


@pytest.fixture
def histopheno():
    return {
        "id": "MONDO:0020121",
        "items": [
            {"label": "musculature", "count": 1751, "id": "HP:0003011"},
            {"label": "nervous_system", "count": 1118, "id": "HP:0000707"},
            {"label": "head_neck", "count": 574, "id": "HP:0000152"},
            {"label": "skeletal_system", "count": 504, "id": "HP:0000924"},
            {"label": "respiratory", "count": 318, "id": "HP:0002086"},
            {"label": "eye", "count": 276, "id": "HP:0000478"},
            {"label": "metabolism_homeostasis", "count": 219, "id": "HP:0001939"},
            {"label": "cardiovascular_system", "count": 192, "id": "HP:0001626"},
            {"label": "blood", "count": 185, "id": "HP:0001871"},
            {"label": "connective_tissue", "count": 165, "id": "HP:0003549"},
            {"label": "digestive_system", "count": 143, "id": "HP:0025031"},
            {"label": "integument", "count": 48, "id": "HP:0001574"},
            {"label": "genitourinary_system", "count": 43, "id": "HP:0000119"},
            {"label": "growth", "count": 33, "id": "HP:0001507"},
            {"label": "ear", "count": 27, "id": "HP:0000598"},
            {"label": "endocrine", "count": 25, "id": "HP:0000818"},
            {"label": "immune_system", "count": 21, "id": "HP:0002715"},
            {"label": "prenatal_or_birth", "count": 20, "id": "HP:0001197"},
            {"label": "neoplasm", "count": 7, "id": "HP:0002664"},
            {"label": "breast", "count": 1, "id": "HP:0000769"},
        ],
    }