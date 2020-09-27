import requests

URL = "https://192.168.16.100"

def test_answer():
    r = requests.get(url = URL)
    assert r.status_code == 200