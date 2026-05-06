#!/usr/bin/env python3
result = ""
for i in range(97, 123):
    lettre = chr(i)
    if lettre == 'q' or lettre == 'e':
        continue
    result += lettre
print("{}".format(result), end="")