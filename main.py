class FlatIterator:

 def __init__(self, list_of_list):
  self._list = list_of_list

 def __iter__(self):
  self.cursor = 0
  self.nested_list = iter([])
  return self

 def __next__(self):
  try:
   return next(self.nested_list)
  except StopIteration:
   if self.cursor == len(self._list):
    raise StopIteration
   main_list = self._list[self.cursor]
   self.cursor += 1
   self.nested_list = iter(main_list)
   return next(self.nested_list)
  return item


# fr = FlatIterator([
#  ['a', 'b', 'c'],
#  ['d', 'e', 'f', 'h', False],
# [1, 2, None]
#  ])
# for item in fr:
#  print(item)

def test_1():

 list_of_lists_1 = [
     ['a', 'b', 'c'],
     ['d', 'e', 'f', 'h', False],
     [1, 2, None]
    ]

 for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
  assert flat_iterator_item == check_item

 assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
 test_1()

