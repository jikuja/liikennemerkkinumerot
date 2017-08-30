#!/usb/bin/env python3

import json
import requests
import re
from lxml import html

page = requests.get("http://finlex.fi/fi/laki/ajantasa/1982/19820182")
tree = html.fromstring(page.content)

foos = tree.xpath('//p[@class="py"]/text()')

data_array = []
data_map = {}

for foo in foos:
    if re.match("^\d+\.", foo) or re.match("^\d+ [a-zöäå]\.", foo):
        splitted = foo.split(".")
        num = splitted[0]
        txt = splitted[1]
        data_array.append({"id": num, "value": txt})
        data_map[num] = txt

print(data_array)
print(data_map)

with open("merkit_array.json", "w") as json_file:
    json_file.write(json.dumps(data_array))

with open("merkit_array.js", "w") as json_file:
    json_file.write("liikennemerkitCallback(" + json.dumps(data_array) + ");")

with open("merkit_map.json", "w") as json_file:
    json_file.write(json.dumps(data_map))

with open("merkit_map.js", "w") as json_file:
    json_file.write("liikennemerkitCallback(" +json.dumps(data_map) + ");")

