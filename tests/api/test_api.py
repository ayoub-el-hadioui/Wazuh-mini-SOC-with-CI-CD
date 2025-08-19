import requests

def test_api_health():
    url = "https://your-domain:55000"
    r = requests.get(url, verify=False)
    assert r.status_code == 200
