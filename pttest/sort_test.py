# -*- coding: utf-8 -*-

a = ["c", "b", "a"]
b = ["12c", "3b5", "23a"]


def get_index_list(para):
    para_in_a = a[0]
    for item in a:
        if item in para:
            para_in_a = item
            break
    return a.index(para_in_a)


c = sorted(b, key=lambda x: get_index_list(x))
b.sort(key=lambda x: get_index_list(x))
print b, c