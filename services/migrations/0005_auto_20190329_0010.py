# Generated by Django 2.1.7 on 2019-03-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190328_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to='services_img', verbose_name='rəsm'),
        ),
    ]
