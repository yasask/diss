import requests
import numpy as np
import pandas as pd
import csv


cookielist = []
temp = []

#datalist
##opening the CSV list
with open('tmp.csv', 'rb') as f:
    reader = csv.reader(f)
    data_list = [line for line in reader if line[0]]
    data_dict = {line[0]: line[1] for line in data_list[3000:4000]}

##Truncating a string
def stringTrunc(tuple):
    string = tuple[0]
    return string;


def get_cookie_data(url):
    try:
        if url is None:
            return
        data = requests.get("http://" + url[0], timeout = 2);
        cookie_data = data.cookies;
        val = requests.utils.dict_from_cookiejar(cookie_data)
        if cookie_data.values():
            print("cookie: ", cookie_data.values())
            return cookie_data

    except requests.exceptions.RequestException as e:
        #print("call")

        return

def cookieJar(data_dict):
    jar = []
    for x in data_dict:
        try:
            if x is None:
                continue
            if x is len(x) == 0:
                continue
            data = requests.get("http://" + x, timeout=1)
            jar.append((data.cookies, x))
        except requests.exceptions.RequestException as e:
            continue
    return jar
    #for url in urls:
        #jar.append(requests.get(url).cookies)
    #return jar

def toList(cj):
    if cj is None:
        return
    for cookie, url in cj:
        for attr in cookie:
            temp = []
            temp.append(attr.domain)
            temp.append(attr.secure)
            temp.append(attr.path)
            temp.append(attr.path_specified)
            temp.append(attr.expires)
            temp.append(attr.discard)
            temp.append(attr.port)
            temp.append(attr.port_specified)
            temp.append(data_dict[url])
            cookielist.append(temp)
    return cookielist

#data_list = data_list[10000:20000]


toCSV = toList(cookieJar(data_dict))
df = pd.DataFrame(toCSV)
df.columns=['Url', 'secure', 'path', 'path_specified', 'expires', 'discard', 'port', 'port_specified', 'tracking']
df.to_csv('list6.csv', index=False)
print(df)