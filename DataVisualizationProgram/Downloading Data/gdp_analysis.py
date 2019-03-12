import json

from pygal.maps.world import World

filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)
    
gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2016':
        country_name = gdp_dict['Country Name']


