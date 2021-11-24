from os import read


f = open("file.txt", "r")

for l in f:
    print(l)

f.close()

#%%
with open("file.txt", "r") as f:
    print(f.read())