# Generated by Django 4.0 on 2021-12-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
