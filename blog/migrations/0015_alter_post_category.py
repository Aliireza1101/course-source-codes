# Generated by Django 5.0 on 2024-01-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Programming', 'Programming'), ('Network', 'Network'), ('IT', 'Information Technology'), ('AI', 'Artificial Intelligence'), ('Others', 'Others')], default='Others', max_length=255),
        ),
    ]
