# Generated by Django 5.1.2 on 2024-10-31 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='link_to_video',
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.CharField(blank=True, help_text='Введите уроки курса', max_length=100, null=True, verbose_name='Уроки'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course_link',
            field=models.ForeignKey(blank=True, help_text='Выберите курс из списка', null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.course', verbose_name='Ссылка на курс'),
        ),
    ]