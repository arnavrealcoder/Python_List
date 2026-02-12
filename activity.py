lst_fruit = ['apple', 'Guava', 'Mango', 'Banana','Kiwi']
print("Length of List:", len(lst_fruit))
print("First Element:", lst_fruit[0])
print("Last Element:", lst_fruit[-1])

lst_fruit.append('Papaya')
print("Updated List :", lst_fruit)

lst_fruit.remove('Guava')
print("Updated List :", lst_fruit)

lst_fruit.sort()
print("Sorted List :", lst_fruit)

lst_fruit.pop(1)
print("Updated List :", lst_fruit)

lst_fruit.reverse()
print("Reversed List :", lst_fruit)

print("Multiplication on list :", lst_fruit*2)

lst_fruit = lst_fruit[:4]
print("Sliced List :", lst_fruit)

lst_fruit.clear()
print("Updated List :", lst_fruit)