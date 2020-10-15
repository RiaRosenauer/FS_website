# Generated by Django 3.1.2 on 2020-10-15 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exam_type', models.CharField(choices=[('p', 'Probeklausur'), ('k', 'Klausur'), ('w', 'Wiederholungsklausur')], default='k', max_length=10)),
                ('year', models.CharField(default='20', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('difficulty', models.CharField(choices=[('e', 'einfach'), ('m', 'mittel'), ('s', 'schwer')], default='e', max_length=10)),
                ('year', models.IntegerField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='LatexImages/')),
                ('courses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FSapp.course')),
                ('exam', models.ManyToManyField(blank=True, to='FSapp.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FSapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failed_exercises', models.ManyToManyField(blank=True, null=True, related_name='student_failed', to='FSapp.Exercise')),
                ('solved_exercises', models.ManyToManyField(blank=True, null=True, related_name='student_solved', to='FSapp.Exercise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='subject',
            field=models.ManyToManyField(blank=True, to='FSapp.Subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FSapp.professor'),
        ),
    ]
