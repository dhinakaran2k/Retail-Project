# Generated by Django 3.2.6 on 2021-09-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/'),
        ),
    ]
