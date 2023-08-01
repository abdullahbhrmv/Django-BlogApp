from django import forms
from .models import Blog, Category

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_name', 'desc', 'image', 'homepage', 'categories']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        
        # Kategorileri seçmek için çoklu seçim yapmak için
        self.fields['categories'].widget.attrs['class'] = 'form-select'
        self.fields['categories'].widget.attrs['multiple'] = True

        # Resim alanını zorunlu değil
        self.fields['image'].required = False
