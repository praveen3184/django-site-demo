# Generated by Django 5.1.1 on 2024-09-10 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cateogry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='courseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filePath', models.FileField(upload_to='pdfFilePath')),
                ('academicYear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.academicyear')),
                ('cateogry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.cateogry')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.course')),
            ],
        ),
    ]
