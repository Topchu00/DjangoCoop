from django.db import models

class UpImages(models.Model):
    image = models.ImageField(upload_to='up_images/', blank=True, null=True)
    price = models.CharField(max_length=150, verbose_name='Цена')
    main_text = models.TextField(verbose_name='Текст')
    star1 = models.ImageField(upload_to='up_images/', blank=True, null=True, default='none')
    star2 = models.ImageField(upload_to='up_images/', blank=True, null=True, default='none')
    star3 = models.ImageField(upload_to='up_images/', blank=True, null=True, default='none')
    star4 = models.ImageField(upload_to='up_images/', blank=True, null=True, default='none')

    def __str__(self):
        return self.price

    class Meta:
        verbose_name_plural = 'Картинки верхней части'
        verbose_name = 'Картинка верхней части'

class FormsList(models.Model):
    name = models.CharField(verbose_name="Ваше имя", max_length=50)
    email = models.EmailField(verbose_name="Ваша почта", max_length=100)
    phone = models.CharField(verbose_name="Ваш номер", max_length=60)
    message = models.TextField(verbose_name="Ваше сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форм"
        verbose_name_plural = "Форм"