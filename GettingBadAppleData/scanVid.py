from os import listdir
from PIL import Image

depth = 7
size = 2**depth

count = 0
res = []

def checkSame(array):
    val = array[0]

    for i in array:
        if i != val:
            return False
    
    return True

def splitArr4(array, _size):
    chunks = [array[i:i+_size//2] for i in range(0, len(array), _size//2)]

    res = [[], [], [], []]

    for i in range(0, _size,2):
        res[0].extend(chunks[i])
        res[1].extend(chunks[i+1])
    
    for i in range(_size, _size*2,2):
        res[2].extend(chunks[i+1])
        res[3].extend(chunks[i])

    return res

def makeQuadTree(array, _size):
    if checkSame(array):
        return str(array[0])
    
    splits = splitArr4(array, _size)
    output = "2"
    for split in splits:
        output += makeQuadTree(split, _size//2)

    return output

res = "[\n"
count = 0

for i in range(1,801):
    filepath = "D:/BackedUp/Projects/2408_NUS_CS1101S_Source_Academy_Runes_BadApple/NUS-CS1101S-Source-Academy-Runes-Bad-Apple/GettingBadAppleData/frames/"+str(i)+".png"

    with Image.open(filepath) as img: # Size of images = (480, 360)
        img = img.crop((60, 0, 420, 360)) #Left, Up, Right, Down

        img = img.resize((size,size))
        img = list(img.getdata())
        img = [0 if w < 20 else 1 for w,x,y,z in img]
        #print(img)

        out = makeQuadTree(img, size)
        #print(out)

        res += "\t\"" + out + "\",\n"

        count += 1

res = res[:-2] + "\n]"

with open("GettingBadAppleData/output.txt", 'w') as outputFile:
    outputFile.write(res)

print("Encoded "+str(count)+" frames")


        
        

    
