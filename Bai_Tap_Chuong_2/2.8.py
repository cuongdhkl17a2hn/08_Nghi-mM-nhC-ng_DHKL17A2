import json

# Đối tượng Python
python_obj = {"ten": "Nguyen Van A", "tuoi": 25, "dia_chi": "Ha Noi"}

# Chuyển đổi đối tượng Python sang chuỗi JSON
json_data = json.dumps(python_obj)

# In ra chuỗi JSON
print(json_data)

# In ra tất cả các giá trị
for value in python_obj.values():
    print(value)