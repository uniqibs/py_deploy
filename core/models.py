from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class UserCategoryPublishes(models.Model):
    PRODUCT_CATEGORIC = [
        ('ТЕХНИКА', 'ТЕХНИКА'),
        ('ОДЕЖДА','ОДЕЖДА'),
        ('ДОМ','ДОМ'),
        ('БИСНЕС','БИЗНЕС'),
        ('ЕДА','ЕДА'),
        ('ДРУГОЕ','ДРУГОЕ')
    ]
    COUNTRI = [
        ('Абхазия','Абхазия'), 
        ('Австралия','Австралия'),
        ('Австрия','Австрия'), 
        ('Азербайджан','Азербайджан'),
        ('Албания','Албания'),
        ('Алжир','Алжир'),
        ('Андорра','Андорра'),
        ('Аргентина','Аргентина'),
        ('Армения','Армения'),
        ('Аруба','Аруба'),
        ('Афганистан','Афганистан'),
        ('Багамы','Багамы'),
        ('Бангладеш','Бангладеш'),
        ('Барбадос','Барбадос'),
        ('Великобритания','Великобритания'),
        ('Германия','Германия'),
        ('Грузия','Грузия'),
        ('Катар','Катар'),
        ('Канада','Канада'),
        ('Россия','Россия'),
        ('Россия','Россия'),
        ('США','США'),
        ('Узбекситан','Узбекситан'),
        ('Украина','Украина'),
        ('Швейцария','Швейцария'),
        ('Швеция','Швеция')
    ]
    NORM_OR_BAD = [
        ('В ОТЛИЧНОМ СОСТОЯНИЕ','В ОТЛИЧНОМ СОСТОЯНИЕ'),
        ('В ПЛОХОМ СОСТОЯНИЕ','В ПЛОХОМ СОСТОЯНИЕ'),
        ('В НОРМАЛЬНОМ СОСТОЯНИЕ','В НОРМАЛЬНОМ СОСТОЯНИЕ'),
        ('В Б/У СОСТОЯНИЕ','В Б/У СОСТОЯНИЕ'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    sell = models.CharField(("цена"), max_length=50)
    name = models.CharField(("название продукта"),max_length=50,null=True)
    category_product = models.CharField(("категория продуктов"), choices = PRODUCT_CATEGORIC, max_length=50)
    country = models.CharField(("название страны"), choices = COUNTRI, max_length=50)
    street = models.CharField(("улица"), max_length=50)
    telphone_number = models.CharField(("телефон номер"),max_length=50)
    good_or_bad_or_norm = models.CharField(("качество товара"), choices = NORM_OR_BAD, max_length=50)
    ofical = models.CharField(("описание вашего продукта"), max_length=50)
    one_photo =models.ImageField(upload_to='img/', null=True,verbose_name='1 фото')
    second_photo = models.ImageField(upload_to='img/',null=True,verbose_name='2 фото')
    # video = models.FileField(upload_to='vidio/');jk
    viewer = models.PositiveIntegerField(default=0)


    

    def __str__(self):
        return self.name
    
    


class UserPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='user_photo/', null=True)


class UserCardInput(models.Model):
    TYPE_CARD = [
        ('СБЕРБАНК', 'СБЕРБАНК'),
        ('UNIVERSALBANK', 'UNIVERSALBANK'),
        ('IPAKYULI', 'IPAKYULI'),
        ('INFIN BANK', 'INFIN BANK'),
        ('HUMO', 'HUMO'),
        ('XALKBANKI', 'XALKBANKI'),
        ('TINKOF', 'TINKOF')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card = models.IntegerField(("номер карты"),null=True)
    type_card = models.CharField(("назавание карты "), choices =TYPE_CARD,  max_length=50)

    



class BanUserProduct(models.Model):
    BAN_OFFICE = [
        ('ПРОПАГАНДА','ПРОРАГАНДА'),
        ('ЗАПРЕШЁННЫЕ ВЕШИ','ЗАПРЕШЁННЫЕ ВЕШИ'),
        ('МНЕ СТАЛО НЕ ПРИЯТНО','МНЕ СТАЛО НЕ ПРИЯТНО'),
        ('НЕТУ ТАКОГО ТОВАРА ','НЕТУ ТАКОГО ТОВАРА'),
        ('НЕ КОРЕКТНОЕ ИМЯ','НЕ КОРЕКТНОЕ ИМЯ'),
        ('ПРОДАВЕЦ СЛИШКОМ ГРУБЫЙ','ПРОДАВЕЦ СЛИШКОМ ГРУБЫЙ')
    ]
    product = models.OneToOneField(UserCategoryPublishes, on_delete=models.CASCADE,null=True)
    ban = models.CharField(("выбирите причину жалаобы"), choices = BAN_OFFICE, max_length=50)

    
    




class Likes(models.Model):
    publish_objects = models.ForeignKey(UserCategoryPublishes, on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    like = models.BooleanField(max_length = 50,blank = True )


class UserSocial(models.Model):
    TYPE_SOCIAL = [
        ('TELEGRAM', 'TELEGRAM'),
        ('INSTAGRAM', 'INSTAGRAM'),
        ('FACEBOOK', 'FACCEBOOK')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(("username"), max_length=50)
    type_social_media = models.CharField(("какую социальную сеть вы исьпользуету"),choices  = TYPE_SOCIAL, max_length=50)




class ConetntView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(UserCategoryPublishes, on_delete=models.CASCADE)