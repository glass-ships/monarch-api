import pytest


@pytest.fixture
def associations_compact():
    return {
        "limit": 20,
        "offset": 0,
        "total": 4700,
        "items": [
            {
                "category": "biolink:Association",
                "subject": "MONDO:0030712",
                "subject_label": "oculopharyngodistal myopathy 4",
                "predicate": "biolink:subclass_of",
                "object": "MONDO:0025193",
                "object_label": "oculopharyngodistal myopathy",
                "negated": None,
            },
            {
                "category": "biolink:Association",
                "subject": "MONDO:0035432",
                "subject_label": "POMGNT2-related limb-girdle muscular dystrophy R24",
                "predicate": "biolink:subclass_of",
                "object": "MONDO:0016971",
                "object_label": "limb-girdle muscular dystrophy",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:26267",
                "subject_label": "POMK",
                "predicate": "biolink:causes",
                "object": "MONDO:0014101",
                "object_label": "muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type a, 12",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:10805",
                "subject_label": "SGCA",
                "predicate": "biolink:causes",
                "object": "MONDO:0011968",
                "object_label": "autosomal recessive limb-girdle muscular dystrophy type 2D",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:9069",
                "subject_label": "PLEC",
                "predicate": "biolink:causes",
                "object": "MONDO:0009181",
                "object_label": "epidermolysis bullosa simplex 5B, with muscular dystrophy",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:15710",
                "subject_label": "LDB3",
                "predicate": "biolink:causes",
                "object": "MONDO:0012277",
                "object_label": "myofibrillar myopathy 4",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:6636",
                "subject_label": "LMNA",
                "predicate": "biolink:causes",
                "object": "MONDO:0014676",
                "object_label": "Emery-Dreifuss muscular dystrophy 3, autosomal recessive",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:2666",
                "subject_label": "DAG1",
                "predicate": "biolink:causes",
                "object": "MONDO:0014683",
                "object_label": "muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A9",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:2188",
                "subject_label": "COL12A1",
                "predicate": "biolink:causes",
                "object": "MONDO:0034022",
                "object_label": "Bethlem myopathy 2",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:2188",
                "subject_label": "COL12A1",
                "predicate": "biolink:causes",
                "object": "MONDO:0014654",
                "object_label": "Ullrich congenital muscular dystrophy 2",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:28596",
                "subject_label": "B3GALNT2",
                "predicate": "biolink:causes",
                "object": "MONDO:0014071",
                "object_label": "muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type a, 11",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:3007",
                "subject_label": "DPM3",
                "predicate": "biolink:causes",
                "object": "MONDO:0013049",
                "object_label": "DPM3-congenital disorder of glycosylation",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:3622",
                "subject_label": "FKTN",
                "predicate": "biolink:causes",
                "object": "MONDO:0012699",
                "object_label": "autosomal recessive limb-girdle muscular dystrophy type 2M",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:3007",
                "subject_label": "DPM3",
                "predicate": "biolink:causes",
                "object": "MONDO:0033556",
                "object_label": "muscular dystrophy-dystroglycanopathy (congenital with impaired intellectual development), type B, 15",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:7577",
                "subject_label": "MYH7",
                "predicate": "biolink:causes",
                "object": "MONDO:0008050",
                "object_label": "MYH7-related skeletal myopathy",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:11802",
                "subject_label": "TIA1",
                "predicate": "biolink:causes",
                "object": "MONDO:0011466",
                "object_label": "distal myopathy, Welander type",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:15685",
                "subject_label": "B4GAT1",
                "predicate": "biolink:causes",
                "object": "MONDO:0014120",
                "object_label": "muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A13",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:17084",
                "subject_label": "SYNE2",
                "predicate": "biolink:causes",
                "object": "MONDO:0013072",
                "object_label": "Emery-Dreifuss muscular dystrophy 5, autosomal dominant",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:17089",
                "subject_label": "SYNE1",
                "predicate": "biolink:causes",
                "object": "MONDO:0013071",
                "object_label": "Emery-Dreifuss muscular dystrophy 4, autosomal dominant",
                "negated": None,
            },
            {
                "category": "biolink:CausalGeneToDiseaseAssociation",
                "subject": "HGNC:9202",
                "subject_label": "POMT1",
                "predicate": "biolink:causes",
                "object": "MONDO:0012248",
                "object_label": "autosomal recessive limb-girdle muscular dystrophy type 2K",
                "negated": None,
            },
        ],
    }
