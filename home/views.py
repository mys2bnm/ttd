from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from django.core.mail import send_mail
from .forms import Subscriber
from django.contrib import messages
from django.views import View

# Create your views here.
def index(request):
    cate = Category.objects.all()
    client = Client.objects.all()
    pro = Project.objects.all()
    pro1 = Project.objects.filter(project_status=1)
    pro2 = Project.objects.filter(project_status=2)
    pro3 = Project.objects.filter(project_status=3)
    shw = Showroom.objects.all()
    context = {
        'cate': cate,
        'client': client,
        'pro': pro,
        'pro1': pro1,
        'pro2': pro2,
        'pro3': pro3,
        'shw': shw,
    }
    return render(request, 'home/index.html', context)


def cateDetail(request, id):
    cD = Category.objects.get(cate_id=id)
    return render(request, 'home/cate-details.html', {'cD': cD})


class Index2(View):
    def get(self, request):
        cate = Category.objects.all()
        client = Client.objects.all()
        pro = Project.objects.all()
        pro1 = Project.objects.filter(project_status=1)
        pro2 = Project.objects.filter(project_status=2)
        pro3 = Project.objects.filter(project_status=3)
        shw = Showroom.objects.all()
        context = {
            'cate': cate,
            'client': client,
            'pro': pro,
            'pro1': pro1,
            'pro2': pro2,
            'pro3': pro3,
            'shw': shw,
        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        g = Subscriber(request.POST)
        if not g.is_valid():

            messages.info(request, 'sai roi!')
        g.save()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email
        send_mail(
            '[CSKH] ' + subject,
            'Người gửi: ' + name + ',\n' + 'Email: ' + email + '\n' + 'Nội dung: ' + message,
            email,
            ['maiknd.ttt@gmail.com']
        )
        return render(request, 'home/index.html', {'email': email})


def index2(request):
    if request.method == 'POST':
        g = Subscriber(request.POST)
        if g.is_valid():
            g.save()
            messages.info(request, 'Bạn đã đăng ký thành công!')
        else:
            return render(request, 'home/index.html')
    #logic vớ vẩn vl
    if request.method == 'POST' and not g.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email
        send_mail(
            '[CSKH] ' + subject,
            'Người gửi: ' + name + ',\n' + 'Email: ' + email + '\n' + 'Nội dung: ' + message,
            email,
            ['maiknd.ttt@gmail.com']
        )
        return render(request, 'home/index.html', {'email': email})
    else:
        return render(request, 'home/index.html', {})
