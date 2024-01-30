car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Mustang

car["year"] = 2020

print(car.get("year"))

#2020
car["color"] = "red"
print(car)
#brand : ford model : mustang year : 2020 color :red
car.pop("model")
print(car)
#brand : ford year : 2020 color :red

car.clear()
print(car)
#{}
