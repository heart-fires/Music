"""dj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView


from . import views
from dj2.settings import dbName as schemaName
# dbName重命名

urlpatterns = [
    path('xadmin/', admin.site.urls),
    path(r'index/',views.index),
    path('{}/'.format(schemaName),include('main.urls')),#导入schemaName
    # python格式化方法，会用schemaName的值替换{}
    # 将以 schemaName 为前缀的路径包含到 main.urls 模块中进行进一步的 URL 匹配。
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)$', views.admin_lib2),
    # (?P<p1>.*)：这是一个命名捕获组，(?P<name>pattern) 是正则表达式中用于定义命名捕获组的语法。
    # p1 是捕获组的名称，.* 表示匹配任意数量的任意字符（除换行符外）。这个捕获组会捕获 admin/lib/
    #  之后到下一个 / 之间的所有字符，并将其作为参数 p1 传递给视图函数。
    # (?P<p2>.*)：另一个命名捕获组，与 (?P<p1>.*) 类似，它会捕获斜杠之后到 URL 末尾的所有字符，
    # 并将其作为参数 p2 传递给视图函数。
    # $表示匹配字符串的末尾，确保 URL 路径以捕获的 p2 内容结束
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.admin_lib3),
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.admin_lib4),
    re_path(r'admin/page/(?P<p1>.*)$', views.admin_page),
    re_path(r'admin/page/(?P<p1>.*)/(?P<p2>.*)$', views.admin_page2),
    re_path(r'admin/pages/(?P<p1>.*)$', views.admin_pages),
    re_path(r'admin/pages/(?P<p1>.*)/(?P<p2>.*)$', views.admin_pages2),
    
    re_path(r'front/(?P<p1>.*)$', views.schema_front1),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)$', views.schema_front2),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.schema_front3),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.schema_front4),
    re_path(r'{}/front/(?P<p1>.*)$'.format(schemaName), views.schema_front1),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)$'.format(schemaName), views.schema_front2),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$'.format(schemaName), views.schema_front3),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$'.format(schemaName), views.schema_front4),
    # re_path(r'assets/(?P<p1>.*)$', views.assets1),
    # re_path(r'assets/(?P<p1>.*)/(?P<p2>.*)$',  views.assets2),
    # re_path(r'assets/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$',  views.assets3),
    # re_path(r'assets/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$',  views.assets4),
    #re_path(r'admin/(?P<p1>.*)$', views.admin_file1),
    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)$', views.admin_file2),
    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.admin_file3),
    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.admin_file4),
    re_path(r'layui/(?P<p1>.*)$', views.layui1),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)$',  views.layui2),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$',  views.layui3),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$',  views.layui4),
    re_path(r'pages/(?P<p1>.*)$', views.front_pages),
    re_path(r'pages/(?P<p1>.*)/(?P<p2>.*)$',  views.front_pages2),
    # re_path(r'pages/(?P<p1>.*)$',  views.front_file1),
    # re_path(r'(?P<p1>css|jss|img|image|iamges|font|fonts)/(?P<p2>.*)$', views.front_file2),
    re_path(r'modules/(?P<p1>.*)$', views.front_modules),
    re_path(r'css/(?P<p1>.*)$', views.css1),
    re_path(r'js/(?P<p1>.*)$', views.js1),
    re_path(r'img/(?P<p1>.*)$', views.img1),
    path(r'test/<str:p1>/',views.test),
    # <str:p1>：这是一个路径转换器。路径转换器用于捕获 URL 中的动态部分，并把它作为参数传递给
    # 对应的视图函数。具体解释如下：
    # str：指定了捕获参数的类型，这里表示捕获的参数是字符串类型。Django 提供了一些内置的路径
    # 转换器，比如 int（用于匹配整数）、str（用于匹配除斜杠外的任意字符串）、slug（用于匹配由
    # ASCII 字母、数字、连字符和下划线组成的字符串）等。
    # p1：是捕获参数的名称，这个名称会作为关键字参数传递给视图函数
    path(r'null',views.null),
]

#判断admin使用vue还是jquery
# 判断目录是否存在
if os.path.isdir(os.path.join(os.getcwd(),"templates/front/admin/dist/")):
    urlpatterns.extend([
        path(r'{}/admin/dist/index.html'.format(schemaName),
             TemplateView.as_view(template_name='front/admin/dist/index.html')),
        path(r'{}/admin/'.format(schemaName), TemplateView.as_view(template_name='front/admin/dist/index.html')),
        # 以下是后台admin的url匹配规则
        path(r'admin/dist/index.html'.format(schemaName),
             TemplateView.as_view(template_name='front/admin/dist/index.html')),
        path(r'admin/', TemplateView.as_view(template_name='front/admin/dist/index.html')),
    ])
else:
    urlpatterns.extend([
        path(r'{}/admin/index.html'.format(schemaName),
             TemplateView.as_view(template_name='front/admin/index.html')),
        path(r'{}/admin/'.format(schemaName), TemplateView.as_view(template_name='front/admin/index.html')),
        # 以下是后台admin的url匹配规则
        path(r'admin/index.html'.format(schemaName),
             TemplateView.as_view(template_name='front/admin/index.html')),
        path(r'admin/', TemplateView.as_view(template_name='front/admin/index.html')),

    ])


if os.path.isfile(os.path.join(os.getcwd(),"templates/front/dist/index.html")):
    urlpatterns.extend([
    path(r'index.html', TemplateView.as_view(template_name='front/dist/index.html')),
     path(r'{}/index.html'.format(schemaName), TemplateView.as_view(template_name='front/dist/index.html')),
     path(r'{}/front/index.html'.format(schemaName), TemplateView.as_view(template_name='front/dist/index.html')),
    path(r'', TemplateView.as_view(template_name='front/dist/index.html')),
    ])
