import pytest


@pytest.fixture
def mappings():
    return {
        "limit": 20,
        "offset": 0,
        "total": 7,
        "items": [
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "DOID:9884",
                "object_label": "muscular dystrophy",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "79cebb50-dc15-427f-b98f-07fafbc2233e",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "ICD10CM:G71.0",
                "object_label": "Muscular dystrophy",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "eb2edd42-6ff7-4a82-bf6b-607b03f6a7c0",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "NCIT:C84910",
                "object_label": "Muscular Dystrophy",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "ca35bb5b-62a1-4e75-a43e-03e43352391f",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "Orphanet:98473",
                "object_label": "Muscular dystrophy",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "cf655e90-9c26-4fea-a78d-925aa43e2581",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "SCTID:73297009",
                "object_label": None,
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "6fccb876-27ff-43e4-aeba-8cc362a6d134",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "UMLS:C0026850",
                "object_label": None,
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "a4a8fd62-7c76-47e6-82b2-2dc0f4e0651f",
            },
            {
                "subject_id": "MONDO:0020121",
                "subject_label": "muscular dystrophy",
                "predicate_id": "skos:exactMatch",
                "object_id": "mesh:D009136",
                "object_label": None,
                "mapping_justification": "semapv:UnspecifiedMatching",
                "id": "fa9fb840-d371-4eb9-bc1f-434abdb145e9",
            },
        ],
    }
