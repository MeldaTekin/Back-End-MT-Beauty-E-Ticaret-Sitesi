# Generated by Django 4.1.2 on 2022-11-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_kategori_sub_category_urun_kategori_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='marka',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
