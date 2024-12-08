# forms.py

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Foydalanuvchi tizimga kirishi uchun forma yaratish
class KirishForm(forms.Form):
	'''
	Foydalanuvchining tizimga kirishi uchun forma.

    Ushbu forma foydalanuvchidan foydalanuvchi nomi va parol kiritilishini talab qiladi. 
    Maydonlar:
    - f_nomi: Foydalanuvchi nomi uchun maydon.
    - parol: Parol uchun maydon.
    
    Shuningdek, foydalanuvchini autentifikatsiya qilish uchun `clean` metodi orqali ma'lumotlarni tekshiradi.
	'''
	f_nomi = forms.CharField( # Foydalanuvchi nomini kiritish uchun maydon yaratiladi
		widget=forms.TextInput(attrs={
			'class': 'form-control', # Maydon CSS stilini qo'llash uchun klassni belgilash
			'placeholder': 'Foydalanuvchi nomini kiriting', # Foydalanuvchini maydon maqsadini ko'rsatish
			'autofocus': True # Sahifa yuklanganda diqqatni ushbu maydonga qaratish
		}),
		label='Foydalanuvchi nomi', # Maydon uchun ko'rinadigan yorliq
		max_length=150 # Foydalanuvchi nomining maksimal uzunligini belgilash
	)

	parol = forms.CharField( # Parolni kiritish uchun maydon yaratiladi
		widget=forms.PasswordInput(attrs={
			'class': 'form-control', # Maydon CSS stilini qo'llash uchun klassni belgilash
			'placeholder': 'Parol kiriting' # Foydalanuvchini parol kiritish kerakligini ko'rsatish
		}),
		label='Parol' # Maydon uchun ko'rinadigan yorliq
	)

	def clean(self):
		# Forma ma'lumotlarini tozalash
		t_data = super().clean()
		f_name = t_data.get('f_name')
		parol = t_data.get('parol')

		# Agar foydalanuvchi nomi va parol kiritilgan bo'lsa
		if f_name and parol:
			f = authenticate(username=f_name, password=parol)
			if f is None:
				raise forms.ValidationError('Foydalanuvchi nomi yoki parol noto\'g\'ri.')
		return t_data # Tozalangan ma'lumotlarni qaytarish

class FROForm(UserCreationForm):
    """
    FROForm foydalanuvchini ro'yxatdan o'tkazish uchun mo'ljallangan forma.
    Django UserCreationForm dan kengaytirilgan.
    """
    class Meta:
        """
        Meta klass formaga oid sozlamalarni belgilaydi.
        Model: User
        Maydonlar: username, email, first_name, last_name, password1, password2
        """
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """
        Formaning atributlari va maxsus sozlamalarini o'rnatish uchun ishlatiladi.
        Maydonlarga Bootstrap klasslarini qo'shadi va kerakli matnlarni belgilaydi.
        """
        super().__init__(*args, **kwargs)

        # Formadagi barcha maydonlarni sozlash
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'  # Bootstrap klass
            self.fields[field_name].label_suffix = ''  # Yorliqdan keyingi standart ':' belgisi olib tashlanadi
            self.fields[field_name].help_text = ''  # Django-ning standart yordam matni olib tashlanadi

        # Maxsus placeholderlar
        self.fields['username'].widget.attrs['placeholder'] = 'Foydalanuvchi nomini yarating'
        self.fields['email'].widget.attrs['placeholder'] = 'Elektron pochtangizni kiriting'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ismingiz'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Familiyangiz'
        self.fields['password1'].widget.attrs['placeholder'] = 'Parol yarating'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolni takrorlang'

        # Yorliqlarni aniqlash
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['email'].label = 'Elektron pochta'
        self.fields['first_name'].label = 'Ism'
        self.fields['last_name'].label = 'Familiya'
        self.fields['password1'].label = 'Parol'
        self.fields['password2'].label = 'Parolni tasdiqlang'

    def clean_email(self):
        """
        Emailni tekshiradi va allaqachon ro'yxatdan o'tgan bo'lsa, xatolik chiqaradi.
        
        Raises:
            forms.ValidationError: Agar email mavjud bo'lsa.
        Returns:
            str: Tozalangan va tasdiqlangan email.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")
        return email