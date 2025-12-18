#swap function

def swap(x, y):
    if isinstance(x, (int,float)) and isinstance(y,(int,float)):
        x,y = y,x
        return(x,y)
    else:
        return -1
    

# Main Calling function - Example 1

print(f"Scenario 1: After swapping {swap('Apple', 10)} ")

#Main Calling function - Example 2

print(f"Scenario 2: After Swapping {swap(9, 17)}")