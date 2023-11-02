import pytest


@pytest.fixture
def search():
    return {
        "limit": 20,
        "offset": 0,
        "total": 100,
        "items": [
            {
                "id": "MONDO:0019391",
                "category": "biolink:Disease",
                "name": "Fanconi anemia",
                "full_name": None,
                "description": "Fanconi anemia (FA) is a hereditary DNA repair disorder characterized by progressive pancytopenia with bone marrow failure, variable congenital malformations and predisposition to develop hematological or solid tumors.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "Fanconi anemia",
                    "Fanconi pancytopenia",
                    "Fanconi panmyelopathy",
                    "Fanconi's anemia",
                    "Panmyelopathy, Fanconi",
                    "pancytopenia, congenital",
                    "primary erythroid hypoplasia",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0001083",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome",
                "full_name": None,
                "description": "A genetic or acquired disorder characterized by impairment of the function of the proximal tubules of the kidney. It results in decreased reabsorption of electrolytes, glucose, amino acids, and other nutrients.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "De toni-Fanconi syndrome",
                    "De toni-debre-Fanconi syndrome",
                    "Fanconi syndrome",
                    "Fanconi's syndrome",
                    "Fanconi-de toni syndrome",
                    "Fanconi-de-toni syndrome",
                    "Lignac-Fanconi syndrome",
                    "adult Fanconi syndrome",
                    "congenital Fanconi syndrome",
                    "deToni Fanconi syndrome",
                    "infantile nephropathic cystinosis",
                    "toni-debre-Fanconi syndrome",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0007600",
                "category": "biolink:Disease",
                "name": "primary Fanconi syndrome",
                "full_name": None,
                "description": "A condition in which the kidneys do not absorb certain substances into the body. These substances, such as cysteine, fructose, galactose, or glycogen, are lost in the urine. Fanconi syndrome is thought to be caused by genetic and environmental factors, and it may be diagnosed at any age. Symptoms of Fanconi syndrome include increased urine production (which may cause dehydration), weakness, and abnormalities of the bones.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": ["FRTS1", "Fanconi renotubular syndrome 1", "primary Fanconi renotubular syndrome"],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009217",
                "category": "biolink:Disease",
                "name": "Fanconi-like syndrome",
                "full_name": None,
                "description": "A syndrome characterized by pancytopenia, immune deficiency and cutaneous malignancies.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": ["Fanconi-like syndrome"],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0060778",
                "category": "biolink:Disease",
                "name": "adult Fanconi syndrome",
                "full_name": None,
                "description": "Probably related to a recessive gene, this is Fanconi Syndrome, characterised by adult onset.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": ["adult Fanconi syndrome", "adult Fanconi's syndrome"],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0060779",
                "category": "biolink:Disease",
                "name": "acquired Fanconi syndrome",
                "full_name": None,
                "description": "Fanconi Syndrome caused by exposure to noxious agents.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": ["acquired Fanconi syndrome"],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0000026",
                "category": "biolink:Disease",
                "name": "obsolete Fanconi renotubular syndrome",
                "full_name": None,
                "description": None,
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0013247",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 2",
                "full_name": None,
                "description": "Any Fanconi syndrome in which the cause of the disease is a mutation in the SLC34A1 gene.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FRTS2",
                    "Fanconi renotubular syndrome 2",
                    "Fanconi renotubular syndrome type 2",
                    "Fanconi syndrome caused by mutation in SLC34A1",
                    "SLC34A1 Fanconi syndrome",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0014275",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 3",
                "full_name": None,
                "description": "Any Fanconi syndrome in which the cause of the disease is a mutation in the EHHADH gene.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "EHHADH Fanconi syndrome",
                    "FRTS3",
                    "Fanconi renotubular syndrome 3",
                    "Fanconi renotubular syndrome type 3",
                    "Fanconi syndrome caused by mutation in EHHADH",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0024525",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 1",
                "full_name": None,
                "description": None,
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "DeToni-Debré-Fanconi syndrome",
                    "FRTS1",
                    "Fanconi renotubular syndrome",
                    "Fanconi renotubular syndrome 1",
                    "Fanconi syndrome without cystinosis",
                    "Luder-Sheldon syndrome",
                    "adult Fanconi syndrome",
                    "primary Fanconi renal syndrome",
                    "primary Fanconi renotubular syndrome",
                    "renal Fanconi syndrome",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0030056",
                "category": "biolink:Disease",
                "name": "Fanconi renotubular syndrome 5",
                "full_name": None,
                "description": None,
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FANCONI RENOTUBULAR SYNDROME 5",
                    "FRTS5",
                    "Fanconi Renotubular Syndrome, Acadian Variant",
                    "Fanconi renotubular syndrome 5",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0100238",
                "category": "biolink:Disease",
                "name": "inherited Fanconi renotubular syndrome",
                "full_name": None,
                "description": "An instance of Fanconi renotubular syndrome that is inherited.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": ["hereditary Fanconi renotubular syndrome"],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009213",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group C",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCC gene. This gene provides instructions for making a protein that delays the onset of apoptosis and promotes homologous recombination repair of damaged DNA.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FA3",
                    "FACC",
                    "FANCC",
                    "Fanconi Anemia, complementation group type C",
                    "Fanconi anemia complementation group C",
                    "Fanconi anemia complementation group type C",
                    "Fanconi anemia, complementation group C",
                    "Fanconi pancytopenia type 3",
                    "Fanconi pancytopenia, type 3",
                    "facc",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009214",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group D2",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCD2 gene. This gene is involved in the repair of DNA double-strand breaks, both by homologous recombination and single-strand annealing.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FA4",
                    "FAD2",
                    "FANCD2",
                    "Fad2",
                    "Fanconi Anemia, complementation group D",
                    "Fanconi anemia complementation group D2",
                    "Fanconi anemia, complementation group D2",
                    "Fanconi pancytopenia type 4",
                    "Fanconi pancytopenia, type 4",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0009215",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group A",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCA gene. FANCA gene mutations are the most common cause of Fanconi anemia. This gene provides instructions for making a protein that is involved in the Fanconi anemia (FA) pathway.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "Estren-Dameshek variant of Fanconi Anemia",
                    "Estren-Dameshek variant of Fanconi pancytopenia",
                    "FANCA",
                    "FANCA Fanconi anemia",
                    "Fanconi Anemia",
                    "Fanconi Anemia, Estren-Dameshek variant",
                    "Fanconi Anemia, complementation group type a",
                    "Fanconi anemia caused by mutation in FANCA",
                    "Fanconi anemia complementation group A",
                    "Fanconi anemia complementation group type A",
                    "Fanconi anemia, complementation group A",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0010351",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group B",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCB gene. This gene encodes the protein for complementation group B.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FA2",
                    "FACB",
                    "FANCB",
                    "Fanconi Anemia, complementation group type B",
                    "Fanconi anemia complementation group B",
                    "Fanconi anemia complementation group type B",
                    "Fanconi anemia, complementation group B",
                    "Fanconi anemia, complementation group B, X-linked recessive",
                    "Fanconi pancytopenia type 2",
                    "Fanconi pancytopenia, type 2",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0010953",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group E",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCE gene. This is a protein coding gene. It is required for the nuclear accumulation of FANCC and provides a critical bridge between the FA complex and FANCD2.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FANCE",
                    "FANCE Fanconi anemia",
                    "Fanconi Anemia, complementation group type E",
                    "Fanconi anemia caused by mutation in FANCE",
                    "Fanconi anemia complementation group E",
                    "Fanconi anemia complementation group type E",
                    "Fanconi anemia, complementation group E",
                    "face",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0011325",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group F",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations of the FANCF gene. This gene encodes a polypeptide with homology to the prokaryotic RNA-binding protein ROM.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FANCF",
                    "Fanconi Anemia, complementation group type F",
                    "Fanconi anemia complementation group F",
                    "Fanconi anemia complementation group type F",
                    "Fanconi anemia, complementation group F",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0011584",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group D1",
                "full_name": None,
                "description": "Inherited cancer-predisposing syndrome due to biallelic BRCA2 mutations is a rare cancer-predisposing syndrome, associated with the D1 subgroup of Fanconi anemia (FA), characterized by progressive bone marrow failure, cardiac, brain, intestinal or skeletal abnormalities and predisposition to various malignancies. Bone marrow suppression and the incidence of developmental abnormalities are less frequent than in other FA, but cancer risk is very high with the spectrum of childhood cancers including Wilms tumor, brain tumor (often medulloblastoma) and ALL/AML.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FAD1",
                    "FANCD1",
                    "Fad1",
                    "Fanconi anemia complementation group D1",
                    "Fanconi anemia, complementation group D1",
                    "inherited cancer-predisposing syndrome due to biallelic BRCA2 mutations",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
            {
                "id": "MONDO:0012186",
                "category": "biolink:Disease",
                "name": "Fanconi anemia complementation group I",
                "full_name": None,
                "description": "Fanconi anemia caused by mutations in the FANCI gene, encoding Fanconi anemia group I protein.",
                "xref": [],
                "provided_by": "phenio_nodes",
                "in_taxon": None,
                "in_taxon_label": None,
                "symbol": None,
                "synonym": [
                    "FANCI",
                    "Fanconi Anemia, complementation Group 1",
                    "Fanconi Anemia, complementation group type 1",
                    "Fanconi anemia complementation group I",
                    "Fanconi anemia complementation group type I",
                    "Fanconi anemia, complementation group I",
                ],
                "uri": None,
                "highlight": None,
                "score": None,
            },
        ],
        "facet_fields": [],
        "facet_queries": [],
    }
