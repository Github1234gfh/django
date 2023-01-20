
from django.contrib import admin
from django.urls import path, include
from books.views import *


urlpatterns = [
	path('admin/', admin.site.urls),
	path("accounts/", include("accounts.urls")),
	path("accounts/", include("django.contrib.auth.urls")),
	path("", Home.as_view(), name="home"),
	path('add/', add.as_view(), name='add'),
	path('delete/<int:pk>', Delete.as_view(), name='delete'),
	path('edit/<int:pk>', Edit.as_view(), name='edit'),
	path('bookrequest/', ViewAply.as_view(), name='aply'),
]
