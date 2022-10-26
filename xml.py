import xml.etree.ElementTree as ET
with open('bookstore.xml') as f:
    for line in f:
        print(line.strip())
        
        
        

tree = ET.parse('bookstore.xml')
root = tree.getroot()
print(root.tag)




for child in root:
    print(child.tag, child.attrib)
    
    
    
print(root[0][1].text)



for title in root.iter('title'):
    print(title.attrib)

    
    
file=open("test.txt","w")
file.write("Now the file has more content!")
file.close()



f = open("test.txt", "r")  
print(f.read())   
f.close()



file = open("sample.bin", "wb")
file.write(b"This binary string will be written to sample.bin")
file.close()



file = open("sample.bin", "rb")  # opening a binary file
print(file.read(3))
file.close()



file=open("array.bin","wb")
num=[2,4,6,8,10]
array=bytearray(num)
file.write(array)
file.close()



f=open("array.bin","rb")
num=list(f.read())
print(num)
f.close()
