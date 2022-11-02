from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TovarForm, UploadFileForm
from django.http import HttpResponse
from .models import Tovar
from .serializer import TovarSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import pandas


# from somewhere import handle_uploaded_file


# class TovaryViewSet(viewsets.ModelViewSet):
#     queryset = Tovar.objects.all()
#     serializer_class = TovarSerializer
#
#     def get(self, request):
#         return Response(self.serializer_class(self.queryset).data)

def tovary(request):
    template = 'tovary/tovar.html'
    tovary = Tovar.objects.all()

    return render(request, template, {'tovary': tovary})


def new_tovar(request):
    form = TovarForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect(reverse_lazy('user_url:index'))
    return render(request, 'tovary/new_tovar.html', {'form': form})


def zagruzka_prodag(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect(reverse_lazy('user_url:index'))
        # handle_uploaded_file(request.FILES['file'])

    else:
        form = UploadFileForm()

    # file = pass
    return render(request, 'tovary/zagruzka_prodag.html', {'form': form})


def handle_uploaded_file(f):
    for line in f:
        print(line)
        # info = line.parse(,)
        # form = prodaja_form(id = info[0], name = info[1])
        # if form.is_valid():
        #   form.save()
