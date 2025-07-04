words = ["donkey " , " bad"]

with open("file2.txt") as f:
    content = f.read()
for word in words:
    contentNew = content.replace(words , "******")
                                 
with open("file2.txt" , "w") as f:
    f.write(contentNew)                                
                                 
