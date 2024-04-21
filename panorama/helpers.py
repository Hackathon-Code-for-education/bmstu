from django.core.files.storage import FileSystemStorage


from panorama.models import Profile
from panorama.panorama_include.panorama_archive_process import archive_process



def add_image_profile(user, request):
    file = request.FILES['image']
    fs = FileSystemStorage()
    path = "users/user_" + str(user.id) + "/avatar." + str(file.name).split(".")[1]
    if fs.exists(path):
        fs.delete(path)

    filename = fs.save("users/user_" + str(user.id) + "/avatar." + str(file.name).split(".")[1], file)
    # file_url = fs.url(filename)
    profile = Profile.objects.get_or_create(user=user)[0]
    profile.image = filename
    profile.save()


def add_zip_file(user, form) -> (bool, str):
    try:
        data = form.cleaned_data
        file = data['file']
        title = data['title']

        fs = FileSystemStorage()
        path = f"tiles/{user.id}-{title}.zip"

        if fs.exists(path):
            fs.delete(path)


        filename = fs.save(path, file)
        file_url = fs.url(filename)


        archive_process("1", "panorama/"+file_url, "panorama/uploads/tiles/")

        print(file_url)

        return (True, file_url)
    except Exception as e:
        print(e)
        return (False, " ")


