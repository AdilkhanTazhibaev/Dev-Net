from django import forms
from .models import Profile, Education, Experience, Social


GENDER_CHOICES = [
  ('Мужской', 'Мужской'),
  ('Женский', 'Женский')
]

STATUS_CHOICES = [
  ('Замужем', 'Замужем'),
  ('Холост', 'Холост')
]

PROFESSION_CHOICES = [
  ('Student or Learning', 'Студент'),
  ('Junior Developer', 'Младший разработчик'),
  ('Senior Developer', 'Ведущий разработчик'),
  ('Developer', 'Разработчик'),
  ('Manager', 'Менеджер'),
  ('Instructor or Teacher', 'Инструктор или Учитель'),
  ('Intern', 'Интерн'),
  ('ussiness Man', 'Бизнесмен'),
  ('Digital Marketer', 'Цифровой Маркетолог'),
  ('Data Scientist', 'Ученый данных'),
  ('Other', 'Другой')
]

DEGREE_CHOICES = [
  ('IT', 'Информационные технологии'),
  ('Bussiness Managment', 'Управление бизнесом'),
  ('Digital Marketing', 'Цифровой маркетинг'),
  ('Computer Science', 'Компьютерная наука'),
  ('Civil Engineering', 'Гражданское строительство'),
  ('AI', 'Искусственный и Интеллект'),
  ('Other', 'Другой')
]


class ProfileForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите имя'
      }
    )
  )

  age = forms.IntegerField(
    widget=forms.NumberInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите возраст'
      }
    )
  )

  gender = forms.ChoiceField(
    choices=GENDER_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  status = forms.ChoiceField(
    choices=STATUS_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  website = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Сайт'
      }
    )
  )

  company = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите компанию'
      }
    )
  )

  profession = forms.ChoiceField(
    choices=PROFESSION_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  
  location = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите место'
      }
    )
  )

  skills = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите навык'
      }
    )
  )

  bio = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Описание',
        'rows': 4
      }
    )
  )

  image = forms.ImageField(
    required=False,
    widget=forms.FileInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )
  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.fields['name'].label = "Имя"
    self.fields['age'].label = "Возраст"
    self.fields['gender'].label = "Пол"
    self.fields['status'].label = "Семейное положение"
    self.fields['company'].label = "Сайт"
    self.fields['profession'].label = "Профессия"
    self.fields['location'].label = "Место проживания"
    self.fields['skills'].label = "Навык"
    self.fields['bio'].label = "О себе"
    self.fields['image'].label = "Изображение"

  class Meta:
    model = Profile
    fields = ('name', 'age', 'gender', 'status', 'website', 'company', 'profession', 'location', 'skills', 'bio', 'image',)

  def clean_age(self, *args, **kwargs):
    age = self.cleaned_data.get('age')
    if age > 50:
      raise forms.ValidationError('Age must be belove 50 years!')
    elif age < 18:
      raise forms.ValidationError('Age must be at least 18 years!')
    else:
      return age


class EducationForm(forms.ModelForm):
  college = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Колледж'
      }
    )
  )

  degree = forms.ChoiceField(
    choices=DEGREE_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  started_at = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  ended_at = forms.DateField(
    required=False,
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  is_currently_studying = forms.BooleanField(
    required=False,
    label='Обучаетесь?',
    widget=forms.CheckboxInput(
      attrs={
        'class': 'form-check',
      }
    )
  )

  def __init__(self, *args, **kwargs):
    super(EducationForm, self).__init__(*args, **kwargs)
    self.fields['college'].label = 'Колледж'
    self.fields['degree'].label = 'Специальность'
    self.fields['started_at'].label = 'Начало'
    self.fields['ended_at'].label = 'Конец обучения'
    



  class Meta:
    model = Education
    fields = ('college', 'degree', 'started_at', 'ended_at', 'is_currently_studying',)


class ExperienceForm(forms.ModelForm):
  company = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите компанию'
      }
    )
  )

  profession = forms.ChoiceField(
    choices=PROFESSION_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  started_at = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  ended_at = forms.DateField(
    required=False,
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  is_currently_working = forms.BooleanField(
    required=False,
    label='Работете?',
    widget=forms.CheckboxInput(
      attrs={
        'class': 'form-check',
      }
    )
  )
  class Meta:
    model = Experience
    fields = ('company', 'profession', 'started_at', 'ended_at', 'is_currently_working',)

  def __init__(self, *args, **kwargs):
    super(ExperienceForm, self).__init__(*args, **kwargs)
    self.fields['company'].label = 'Компания'
    self.fields['profession'].label = 'Специальность'
    self.fields['started_at'].label = 'Начало'
    self.fields['ended_at'].label = 'Конец'


class SocialForm(forms.ModelForm):
  facebook = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Facebook URL'
      }
    )
  )

  youtube = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Youtube URL'
      }
    )
  )

  twitter = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Twitter URL'
      }
    )
  )

  linkedin = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Linkedin URL'
      }
    )
  )

  instagram = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Instagram URL'
      }
    )
  )

  github = forms.URLField(
    required=False,
    widget=forms.URLInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Github URL'
      }
    )
  )

  class Meta:
    model = Social
    fields = ['facebook', 'youtube', 'twitter', 'linkedin', 'instagram', 'github']
