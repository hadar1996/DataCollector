from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests
from importlib.metadata import version
import csv
import json
import pandas as pd
from datetime import datetime
import calendar
import time
import datetime

# import urls of product list
# data = open("C:\Users\Hadar Snir\Documents\urls.csv")
# product = csv.reader(data)

# passing all over the products and get the relevant data we need.
# for url in product:
# access to data in url by html file
url = 'https://www.cisco.com/c/en/us/support/routers/910-industrial-router/model.html'
results = requests.get(url)
doc = BeautifulSoup(results.content, "html.parser")
vendor = 'https://www.cisco.com'
url = url
series = doc.find('a', class_='birth-cert-series').text
category = doc.select('td')[1].text
# the path define as metadata, I success to extract it but with error message.
# metas = metadata_parser.MetadataParser(url)
# path = metas.get_metadata('iaPath')
model = doc.find('h1').text
release = doc.select('td')[3].text
endofsale = doc.select('td')[4].text.rstrip().lstrip()
endofsupport = doc.find('td', class_='eosHighlight').text.rstrip().lstrip() # V
data = {
        "vendor": vendor,
        "url": url,
        "series": series,
        "category": category,
        "model": model,
        #"path":
        "release": release,
        "endofsale": endofsale,
        "endofsupport": endofsupport
    }

# convert into JSON:
JsonMode = json.dumps(data)

# the result is a JSON string:
#print(JsonMode)

# from Json to CSV - to comfortable using
pdObj = pd.read_json(JsonMode, orient='index')
csvData = pdObj.to_csv(index=False)
#print(csvData)






