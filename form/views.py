#from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404

from .models import *
from .forms import *
# Create your views here.

from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404

from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404
from django.contrib import auth, messages
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.db.models import *




def get_book(request):

	if request.method == 'POST':
		book_form= BookForm(request.POST)
		if book_form.is_valid():
			book_form.save()
			return redirect("done") 

	return render(request, 'form/book.html')


def done(request):
	form = bookdetails.objects.all()
	return render(request, 'form/done.html', {'form':form})



def book_edit(request, id):
	form = bookdetails.objects.get(id=id)
	if request.method == "POST":
		update_form = BookFormUpdate(request.POST, instance=form)
		if update_form.is_valid():
			update=True
			update_form.save(update,id)
			return redirect("done")

	return render(request, 'form/edit.html', {'form':form})

def delete(request,id):
	form=bookdetails.objects.filter(id=id)
	form.delete()
	return redirect('done')




