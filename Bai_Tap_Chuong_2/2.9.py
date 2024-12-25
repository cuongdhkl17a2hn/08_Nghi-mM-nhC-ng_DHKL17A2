import json

# Đối tượng từ điển Python
python_dict = {"dia_chi": "Ha Noi", "tuoi": 25, "ten": "Nguyen Van A"}

# Sắp xếp từ điển theo khóa và chuyển đổi sang JSON
sorted_json = json.dumps(python_dict, indent=4, sort_keys=True)

# In ra chuỗi JSON với mức thụt lề 4
print(sorted_json)
