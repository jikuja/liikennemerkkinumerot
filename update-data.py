#!/usb/bin/env python3
import sys

__author__ = "jikuja"
__license__ = "CC0 1.0"
__copyright__ = """<PROGRAM NAME> - <DESCRIPTION>
    Written in 2016 by jikuja

    To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to 
    this software to the public domain worldwide. This software is distributed without any warranty.
    
    You should have received a copy of the CC0 Public Domain Dedication along with this software. 
    If not, see <http://creativecommons.org/publicdomain/zero/1.0/>."
"""

import json
import requests
import re
from lxml import html


def add_data(num, txt):
    data_array.append({"id": num, "value": txt})
    data_map[num] = txt

page = requests.get("http://finlex.fi/fi/laki/ajantasa/1982/19820182")
# TODO: use local cache
tree = html.fromstring(page.content)

foos = tree.xpath('//p[@class="py"]/text()')

data_array = []
data_map = {}

for foo in foos:
    print(foo, end="")
    if re.match("^\d+\.", foo) or re.match("^\d+ [a-zöäå]\.", foo):
        print(" MATCH")
        splitted = foo.split(". ")
        num = splitted[0]
        txt = splitted[1]
        data_array.append({"id": num, "value": txt})
        data_map[num] = txt
    else:
        print("")

# fixes
add_data("173", "Rautatien tasoristeyksen lähestymismerkki")
add_data("174", "Rautatien tasoristeyksen lähestymismerkki")
add_data("175", "Rautatien tasoristeyksen lähestymismerkki")

if len(sys.argv) > 1 and sys.argv[1] == "dry":
    sys.exit(0)

with open("merkit_array.json", "w") as json_file:
    json_file.write(json.dumps(data_array))

with open("merkit_array.js", "w") as json_file:
    json_file.write("liikennemerkitCallback(" + json.dumps(data_array) + ");")

with open("merkit_map.json", "w") as json_file:
    json_file.write(json.dumps(data_map))

with open("merkit_map.js", "w") as json_file:
    json_file.write("liikennemerkitCallback(" +json.dumps(data_map) + ");")



