# update dictionary Function 
def update_dictionary(dct, key, value):
  if key in dct:
    print(f'Key exists {key} in dictionary with value as {dct[key]}')
  dct[key] = value
  return dct

upd1_dict = update_dictionary({},'name','Alice')
print(f'Update 1 Dict: {upd1_dict}')
upd2_dict = update_dictionary({'age': 25}, 'age', 26)
print(f'Update 2 Dict: {upd2_dict}')
