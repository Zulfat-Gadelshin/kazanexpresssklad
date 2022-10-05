from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TovarForm
from django.http import HttpResponse
from .models import Tovar
from .serializer import TovarSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class TovaryViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer


    def get(self, request):
        return Response(self.serializer_class(self.queryset).data)



def new_tovar(request):
    form = TovarForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect(reverse_lazy('user_url:index'))
    return render(request, 'tovary/new_tovar.html', {'form': form})
