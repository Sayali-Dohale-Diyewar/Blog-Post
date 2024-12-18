from django import forms
from .models import Posts, Comment, Reply, CustomUser

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'author', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),  # Correctly using Textarea for description
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('posts', 'comment')
        widgets = {
            'posts': forms.Select(attrs={'class': 'form-control'}),  # Use Select widget for ForeignKey
            'comment': forms.Textarea(attrs={'class': 'form-control'}),  # Use Textarea for text input
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('comment', 'reply')
        widgets = {
            'comment': forms.Select(attrs={'class': 'form-control'}),  # Use Select widget for ForeignKey
            'reply': forms.Textarea(attrs={'class': 'form-control'}),  # Use Textarea for text input
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        
        fields = ('first_name','last_name','phone_number','email','password','user_bio','user_profile_image')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),   # type: ignore
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
            'user_bio': forms.TextInput(attrs={'class': 'form-control'}),
            'user_profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }
    

