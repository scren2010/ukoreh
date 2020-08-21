from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
from PIL import Image
import os

"""Получаем модель юзера"""
User = get_user_model()


# class CustomerCategories(models.Model):
#     """Категориии пользователей"""
#     name = models.CharField('Наименование категории', max_length=100)


class Profile(models.Model):
    """Профиль пользователя"""

    user = models.OneToOneField(User, verbose_name='Login', on_delete=models.CASCADE)
    picture = models.CharField('Аватарка из соц сети', max_length=355, blank=True, null=True)
    about = models.TextField('О себе', blank=True, null=True)
    avatar = models.ImageField('Загрузить свою картинку', upload_to='userprofile/', null=True, blank=True)

    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        else:
            return '/static/img/default.png'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

    def __str__(self):
        return f'Profile for: {self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance, id=instance.id)
        instance.profile.save()
