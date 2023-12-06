import requests as r
import json
try:
    with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as fi:
        urls = json.load(fi)
    url_post = urls["pst"]
    url_reg = urls["reg"]
    url_in = urls["in"]
    url_rl = urls["rl"]
    url_func = urls["fn"]
except:
    ip="http://127.0.0.1:5000"
    url_rul = f"{ip}/get/rules"
    url_post = f"{ip}/API/fr2"
    url_get = f"{ip}/API/fr2rd"
    url_reg = f"{ip}/reg/weqff/23rfew"
    url_inp = f"{ip}/in/weqff/23rfew"
    url_fn = f"{ip}/chng/qwdas/2312/fewsd33/s"
    urls = {"pst": url_post, "get": url_get, "reg": url_reg,
            "in": url_inp, "rl": url_rul, "fn": url_fn}
    with open(r"C:/Users/Public/Documents/urls.txt", "w", encoding="UTF-8") as f:
        json.dump(urls, f)

class Send_ms:
    """This class sending message"""

    def __init__(self, url_post=url_post, url_reg=url_reg, url_in=url_in, url_rl=url_rl, url_func=url_func):
        self.url_post = url_post
        self.url_reg = url_reg
        self.url_in = url_in
        self.url_rl = url_rl
        self.url_func = url_func

    def send(self, text, id,name,password):
        r.post(f"{self.url_post}/{id}", json={'messange': text,"name":name,"password":password})

    def reg(self, name, password):
        return r.post(self.url_reg, json={"name": name, "password": password}).text

    def ins(self, name, password):
        if r.post(self.url_in, json={"name": name, "password": password}).text == "Sucs":
            return "sc"
        else:
            return "bad"

    def get_rl(self, name, password):
        return r.post(self.url_rl, json={"name": name, "password": password}).json()

    def funcs(self, js):
        return r.post(self.url_func, json=js).text
    
    def change_ip(self):
        with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as fi:
            urls = json.load(fi)
        self.url_post = urls["pst"]
        self.url_reg = urls["reg"]
        self.url_in = urls["in"]
        self.url_rl = urls["rl"]
        self.url_func = urls["fn"]
