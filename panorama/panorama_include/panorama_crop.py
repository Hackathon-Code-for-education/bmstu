from PIL import Image
import os

def crop_and_load(image, cell_size, org, name, index):
    size = image.size
    print("image_size=", size)
    if size[0]%cell_size !=0:
        raise Exception("wrong size: "+str(size)+"need to be multiple "+str(cell_size))
    path = create_directory(org, name, index)
    
    count = [0,0]
    count[0] = int(size[0]/cell_size)

    count[1] = size[1]/cell_size
    if int(count[1]) < count[1]:
        count[1]+=1
    count[1] = int(count[1])


    for x in range(count[0]):
        for y in range(count[1]):
            b_image = image.crop((x*cell_size, y*cell_size, 
                      min((x+1)*cell_size, size[0]),min((y+1)*cell_size, size[1])))
            b_image.save(path+"/hq/{0}-{1}.jpg".format(x,y))
            print("\r image {0}-{1}.jpg saved".format(x,y), end="")
    print()
    c_image =  image.resize((512, size[1]*512//size[0]))
    c_image.save(path+"/lq/0-0.jpg")
    print("done")


def create_directory(org, name, index):
    path = [0,0,0,0,0]    
    path[0] = "../uploads/tiles/"+org
    path[1] = "../uploads/tiles/"+org+"/"+name
    path[2] = "../uploads/tiles/"+org+"/"+name+"/"+index
    path[3] = "../uploads/tiles/"+org+"/"+name+"/"+index +"/hq"
    path[4] = "../uploads/tiles/"+org+"/"+name+"/"+index + "/lq"
    for i in path:
        try:
            os.mkdir(i)
        except FileExistsError:
            print("path "+i+" already exist")
    return path[2]
