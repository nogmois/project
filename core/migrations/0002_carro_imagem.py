# Generated by Django 5.1.3 on 2024-12-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='carros/'),
        ),
    ]
