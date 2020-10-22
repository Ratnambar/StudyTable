from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.


class UserCreateView(CreateView):
    template_name = 'Task/signup.html'
    form_class = SignupForm
    success_url = 'home/'


def home(request):
    return render(request, 'Task/base.html')




