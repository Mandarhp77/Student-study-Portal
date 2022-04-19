# Generated by Django 4.0.2 on 2022-04-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('todostatus', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Todo',
            },
        ),
    ]
