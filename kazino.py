import random
chis = random.randint(1,10)
col = random.randint(1,2)

i=0
while i <5:
    i=i+1
    chisint = int(input("vvedite chislo: "))
    colint = int (input('vvedite cvet, 1-red, 2-black: '))
    if chisint < chis:
        print ("chislo bol'she")
        if colint ==col:
            print("cvet pravil'nii")
        else:
            print ("cvet ne tot")
    elif chisint>chis:
        print ("chislo men'she")
        if colint == col:
            print("cvet pravil'nii")
        else:
            print("cvet ne tot")
    elif chisint == chis and colint != col:
        print ("chislo pravil'no, cvet net")
    elif chisint == chis and colint == col:
        print ("vse pravil'no")
        break
    if i <5:
        print ("probui esche")
    else: print ("ti proigral, eto bilo: ",chis,col)
