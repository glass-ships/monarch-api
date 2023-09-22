import pytest


@pytest.fixture
def autocomplete_response():
    return {
        "responseHeader": {
            "QTime": 0,
            "params": {
                "mm": "100%",
                "q": "fanc",
                "defType": "edismax",
                "facet_min_count": "1",
                "qf": "id^100 name^10 name_t^5 name_ac symbol^10 symbol_t^5 symbol_ac synonym synonym_t synonym_ac",
                "start": "0",
                "boost": 'product(if(termfreq(category,"biolink:Disease"),10.0,1),if(and(termfreq(in_taxon,"NCBITaxon:9606"),termfreq(category,"biolink:Gene")),5.0,1))',
                "rows": "20",
                "facet": "true",
            },
        },
        "response": {
            "num_found": 215,
            "start": 0,
            "docs": [
                {
                    "id": "MONDO:0001083",
                    "category": "biolink:Disease",
                    "name": "Fanconi renotubular syndrome",
                    "provided_by": "phenio_nodes",
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
                    "description": "A genetic or acquired disorder characterized by impairment of the function of the proximal tubules of the kidney. It results in decreased reabsorption of electrolytes, glucose, amino acids, and other nutrients.",
                },
                {
                    "id": "MONDO:0009215",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group A",
                    "provided_by": "phenio_nodes",
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
                    "description": "Fanconi anemia caused by mutations of the FANCA gene. FANCA gene mutations are the most common cause of Fanconi anemia. This gene provides instructions for making a protein that is involved in the Fanconi anemia (FA) pathway.",
                },
                {
                    "id": "MONDO:0013566",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group L",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCL",
                        "FANCL Fanconi anemia",
                        "Fanconi Anemia, complementation Group 50",
                        "Fanconi Anemia, complementation group type 50",
                        "Fanconi anemia caused by mutation in FANCL",
                        "Fanconi anemia complementation group L",
                        "Fanconi anemia complementation group type L",
                        "Fanconi anemia, complementation group L",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the FANCL gene.",
                },
                {
                    "id": "MONDO:0010953",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group E",
                    "provided_by": "phenio_nodes",
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
                    "description": "Fanconi anemia caused by mutations of the FANCE gene. This is a protein coding gene. It is required for the nuclear accumulation of FANCC and provides a critical bridge between the FA complex and FANCD2.",
                },
                {
                    "id": "MONDO:0024525",
                    "category": "biolink:Disease",
                    "name": "Fanconi renotubular syndrome 1",
                    "provided_by": "phenio_nodes",
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
                },
                {
                    "id": "MONDO:0019391",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "Fanconi anemia",
                        "Fanconi pancytopenia",
                        "Fanconi panmyelopathy",
                        "Fanconi's anemia",
                        "Panmyelopathy, Fanconi",
                        "pancytopenia, congenital",
                        "primary erythroid hypoplasia",
                    ],
                    "description": "Fanconi anemia (FA) is a hereditary DNA repair disorder characterized by progressive pancytopenia with bone marrow failure, variable congenital malformations and predisposition to develop hematological or solid tumors.",
                },
                {
                    "id": "MONDO:0013248",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group O",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCO",
                        "Fanconi Anemia, complementation group type O",
                        "Fanconi anemia caused by mutation in RAD51C",
                        "Fanconi anemia caused by mutation in Rad51C",
                        "Fanconi anemia complementation group type O",
                        "Fanconi anemia, complementation group O",
                        "RAD51C Fanconi anemia",
                        "Rad51C Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the RAD51C gene.",
                },
                {
                    "id": "MONDO:0013499",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group P",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCP",
                        "Fanconi Anemia, complementation group type P",
                        "Fanconi anemia caused by mutation in SLX4",
                        "Fanconi anemia caused by mutation in Slx4",
                        "Fanconi anemia complementation group type P",
                        "Fanconi anemia, complementation group P",
                        "SLX4 Fanconi anemia",
                        "Slx4 Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the SLX4 gene.",
                },
                {
                    "id": "MONDO:0014985",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group V",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCV",
                        "Fanconi Anemia, complementation Group 5",
                        "Fanconi Anemia, complementation group V",
                        "Fanconi Anemia, complementation group type V",
                        "Fanconi anemia caused by mutation in MAD2L2",
                        "Fanconi anemia complementation group type V",
                        "Fanconi anemia, complementation GROUP V",
                        "MAD2L2 Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the MAD2L2 gene.",
                },
                {
                    "id": "MONDO:0100136",
                    "category": "biolink:Disease",
                    "name": "obsolete Fanconia anemia complementation group M",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCM Fanconi anemia",
                        "Fanconi anemia caused by mutation in FANCM",
                    ],
                    "description": "OBSOLETE Any Fanconi anemia in which the cause of the disease is a mutation in the FANCM gene.",
                },
                {
                    "id": "MONDO:0010351",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group B",
                    "provided_by": "phenio_nodes",
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
                    "description": "Fanconi anemia caused by mutations of the FANCB gene. This gene encodes the protein for complementation group B.",
                },
                {
                    "id": "MONDO:0012565",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group N",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCN",
                        "Fanconi Anemia, complementation group type N",
                        "Fanconi anemia caused by mutation in PALB2",
                        "Fanconi anemia complementation group N",
                        "Fanconi anemia complementation group type N",
                        "Fanconi anemia, complementation group N",
                        "PALB2 Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the PALB2 gene.",
                },
                {
                    "id": "MONDO:0014986",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group R",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCR",
                        "Fanconi Anemia, complementation group R",
                        "Fanconi Anemia, complementation group type R",
                        "Fanconi anemia caused by mutation in RAD51",
                        "Fanconi anemia complementation group type R",
                        "Fanconi anemia, complementation GROUP R",
                        "RAD51 Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the RAD51 gene.",
                },
                {
                    "id": "MONDO:0014987",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group U",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCU",
                        "Fanconi Anemia, complementation group U",
                        "Fanconi Anemia, complementation group type U",
                        "Fanconi anemia caused by mutation in XRCC2",
                        "Fanconi anemia complementation group type U",
                        "Fanconi anemia, complementation GROUP U",
                        "XRCC2 Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the XRCC2 gene.",
                },
                {
                    "id": "MONDO:0009213",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group C",
                    "provided_by": "phenio_nodes",
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
                    "description": "Fanconi anemia caused by mutations of the FANCC gene. This gene provides instructions for making a protein that delays the onset of apoptosis and promotes homologous recombination repair of damaged DNA.",
                },
                {
                    "id": "MONDO:0009214",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group D2",
                    "provided_by": "phenio_nodes",
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
                    "description": "Fanconi anemia caused by mutations of the FANCD2 gene. This gene is involved in the repair of DNA double-strand breaks, both by homologous recombination and single-strand annealing.",
                },
                {
                    "id": "MONDO:0012186",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group I",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCI",
                        "Fanconi Anemia, complementation Group 1",
                        "Fanconi Anemia, complementation group type 1",
                        "Fanconi anemia complementation group I",
                        "Fanconi anemia complementation group type I",
                        "Fanconi anemia, complementation group I",
                    ],
                    "description": "Fanconi anemia caused by mutations in the FANCI gene, encoding Fanconi anemia group I protein.",
                },
                {
                    "id": "MONDO:0014108",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group Q",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "ERCC4 Fanconi anemia",
                        "FANCQ",
                        "Fanconi Anemia, complementation group type Q",
                        "Fanconi anemia caused by mutation in ERCC4",
                        "Fanconi anemia complementation group type Q",
                        "Fanconi anemia, complementation group Q",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the ERCC4 gene.",
                },
                {
                    "id": "MONDO:0014638",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group T",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCT",
                        "Fanconi Anemia, complementation group type T",
                        "Fanconi anemia caused by mutation in UBE2T",
                        "Fanconi anemia complementation group type T",
                        "Fanconi anemia, complementation group T",
                        "UBE2T Fanconi anemia",
                    ],
                    "description": "Any Fanconi anemia in which the cause of the disease is a mutation in the UBE2T gene.",
                },
                {
                    "id": "MONDO:0011325",
                    "category": "biolink:Disease",
                    "name": "Fanconi anemia complementation group F",
                    "provided_by": "phenio_nodes",
                    "synonym": [
                        "FANCF",
                        "Fanconi Anemia, complementation group type F",
                        "Fanconi anemia complementation group F",
                        "Fanconi anemia complementation group type F",
                        "Fanconi anemia, complementation group F",
                    ],
                    "description": "Fanconi anemia caused by mutations of the FANCF gene. This gene encodes a polypeptide with homology to the prokaryotic RNA-binding protein ROM.",
                },
            ],
        },
        "facet_counts": {"facet_fields": {}, "facet_queries": {}},
    }
