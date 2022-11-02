from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.http import HttpResponse
from tovar.models import Tovar


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('post_url:index')
    template_name = 'users/signup.html'


def index(request):
    template = 'vizual/index.html'
    tovary = Tovar.objects.all()

    return render(request,template, {'tovary': tovary})

