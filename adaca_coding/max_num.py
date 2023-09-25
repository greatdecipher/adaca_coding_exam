# 1. Python Fundamentals

# 1.1. Complete the function below.
def max_repeat(numbers):
    """
    Given a list of integers, return the integer with the maximum number of repeated digits.
    """
    number_of_occurences_list = []
    for num in numbers:
        count = 0
        str_num = str(num)  # Convert the number to a string
    
        for i in range(len(str_num)): 
            for j in range(i+1, len(str_num)):
                if str_num[i] == str_num[j]: 
                    count += 1                  # counter of times a number string repeats itself
    
        number_of_occurences_list.append(count)  #append to a list
    
    # Now we find the max count, then get the index and use it as an index for the 'numbers' list
    return numbers[number_of_occurences_list.index(max(number_of_occurences_list))]

if __name__ == "__main__":
    """Python Fundamentals 1.1, run code below"""
    print(max_repeat([123, 1123, 332, 4445, 5566]))
    assert max_repeat([123, 1123, 332, 4445, 5566]) == 4445

