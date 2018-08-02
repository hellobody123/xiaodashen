from django.shortcuts import render, redirect, HttpResponse
#导入框架自带的用户验证应用的用户模型User
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(requset):
    return render(requset, 'user/首页.html')


#注册
def sign_up(request):
    return render(request, 'user/注册.html')


#处理注册请求
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username, email=email, password=password)
    return redirect('sign_in')


#登录
def sign_in(request):
    return render(request, 'user/登录.html')


#处理登录请求
def log_in(request):
    if request.method == 'GET':
        next_url = request.GET.get('next', '')
        return render(request, '登录.html', {'next':next_url})
    else:
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(username=username, password=password)
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)   #login方法为了存储登录用户

                #return render(request, 'user/首页.html')
                return HttpResponse('成功')

            else:
                return HttpResponse('用户未激活')
        else:

            return HttpResponse('用户未注册，请注册')


def do_logout(request):
    """退出登录"""
    logout(request)
    return redirect('index')


def write(request):
    return render(request, 'user/博客写作.html')







