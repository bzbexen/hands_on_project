sentence = input("Please enter your sentence : ")
count = {}

for i in sentence:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
        
print(count)
        
