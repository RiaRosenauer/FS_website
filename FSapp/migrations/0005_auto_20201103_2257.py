# Generated by Django 3.1.2 on 2020-11-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0004_auto_20201103_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='answer10',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer5',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer6',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer7',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer8',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='answer9',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question10',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question6',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question7',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question8',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question9',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='answer1',
            field=models.FileField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='question1',
            field=models.FileField(blank=True, null=True, upload_to='question'),
        ),
    ]
