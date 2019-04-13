from django.db import models

# Create your models here.

class Services(models.Model):
    image = models.ImageField(verbose_name='rəsm', blank=False, null=True, upload_to='services_img')
    name = models.CharField(verbose_name='Xidmət adı', blank=False, max_length=100)
    description = models.TextField(verbose_name='Məlumat', blank=False)
    price = models.FloatField(verbose_name='Qiymət', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmətlər'
