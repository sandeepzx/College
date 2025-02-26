# Generated by Django 5.0.7 on 2024-07-24 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=250)),
                ('Course_Fee', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_Lname', models.CharField(max_length=250)),
                ('Stu_Rname', models.CharField(max_length=250)),
                ('Stu_Age', models.IntegerField(null=True)),
                ('Stu_Email', models.EmailField(max_length=254, null=True)),
                ('Stu_Number', models.CharField(max_length=250)),
                ('Stu_Address', models.TextField(null=True)),
                ('Stu_Image', models.ImageField(null=True, upload_to='Image/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teach_Lname', models.CharField(max_length=250)),
                ('Teach_Rname', models.CharField(max_length=250)),
                ('Teach_Age', models.IntegerField(null=True)),
                ('Teach_Email', models.EmailField(max_length=254, null=True)),
                ('Teach_Number', models.CharField(max_length=250)),
                ('Teach_Uname', models.CharField(max_length=250)),
                ('Teach_Address', models.TextField(null=True)),
                ('Teach_Pass', models.CharField(max_length=250)),
                ('Teach_Image', models.ImageField(null=True, upload_to='Image/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
