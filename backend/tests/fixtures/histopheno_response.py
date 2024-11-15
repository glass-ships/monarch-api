import pytest


@pytest.fixture
def histopheno_response():
    return {
        "responseHeader": {
            "QTime": 1,
            "params": {
                "facet.query": [
                    'object_closure:"UPHENO:0002964"',
                    'object_closure:"UPHENO:0004523"',
                    'object_closure:"UPHENO:0002764"',
                    'object_closure:"UPHENO:0002635"',
                    'object_closure:"UPHENO:0003020"',
                    'object_closure:"UPHENO:0080362"',
                    'object_closure:"HP:0001939"',
                    'object_closure:"UPHENO:0002642"',
                    'object_closure:"UPHENO:0002833"',
                    'object_closure:"HP:0002664"',
                    'object_closure:"UPHENO:0004459"',
                    'object_closure:"UPHENO:0002948"',
                    'object_closure:"UPHENO:0003116"',
                    'object_closure:"UPHENO:0002816"',
                    'object_closure:"UPHENO:0004536"',
                    'object_closure:"HP:0000598"',
                    'object_closure:"UPHENO:0002712"',
                    'object_closure:"UPHENO:0075949"',
                    'object_closure:"UPHENO:0049874"',
                    'object_closure:"UPHENO:0003013"',
                ],
                "mm": "100%",
                "q": "*:*",
                "defType": "edismax",
                "facet_min_count": "1",
                "start": "0",
                "q.op": "AND",
                "fq": 'subject:"MONDO:0020121" OR subject_closure:"MONDO:0020121"',
                "facet.mincount": "1",
                "rows": "0",
                "facet": "true",
            },
        },
        "response": {"num_found": 4599, "start": 0, "docs": []},
        "facet_counts": {
            "facet_fields": {},
            "facet_queries": {
                'object_closure:"UPHENO:0002964"': 509,
                'object_closure:"UPHENO:0004523"': 1126,
                'object_closure:"UPHENO:0002764"': 597,
                'object_closure:"UPHENO:0002635"': 49,
                'object_closure:"UPHENO:0003020"': 297,
                'object_closure:"UPHENO:0080362"': 0,
                'object_closure:"HP:0001939"': 228,
                'object_closure:"UPHENO:0002642"': 49,
                'object_closure:"UPHENO:0002833"': 154,
                'object_closure:"HP:0002664"': 7,
                'object_closure:"UPHENO:0004459"': 185,
                'object_closure:"UPHENO:0002948"': 28,
                'object_closure:"UPHENO:0003116"': 25,
                'object_closure:"UPHENO:0002816"': 2068,
                'object_closure:"UPHENO:0004536"': 158,
                'object_closure:"HP:0000598"': 28,
                'object_closure:"UPHENO:0002712"': 175,
                'object_closure:"UPHENO:0075949"': 22,
                'object_closure:"UPHENO:0049874"': 32,
                'object_closure:"UPHENO:0003013"': 1,
            },
        },
    }
