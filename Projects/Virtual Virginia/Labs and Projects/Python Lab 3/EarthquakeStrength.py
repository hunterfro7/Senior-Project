#Enter the earthquake size
size = eval(input("Enter the earthquake's richter scale value"))

# decisions to determine what output is associated with 
# the size of the earthquake
# if (size >= 8) then display most structures fall
# if (size >= 7) then display many buildings destroyed
# if (size >= 6) then display many buildings damamged
# if (size >= 4.5) then display damamge to poorly constructed buildings
# else then display nothing happens
if(size >= 8):
    print("most structures fall")
elif(size >= 7):
    print("many buildings destroyed")
elif(size >= 6):
    print("many buildings damamged")
elif(size >= 4.5):
    print("damage to poorly constructed buildings")
else:
    print("nothing happens")
