import camelcase
# Every word 1st Letter will be Capital using camelcase
c=camelcase.CamelCase()
fread=open("sample.txt")
text=fread.read()
text1=c.hump(text)
file=open("sample1.txt","w")
file.write(text1)
file.close()