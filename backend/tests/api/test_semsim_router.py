import pytest
from fastapi.testclient import TestClient
from fastapi import status
from unittest.mock import MagicMock, patch

from monarch_py.api.additional_models import SemsimSearchGroup
from monarch_py.api.semsim import router

client = TestClient(router)


@patch("monarch_py.api.config.SemsimianHTTPRequester.search")
@pytest.mark.parametrize("termset", [
    "HP:123,HP:456",
    "HP:123, HP:456",
    " HP:123, HP:456 "
])
def test_get_search(mock_search, termset: str):
    mock_search.return_value = MagicMock()

    group = SemsimSearchGroup.HGNC
    limit = 5

    response = client.get(f"/search/{termset}/{group.value}?limit={limit}")

    assert response.status_code == status.HTTP_200_OK
    mock_search.assert_called_once_with(termset=["HP:123", "HP:456"], prefix=group.name, limit=limit)

