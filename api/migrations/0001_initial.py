# Generated by Django 4.2.1 on 2023-05-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('APP', 'App Support'), ('PAY', 'Payment Support'), ('HR', 'HR/Jobs'), ('OTH', 'Other')], max_length=3)),
                ('message', models.TextField(max_length=500)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('PRG', 'In progress'), ('RSL', 'Resolved')], default='NEW', max_length=3)),
            ],
        ),
    ]