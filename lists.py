fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#"banana"

fruits[0] = "kiwi"

print(fruits)

#kiwi, banana, cherry

fruits.append("orange")
print(fruits)

#kiwi, banana, cherry, orange

fruits.insert(1, "lemon")
print(fruits)

#kiwi, lemon, banana, cherry, orange

fruits.remove("banana")
print(fruits)

#kiwi, lemon, cherry, orange

print(fruits[-1])

#orange
fruits1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits1[2:5])

#['cherry', 'orange', 'kiwi']

print(len(fruits))

#4


