# Generated by Django 3.0.3 on 2020-03-02 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200302_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('brief', models.TextField(blank=True, null=True, verbose_name='简介')),
                ('content', models.TextField(verbose_name='内容')),
                ('thumbnail', models.CharField(blank=True, max_length=128, null=True, verbose_name='缩略图')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('hot', models.IntegerField(default=0, verbose_name='热度')),
                ('fav_count', models.IntegerField(default=0, verbose_name='赞')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('status', models.BooleanField(default=True, null=True, verbose_name='是否发布')),
                ('top', models.BooleanField(default=False, null=True, verbose_name='是否置顶')),
                ('essence', models.BooleanField(default=False, null=True, verbose_name='精华')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=32, verbose_name='文章分类')),
                ('level', models.IntegerField(default=0, verbose_name='显示优先级')),
                ('icon', models.CharField(default='', max_length=64, verbose_name='图标地址')),
                ('official', models.BooleanField(default=False, verbose_name='官方文章')),
            ],
            options={
                'verbose_name': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024, verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='community.Article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32, verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to='community.ArticleComment')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='community.CommentReply')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleFavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favour', to='community.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_favour', to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='community.ArticleClassification', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', to='community.ArticleTag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='user.User', verbose_name='作者'),
        ),
    ]