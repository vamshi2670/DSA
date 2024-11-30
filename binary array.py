binary_array=['R', 'A', 'B', 'C', 'D', 'E', 'F', 
              None, None, None, None, None, None, 'G']
def left_child_index(index):
    return 2 * index + 1
def right_child_index(index):
    return 2 * index +1
def get_data(index):
    if 0 <= index < len(binary_array):
        return binary_array[index]
    return None
right_child=right_child_index(0)
left_child_of_right=left_child_index(right_child)
data=get_data(left_child_of_right)
print(data)