import xml.etree.ElementTree as ET

tree_a = ET.parse('data.xml')
root_a = tree_a.getroot()

print(root_a)
print(root_a.tag)
print(root_a.attrib)

print(tree_a)
