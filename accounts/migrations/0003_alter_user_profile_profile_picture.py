# Generated by Django 4.0.4 on 2022-07-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(default='perfil_prueba.jpg', upload_to='profile_picture'),
        ),
    ]