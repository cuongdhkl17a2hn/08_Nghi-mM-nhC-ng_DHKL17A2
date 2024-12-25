from xml.dom import minidom

# Tải và phân tích tệp XML
doc = minidom.parse("sample.xml")

# In ra nội dung gốc của tệp XML
print(doc.toprettyxml(indent="  "))