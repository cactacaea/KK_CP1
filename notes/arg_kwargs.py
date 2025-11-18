# KK 2nd *args and **kwargs Notes

def hello(age = 29,name = "Tia"):
    return(f"Hello {name}! You are {age}.")

print(hello())
print(hello("Xavier"))
print(hello(name = "Treyson",age = 19))

# args are when we don't know how many positional arguments to give/there are

# positional arguments, *args, keyword arguments, **kwargs
def hello2(*names, **last):
    print(type(names))
    print(last)
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['v_last']}")
        else:
            print(f"Hello, {name} {last['alast']}")

hello2("Alexander","Kathryn","Andrew","Vienna","Victoria","Treyson","Xavier","Jake", alast = "LaRose", v_last = "Atkin")