# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, AbstractUser
from django.db import models

class From_where(models.Model):
    from_where = models.CharField(max_length=200, verbose_name='Откуда')

    def __unicode__(self):
        return self.from_where

class Where(models.Model):
    where = models.CharField(max_length=200, verbose_name='Куда')

    def __unicode__(self):
        return self.where



class Registr_taxi(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя водителя')
    second_name = models.CharField(max_length=200, verbose_name='Фамилия водителя')
    phone_number = models.CharField(max_length='200', verbose_name='Тел номер водителя')
    car_model = models.CharField(max_length=200, verbose_name='Модель машины')
    car_photo = models.FileField(blank=True,  upload_to='cars_photo', verbose_name='Фото машины')
    car_number = models.CharField(max_length=200, verbose_name='Номер машины')
    price = models.IntegerField(verbose_name='Цена')
    from_where = models.ForeignKey(From_where, verbose_name='От куда')
    where = models.ForeignKey(Where, verbose_name='Куда')
    end_time = models.DateField(verbose_name='Время оканчание заказа')
    about = models.TextField(verbose_name='Еще информация')
    add_time = models.DateField(auto_now=True)
    user = models.ForeignKey(User, blank=True)

    def __unicode__(self):
        return self.name


