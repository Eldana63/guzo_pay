'''word={"cake":4,"chair":5,"banana":6}

def main():
    print("welcome")
    print("you have: A B C F K I H R")
    dd= input("what do you wanna to do?" )
    if dd=="play":
        while len(word)>0:
            guess=input("guss word ")
            if guess in word.keys():
                if guess=="ABABA":
                    word.clear()
                    print("you won")
                del word[guess]
                print (f"you left {len(word)}")
            else:
                print("you lost")
                ask=input("you wanna stop: ")
                if ask=="yes":
                    break
                else:
                    continue

    elif dd=="check":
        for key,value in word.items():
            print(f"{key} worth {value} point")
    else:
        print("invalid") 

main()



def main():
    n=int(input())
    for _ in range(n):
        print(letter(input(),"mario"))

def letter(reciever,sender):
    return f"""
===========================================
  Dear {reciever}\
  hvcjhsgyfgsxznmpfo'w;eovc,
  to{sender}

"""

main()
'''


def main():
    counts={}
    words = get_words("file.txt")

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    save_counts(counts)

main()    

