# Generated by Django 3.0.3 on 2020-03-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='活动标题')),
                ('img_url', models.CharField(max_length=256, verbose_name='横幅图片')),
                ('link', models.CharField(max_length=256, verbose_name='指向链接')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='横幅标题')),
                ('img_url', models.CharField(max_length=256, verbose_name='横幅图片')),
                ('link', models.CharField(blank=True, max_length=256, null=True, verbose_name='指向链接')),
                ('level', models.IntegerField(default=0, verbose_name='显示顺序')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='网站')),
                ('link', models.CharField(max_length=256, verbose_name='链接')),
                ('level', models.IntegerField(default=0, verbose_name='显示顺序')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '友情连接',
                'verbose_name_plural': '友情连接',
            },
        ),
    ]
