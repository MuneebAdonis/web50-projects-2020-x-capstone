# Generated by Django 4.1.3 on 2023-01-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_slide_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.CharField(default='1.jpg', max_length=200),
            preserve_default=False,
        ),
    ]