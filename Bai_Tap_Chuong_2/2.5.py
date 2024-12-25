from xml.dom import minidom

# Tải và phân tích tệp XML
doc = minidom.parse("sample.xml")

# Lấy danh sách các phần tử name
names = doc.getElementsByTagName("name")

# In ra tên của từng phần tử
for name in names:
    print(name.firstChild.data.strip())