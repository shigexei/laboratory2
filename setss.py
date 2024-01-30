fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#"Yes, apple is a fruit!"
  
fruits.add("orange")
print(fruits)
#apple banana cherry orange

more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#apple banana cherry orange mango grapes

fruits.remove('banana')
print(fruits)
#apple cherry orange mango grapes

fruits.discard("cherry")
print(fruits)
#apple orange mango grapes
