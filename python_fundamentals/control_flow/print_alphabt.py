#!/usr/bin/env python3
for i in range(97, 123):
    lettre = chr(i)
    if lettre == 'q' or lettre == 'e':
        continue
    print(lettre, end="")
    