# Generated by Django 2.1.5 on 2019-02-25 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190222_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_create_post', 'Can post blog'), ('can_update_post', 'Can update blog post'), ('can_delete_post', 'Can delete posts')]},
        ),
    ]
