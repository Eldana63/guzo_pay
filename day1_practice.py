
'''def FizzBuzz(n):
  for i in range(1,n+1):
     if i%3==0 and i%5==0:
        print("Fizzbuzz")
     elif i % 3==0:
           print("fizz")
     elif i % 5==0:
           print("buzz")
     else:
           print(i)
n=input("Enter a number: ")
FizzBuzz(int(n))

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'''

b=2
c=1
a=4
dis=b**2-4*a*c
if dis>0:
    root1=(-b+dis**0.5)/(2*a)
    root2=(-b-dis**0.5)/(2*a)
    print(root1 & root2)
elif dis==0:
    root1=root2=(-b) /(2*a)
    print(root1)
else:
    print("no real sol")

