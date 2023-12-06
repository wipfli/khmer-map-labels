import json

with open('cities.geojson') as f:
    geojson = json.load(f)

with open('encoded_labels.json') as f:
    encoded_labels = json.load(f)

for i, feature in enumerate(geojson['features']):
    feature['properties']['name:km_encoded'] = encoded_labels[i]

with open('cities_encoded.geojson', 'w') as f:
    json.dump(geojson, f, indent=2)
