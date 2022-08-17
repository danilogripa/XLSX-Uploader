import requests


def send(red, os, ag, tp, key, tg, af):
    url = 'http://127.0.0.1:5000/convert'
    myobj = {"red": red, "os": os, "ag": ag, "type": tp, "key": key, "tg": tg, "af": af}
    x = requests.post(url, json=myobj)
    return x.text
