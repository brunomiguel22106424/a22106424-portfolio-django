# Generated by Django 4.2 on 2023-06-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]