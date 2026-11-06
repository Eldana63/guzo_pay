'''Amount=50

print("Amount Due:", Amount)
while Amount>0:
    put=int(input("Insert coin: "))
    if put in [25,10,5]:
       Amount-=put
       if Amount<=0:
           print("Changed owe:",- Amount)
       else:
          print("Amount Due:", Amount)
    else:
           print("Amount Due:", Amount)
'''

vowel=['a','e','i','o','u']

ask=input()
for letter in vowel:
     ask=ask.replace(letter,"")
print (ask)


