from django.core.files.storage import FileSystemStorage


from panorama.models import Profile

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

