"""定义users的URL模式"""
from django.urls import path, include
from django.contrib.auth.views import LoginView ,LogoutView#导入类
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    #登陆页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    #注册页面
    path(r'register/', views.register, name='register'),
]

# 也可以下面
# from django.urls import path, include
# from django.contrib.auth.views import LoginView#导入类
# from . import views
# # 修改模板路径

# LoginView.template_name = 'users/login.html'
# urlpatterns = [
#     # 登录界面
#     path('login/', LoginView.as_view(),
#          name='login')
# ]
# app_name = 'users'