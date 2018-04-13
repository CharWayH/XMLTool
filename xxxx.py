# coding=utf-8
import xml.etree.cElementTree as ET

tree = ET.parse('output.xml')
root = tree.getroot()
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank>50 :
        root.remove(country)
tree.write('output1.xml')