from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import Employee, OverTime
from .forms import OverTimeAdd, CreateEmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    total_emp = Employee.objects.filter(user = request.user)

    total_empl = 0
    for total in total_emp:
        total_empl += 1
    context = {
        'total_employee' : total_empl
    }

    return render(request, 'working/html/index.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        user = authenticate(request, username=email, password=passwd)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    return render(request, 'working/html/login.html')

def logOut(request):
    auth_logout(request)
    return redirect('/')

def adminPage(request):
    forms = OverTimeAdd(request.GET)
    fm_emp = OverTimeAdd.emp_user(request.user)

    if request.method == "GET":
        if forms.is_valid():
            forms.save()

    contex = {   

        'forms': forms,
        'fm_emp' : fm_emp
    }

    return render(request, 'working/html/admin_page.html', contex)


def signUp(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        pass_1 = request.POST['pass_1']
        user = User.objects.create_user(
            first_name=f_name,
            last_name=l_name,
            username=user_name,
            email=email,
            password=pass_1
        )
        
        user.save()
        print(f_name)
        return redirect('/')
    return render(request, 'working/html/signUp.html')

@login_required(login_url='login')
def add_Ot(request, pk = 2):

    emp = Employee.objects.filter(user = request.user)
    forms = OverTimeAdd(request.POST)

    try:
        detail_id = Employee.objects.get(pk = pk)
        datas = OverTime.objects.filter(emp_user = detail_id)

    except:
        return render(request, 'working/html/add_Ot.html')

    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Over Time added !')

    contex = {
        'emp': emp,
        'forms': forms,
        'datas' : datas
    }

    return render(request, 'working/html/add_Ot.html', contex)


def add_employee(request):
    forms = CreateEmployeeForm(request.POST)
    user = request.user

    if request.method == "POST":
        if forms.is_valid():
            emp_name = forms.cleaned_data['emp_name']
            emp_lname = forms.cleaned_data['emp_l_name']
            emp_email = forms.cleaned_data['emp_email']
            emp_number = forms.cleaned_data['emp_number']

            form_db = Employee(
                user = user,
                emp_name = emp_name,
                emp_l_name = emp_lname,
                emp_email = emp_email,
                emp_number  = emp_number
            )

            form_db.save()

    contex = {'forms': forms}
    template = 'working/html/add_employee.html'
    return render(request, template, contex)
    # need to add-ot templates funcsnality needs to be done from dadabse integration
    # titlle is pending
    # some page setup and touch up in tempats are pending
