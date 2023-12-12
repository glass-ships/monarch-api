import pytest


@pytest.fixture
def phenotype_explorer_search():
    return [
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0002909": {"id": "ZP:0002909", "label": "whole organism dwarf-like, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0002909": {
                        "match_source": "ZP:0002909",
                        "match_source_label": "whole organism dwarf-like, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0002909": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4444444444444444",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.198054183387448",
                        "subject_id": "ZP:0002909",
                    }
                },
                "object_termset": [
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0002909",
                        "match_target_label": "whole organism dwarf-like, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0002909",
                        "match_target_label": "whole organism dwarf-like, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0002909",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4444444444444444",
                        "object_id": "ZP:0002909",
                        "phenodigm_score": "2.198054183387448",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-070117-1426",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-081022-128",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-111209-1",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-070117-1424",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-030131-4487",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-070117-1594",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-070117-1423",
        ],
        [
            8.153058700868163,
            {
                "subject_termset": [
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}}
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    }
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    }
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 8.153058700868163,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-100729-3",
        ],
        [
            7.661460799028868,
            {
                "subject_termset": [
                    {"ZP:0014819": {"id": "ZP:0014819", "label": "growth decreased process quality, abnormal (ZPO)"}},
                    {"ZP:0000473": {"id": "ZP:0000473", "label": "whole organism decreased length, abnormal (ZPO)"}},
                ],
                "subject_best_matches": {
                    "ZP:0000473": {
                        "match_source": "ZP:0000473",
                        "match_source_label": "whole organism decreased length, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    },
                    "ZP:0014819": {
                        "match_source": "ZP:0014819",
                        "match_source_label": "growth decreased process quality, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "8.904353327133704",
                    },
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000473": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "ZP:0000473",
                    },
                    "ZP:0014819": {
                        "ancestor_id": "UPHENO:0049874",
                        "ancestor_information_content": "8.904353327133704",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.3333333333333333",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "1.7228226187600493",
                        "subject_id": "ZP:0014819",
                    },
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0014819",
                        "match_target_label": "growth decreased process quality, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000473",
                        "match_target_label": "whole organism decreased length, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0014819",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.4",
                        "object_id": "ZP:0000473",
                        "phenodigm_score": "2.0852572919897328",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 7.661460799028868,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-120919-4",
        ],
        [
            6.283193403469026,
            {
                "subject_termset": [
                    {"ZP:0000324": {"id": "ZP:0000324", "label": "whole organism decreased size, abnormal (ZPO)"}},
                    {"ZP:0001589": {"id": "ZP:0001589", "label": "embryo development disrupted, abnormal (ZPO)"}},
                ],
                "subject_best_matches": {
                    "ZP:0000324": {
                        "match_source": "ZP:0000324",
                        "match_source_label": "whole organism decreased size, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "10.870744934490885",
                    },
                    "ZP:0001589": {
                        "match_source": "ZP:0001589",
                        "match_source_label": "embryo development disrupted, abnormal (ZPO)",
                        "match_target": "HP:0000002",
                        "match_target_label": "Abnormality of body height (HPO)",
                        "score": "3.3912837448943334",
                    },
                },
                "subject_best_matches_similarity_map": {
                    "ZP:0000324": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.45714285714285713",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "2.22923381425646",
                        "subject_id": "ZP:0000324",
                    },
                    "ZP:0001589": {
                        "ancestor_id": "UPHENO:0049587",
                        "ancestor_information_content": "3.3912837448943334",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.2727272727272727",
                        "object_id": "HP:0000002",
                        "phenodigm_score": "0.9617149093101155",
                        "subject_id": "ZP:0001589",
                    },
                },
                "object_termset": [
                    {"HP:0000001": {"id": "HP:0000001", "label": "All (HPO)"}},
                    {"HP:0000002": {"id": "HP:0000002", "label": "Abnormality of body height (HPO)"}},
                ],
                "object_best_matches": {
                    "HP:0000001": {
                        "match_source": "HP:0000001",
                        "match_source_label": "All (HPO)",
                        "match_target": "ZP:0001589",
                        "match_target_label": "embryo development disrupted, abnormal (ZPO)",
                        "score": "0",
                    },
                    "HP:0000002": {
                        "match_source": "HP:0000002",
                        "match_source_label": "Abnormality of body height (HPO)",
                        "match_target": "ZP:0000324",
                        "match_target_label": "whole organism decreased size, abnormal (ZPO)",
                        "score": "10.870744934490885",
                    },
                },
                "object_best_matches_similarity_map": {
                    "HP:0000001": {
                        "ancestor_id": "NO_ANCESTOR_FOUND",
                        "ancestor_information_content": "0",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0",
                        "object_id": "ZP:0001589",
                        "phenodigm_score": "0",
                        "subject_id": "HP:0000001",
                    },
                    "HP:0000002": {
                        "ancestor_id": "UPHENO:0075159",
                        "ancestor_information_content": "10.870744934490885",
                        "ancestor_label": "",
                        "cosine_similarity": "NaN",
                        "jaccard_similarity": "0.45714285714285713",
                        "object_id": "ZP:0000324",
                        "phenodigm_score": "2.22923381425646",
                        "subject_id": "HP:0000002",
                    },
                },
                "average_score": 6.283193403469026,
                "best_score": 10.870744934490885,
                "metric": "ancestor_information_content",
            },
            "ZFIN:ZDB-GENE-130726-2",
        ],
    ]
