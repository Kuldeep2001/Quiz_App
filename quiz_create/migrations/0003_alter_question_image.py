# Generated by Django 4.0.6 on 2022-07-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_create', '0002_alter_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='quiz_create/images'),
        ),
    ]