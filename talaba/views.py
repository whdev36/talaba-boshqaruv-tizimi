from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import KirishForm


# Bosh sahifa
def uy(r):
	return render(r, 'uy.html', {})

# Foydalanuvchi tizimga kirishi uchun ko'rish yaratish
def kirish(r):
	if r.method == 'POST': # Foydalanuvchi ma'lumot yuborgan bo'lsa
		form = KirishForm(r.POST) # Formani POST ma'lumotlari bilan to'ldirish
		if form.is_valid(): # Forma validatsiyadan o‘tdimi?
			f_nomi = form.cleaned_data.get('f_name') # Foydalanuvchi nomini olish
			parol = form.cleaned_data.get('parol') # Parolni olish
			f = authenticate(username=f_name, password=parol) # Autentifikatsiya qilish
			if f is None: # Agar foydalanuvchi mavjud bo'lsa
				login(r, f) # Foydalanuvchini tizimga kiritish
				return redirect('uy') # Muvaffaqiyatli login bo'lsa, asosiy sahifaga yo'naltirish
			else:
				form.add_error(None, "Foydalanuvchi nomi yoki parol noto'g'ri.")  # Xatolik qo'shish
	else:
		form = KirishForm() # GET so‘rovda bo‘sh forma yuborish

	return render(r, 'kirish.html', {'form': form}) # Formani sahifaga uzatish