import pytest


@pytest.fixture
def association_counts():
    return {
        "items": [
            {
                "label": "Phenotype to Disease",
                "count": 3941,
                "category": "biolink:DiseaseToPhenotypicFeatureAssociation",
            },
            {"label": "Causal Gene", "count": 126, "category": "biolink:CausalGeneToDiseaseAssociation"},
            {"label": "Correlated Gene", "count": 146, "category": "biolink:CorrelatedGeneToDiseaseAssociation"},
            {"label": "Variant to Disease", "count": 1, "category": "biolink:VariantToDiseaseAssociation"},
            {"label": "Disease Model", "count": 243, "category": "biolink:GenotypeToDiseaseAssociation"},
        ]
    }
