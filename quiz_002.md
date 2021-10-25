```.p
def mysterybox(a,b,c):
    tr=0
    tr= a-b
    if b-c > tr:
        tr=b-c
    if b-a>tr:
        tr=b-a
    if c-b>tr:
        tr=c-b
    return tr
```
