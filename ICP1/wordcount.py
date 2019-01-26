S = input("Enter a string: ")
D = 0
L = 0

for p in S:
    if p.isdigit():
        D = D + 1
    elif p.isalpha():
        L = L + 1
    else:
        pass
print("no. of Letters: ", L)
print("number of words: ", len(S.split()))
print("no. of Digits: ", D)