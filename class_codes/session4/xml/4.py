import xml.etree.ElementTree as ET

tree_a = ET.parse('data.xml')
root_a = tree_a.getroot()

for x in root_a:
    for y in x:
        print(y.tag, "=", y.text)
    print("-----")
