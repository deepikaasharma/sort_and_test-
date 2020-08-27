"""Complete the function named sort_and_test(). This function will take two parameters, both of which will be lists. Your function should sort the first argument without altering the original list, and then compare the sorted list to the second argument. Your function will return a boolean value, which is the result of the comparison(True or False).

Note:

    We have included a doc string in this function that describes what the function is doing. As well as what each parameter is doing and what should be returned
    Please write your function after the doc string

"""

# # leave these two lines alone
# x = [10, 9, 8, 7, 6, 5]
# y = list(range(5, 11))

# # replace `pass` with the necessary logic
# def sort_and_test(list_1, list_2):
#     '''
#     Tests whether the sorted version of one list is equal to another list.

#     Parameters:
#     ----------
#     list_1 : (list)
#         A list to be sorted.
#     list_2 : (list)
#         The list to be compared.

#     Returns:
#     ----------
#     Bool : (True or False)
#     '''
#     list_1sorted = sorted(list_1)
#     return list_1sorted == list_2


# # leave this line alone
# result = sort_and_test(x, y)

# print(result)


# Complete the below function. Please follow the description in the docstring to do this.

def take_last_element_of_reversed_list(list_1):
    '''
    Reverses the input list and removes the last element of the now
    reversed list and returns that element.

    Parameters:
    ----------
    list_1 : (list)
        A numeric list altered.

    Returns:
    ----------
    int

    '''
    list_1.reverse()
    return list_1.pop()


# leave these lines alone
x = list(range(-10, 11))
result = take_last_element_of_reversed_list(x)

print(result)
