from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def base_view(request):
    return render(request, template_name='base.html')


class SignUpForm(UserCreationForm):
    ...

class AddUser(CreateView):
    template_name= 'adduser.html'
    form_class= SignUpForm
    ...
