"""
对 Django 管理界面进行配置，包括设置管理界面的标题信息，
以及自动将 main 应用中的所有模型注册到 Django 管理界面，
同时为每个模型设置显示字段和搜索字段
"""
from django.contrib import admin

from django.apps import apps, AppConfig
# Register your models here.

from dj2.settings import dbName as schemaName
from main.users_model import users
from main.config_model import config

try:
    from main.models import *
except:
    pass
# 尝试导入所有模型，如果失败则忽略该异常
# change title
admin.site.site_title = schemaName  # 设置页面标题
admin.site.site_header = schemaName  # 设置网站页头
admin.site.index_title = schemaName  # 设置首页标语

allModels = apps.get_app_config('main').get_models()
# 获取main中的所有模型

for ind, model in enumerate(allModels):
# ind是索引，model是值
    class modelsite(admin.ModelAdmin):
        list_display = []
        for col in model._meta.fields:
            list_display.append(col.name)

        search_fields = list_display
        # 将 search_fields 设置为 list_display，表示可以在管理界面
        # 的搜索框中搜索模型的所有字段。
    admin.site.register(model, modelsite)
