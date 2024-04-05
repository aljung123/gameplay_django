from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import user_form
from .models import user_comment
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = user_form()
            tasks = user_comment.objects.all()
            context = {"tasks" : user_comment.objects.filter(user=request.user), "taskform" : form}
            return render(request, 'home_private.html', context)
        elif request.method == 'POST':
            form = user_form(request.POST)
            if form.is_valid():
                user_comment.objects.create(comment=form.cleaned_data['comment'], user=request.user)
                # Redirect using the URL pattern name instead of the template name
                return redirect('home')
            else:
                # If form is not valid, you might want to show the form again with errors
                tasks = user_comment.objects.all()
                return render(request, 'home_private.html', {'taskform': form, 'tasks': tasks})
    else:
        if request.method == 'GET':
            tasks = user_comment.objects.all()
            context = {"tasks" : tasks}
            return render(request, 'home_public.html', context)


    
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(user_comment, id=comment_id)
    comment.delete()
    return redirect('home')
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   
        if form.is_valid():  
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form
    }  
    return render(request, 'register.html', context) 


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # This method is provided by AuthenticationForm
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm() #blank form 
    return render(request, 'login.html', {'form': form})