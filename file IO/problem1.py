f = open("poem.txt")
content = f.read()

if("twinkle" in  content):
    print("Yes, twinkle is present in the file")
else:
    print("No, twinkle is not present in the file")

f.close()