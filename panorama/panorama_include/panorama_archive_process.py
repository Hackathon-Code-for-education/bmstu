import panorama_crop
from zipfile import ZipFile, ZipInfo
from PIL import Image
import os, json

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
                    panorama_crop.crop_and_load(img, 512, org, archive_name.split(".")[0], str(i-1))
            setJson(org, archive_name.split(".")[0], info, image_size)
            deleteall(info)
            myzip.close()
        os.remove(archive_path)
    except:
        print(exception)
            
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
