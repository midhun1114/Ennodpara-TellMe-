# Generated by Django 3.2 on 2021-05-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_alter_cart_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='song',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
