from django import forms
from .models import *
import os



class BookForm(forms.ModelForm):

	class Meta:
		model = bookdetails		
		fields = '__all__'

	
	def clean(self):				
		cleaned_data=super().clean()
		return cleaned_data

	
	def save(self):		
		new_user = bookdetails.objects.create(
			book_name = self.cleaned_data['book_name'],
			isbn_number = self.cleaned_data['isbn_number'],
			price = self.cleaned_data['price'],
			author= self.cleaned_data['author'],
				)
		return new_user



class BookFormUpdate(forms.ModelForm):
	class Meta:
		model = bookdetails		
		fields = '__all__'



	def clean(self):				
		cleaned_data=super().clean()
		return cleaned_data

	
	def save(self, mode, id):	
		if mode:	
			new_user = bookdetails.objects.filter(id=id).update(
				book_name = self.cleaned_data['book_name'],
				isbn_number = self.cleaned_data['isbn_number'],
				price = self.cleaned_data['price'],
				author= self.cleaned_data['author'],
				id=id,
				)
		else:
			new_user = bookdetails.objects.create(
				book_name = self.cleaned_data['book_name'],
				isbn_number = self.cleaned_data['isbn_number'],
				price = self.cleaned_data['price'],
				author= self.cleaned_data['author'],

					)
		return new_user
