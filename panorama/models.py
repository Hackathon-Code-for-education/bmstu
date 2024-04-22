from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum, Count



def user_directory_path(instance, filename):
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)

def univer_certificate_path(instance, filename):
    return 'univers/user_{0}/{1}'.format(instance.user.id, filename)

def univer_directory_path(instance, filename):
    return 'univers/user_{0}/{1}'.format(instance.user.id, filename)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=200, null=False, blank=False)

    on_moderate = "MO"
    declined = "DE"
    accepted = "AC"

    check_type_choises = {
        on_moderate: "На модерации",
        declined: "Отклонен",
        accepted: "Принят"
    }

    check_type = models.CharField(
        max_length=2,
        choices=check_type_choises,
        default=on_moderate,
    )


class LikeDisManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

class LikeDis(models.Model):
    LIKE = 1
    DISLIKE = -1
    remove = 0
    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится'),
        (remove, 'Убрал голос')
    )

    vote = models.SmallIntegerField(choices=VOTES)
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.PROTECT)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDisManager()

    def __str__(self):
        return f"{self.user.first_name} {self.vote}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=600, null=False, blank=False)

    on_moderate = "MO"
    declined = "DE"
    accepted = "AC"

    check_type_choises = {
        on_moderate: "На модерации",
        declined: "Отклонен",
        accepted: "Принят"
    }

    check_type = models.CharField(
        max_length=2,
        choices=check_type_choises,
        default=on_moderate,
    )

    likes = GenericRelation(LikeDis, related_query_name='answers')
    comments = models.ManyToManyField('Comment', null=True, blank=True, related_name='reviews')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_directory_path,
        blank=False,
        null=False
    )
    birth_date = models.DateField(null=False, blank=False)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)

    base_general = "BG"
    midle_general = "MG"
    higher = "HR"

    education_choices = {
        base_general: "Основное общее",
        midle_general: "Cреднее общее",
        higher: "Высшее"
    }

    education = models.CharField(
        max_length=2,
        choices=education_choices,
        default=base_general,
    )

    student = "ST"
    matriculant = "AB"
    teacher = "TE"
    representative = "RE"

    user_type_choises = {
        student: "Студент",
        matriculant: "Абитуриент",
        teacher: "Преподаватель",
        representative: "Представитель"

    }

    user_type = models.CharField(
        max_length=2,
        choices=user_type_choises,
        default=matriculant,
    )



class University(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)

    image = models.ImageField(
        upload_to=univer_directory_path,
        blank=False,
        null=False
    )
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False, blank=False)

    description = models.CharField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    reviews = models.ManyToManyField('Review', null=True, blank=True, related_name='universities')

    certificate = models.FileField(
        upload_to=univer_certificate_path,
        blank=False,
        null=False
    )


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


