from django import forms
from post.models import Post


class NewPostform(forms.ModelForm):
    # content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
    
    image = forms.ImageField(required=True)
    image_caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'image_caption'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Tags | Seperate with comma'}))

    class Meta:
        model = Post
        fields = ['image', 'image_caption', 'tags']
