def say_hi(name:str, age:int):
    if age < 0:
        return "Age error"
    if name == "":
        return "name error"
    return f"Hi. My name is {name} and I'm {age} years old"

print(say_hi("Alex", 20))
print(say_hi("Frank", 18))