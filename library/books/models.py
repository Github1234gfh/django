from django.db import models


class Category(models.Model):
	name = models.CharField('Категории', max_length=50)

	def __str__(self):
		return self.name

class Books(models.Model):
	name_book = models.CharField('Назване книги', max_length=50)
	autor = models.CharField('Автор', max_length=100)
	date = models.DateField('Дата издания')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return '/'

	def __str__(self):
		return self.name_book

class Aply(models.Model):
	name = models.CharField('ФИО', max_length=50)
	book = models.ForeignKey(Books, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return '/'

	def __str__(self):
		return self.name