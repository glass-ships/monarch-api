import pytest


@pytest.fixture
def histopheno_response():
    return {
        "responseHeader": {
            "QTime": 0,
            "params": {
                "facet.query": [
                    'object_closure:"HP:0000924"',
                    'object_closure:"HP:0000707"',
                    'object_closure:"HP:0000152"',
                    'object_closure:"HP:0001574"',
                    'object_closure:"HP:0000478"',
                    'object_closure:"HP:0001626"',
                    'object_closure:"HP:0001939"',
                    'object_closure:"HP:0000119"',
                    'object_closure:"HP:0025031"',
                    'object_closure:"HP:0002664"',
                    'object_closure:"HP:0001871"',
                    'object_closure:"HP:0002715"',
                    'object_closure:"HP:0000818"',
                    'object_closure:"HP:0003011"',
                    'object_closure:"HP:0002086"',
                    'object_closure:"HP:0000598"',
                    'object_closure:"HP:0003549"',
                    'object_closure:"HP:0001197"',
                    'object_closure:"HP:0001507"',
                    'object_closure:"HP:0000769"',
                ],
                "mm": "100%",
                "q": "*:*",
                "defType": "edismax",
                "facet_min_count": "1",
                "start": "0",
                "fq": "subject_closure:MONDO\\:0020121",
                "rows": "0",
                "facet": "true",
            },
        },
        "response": {"num_found": 4538, "start": 0, "docs": []},
        "facet_counts": {
            "facet_fields": {},
            "facet_queries": {
                'object_closure:"HP:0000924"': 504,
                'object_closure:"HP:0000707"': 1118,
                'object_closure:"HP:0000152"': 573,
                'object_closure:"HP:0001574"': 48,
                'object_closure:"HP:0000478"': 276,
                'object_closure:"HP:0001626"': 192,
                'object_closure:"HP:0001939"': 219,
                'object_closure:"HP:0000119"': 43,
                'object_closure:"HP:0025031"': 143,
                'object_closure:"HP:0002664"': 7,
                'object_closure:"HP:0001871"': 185,
                'object_closure:"HP:0002715"': 21,
                'object_closure:"HP:0000818"': 25,
                'object_closure:"HP:0003011"': 1747,
                'object_closure:"HP:0002086"': 318,
                'object_closure:"HP:0000598"': 27,
                'object_closure:"HP:0003549"': 165,
                'object_closure:"HP:0001197"': 20,
                'object_closure:"HP:0001507"': 33,
                'object_closure:"HP:0000769"': 1,
            },
        },
    }
