# 1. print a list of integers

def print_list_integer(my_list = []):
    for i in range(len(my_list)):
        print('{:d}'.format(my_list[i]))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

# 2. Secure access to an element in a list
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# 3. Replace element
def replace_in_list(my_list, idx, new_element):
    if idx < 0 or idx > len(my_list):
        return my_list
    my_list[idx] = new_element
    return (my_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

def print_reversed_list_integer(my_list=[]):
    """ prints a list in reverse"""
    if my_list is None:
        return None
    start = len(my_list) -1  
    reversed = [my_list[i] for i in range(start, -1, -1)]
    print(reversed)

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)



