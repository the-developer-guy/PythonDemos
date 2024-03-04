import xml.etree.ElementTree as ET

xml_string = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

root = ET.fromstring(xml_string)
print(root.tag)
for country in root:
    print(country.findtext("rank"))
    for item in country:
        print(item.tag, item.attrib, item.text)

print("XPath examples")
for rank in root.findall("./country/rank"):
    print(rank.text)

for easterns in root.findall(".//*[@direction='E']"):
    print("Eastern:", easterns.tag, easterns.attrib, easterns.text)