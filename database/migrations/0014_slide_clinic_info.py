# Generated by Django 4.1.3 on 2023-02-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='clinic_info',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]