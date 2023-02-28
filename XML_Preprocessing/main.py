# import xml.sax
#
# class GestureHandler(xml.sax.ContentHandler):
#     def startElement(self, name, attrs):
#         self.current = name
#         if name == "Gesture":
#             print(f"-- Gesture {attrs['Name']} --")
#
#     def characters(self, content):
#
#
#
# handler = xml.sax.ContentHandler()
# parser = xml.sax.make_parser()
# parser.setContentHandler(handler)

# from bs4 import BeautifulSoup
#
# #Reading the data inside the xml file to a variable under the name data
#
# with open('arrow01.xml', 'r') as f:
#     data = f.read()
#
# Bs_data = BeautifulSoup(data, "xml")
#
# b_unique = Bs_data.find_all('unique')
#
# print(b_unique)

import xml.etree.ElementTree as ET

tree = ET.parse('arrow01.xml')

root = tree.getroot()
print(len(root))
print(root.attrib['Name'])
points = []

for i in range(0, len(root)):
    points.append(root[i].attrib)
print(points)


