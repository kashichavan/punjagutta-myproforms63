from django.shortcuts import render,HttpResponse
from .models import EmployeeModel
from .forms import EmployeeForm
# Create your views here.

def empRegister(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            a=request.POST.get('ename')
            b=request.POST.get('eage')
            c=request.POST.get('email')
            d=request.POST.get('sal')
            obj=EmployeeModel(ename=a,eage=b,email=c,sal=d)
            obj.save()
            return HttpResponse("<h1>Form is Submitted </h1>")
    form = EmployeeForm()
    return render(request,'form.html',{'form':form})



