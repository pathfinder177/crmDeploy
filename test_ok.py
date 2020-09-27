import requests

def test_answer():
    URL = "http://192.168.16.100"
    r = requests.get(url = URL)
    sc = r.status_code
    assert sc == 200