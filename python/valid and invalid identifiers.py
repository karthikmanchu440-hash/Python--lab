import keyword

identifiers = ["2value", "value_2", "_hidden", "class", "my-var", "MyClass", "total$"]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(name, "-> Valid")
    else:
        print(name, "-> Invalid")
