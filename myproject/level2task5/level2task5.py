    ##  File Manipulation  ##
file= open("collec.txt","r")
total=dict()
for i in file:
    i = i.strip()
    i = i.lower()
    words=i.split(" ")
    for j in words:
        if j in total:
            total[j]= total[j] + 1
        else:
            total[j] = 1
file.close()         
sorted_words= sorted(total.items(),key=lambda x: x[0])
for word, count in sorted_words:
    print(f"{word} : {count}")
