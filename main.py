class FlatIterator:

 def __init__(self, list_of_list):
  self.list_of_list = list_of_list

 def __iter__(self):
  self.list_of_iter = iter(self.list_of_list)
  self.next_list = iter(next(self.list_of_iter))
  return self


 def __next__(self):
  try:
   next_item = next(self.next_list)
  # пробуем получить следующий элемент

  except StopIteration:
   #  если элементы в текущем списке закончились, то выбросится StopIteration
   # значит нам нужно извлечь следующий список из self.list_of_iter и положить в self.next_list
   # получаем слеюущий элемент из нового self.next_list
   return next_item


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

