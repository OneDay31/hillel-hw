set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}


# 1
res = set_a | set_b | set_c
print(f'#1\nres = {res}')


# 2
res_a_b = set_a - set_b
res_b_c = set_b - set_c
res_a_c = set_a - set_c
print(f'#2\nres_a_b = {res_a_b}\nres_b_c = {res_b_c}\nres_a_c = {res_a_c}')


# 3
res_a_b = set_a & set_b
res_b_c = set_b & set_c
res_a_c = set_a & set_c
print(f'#3\nres_a_b = {res_a_b}\nres_b_c = {res_b_c}\nres_a_c = {res_a_c}')



# 4
set_1 = {1, 2}
print('#4\n', 'является ли set_1 подмножеством set_a = ', set_1.issubset(set_a), '\n', 'является ли set_1 подмножеством set_b = ',
      set_1.issubset(set_b), '\n', 'является ли set_1 подмножеством set_c = ', set_1.issubset(set_c), sep='')


# 5
res_1 = set()
res_2 = set()
for i in res:
    if i % 2 == 0:
        res_1.add(i)
    else:
        res_2.add(i)
print(f'#5\nres_1 = {res_1}\nres_2= {res_2}')
