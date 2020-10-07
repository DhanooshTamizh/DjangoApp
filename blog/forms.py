
from django import forms
from .models import Posts,Comment

class PostForm(forms.ModelForm):
		
		class Meta:
			model=Posts
			fields=['title','content','git_link']

			widgets = {

					'title' : forms.TextInput(attrs={'class':'form-control'}),
					'content' : forms.Textarea(attrs={'class':'form-control'}),
					'git_link' : forms.TextInput(attrs={'class':'form-control'}),


			}

class CommentForm(forms.ModelForm):

	class Meta:
		model=Comment
		fields=['comments']
