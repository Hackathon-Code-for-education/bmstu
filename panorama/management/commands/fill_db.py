import datetime
import random

from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from panorama.models import *


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными данными'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help=u'Количество создаваемых объектов')

    def handle(self, *args, **kwargs):
        """
        пользователей — равное ratio;
        вопросов — ratio * 10;
        ответы — ratio * 100;
        тэгов - ratio;
        оценок пользователей - ratio * 200;
        """
        total = kwargs['ratio']
        fake = Faker()
        # images_pack = "vk_web/static/img/test"
        last_user_id = 1
        el = User.objects.last()
        if el is not None:
            last_user_id = el.id


        for i in range(total):
            try:
                name = fake.name().split(" ")
                user = User.objects.create_user(username=get_random_string(length=10), email=fake.email(),
                                                password='123',
                                                first_name=name[0], last_name=name[1])

                filename = 'test/' + str(random.randint(1, 7)) + '.jpeg'
                profile = Profile.objects.get_or_create(user=user)[0]
                profile.image = filename
                profile.birth_date = datetime.date.today()
                profile.phoneNumber = "89679083457"
                profile.education = "MG"
                profile.user_type = "AB"
                profile.save()

            except Exception as e:
                continue

        for i in range(total//5):

            univer = University.objects.create()


            admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
            name = models.CharField(max_length=200, null=False, blank=False)

            image = models.ImageField(
                upload_to=user_directory_path,
                blank=True,
                null=True
            )
            phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
            phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False,
                                           blank=False)

            description = models.CharField(max_length=500, null=False, blank=False)
            created = models.DateTimeField(auto_now_add=True)
            modified = models.DateTimeField(auto_now=True)

            reviews = models.ManyToManyField('Review', null=True, blank=True, related_name='universities')

            verified = "VF"
            no_verified = "NF"
            on_moderate = "MO"
            declined = "DE"

            check_type_choises = {
                verified: "Верифицирован",
                no_verified: "Не Верифицирован",
                on_moderate: "На модерации",
                declined: "Отклонен",
            }

            check_type = models.CharField(
                max_length=2,
                choices=check_type_choises,
                default=no_verified,
            )




