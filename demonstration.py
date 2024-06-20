import debug_logger as DL
from typing import List, Optional

@DL.function_logger
def experimental_function(arr: List[int], even: Optional[bool] = True):
    
    """
    experimental_function reqiures an list "arr" of integers, 
    and the boolean "even" is True by default. If true, 
    experimental_function will evaluate all elemets of the 
    list for even values and return only the even values. If 
    false, it will return the odd values instead.
    """
    
    new_arr = []
    
    if even == True:
        for x in arr:
            if x % 2 == 0:
                new_arr.append(x)
    if even == False:
        for x in arr:
            if x % 2 == 1:
                new_arr.append(x)
    
    return new_arr

@DL.function_logger
def error_function(arr: List[int]):      # returns list of tuples that are floor div & div 2 of x
    new_arr = [(x//2, x/2) for x in arr]
    return new_arr

@DL.function_logger
def second_error(arr: List[int], ind: int):  # raises error if value at index less than 10
    if arr[ind] >= 10:
        return "You got 10 or more! Good Job!"
    else: 
        # raise ValueError("You got less than 10, how sad...")
        raise ZeroDivisionError("You got less than 10, how sad...")

numbers = [x for x in range(1,26)]

not_nums = "Hello World!"

if __name__ == "__main__":
    print(experimental_function(numbers, even=False))
    
    print(error_function(numbers))
    
    print(error_function(not_nums))  # expecting TypeError
    
    print(second_error(numbers, 12))
    
    print(second_error(numbers, 4))  # Expecting error of type uncommented in function def