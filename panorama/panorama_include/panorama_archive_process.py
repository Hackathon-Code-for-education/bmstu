from zipfile import ZipFile, ZipInfo
from PIL import Image
import os, json

from PIL import Image
import os


def crop_and_load(image, cell_size, org, name, index):
    size = image.size
    print("image_size=", size)
    if size[0] % cell_size != 0:
        raise Exception("wrong size: " + str(size) + "need to be multiple " + str(cell_size))
    path = create_directory(org, name, index)

    count = [0, 0]
    count[0] = int(size[0] / cell_size)

    count[1] = size[1] / cell_size
    if int(count[1]) < count[1]:
        count[1] += 1
    count[1] = int(count[1])

    for x in range(count[0]):
        for y in range(count[1]):
            b_image = image.crop((x * cell_size, y * cell_size,
                                  min((x + 1) * cell_size, size[0]), min((y + 1) * cell_size, size[1])))
            b_image.save(path + "/hq/{0}-{1}.jpg".format(x, y))
            print("\r image {0}-{1}.jpg saved".format(x, y), end="")
    print()
    c_image = image.resize((512, size[1] * 512 // size[0]))
    c_image.save(path + "/lq/0-0.jpg")
    print("done")


def create_directory(org, name, index):
    path = [0, 0, 0, 0, 0]
    path[0] = "../uploads/tiles/" + org
    path[1] = "../uploads/tiles/" + org + "/" + name
    path[2] = "../uploads/tiles/" + org + "/" + name + "/" + index
    path[3] = "../uploads/tiles/" + org + "/" + name + "/" + index + "/hq"
    path[4] = "../uploads/tiles/" + org + "/" + name + "/" + index + "/lq"
    for i in path:
        try:
            os.mkdir(i)
        except FileExistsError:
            print("path " + i + " already exist")
    return path[2]


def archive_process(org, archive_path):
    try:
        archive_name = ZipInfo.from_file(archive_path).filename
        create_dir(org, archive_name.split(".")[0])    
        with ZipFile(archive_path, "r") as myzip:
            
            info = myzip.namelist()
            #info = list(map(lambda x: x.split("/")[1] ,info[1:]))
            
            myzip.extractall("./temp")
            image_size = []            
            for i in range(1,len(info)):
                with Image.open("./temp/"+info[i]) as img:
                    image_size = img.size
                    #print(image_size)
                    crop_and_load(img, 512, org, archive_name.split(".")[0], str(i-1))
            setJson(org, archive_name.split(".")[0], info, image_size)
            deleteall(info)
            myzip.close()
        os.remove(archive_path)
    except Exception as e:
        print(e)
            
def setJson(org, r_name, info, image_size):
    f = open("../uploads/tiles/"+org+"/property.json", "r")
    str_in = f.read()
    f.close()
    json_text = json.loads(str_in)
    names = []
    for i in json_text["routes"]:
        names.append(i["name"])
    if r_name not in names:
        json_text["routes"].append({"name":r_name, "count":len(info)-1, "tile_size":[512,512], "size":image_size})
    str_out = json.dumps(json_text)
    
    f = open("../uploads/tiles/"+org+"/property.json", "w")
    f.write(str_out)
    f.close()

def deleteall(info):
    for i in info[1:]:
        os.remove("./temp/"+i)
    os.rmdir("./temp/"+info[0])

def create_dir(org, name):
    path = [0,0]    
    path[0] = "../uploads/tiles/"+org
    path[1] = "../uploads/tiles/"+org+"/"+name
    for i in path:
        try:
            os.mkdir(i)
        except FileExistsError:
            print("path "+i+" already exist")
        
if __name__ == "__main__":
    archive_process("1", "подъезд.zip")
