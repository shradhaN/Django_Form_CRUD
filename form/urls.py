

from django.conf.urls import url
from form import views



urlpatterns = [

	url(r'^get_book/$', views.get_book, name='book'),
	url(r'^done/$', views.done,name="done"),
	url(r'^edit/(?P<id>[\d]+)/$', views.book_edit, name="edit"),
	url(r'^delete/(?P<id>[\d]+)/$', views.delete, name="delete")

]