numbers = [1, 2, 3, 4, 4, 4, 4]
first, second, *other = numbers

print(first)
print(other)


# dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
