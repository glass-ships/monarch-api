# write a test that uses mocking to test the get_node_hierarchy function
from unittest.mock import Mock

from monarch_py.datamodels.model import AssociationResults, Entity
from monarch_py.implementations.solr.solr_implementation import SolrImplementation


def test_get_node_hierarchy():
    """
    Test that get_node_hierarchy calls get_associations from monarch_py
    """

    # create a mock solr implementation
    si = Mock(
        spec=SolrImplementation,
        get_associations=Mock(
            return_value=AssociationResults(limit=20, offset=0, total=100)
        ),
    )

    # call get_node_hierarchy and assert that it calls get_associations
    si._get_node_hierarchy(Entity(id="MONDO:0007947"), si)

    # Assert that get_associations was called three times
    assert si.get_associations.call_count == 3
