from django.shortcuts import render
from django.shortcuts import redirect

from django.views import View
from django.views import generic

# Create your views here.

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        templates_name = 'todo_main/index.html'
        return render(request, templates_name)
