from django.shortcuts import render
from .models import cow_info_model
from .forms import cow_info_form,signupform
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import cow_serializer

from django.db.models import Q,Min,Max,Sum,Count,Avg

# Create your views here.

class cow_info_get_post_api(APIView):
    def get(self,r):
        cow_obj = cow_info_model.objects.all()
        cow_serobj = cow_serializer(cow_obj,many=True)
        return Response(cow_serobj.data)

    def post(self,r):
        cow_serobj = cow_serializer(data=r.data)
        if cow_serobj.is_valid():
            cow_serobj.save()
            return Response(cow_serobj.data,status=status.HTTP_201_CREATED)
        return Response(cow_serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class cow_info_put_delete_api(APIView):
    def put(self,r,id):
        cow_obj = cow_info_model.objects.get(id=id)
        cow_serobj = cow_serializer(cow_obj,data=r.data)
        if cow_serobj.is_valid():
            cow_serobj.save()
            return Response(cow_serobj.data,status=status.HTTP_200_OK)
        return Response(cow_serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,id):
        cow_obj = cow_info_model.objects.get(id=id)
        cow_obj.delete()
        return Response(status=status.HTTP_200_OK)




def home(r):
    return render(r,'base.html')

def login_msg(r):
    return render(r,'cow/loginmsg.html')

def logout_msg(r):
    return render(r,'cow/logoutmsg.html')

def regmsg(r):
    return render(r,'cow/regmsg.html')

def signinform(r):
    form = signupform()
    if r.method == 'POST':
        form = signupform(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(r,'cow/signupform.html',{'form':form})


@login_required()
def show_cow_info(r):
    cow_list = cow_info_model.objects.all()
    # cow_list = cow_info_model.objects.filter(name='saiwal')
    # # cow_list = cow_info_model.objects.create(name='jersi',milk='25',color='black')
    # # cow_list.save()
    #
    # cow_list = cow_info_model.objects.filter(name__exact='jersi')
    # cow_list = cow_info_model.objects.filter(name__iexact='jersi')
    #
    # cow_list = cow_info_model.objects.filter(name__contains='a')
    # cow_list = cow_info_model.objects.filter(name__icontains='a')
    #
    # cow_list = cow_info_model.objects.filter(~Q(name__contains='a'))
    #
    # cow_list = cow_info_model.objects.filter(~Q(name__exact='jersi'))
    #
    # cow_list = cow_info_model.objects.filter(milk__gt=30)
    # cow_list = cow_info_model.objects.filter(milk__gte=30)
    #
    # cow_list = cow_info_model.objects.filter(milk__lt=30)
    # cow_list = cow_info_model.objects.filter(milk__lte=30)
    #
    # cow_list = cow_info_model.objects.filter(~Q(milk__lte=30))
    #
    # cow_list = cow_info_model.objects.filter(name__startswith='s')
    # cow_list = cow_info_model.objects.filter(name__endswith='i')
    #
    # cow_list = cow_info_model.objects.filter(~Q(name__startswith='s'))
    # cow_list = cow_info_model.objects.filter(~Q(name__endswith='i'))
    #
    # cow_list = cow_info_model.objects.filter(name__in=['saiwal','gir'])
    # cow_list = cow_info_model.objects.filter(~Q(name__in=['saiwal','gir']))
    #
    # cow_list = cow_info_model.objects.filter(name='saiwal')|cow_info_model.objects.filter(color='black')
    # cow_list = cow_info_model.objects.filter(Q(name='saiwal')|Q(color='brown'))
    #
    # cow_list = cow_info_model.objects.filter(name='saiwal')&cow_info_model.objects.filter(milk=60)
    # cow_list = cow_info_model.objects.filter(Q(name='saiwal')&Q(color='black'))
    # cow_list = cow_info_model.objects.filter(name='saiwal',milk='60')
    #
    # cow_list = cow_info_model.objects.exclude(name='saiwal')
    #
    # a = cow_info_model.objects.filter(name='saiwal')
    # b = cow_info_model.objects.filter(color='brown')
    # cow_list=a.union(b)
    #
    # max = cow_info_model.objects.aggregate(Max('milk'))
    # print(max)
    #
    # min = cow_info_model.objects.aggregate(Min('milk'))
    # print(min)
    #
    # sum = cow_info_model.objects.aggregate(Sum('milk'))
    # print(sum)
    #
    # avg = cow_info_model.objects.aggregate(Avg('milk'))
    # print(avg)
    #
    # count = cow_info_model.objects.aggregate(Count('milk'))
    # print(count)
    #
    # cow_list = cow_info_model.objects.order_by('milk')
    # cow_list = cow_info_model.objects.order_by('-milk')
    #
    # cow_list = cow_info_model.objects.order_by('-milk')[:1]
    # cow_list = cow_info_model.objects.order_by('-milk')[1:2]




    return render(r,'cow/cow_list.html',{'cow_list':cow_list})

@login_required()
def insert_cow_form(r):
    cow_obj = cow_info_form()
    if r.method == 'POST':
        cow_obj = cow_info_form(r.POST)
        if cow_obj.is_valid():
            cow_obj.save(commit=True)
            return HttpResponseRedirect('/cow/show')
    return render(r,'cow/cow_form.html',{'form':cow_obj})

def update_cow_info(r,id):
    cow_obj = cow_info_model.objects.get(id=id)
    cobj = cow_info_form()

    if r.method == 'POST':
        cobj = cow_info_form(r.POST,instance=cow_obj)
        if cobj.is_valid():
            cow_obj.save()
            return HttpResponseRedirect('/cow/show')
    return render(r,'cow/cow_info_update.html',{'cow_obj':cow_obj})

def delete_cow_info(r,id):
    cow_obj = cow_info_model.objects.get(id=id)
    cow_obj.delete()
    return HttpResponseRedirect('/cow/show')





