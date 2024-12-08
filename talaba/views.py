from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import KirishForm, FROForm


# Bosh sahifa
def uy(r):
	return render(r, 'uy.html', {})

# Foydalanuvchi tizimga kirishi uchun ko'rish yaratish
def kirish(r):
	if r.method == 'POST': # Foydalanuvchi ma'lumot yuborgan bo'lsa
		form = KirishForm(r.POST) # Formani POST ma'lumotlari bilan to'ldirish
		if form.is_valid(): # Forma validatsiyadan o‘tdimi?
			f_nomi = form.cleaned_data.get('f_nomi') # Foydalanuvchi nomini olish
			parol = form.cleaned_data.get('parol') # Parolni olish
			f = authenticate(username=f_nomi, password=parol) # Autentifikatsiya qilish
			if f is not None: # Agar foydalanuvchi mavjud bo'lsa
				login(r, f) # Foydalanuvchini tizimga kiritish
				return redirect('uy') # Muvaffaqiyatli login bo'lsa, asosiy sahifaga yo'naltirish
			else:
				form.add_error(None, "Foydalanuvchi nomi yoki parol noto'g'ri.")  # Xatolik qo'shish
	else:
		form = KirishForm() # GET so‘rovda bo‘sh forma yuborish

	return render(r, 'kirish.html', {'form': form}) # Formani sahifaga uzatish

def ro(r):
	if r.method == 'POST':  # Foydalanuvchi ma'lumot yuborgan bo'lsa
		form = FROForm(r.POST)  # Formani foydalanuvchi yuborgan ma'lumotlar bilan to'ldirish
		if form.is_valid():  # Forma validatsiyadan o'tdimi?
			f = form.save()  # Yangi foydalanuvchini yaratish va saqlash
			login(r, f)  # Yangi foydalanuvchini tizimga kiritish
			return redirect('uy')  # Muvaffaqiyatli ro'yxatdan o'tgach, asosiy sahifaga yo'naltirish
	else:
		form = FROForm()  # GET so'rovda bo'sh forma yaratish

	# Formani sahifaga yuborish
	return render(r, 'ro.html', {'form': form})