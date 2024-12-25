import json

# Dữ liệu JSON
json_data = '{"ten": "Nguyen Van A", "tuoi": 25, "dia_chi": "Ha Noi"}'

# Chuyển đổi JSON thành đối tượng Python
python_obj = json.loads(json_data)

# In ra đối tượng Python
print(python_obj)