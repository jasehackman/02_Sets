
# 1
showroom = set()

# 2
showroom.update(["accord", "element", "tundra", "camero"])
# 3
print(showroom)

#4
showroom.add("accord")

#5
print(showroom)

#6
showroom.update({"winstar", "viper"})
print(showroom)

#7
showroom.discard("accord")
print(showroom)

#**************************************************
#1
junkyard = {"car1", "car2", "car3", "viper", "winstar"}

#2
print(junkyard.intersection(showroom))

print(junkyard)
#3

new_showroom = showroom.union(junkyard)
print(new_showroom)

#4
junkyard.discard("car1")
junkyard.discard("car2")
junkyard.discard("car3")
print(junkyard)