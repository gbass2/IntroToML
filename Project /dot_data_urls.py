
import pandas as pd
import urllib.request, json
# with urllib.request.urlopen("https://data.transportation.gov/data.json") as url:
#     data = json.loads(url.read().decode())
#     results = json.dumps(data['dataset'], indent=4)
#     print(results)

dataset = pd.read_csv("http://www.dot.gov/sites/dot.dev/files/docs/Table%206%20Domestic%20Airline%20Fares%20First%20Quarter%202001.csv")

print(dataset)
