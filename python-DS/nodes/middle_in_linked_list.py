from linked_list import LinkedList

# Complete this function:
def find_middle(linked_list):
  fast_pointer = linked_list.head_node
  slow_pointer = linked_list.head_node
  while fast_pointer.get_value() is not None:
    fast_pointer = fast_pointer.get_next_node()
    print("fast_pointer="+str(fast_pointer.get_value()))
    if fast_pointer.get_value() is not None:
      fast_pointer = fast_pointer.get_next_node()
    #   print("fast_pointer_next="+str(fast_pointer.get_value()))
      slow_pointer = slow_pointer.get_next_node()
      print("slow_pointer="+str(slow_pointer.get_value()))
  return slow_pointer

#time complexity is O(n) and space complexity is O(1)

# ------------------------------------- alternate solution----------------------------------------------------------------

# def find_middle_alt(linked_list):
#   count = 1
#   fast = linked_list.head_node
#   slow = linked_list.head_node
#   while fast.get_value() is not None:
#     fast = fast.get_next_node()
#     if count % 2 != 0:
#       slow = slow.get_next_node()
#     count += 1
#   print(slow,count)
#   return slow

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:

test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)

# test_list = generate_test_linked_list(7)
# print(test_list.stringify_list())
# middle_node = find_middle_alt(test_list)
# print(middle_node.value)
