dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}
# 1
res = dict_a | dict_b
print(f'#1\nres = {res}')

# 2
res_1 = dict(zip(dict_a.keys(), dict_b.values()))
print(f'#2\nres = {res_1}')



# 3
res_2 = dict(zip(dict_b.values(), dict_a.keys()))
print(f'#3\nres = {res_2}')

# 4
res_3 = {}
for keys, values in res.items():
    number = int(keys.split('_')[-1])
    if number % 2 != 0:
        res_3[keys] = values
print(f'#4\nres = {res_3}')



# 5
set_a = set(dict_a.items())
set_b = set(dict_b.items())
set_c = set(dict_c.items())
res = {'dict_a': len(set_a & set_c), 'dict_b': len(set_b & set_c)}
print(f'#5\nres = {res}')
