from fastapi.testclient import TestClient
from main import app  # Replace with the name of your file containing the FastAPI app

client = TestClient(app)


def test_compress_decompress():
    response = client.post("/compress", json={"mzs": [100.0, 200.0, 300.0], "intensities": [10.0, 20.0, 30.0]})
    assert response.status_code == 200
    assert "compressed_data" in response.json()
    response = client.post("/decompress", json={"compressed_data": response.json()["compressed_data"]})
    assert response.status_code == 200
    assert "mzs" in response.json() and "intensities" in response.json()
    assert response.json()["mzs"] == [100.0, 200.0, 300.0] and response.json()["intensities"] == [10.0, 20.0, 30.0]


def test_store_and_retrieve():
    # First, compress and store data
    store_response = client.post("/store", json={"mzs": [100.0, 200.0, 300.0], "intensities": [10.0, 20.0, 30.0]})
    assert store_response.status_code == 200
    key = store_response.json()["key"]

    # Then retrieve it
    retrieve_response = client.get(f"/retrieve/{key}")
    assert retrieve_response.status_code == 200
    assert "mzs" in retrieve_response.json() and "intensities" in retrieve_response.json()

    # Check that the retrieved data is the same as the original data
    assert retrieve_response.json()["mzs"] == [100.0, 200.0, 300.0] and retrieve_response.json()["intensities"] == [10.0, 20.0, 30.0]
