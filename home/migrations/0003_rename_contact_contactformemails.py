# Generated by Django 3.2.15 on 2022-10-03 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_messages_contact_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactFormEmails',
        ),
    ]
