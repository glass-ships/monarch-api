import pytest


@pytest.fixture
def association_counts():
    return {
        "items": [
            {"label": "Phenotypes", "count": 3932, "category": "biolink:DiseaseToPhenotypicFeatureAssociation"},
            {"label": "Causal Genes", "count": 126, "category": "biolink:CausalGeneToDiseaseAssociation"},
            {"label": "Correlated Genes", "count": 146, "category": "biolink:CorrelatedGeneToDiseaseAssociation"},
        ]
    }
