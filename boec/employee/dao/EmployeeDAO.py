from django.shortcuts import render, redirect

from boec.forms.EmployeeLoginForm import EmployeeLoginForm


def cms_home(request):
    return render(request, 'cms/cms_home.html')

def cms_login(request):
    form = EmployeeLoginForm()
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            employee = form.getEmployee()
            request.session['employee_id'] = employee.id
            return redirect('cms-home')
    return render(request, 'cms/employee_login.html', {'form': form})

def cms_logout(request):
    del request.session['employee_id']
    return redirect('cms-login')
