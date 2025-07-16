import requests


# def test_always_passes():
#     assert True


def test_hello_endpoint():
    response = requests.get("http://localhost:8081/api/hello")
    assert response.status_code == 200
    assert response.text == "Hello from Spring Boot!"
