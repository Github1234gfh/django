from django.shortcuts import render, redirect
from .models import Category, Books
from .forms import BookForm, AplyForm
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

class Home(ListView):
	model = Books
	template_name = 'books/home.html'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['menu'] = Category.objects.all()
		return context

class Edit(UpdateView): 
	model = Books
	template_name = 'books/edit.html'
	context_object_name = 'form'
	form_class = BookForm

class Delete(DeleteView):
	model = Books
	template_name = 'books/delete.html'
	success_url = '/'
	context_object_name = 'delete'

class add(CreateView):
	template_name = 'books/add.html'
	context_object_name = 'form'
	form_class = BookForm

class ViewAply(CreateView):
	template_name = 'books/aply.html'
	context_object_name = 'form'
	form_class = AplyForm