import json

with open('cities.geojson') as f:
    geojson = json.load(f)

labels = []
for feature in geojson['features']:
    labels.append(feature['properties']['name:km'])

with open('labels.json', 'w') as f:
    json.dump(labels, f, indent=2)
    