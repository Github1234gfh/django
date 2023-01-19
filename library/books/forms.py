from django.forms import  ModelForm, TextInput, Textarea, Select
from .models import Books, Aply

class BookForm(ModelForm):
	class Meta:
		model = Books
		fields = ['name_book', 'autor', 'date', 'category']

		widgets = {
			'name_book': TextInput(attrs={
				'class': 'form_title',
				'placeholder': 'book name',
			}),
			'autor': Textarea(attrs={
				'class': 'form_title',
				'placeholder': 'Aftor book',
			}),
			'date': TextInput(attrs={
				'class': 'form_title',
				'placeholder': 'Date public',
				'type': 'date',
			}),
			'category': Select(attrs={
				'class': 'form_title',
			})
		}


class AplyForm(ModelForm):
	class Meta:
		model = Aply
		fields = ['name', 'book']

		widgets = {
			'name': TextInput(attrs={
				'class': 'form_title',
				'placeholder': 'Your name and surname',
			}),
			'book': Select(attrs={
				'class': 'form_title',
				'placeholder': 'Your book',
			}),
	}