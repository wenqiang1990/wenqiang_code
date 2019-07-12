#coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.shortcuts import render,redirect,HttpResponse
#引入 auth 模块
from  django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
import json,os
from app.models import StatisticalData
from django.shortcuts import render,render_to_response


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('passowrd')
        print("username %s" % user)
        # 验证用户是否存在
        user = authenticate(username=user,password=pwd)
        print("user %s" % user)
        if user:
            auth.login(request,user) #request.user  :当前登录用户
            next_url = request.GET.get("next", "/index/")
            #  这么写的目的如果没有权限的用户访问index就会在url中提示/login/?next=/index/
            return  redirect(next_url)
            # return redirect("/index/")
        else:
            print("用户名或密码错误")
    return render(request,'login.html')
@login_required
def index(request):
    lindata = StatisticalData.objects.get(s_id=1)
    print(lindata)
    context = {'lindata':lindata }
    return render(request, 'index.html', context)
#@login_required
@login_required
def charts(request):
    return render(request, 'charts.html')
