# Generated by Django 4.2.5 on 2023-09-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='comprovante',
            field=models.ImageField(null=True, upload_to='comprovante'),
        ),
    ]