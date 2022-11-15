def my_zip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]


print('my_zip:')
print(list(zip(range(10), range(15), range(8))) == my_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == my_zip(range(10), range(15), []))
print(list(zip(range(10))) == my_zip(range(10)))


def my_enumerate(iterable, start=0):
    return [(index + start, iterable[index]) for index in range(len(iterable))]


print('my_enumerate:')
print(list(enumerate('1234567890', 1)) == my_enumerate('1234567890', 1))


def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print('my_any:')
print(any([]) == my_any([]))
print(any([True, False]) == my_any([True, False]))
print(any([True, True]) == my_any([True, True]))
print(any([False, False]) == my_any([False, False]))


def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print('my_all:')
print(all([]) == my_all([]))
print(all([True, False]) == my_all([True, False]))
print(all([True, True]) == my_all([True, True]))
print(all([False, False]) == my_all([False, False]))


def my_sum(iterable, /, start=0):
    sum = start
    for item in iterable:
        sum += iterable[item]
    return sum


print('my_sum:')
print(sum(range(10)) == my_sum(range(10)))
print(sum([]) == my_sum([]))


def my_range(start, stop=None, step=1):
    res = []
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            res.append(start)
            start += step
        return res
    else:
        while start > stop:
            res.append(start)
            start += step
        return res


print('my_range:')
print(list(range(10)) == my_range(10))
print(list(range(10, 20)) == my_range(10, 20))
print(list(range(10, 20, 3)) == my_range(10, 20, 3))
print(list(range(20, 10, 3)) == my_range(20, 10, 3))
print(list(range(20, 10, -3)) == my_range(20, 10, -3))
print(list(range(20, 10)) == my_range(20, 10))



def my_map(func, *args):
    res = []
    count_item = len(args)
    min_len_obj = float('inf')
    for obj in args:
        if len(obj) < min_len_obj:
            min_len_obj = len(obj)
    for x in range(min_len_obj):
        if count_item > 1:
            temp_res = []
            for item in args:
                temp_res.append(item[x])
            res.append(func(temp_res))
        else:
            for item in args:
                res.append(func(item[x]))
    return res


print('my_map:')
print(list(map(int, '1234567890')) == my_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == my_map(min, range(10), range(20, 30), range(25, 15, -1)))


def my_filter(func=None, *args):
    res = []
    if func is None:
        for item in args:
            for i in item:
                # print(i)
                if bool(i):
                    res.append(i)
        return res
    else:
        for item in args:
            for i in item:
                if func(i):
                    res.append(i)
        return res


print('my_filter:')
print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == my_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
print(list(filter(lambda a: a % 2 == 0, range(10+1))) == my_filter(lambda a: a % 2 == 0, range(10+1)))