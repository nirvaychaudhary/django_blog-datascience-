from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import UserAdminCreationForm

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})

def Setsession(request):
    # data['email'] = request.user
    print(request.user)
    request.session['email'] = request.user.email
    print(request.session['email'])
    return render(request, 'session/setsession.html')

def Getsession(request):
    # request.session['email'] = request.user
    if 'email' in request.session:
        email = request.session['email']
        print(email)
        request.session.modified = True 
        return render(request, 'session/getsession.html', {'email':email})
    else:
        return HttpResponse('Your session has expired, please set the session again!')

def Delsession(request):
    request.session.flush()
    request.session.clear_expired() 
    return render(request, 'session/deletesession.html')


