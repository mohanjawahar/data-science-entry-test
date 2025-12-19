# String reverse function
def string_reverse(s):
  rs = s[::-1]
  return rs

# Main Calling function - Scenario 1
rs1 = string_reverse("Hello World")
print(f'Reversed String value: {rs1}')

# Main Calling function - Scenario 2
rs2 = string_reverse("Python")
print(f'Reversed String value: {rs2}')
