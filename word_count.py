temp_array=[]

#Opening file and copying the contents to a string variable in lowercase letter 
content = open('text.txt', 'r').read().lower()

#Spliting the string without taking special characters and storng it into an array
content_array=[''.join(c for c in word if c.isalpha() or c=="'") for word in content.split()]

#print only the words with count=1 and delete all its instances when a word is checked 
# print(content_array)
print("Count of each words in the file are: ")
for i in content_array:
    if i not in temp_array:
        print (i,": ",str(content_array.count(i)))
        temp_array.append(i)
