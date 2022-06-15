import xml.etree.ElementTree as ET

tree_a = ET.parse('data.xml')
root_a = tree_a.getroot()

print(root_a[0].tag)
print(root_a[0].attrib)

print(len(root_a))
