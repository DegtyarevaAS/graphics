n = int(input())
cl = 30000

for i in range(n):
    inp = str(input())
    if inp[len(inp)-1::] == '3' and int(inp) < cl:
        cl = int(inp)

print(cl)
