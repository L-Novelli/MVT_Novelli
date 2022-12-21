from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

from family.models import Family

# Create your views here.
def AddFamMember(request):
    new_member = Family.objects.create(name = 'Max', age = 2.7, work = False)
    print(new_member)
    return HttpResponse('New family member added')

def FamList(request):
    all_Family = Family.objects.all()
    print(all_Family)
    context = {
        'Family':all_Family,
    }
    return render(request, 'Family.html', context=context)