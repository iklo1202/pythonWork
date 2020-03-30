from urllib.request import urlopen, urlretrieve
import json
import os

# range(12) == range(0, 12)
for m in range(12):
    url = "https://www.google.com/doodles/json/2020/" + str(m + 1) + "?hl=zh_TW"
    response = urlopen(url)

    #print(response.read())

    doodles = json.load(response)
    print(doodles)

    dirname = "doodles/" + str(m + 1) + "/"
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    #doodles -> List d -> Dictionary
    times = 0
    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)

        fname = "doodles/" + str(m + 1) + "/" +  url.split("/")[-1]
        urlretrieve(url, fname)