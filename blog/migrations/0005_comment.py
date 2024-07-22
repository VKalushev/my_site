# Generated by Django 5.0.7 on 2024-07-21 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('comment_text', models.TextField(max_length=200, validators=[django.core.validators.MinValueValidator(10)])),
            ],
        ),
    ]