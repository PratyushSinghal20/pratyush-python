word = "donkey"

with open("file2.txt") as f:
    content = f.read()

    contentNew = content.replace(word , "******")
                                 
with open("file2.txt" , "w") as f:
    f.write(contentNew)                                
                                 
