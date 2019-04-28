from django.db import models
from users.models import UserProfile
from datetime import datetime

# Create your models here.


class Topic(models.Model):
    views = models.IntegerField(default=0, verbose_name=u'点击次数')
    title = models.CharField(max_length=50, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE,)
    created_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now, null=True, blank=True)

    class Meta:
        verbose_name = u"论坛帖子"
        verbose_name_plural = verbose_name


class Reply(models.Model):
    content = models.TextField(verbose_name=u'评论内容')
    topic = models.ForeignKey(Topic, verbose_name=u'帖子', on_delete=models.CASCADE,)
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE,)
    created_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now, null=True, blank=True)

    class Meta:
        verbose_name = u'帖子评论'
        verbose_name_plural = verbose_name
