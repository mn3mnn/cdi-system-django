import json
from datetime import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from welly.models import WorkList, Specialist

@login_required(login_url='welly:page-login')
def index(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'welly/index.html',context)

@login_required(login_url='welly:page-login')
def work_list(request):
    role = ''
    work_list_items = []
    all_specialists = None

    if request.user.groups.filter(name='manager').exists():
        role = 'manager'
        all_specialists = Specialist.objects.all()
        work_list_items = WorkList.objects.all()
    elif request.user.groups.filter(name='specialist').exists():
        role = 'specialist'
        work_list_items = WorkList.objects.filter(assigned_specialist=request.user.specialist)

    context = {
        "page_title": "Work List",
        "role": role,
        "work_list_items": work_list_items,
        "specialists": all_specialists
    }
    return render(request,'welly/work-list.html', context)

def assign(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            work_list_ids = data['selectedItemsIds']
            specialist_id = data['selectedSpecialistId']
            work_list_ids = [int(i) for i in work_list_ids]
            specialist_id = int(specialist_id)

            work_lists = WorkList.objects.filter(work_list_id__in=work_list_ids)
            specialist = Specialist.objects.get(specialist_id=specialist_id)
            for w in work_lists:
                w.assigned_specialist = specialist
                w.assignment_date = datetime.utcnow()
                w.save()

            return HttpResponse('success', status=201)
        except Exception as e:
            print(e)

    return HttpResponse('failed', status=500)

def details(request, work_list_id):
    work_list = WorkList.objects.get(work_list_id=work_list_id)
    context={
        "page_title":"Details",
        "work_list": work_list
    }
    return render(request,'welly/details.html',context)

def notifications(request):
    context={
        "page_title":"Notifications"
    }
    return render(request,'welly/notifications.html',context)

def page_register(request):
    return render(request,'welly/pages/page-register.html')

def page_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('login successful')
            return redirect('welly:index')

    return render(request,'welly/pages/page-login.html')

def page_logout(request):
    logout(request)
    return redirect('welly:page-login')

def page_forgot_password(request):
    return render(request,'welly/pages/page-forgot-password.html')

def page_lock_screen(request):
    return render(request,'welly/pages/page-lock-screen.html')

def page_empty(request):
    context={
        "page_title":"Empty Page"
    }
    return render(request,'welly/pages/page-empty.html',context)

def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')
