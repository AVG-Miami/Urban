def all_variants(text):
    i=0
    while i!=len(text):
        yield text[i]
        i+=1
    yield text[0]+text[1]
    yield text[1]+text[2]
    yield text[0]+text[1]+text[2]

a = all_variants("abc")
for i in a:
    print(i)