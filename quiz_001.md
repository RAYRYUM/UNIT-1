```.p
def mysterybox(a,b):
    tr=0
    if a==20 or b==20:
        tr="TRUE"
    elif a+b==20:
        tr="TRUE"
    else:
        tr="FALSE"
    return tr

output=mysterybox(11,9)
print(output)
```
/Users/rayryu/Documents/pythonProject4/bin/python "/Users/rayryu/Library/Application Support/JetBrains/PyCharm2021.2/scratches/scratch_1.pyx"
TRUE

Process finished with exit code 0
