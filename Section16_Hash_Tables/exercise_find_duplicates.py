# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#
#     return duplicates
def find_duplicates(nums):
    my_dict = {}
    duplicated_list = []
    for num in nums:
        my_dict[num] = []
    for num in nums:
        my_dict[num].append(num)

    for num in nums:
        if len(my_dict[num]) > 1 and not num in duplicated_list:
            duplicated_list.append(num)

    return duplicated_list


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

