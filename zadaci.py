#1
#%%
f = open("file2.txt", "w")

f.write("Dobar dan\n")

f.close()
#%%
#2 #3

c=''
f = open("file3.txt","r+")
while c!= "!quit":
    c = input("Unos:  ")
    f.write(c+"\n")

f.seek(0,0)
a = f.read()
print(a)


# %%
#4 #5
f = open("knjige.txt", "r+")

izbor = input('Zelite li unijeti knjigu?\n Odaberite 1  za dodavanje knjiga\n 2 za izlistavanje knjiga\n 3 za izlay iz programa')
while True:
    if izbor == "1":
        x = input('unosi naslov: ')
        if x != '!#quit$':
            f.write('Naslov: ')
            f.write(x)
            x = input('unosi autora: ')
            f.write('\nAutor: ')
            f.write(x)
            x = input('unosi godinu izdanja: ')
            f.write('\nGodina izdanja: ')
            f.write(x)
            x = input('unosi cijenu: ')
            f.write('\nCijena: ')
            f.write(x)
            f.write('\n\n')
          
        izbor = input('Zelite li unijeti knjigu? ')
    elif izbor== "2":
        f.seek(0,0)
        a=f.read()
        print(a)
        break
    elif izbor =="3":
        break

f.close()
# %%
