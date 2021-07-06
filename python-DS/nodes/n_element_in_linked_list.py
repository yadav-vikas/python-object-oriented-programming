from linked_list import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker.get_value() is not None:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current

#time complexity is O(n) and space complexity is O(1)


# ------------------------------------- alternate solution----------------------------------------------------------------
# def list_nth_last(linked_list, n):
#   linked_list_as_list = []
#   current_node = linked_list.head_node
#   while current_node:
#     linked_list_as_list.append(current_node)
#     current_node = current_node.get_next_node()
#   return linked_list_as_list[len(linked_list_as_list) - n]

#time complexity is O(n) and space complexity is O(n)

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

