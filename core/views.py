from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class MainpageView(ListView):
    template_name = "main-page/mainpage.html"

    def get_context(self):
        context = {
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())