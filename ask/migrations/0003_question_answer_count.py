# Generated by Django 2.0.3 on 2018-03-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_question_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_count',
            field=models.IntegerField(default=0),
        ),
    ]
