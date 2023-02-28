# Generated by Django 4.1.3 on 2023-01-30 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_slide_age_slide_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='slide',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]