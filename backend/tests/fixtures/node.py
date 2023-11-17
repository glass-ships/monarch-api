import pytest


@pytest.fixture
def node():
    return {
        "id": "MONDO:0020121",
        "category": "biolink:Disease",
        "name": "muscular dystrophy",
        "full_name": None,
        "deprecated": None,
        "description": "Muscular dystrophy (MD) refers to a group of more than 30 genetic diseases characterized by progressive weakness and degeneration of the skeletal muscles that control movement. Some forms of MD are seen in newborns, infants or children, while others have late-onset and may not appear until middle age or later. The disorders differ in terms of the distribution and extent of muscle weakness (some forms of MD also affect cardiac muscle), age of onset, rate of progression, and pattern of inheritance. The prognosis for people with MD varies according to the type and progression of the disorder. There is no specific treatment to stop or reverse any form of MD. Treatment is supportive and may include physical therapy, respiratory therapy, speech therapy, orthopedic appliances used for support, corrective orthopedic surgery, and medicationsincluding corticosteroids, anticonvulsants (seizure medications), immunosuppressants, and antibiotics. Some individuals may need assisted ventilation to treat respiratory muscle weaknessor a pacemaker for cardiac (heart)abnormalities.",
        "xref": [],
        "provided_by": "phenio_nodes",
        "in_taxon": None,
        "in_taxon_label": None,
        "symbol": None,
        "synonym": [],
        "uri": None,
        "inheritance": None,
        "causal_gene": [],
        "causes_disease": [],
        "mappings": [
            {"id": "DOID:9884", "url": "http://purl.obolibrary.org/obo/DOID_9884"},
            {"id": "ICD10CM:G71.0", "url": "https://icd.codes/icd10cm/G71.0"},
            {"id": "MESH:D009136", "url": "http://identifiers.org/mesh/D009136"},
            {"id": "NCIT:C84910", "url": "http://purl.obolibrary.org/obo/NCIT_C84910"},
            {"id": "SCTID:73297009", "url": None},
            {"id": "UMLS:C0026850", "url": "http://identifiers.org/umls/C0026850"},
            {"id": "Orphanet:98473", "url": None},
        ],
        "external_links": [],
        "provided_by_link": {
            "id": "phenio",
            "url": "https://monarch-initiative.github.io/monarch-ingest/Sources/phenio/#",
        },
        "association_counts": [
            {"label": "Phenotypes", "count": 4027, "category": "biolink:DiseaseToPhenotypicFeatureAssociation"},
            {"label": "Causal Genes", "count": 124, "category": "biolink:CausalGeneToDiseaseAssociation"},
            {"label": "Correlated Genes", "count": 151, "category": "biolink:CorrelatedGeneToDiseaseAssociation"},
        ],
        "node_hierarchy": {
            "super_classes": [
                {
                    "id": "MONDO:0019056",
                    "category": "biolink:Disease",
                    "name": "neuromuscular disease",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0700223",
                    "category": "biolink:Disease",
                    "name": "hereditary skeletal muscle disorder",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0005336",
                    "category": "biolink:Disease",
                    "name": "myopathy",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
            ],
            "sub_classes": [
                {
                    "id": "MONDO:0008028",
                    "category": "biolink:Disease",
                    "name": "muscular dystrophy, Barnes type",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0010675",
                    "category": "biolink:Disease",
                    "name": "muscular dystrophy, cardiac type",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0010676",
                    "category": "biolink:Disease",
                    "name": "muscular dystrophy, Hemizygous lethal type",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0010677",
                    "category": "biolink:Disease",
                    "name": "muscular dystrophy, Mabry type",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0010678",
                    "category": "biolink:Disease",
                    "name": "muscular dystrophy, progressive Pectorodorsal",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0019950",
                    "category": "biolink:Disease",
                    "name": "congenital muscular dystrophy",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0023204",
                    "category": "biolink:Disease",
                    "name": "Fukuda-Miyanomae-Nakata syndrome",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0100228",
                    "category": "biolink:Disease",
                    "name": "LAMA2-related muscular dystrophy",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0018949",
                    "category": "biolink:Disease",
                    "name": "distal myopathy",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
                {
                    "id": "MONDO:0016106",
                    "category": "biolink:Disease",
                    "name": "progressive muscular dystrophy",
                    "full_name": None,
                    "deprecated": None,
                    "description": None,
                    "xref": [],
                    "provided_by": None,
                    "in_taxon": None,
                    "in_taxon_label": None,
                    "symbol": None,
                    "synonym": [],
                    "uri": None,
                },
            ],
        },
    }
