# coding=utf-8
from xml.etree.cElementTree import Element,SubElement,ElementTree
# 生成根节点
root = Element('root')

# 生成第一个子节点 head
head = SubElement(root, 'head')
# head 节点的子节点
title = SubElement(head, 'title')
title.text = 'Well Tiffany!'
# 生成 root 的第二个子节点 body
body = SubElement(root, 'body')
body.text = 'I love Tiffany!'

#把内容放入XML树中
tree = ElementTree(root)
#输出XML
tree.write('Tiffany.xml',encoding='utf-8')