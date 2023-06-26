from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import PostModel
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def my_home_view(request):
    posts = PostModel.objects.all()
    return render(request, 'view_post.html', {'posts': posts})
    

class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'signin.html' 
    success_url = reverse_lazy('login')
     

class MyLogoutView(LogoutView):
    pass

@login_required
def create_my_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('viewpost')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def my_post_list(request):
    posts = PostModel.objects.all()
    return render(request, 'view_post.html', {'posts': posts})




