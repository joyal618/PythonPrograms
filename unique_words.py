content = open('text.txt', 'r').read().lower()

content_array=[''.join(c for c in word if c.isalpha() or c=="'") for word in content.split()]


for i in content_array:
    if content_array.count(i)==1:
        print (i)
        filter(lambda a: a != i, content_array)