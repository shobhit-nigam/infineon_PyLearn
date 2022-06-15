import xml.etree.ElementTree as ET

tree_a = ET.parse('data.xml')
root_a = tree_a.getroot()


for x in root_a:
    tag_text = {}
    for y in x:
        tag_text[y.tag] = y.text
    print(tag_text)
    print("-----")
