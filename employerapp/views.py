from django.shortcuts import render, redirect
from .models import Employer, Departement
from .forms import Form_employer


# Create your views here.

# To create employee
def anp(request):
    if request.method == "POST":

        form = Form_employer(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showanp")
            except:
                pass
    else:
        form = Form_employer()
    return render(request, "index.html", {'form':form})

# To show employee details
def showAnp(request):
    employees = Employer.objects.all()
    return render(request, "main.html", {'employees':employees})

# To delete employee details
def deleteAnp(request, pk):
    employee = Employer.objects.get(pk=pk)
    employee.delete()
    return redirect("/showAnp")

# To edit employee details
def editAnp(request, pk):
    employee = Employer.objects.get(pk=pk)
    return render(request, "edit.html", {'employee':employee})

# To update employee details
def updateAnp(request, pk):
    employee = Employer.objects.get(pk=pk)
    form = Form_employer(request.POST, instance= employee)
    if form.is_valid():        
        form.save()
        return redirect("/showAnp")
    return render(request, "main.html", {'employee': employee})


