from django import forms
from blog.models import Contact,Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title', 'text','post_image','link_to_code',)

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'postcontent'}),
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'postcontent'}),
        }

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'
