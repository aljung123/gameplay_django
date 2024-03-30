from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import user_form
from .models import user_comment
from django.views.decorators.http import require_POST

# Create your views here.

def main(request):
    if request.method == 'GET':
        form = user_form()
        tasks = user_comment.objects.all()
        context = {"taskform" : form,
                    "tasks": tasks}
        return render(request, 'home.html', context)
    
    elif request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user_comment.objects.create(comment=form.cleaned_data['comment'])
        return redirect('home')
    else:
        return redirect('home')
    
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(user_comment, id=comment_id)
    comment.delete()
    return redirect('home')