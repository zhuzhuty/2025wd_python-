"""
Created on 2025-01-08
"""

# Your code starts here
# 字典
info_dict = {'name': 'xiaoming', 'age': 18, 'height': 1.75}
print(info_dict.keys())
print(info_dict.values())
print(info_dict.items())
print(info_dict)

xiaoming_dict = {'name': 'xiaoming'}
xiaoming_dict['age'] = 18
xiaoming_dict['name'] = '小明'

#xiaoming_dict.pop('age')
del xiaoming_dict['age']
print(xiaoming_dict)

temp_dict = {'name': 'xiaoming', 'age': 18}
xiaoming_dict.update(temp_dict)  # update如果有相同的key,会覆盖
print(xiaoming_dict)
# 字典遍历
print('-'* 100)
for item in info_dict.items():
    print(item)
