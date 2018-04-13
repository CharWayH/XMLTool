# coding=utf-8
import xml.etree.cElementTree as ET
#生成XML
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
a.write('out.xml')