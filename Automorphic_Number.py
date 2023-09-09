n=int(input())
s=n**2
n_string = str(n)
s_string = str(s)
if s_string.endswith(n_string):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")