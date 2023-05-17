# def create_an_empty_list():
#     return None

# def create_a_list():
#     return None

# def add_element_to_end_of_list(l, element):
#     return None

# def add_element_to_start_of_list(l, element):
#     return None

# def remove_element_from_end_of_list(l):
#     return None

# def remove_element_from_start_of_list(l):
#     return None

# def retrieve_first_element_from_list(l):
#     return None

# def retrieve_element_from_index(l, index):
#     return None

# def retrieve_last_element_from_list(l):
#     return None




def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(lst, element):
    lst.append(element)

def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)

def remove_element_from_end_of_list(lst):
    lst.pop()

def remove_element_from_start_of_list(lst):
    del lst[0]

def retrieve_first_element_from_list(lst):
    return lst[0]

def retrieve_element_from_index(lst, index):
    return lst[index]

def retrieve_last_element_from_list(lst):
    return lst[-1]


# Example usage
my_list = create_a_list()
print(my_list)

add_element_to_end_of_list(my_list, 5)
print(my_list)

add_element_to_start_of_list(my_list, 0)
print(my_list)

remove_element_from_end_of_list(my_list)
print(my_list)

remove_element_from_start_of_list(my_list)
print(my_list)

first_element = retrieve_first_element_from_list(my_list)
print(first_element)

element_at_index = retrieve_element_from_index(my_list, 2)
print(element_at_index)

last_element = retrieve_last_element_from_list(my_list)
print(last_element)

