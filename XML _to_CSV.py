# A program to parse the Paloalto Firewall's .XML configuration file into CSV file

"""
Paloalto firewall's settings/configurations can be inported into .XML format, but this format is not straightforward to many of the consumers.
Have written a script that converts a XML file into CSV (be aware that only few important fields are considered for conversion as requested)

pre-requisites:

1, Modules loaded are xml and csv
2, Install python 3.0+ to facilidate the use of "|" operator which helps in merging the dictionaries
"""

import csv
import xml.etree.ElementTree as ET

#Code to parse the .XML file and get the root element
tree = ET.parse('/home/rock/Desktop/Up Work Projects/XML_extract_ data/Paloalto_firewall_conf.xml')
root = tree.getroot()

#Series of FOR loops to iterate over various elements to extract their Tags, Attributes and Texts
for domain in root.iter('domain'):
    result_domain_tag = domain.tag
    result_domain_attrib = domain.attrib
    result_domain_text = domain.text
    dict_1 = {result_domain_tag : result_domain_attrib['type']}

for name in root.iter('name'):
    result_name_tag = name.tag
    result_name_attrib = name.attrib
    result_name_text = name.text
    dict_2 = {result_name_tag : result_name_text}

for os in root.iter('os'):
    result_os_tag = os[0].tag
    result_os_attrib = os[0].attrib
    result_os_text = os[0].text
    dict_3 = {result_os_tag : result_os_attrib['arch']}

for input in root.iter('input'):
    result_input_tag = input.tag
    result_input_attrib = input.attrib
    result_input_text = input.text
    dict_4 = {result_input_tag : result_input_attrib['type']}

for graphics in root.iter('graphics'):
    result_graphics_tag = graphics.tag
    result_graphics_attrib = graphics.attrib
    result_graphics_text = graphics.text
    dict_5 = {result_graphics_tag : result_graphics_attrib['type']}

#Combine dictionaries into single dictionary

consolidated_dict = {**dict_1,**dict_2,**dict_3,**dict_4,**dict_5}

#Convert the dictionary into CSV data

with open('controller.csv', 'w') as f:
    w = csv.DictWriter(f, consolidated_dict.keys())
    w.writeheader()
    w.writerow(consolidated_dict)