# forms.py

from django import forms
from django.contrib.auth import authenticate

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

