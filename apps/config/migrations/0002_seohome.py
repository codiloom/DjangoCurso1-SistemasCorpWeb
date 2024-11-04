# Generated by Django 5.1.2 on 2024-11-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEOHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta descrição')),
                ('meta_keywords', models.CharField(help_text='Separadas por virgula', max_length=255, verbose_name='Palavras chaves')),
            ],
            options={
                'verbose_name': 'SEO Home',
                'verbose_name_plural': 'SEO Home',
            },
        ),
    ]
