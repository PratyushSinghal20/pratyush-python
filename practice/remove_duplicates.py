def remove_duplicates(original_list):
    unique_list = []
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 3, 2, 4, 1, 5, 3, 6]
result = remove_duplicates(my_list)
print("Original List:", my_list)
print("List after removing duplicates:", result)
