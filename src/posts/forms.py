from django import forms
from .models import Post


class PostForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите заголовок'
      }
    )
  )

  description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите описание',
        'rows': 3
      }
    )
  )
  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['title'].label = "Заголовок"
    self.fields['description'].label = "Описание"

  class Meta:
    model = Post
    fields = ('title', 'description',)

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get('title')
    if not title.strip():
      raise forms.ValidationError('Invalid title!')
    else:
      return title

  def clean_description(self, *args, **kwargs):
    description = self.cleaned_data.get('description')
    if not description.strip():
      raise forms.ValidationError('Invalid description!')
    else:
      return description
