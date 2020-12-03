import os
def fileopen(data):
     
    with open(data,'r',encoding='UTF8') as file:
    
        text = file.read()
        
        splitdata = text.split()
        
    return len(splitdata)

dir_path = "/Users/yujin/Documents/2020-2/SemanticWebService/termproject/semantic-web/data/raw/"

text_length = 0
for i in range(1):
    if i < 10:
        text_file_path = os.path.join(dir_path,"0{}.txt".format(i))
    else:
        text_file_path = os.path.join(dir_path,"{}.txt".format(i))
    text_length += fileopen(text_file_path)

print(text_length)