# Generated by Django 4.0.5 on 2022-07-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'customers',
            },
        ),
    ]