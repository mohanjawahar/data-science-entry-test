def find_and_replace(val, find_val, replace_val):
    a = list(map(lambda x: replace_val if x == find_val else x, val))
    return a


val1 = find_and_replace([1,2,3,4,2,2],2,5)
print(val1)
val2 = find_and_replace(['apple','banana','apple'],'apple','orange')
print(val2)
