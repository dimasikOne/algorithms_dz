def get_letters(num):
    if num==2:
        return ['a','b','c']
    elif num==3:
        return ['d', 'e', 'f']
    elif num==4:
        return ['g','h','i']
    elif num==5:
        return ['j','k','l']
    elif num==6:
        return ['m','n','o']
    elif num==7:
        return ['p','q','r','s']
    elif num==8:
        return ['t','u','v']
    elif num==9:
        return ['w','x','y','z']

def decart_mult(left, right):
    answ=[]
    index=0
    for i in left:
        for j in right:
            answ.insert(index, str(i)+str(j))
            index=index+1
    return answ;

print("Enter a string of numbers: ")
num=input()
mas=[]
letters=[]
index=0
for i in num:
    mas.insert(index,int(i))
    index=index+1

index=0
for i in mas:
    letters.insert(index, get_letters(i))
    index=index+1

answ=letters[0]
i=1
while i<len(letters):
    temp=decart_mult(letters[i],answ)
    answ=temp
    i=i+1
print(answ)

