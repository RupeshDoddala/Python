I = int(input("Enter Start Value:"))
F = int(input("Enter End Value:"))

items = []
for i in range(I,F):
    s = str(i)
    if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0):
        items.append(s)
print( ",".join(items))