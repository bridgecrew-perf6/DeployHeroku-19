# Generated by Django 4.0 on 2022-01-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_produtos_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
