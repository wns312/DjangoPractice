from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def index(request):
    member = Member(name="준영", city="서울", street="상왕십리", zipcode="1111")
    member.save()
    member.delete()
    return HttpResponse("This is Members")
