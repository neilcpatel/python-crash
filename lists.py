bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
bicycles[0] = "Cobra"
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
bicycles.append("Trek")
print(bicycles)
bicycles.insert(0, "Yamaha")
print(bicycles)
del bicycles[0]
print(bicycles)
popped_bicycles = bicycles.pop()
print(popped_bicycles)
message = f"My last bicycle was a {popped_bicycles.title()}"
print(message)
first_owned = bicycles.pop(0)
message = f"My first bicycle was a {first_owned.title()}"
print(message)
bicycles.remove("specialized")
print(bicycles)
