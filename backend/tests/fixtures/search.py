import pytest


@pytest.fixture
def search():
    return {
        "limit": 20,
        "offset": 0,
        "total": 110,
        "items": [
            {
                "id": "MONDO:0019391",
                "category": "biolink:Disease",
                "name": "Fanconi anemia",
                "description": "Fanconi anemia (FA) is a hereditary DNA repair disorder characterized by progressive pancytopenia with bone marrow failure, variable congenital malformations and predisposition to develop hematological or solid tumors.",
                "xref": [
                    "DOID:13636",
                    "GARD:0006425",
                    "ICD9:284.09",
                    "MESH:D005199",
                    "MedDRA:10055206",
                    "NCIT:C62505",
                    "OMIMPS:227650",
                    "Orphanet:84",
                    "SCTID:30575002",
                    "UMLS:C0015625",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0001083",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome",
                "description": "A genetic or acquired disorder characterized by impairment of the function of the proximal tubules of the kidney. It results in decreased reabsorption of electrolytes, glucose, amino acids, and other nutrients.",
                "xref": [
                    "DOID:1062",
                    "GARD:0009120",
                    "MESH:D005198",
                    "NCIT:C3034",
                    "SCTID:40488004",
                    "UMLS:C0015624",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0007600",
                "category": "biolink:Disease",
                "name": "primary Fanconi syndrome",
                "description": "A condition in which the kidneys do not absorb certain substances into the body. These substances, such as cysteine, fructose, galactose, or glycogen, are lost in the urine. Fanconi syndrome is thought to be caused by genetic and environmental factors, and it may be diagnosed at any age. Symptoms of Fanconi syndrome include increased urine production (which may cause dehydration), weakness, and abnormalities of the bones.",
                "xref": ["GARD:0009118", "NCIT:C123229"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009217",
                "category": "biolink:Disease",
                "name": "Fanconi-like syndrome",
                "description": "A syndrome characterized by pancytopenia, immune deficiency and cutaneous malignancies.",
                "xref": [
                    "DOID:0090066",
                    "MESH:C536855",
                    "OMIM:227850",
                    "SCTID:236469003",
                    "UMLS:C0151638",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0060778",
                "category": "biolink:Disease",
                "name": "adult Fanconi syndrome",
                "description": "Probably related to a recessive gene, this is Fanconi Syndrome, characterised by adult onset.",
                "xref": ["NCIT:C4377"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0060779",
                "category": "biolink:Disease",
                "name": "acquired Fanconi syndrome",
                "description": "Fanconi Syndrome caused by exposure to noxious agents.",
                "xref": ["NCIT:C78296", "SCTID:236467001", "UMLS:C0341702"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0000026",
                "category": "biolink:Disease",
                "name": "obsolete Fanconi renotubular syndrome",
                "description": None,
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0013247",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 2",
                "description": "Any Fanconi syndrome in which the cause of the disease is a mutation in the SLC34A1 gene.",
                "xref": ["DOID:0080758", "OMIM:613388", "UMLS:C3150652"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0014275",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 3",
                "description": "Any Fanconi syndrome in which the cause of the disease is a mutation in the EHHADH gene.",
                "xref": ["DOID:0080759", "OMIM:615605", "UMLS:C3810100"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0024525",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 1",
                "description": None,
                "xref": ["DOID:0080757", "OMIM:134600", "Orphanet:3337"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0030056",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 5",
                "description": None,
                "xref": ["DOID:0080761", "OMIM:618913"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0100238",
                "category": "biolink:Disease",
                "name": "inherited Fanconi renotubular syndrome",
                "description": "An instance of Fanconi renotubular syndrome that is inherited.",
                "xref": ["OMIMPS:134600"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009213",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group C",
                "description": "Fanconi anemia caused by mutations of the FANCC gene. This gene provides instructions for making a protein that delays the onset of apoptosis and promotes homologous recombination repair of damaged DNA.",
                "xref": [
                    "DOID:0111087",
                    "NCIT:C125704",
                    "OMIM:227645",
                    "UMLS:C3468041",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009214",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group D2",
                "description": "Fanconi anemia caused by mutations of the FANCD2 gene. This gene is involved in the repair of DNA double-strand breaks, both by homologous recombination and single-strand annealing.",
                "xref": [
                    "DOID:0111083",
                    "NCIT:C125706",
                    "OMIM:227646",
                    "UMLS:C3160738",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009215",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group A",
                "description": "Fanconi anemia caused by mutations of the FANCA gene. FANCA gene mutations are the most common cause of Fanconi anemia. This gene provides instructions for making a protein that is involved in the Fanconi anemia (FA) pathway.",
                "xref": [
                    "DOID:0111095",
                    "EFO:0009044",
                    "GTR:AN1051558",
                    "NCIT:C125702",
                    "OMIM:227650",
                    "UMLS:CN653908",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0010351",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group B",
                "description": "Fanconi anemia caused by mutations of the FANCB gene. This gene encodes the protein for complementation group B.",
                "xref": [
                    "DOID:0111098",
                    "MESH:C564497",
                    "NCIT:C125703",
                    "OMIM:300514",
                    "UMLS:C1845292",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0010953",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group E",
                "description": "Fanconi anemia caused by mutations of the FANCE gene. This is a protein coding gene. It is required for the nuclear accumulation of FANCC and provides a critical bridge between the FA complex and FANCD2.",
                "xref": [
                    "DOID:0111084",
                    "NCIT:C125709",
                    "OMIM:600901",
                    "UMLS:C3160739",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0011325",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group F",
                "description": "Fanconi anemia caused by mutations of the FANCF gene. This gene encodes a polypeptide with homology to the prokaryotic RNA-binding protein ROM.",
                "xref": ["DOID:0111088", "EFO:0009045", "NCIT:C125707", "OMIM:603467"],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0011584",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group D1",
                "description": "Inherited cancer-predisposing syndrome due to biallelic BRCA2 mutations is a rare cancer-predisposing syndrome, associated with the D1 subgroup of Fanconi anemia (FA), characterized by progressive bone marrow failure, cardiac, brain, intestinal or skeletal abnormalities and predisposition to various malignancies. Bone marrow suppression and the incidence of developmental abnormalities are less frequent than in other FA, but cancer risk is very high with the spectrum of childhood cancers including Wilms tumor, brain tumor (often medulloblastoma) and ALL/AML.",
                "xref": [
                    "DOID:0111089",
                    "MESH:C563980",
                    "NCIT:C125705",
                    "OMIM:605724",
                    "Orphanet:319462",
                    "SCTID:766707003",
                    "UMLS:C1838457",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0012186",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group I",
                "description": "Fanconi anemia caused by mutations in the FANCI gene, encoding Fanconi anemia group I protein.",
                "xref": [
                    "DOID:0111091",
                    "MESH:C563802",
                    "NCIT:C129026",
                    "OMIM:609053",
                    "UMLS:C1836861",
                ],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "highlight": None,
                "score": None,
            },
        ],
        "facet_fields": [],
        "facet_queries": [],
    }
