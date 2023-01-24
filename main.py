class FlatIterator:

 def __init__(self, list_of_list):
  self.list_of_list = list_of_list

 def __iter__(self):
  self.list = iter(self.list_of_list)
  self.next_list = next(self.list)
  self.list_of_iter = iter(self.next_list)
  # self.next_list = next(self.list_of_iter)
  self.flat_list = []
  return self

 def __next__(self):
  if self.next_list is None:
   raise StopIteration
  else:
   # self.next_list = next(self.list)
   # self.list_of_iter = iter(self.next_list)
   item = next(self.list_of_iter)

  return item

fr = FlatIterator([
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
[1, 2, None]
 ])
for item in fr:
 print(item)

# def test_1():
#
#  list_of_lists_1 = [
#  ['a', 'b', 'c'],
#  ['d', 'e', 'f', 'h', False],
# [1, 2, None]
#  ]
#
#  for flat_iterator_item, check_item in zip(
#  FlatIterator(list_of_lists_1),
# ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#  ):
#
#  assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# if __name__ == '__main__': test_1()

