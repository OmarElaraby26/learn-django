# Generated by Django 4.1.2 on 2022-10-26 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('year', models.PositiveIntegerField()),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents', to='parents.parent')),
                ('subjects', models.ManyToManyField(related_name='subjects', to='subjects.subject')),
            ],
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['firstname', 'lastname'], name='first_last_name_index'),
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.CheckConstraint(check=models.Q(('age__gt', 15)), name='age greater than 15'),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('firstname', 'lastname')},
        ),
    ]
