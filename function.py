def greetHello(name, ending):
    print("Hello " + name)
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

def letterGenerator(name, date):
    st = f"Hi mam, \nThis is {name} and I will not come to school on {date}"
    print(st)

def average(a, b):
    return (a+b)/2

print("Executing function...")
greetHello("Amit", "Thank You")
greetHello("Shivam", "Thanks")
letterGenerator("Amit","26th nov")
letterGenerator("Subham", "4th oct")
print(average(34,23))
print("done")