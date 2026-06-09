S1 = input()
S2 = input()

pos = S1.rfind(S2)

if pos != -1:
    S1 = S1[:pos] + S1[pos + len(S2):]

print(S1)