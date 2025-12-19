# Check Divisibile Function
def check_divisibility(num, divisor):
    if isinstance(num,(int,float)) and isinstance(divisor,(int,float)):
       result = num / divisor
       if (result.is_integer()):
            return True
       else:
           return False
    else:
        print (f'Either NUM value {num} or Divisor value {divisor} is not numeric')
        return result

# Main Calling function - Scenario 1 
print(f'Is Number is divisible by divisor: {check_divisibility(10,2)}') 

# Main Calling function - Scenario 2
print(f'Is Number is divisible by divisor: {check_divisibility(7,3)}')
