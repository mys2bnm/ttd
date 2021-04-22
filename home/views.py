from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from django.core.mail import send_mail
from .forms import Subscriber, Subs
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
        form1 = Subscriber()
        form2 = Subs()
        context = {
            'cate': cate,
            'client': client,
            'pro': pro,
            'pro1': pro1,
            'pro2': pro2,
            'pro3': pro3,
            'shw': shw,
            'form1':form1,
            'form2':form2

        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        if request.method == 'POST':
            form1 = Subs(request.POST)
            form2 = Subscriber(request.POST)
            if form2.is_valid():
                form2.save()
                messages.info(request, 'Bạn đã đăng ký thành công!')
            if form1.is_valid():
                name = form1.cleaned_data["name"]
                email = form1.cleaned_data["email"]
                subject = form1.cleaned_data["subject"]
                message = form1.cleaned_data["message"]
        # send an email
                send_mail(
                    '[CSKH] ' + subject,
                    'Người gửi: ' + name + ',\n' + 'Email: ' + email + '\n' + 'Nội dung: ' + message,
                    email,
                    ['maiknd.ttt@gmail.com']
                )
            form1=Subscriber()
            form2=Subs()
            context={"form1":form1,"form2":form2}
            return render(request, 'home/index.html',context)
