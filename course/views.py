from multiprocessing import context
from django.shortcuts import render,redirect
from course.models import Course
from course.forms import CustomPaymentForm
from course.pay import process_payment

# Create your views here.
def RegisterCourse(request):
    courses = Course.objects.all()
    total = 0
    for course in courses:
        total+=1

    context = {'courses': courses}
    return render(request, "payCourse.html", context)

def custom_payment(request):
    courses = Course.objects.all()
    form = CustomPaymentForm()
    if request.method=='POST':
        form =CustomPaymentForm(request.POST)
        if form.is_valid():
            Total_course = form.cleaned_data['Total_course']
            TotalCredit= form.cleaned_data['TotalCredit']
            TotalFees  = form.cleaned_data['TotalFees ']
            email = form.cleaned_data['email ']
            return redirect(process_payment(Total_course, TotalCredit,TotalFees,email))

    context = {'form': form,'courses': courses}
    return render(request, "payCourse.html", context)