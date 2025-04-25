"""
一个 Django 模型类的定义，
用于在数据库中创建 config 表来存储配置信息
"""
# coding:utf-8
__author__ = "ila"

from django.db import models

from .model import BaseModel


class config(BaseModel):
    # id=models.BigIntegerField(verbose_name="自增id")
    # 在 Django 中，如果没有显式定义主键字段，Django 会自动为模型
    # 添加一个名为 id 的自增整数主键字段。
    name = models.CharField(max_length=100, verbose_name=u'键名')
    value = models.CharField(max_length=100, verbose_name=u'键值')
    url = models.CharField(max_length=100, verbose_name=u'键值')
    # 定义管理界面显示的名字
    __tablename__ = 'config'
    class Meta:
        db_table = 'config' # 设置该模型在数据库中对应的表名
        verbose_name = verbose_name_plural = u'配置表'

    # def __str__(self):
    #     return self.name
