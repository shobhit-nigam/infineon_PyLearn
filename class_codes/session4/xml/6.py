import xml.etree.ElementTree as ET

tree_a = ET.parse('data.xml')
root_a = tree_a.getroot()

fa = open("books_xml.txt", "w")

for x in root_a:
    fa.write(x[0].tag + " = " + x[0].text + "\n")
    fa.write(x[1].tag + " = " + x[1].text+ "\n")
    fa.write("-"*10 + "\n")

fa.close()
