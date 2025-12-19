# Negative check function
def find_first_negative(lst):
  i = 0
  j = len(lst)
  while i < j:
    if lst[i] < 0:
      return lst[i]
    i += 1

# Main Function calling to check Negative values in list - Scenario 1
    
neg1 = find_first_negative ([3, 5, -1, 7, -2, 8])

if neg1 == None:
   print("No Negatives")
else:
   print(f'First Negative Value: {neg1}')


# Main Function calling to check Negative values in list - Scenario 2
neg2 = find_first_negative ([2, 10, 7, 0])

if neg2 == None:
   print("No Negatives")
else:
   print(f'First Negative Value: {neg2}')
