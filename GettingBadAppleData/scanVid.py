from os import listdir
from PIL import Image

size = 20

count = 0
res = "[\n"

for i in range(1,300+1):
    filepath = "./images/"+str(i)+".png"

    with Image.open(filepath) as img: # Size of images = (480, 360)
        img = img.crop((60, 0, 420, 360)) #Left, Up, Right, Down
        img = img.resize((size,size))
        img = list(img.getdata())
        img = [0 if w < 20 else 1 for w,x,y,z in img]

        encoded = []
        for i in range(size):
            num = 0
            for j in range(size):
                if img[i*size+j] == 1:
                    num += 2 ** j
            encoded.append(num)
        res += "\t" + str(encoded) + ",\n"

        count += 1

res = res[:-2] + "\n];"

with open("./output.txt", "w") as output_file:
    output_file.write(res)

print("Total of",count,"frames")