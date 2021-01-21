from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from codes.forms import CodeForm
from users.models import CustumUser
from codes.models import Code


 
@login_required
def home(request):
    return render(request,'main.html',{})


def user_login(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('Verify')
    return render(request,'login.html',{'form':form})


def verify(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustumUser.objects.get(pk=pk)
        code = user.code.code
        print('code',code)
        if not request.POST:
            print('user code',code)
        if form.is_valid():
            num = form.cleaned_data.get('code')
            if str(code)==num:
                login(request,user)
                return redirect('Home')
            else:
                return redirect('Login')
    return render(request,'verify.html',{'form':form})