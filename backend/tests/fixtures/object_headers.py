import pytest


@pytest.fixture
def node_headers():
    return [
        "id",
        "category",
        "name",
        "full_name",
        "deprecated",
        "description",
        "xref",
        "provided_by",
        "in_taxon",
        "in_taxon_label",
        "symbol",
        "synonym",
        "uri",
        "inheritance",
        "causal_gene",
        "causes_disease",
        "mappings",
        "external_links",
        "provided_by_link",
        "association_counts",
        "node_hierarchy",
    ]


@pytest.fixture
def search_headers():
    return [
        "id",
        "category",
        "name",
        "full_name",
        "deprecated",
        "description",
        "xref",
        "provided_by",
        "in_taxon",
        "in_taxon_label",
        "symbol",
        "synonym",
        "uri",
        "highlight",
        "score",
    ]


@pytest.fixture
def histopheno_headers():
    return ["label", "count", "id"]


@pytest.fixture
def association_headers():
    return [
        "id",
        "category",
        "subject",
        "original_subject",
        "subject_namespace",
        "subject_category",
        "subject_closure",
        "subject_label",
        "subject_closure_label",
        "subject_taxon",
        "subject_taxon_label",
        "predicate",
        "object",
        "original_object",
        "object_namespace",
        "object_category",
        "object_closure",
        "object_label",
        "object_closure_label",
        "object_taxon",
        "object_taxon_label",
        "primary_knowledge_source",
        "aggregator_knowledge_source",
        "negated",
        "pathway",
        "evidence_count",
        "has_evidence",
        "has_evidence_links",
        "grouping_key",
        "provided_by",
        "provided_by_link",
        "publications",
        "publications_links",
        "qualifiers",
        "frequency_qualifier",
        "onset_qualifier",
        "sex_qualifier",
        "stage_qualifier",
        "qualifiers_label",
        "qualifiers_namespace",
        "qualifiers_category",
        "qualifiers_closure",
        "qualifiers_closure_label",
        "frequency_qualifier_label",
        "frequency_qualifier_namespace",
        "frequency_qualifier_category",
        "frequency_qualifier_closure",
        "frequency_qualifier_closure_label",
        "onset_qualifier_label",
        "onset_qualifier_namespace",
        "onset_qualifier_category",
        "onset_qualifier_closure",
        "onset_qualifier_closure_label",
        "sex_qualifier_label",
        "sex_qualifier_namespace",
        "sex_qualifier_category",
        "sex_qualifier_closure",
        "sex_qualifier_closure_label",
        "stage_qualifier_label",
        "stage_qualifier_namespace",
        "stage_qualifier_category",
        "stage_qualifier_closure",
        "stage_qualifier_closure_label",
    ]
