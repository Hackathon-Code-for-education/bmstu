from PIL import Image

def panorama_crop_and_load(image, cell_size, org, name, index):
    size = image.size()
    if size[0]%cell_size !=0:
        raise Exception("wrong size: "+str(size)+"need to be multiple "+str(cell_size))

    path = create_directory(org, name, index)

    for x in range(int(size[0]/cell_size)):
        t = size[0]/cell_size
        if int(t) < t:
            t = int(t)+1
        for y in range(t):
            b_image = image.crop((x*cell_size, y*cell_size, 
                      min((x+1)*cell_size, size[0]),min((y+1)*cell_size, size[1])))
            b_image.save(path+"{0}-{1}.jpg".format(x,y))
    c_image =  


def create_directory(org, name, index):
    path = [0,0,0]    
    path[0] = "../uploads/tiles"+org
    path[1] = "../uploads/tiles"+org+"/"+name
    path[2] = "../uploads/tiles"+org+"/"+name+"/"+index
    for i in path:
        try:
            os.mkdir(i)
        except FileExistError:
            print("path "+i+" already exist")
