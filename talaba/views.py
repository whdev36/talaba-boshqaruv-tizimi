from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import KirishForm, FROForm
from django.contrib import messages as m
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json


# Bosh sahifa
def uy(r):
	return render(r, 'uy.html', {})

# Foydalanuvchi tizimga kirishi uchun ko'rish yaratish
def kirish(r):
	if r.method == 'POST': # Foydalanuvchi ma'lumot yuborgan bo'lsa
		form = KirishForm(r.POST) # Formani POST ma'lumotlari bilan to'ldirish
		if form.is_valid(): # Forma validatsiyadan o'tdimi?
			f_nomi = form.cleaned_data.get('f_nomi') # Foydalanuvchi nomini olish
			parol = form.cleaned_data.get('parol') # Parolni olish
			f = authenticate(username=f_nomi, password=parol) # Autentifikatsiya qilish
			if f is not None: # Agar foydalanuvchi mavjud bo'lsa
				login(r, f) # Foydalanuvchini tizimga kiritish
				m.success(r, 'Tizimga muvaffaqiyatli kirdingiz.') # Muvaffaqiyatli xabar
				return redirect('uy') # Muvaffaqiyatli login bo'lsa, asosiy sahifaga yo'naltirish
			else:
				m.error(r, 'Foydalanuvchi nomi yoki parol noto\'g\'ri.') # Xatolik xabari
				form.add_error(None, "Foydalanuvchi nomi yoki parol noto'g'ri.")  # Xatolik qo'shish
		else:
			m.warning('Forma to\'g\'ri to\'ldirilmagan.') # Forma xatoligi haqida ogohlantirish
	else:
		form = KirishForm() # GET so‘rovda bo‘sh forma yuborish

	return render(r, 'kirish.html', {'form': form}) # Formani sahifaga uzatish

def ro(r):
	"""
    Ro'yxatdan o'tish ko'rinishi.
    Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tganda tizimga kiradi va 
    xabar orqali muvaffaqiyatli ro'yxatdan o'tganligini bildiradi.
    """
	if r.method == 'POST':  # Foydalanuvchi ma'lumot yuborgan bo'lsa
		form = FROForm(r.POST)  # Formani foydalanuvchi yuborgan ma'lumotlar bilan to'ldirish
		if form.is_valid():  # Forma validatsiyadan o'tdimi?
			f = form.save()  # Yangi foydalanuvchini yaratish va saqlash
			login(r, f)  # Yangi foydalanuvchini tizimga kiritish
			m.success(r, 'Muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
			return redirect('uy')  # Muvaffaqiyatli ro'yxatdan o'tgach, asosiy sahifaga yo'naltirish
		else:
			m.error(r, 'Ro\'yxatdan o\'tishda xatolik yuz berdi. Iltimos, formani to\'g\'ri to\'ldiring.')
	else:
		form = FROForm()  # GET so'rovda bo'sh forma yaratish

	# Formani sahifaga yuborish
	return render(r, 'ro.html', {'form': form})

def chiqish(r):
    """
    Foydalanuvchini tizimdan chiqarish.
    Chiqib ketgandan so'ng foydalanuvchini bosh sahifaga yo'naltiradi
    va xabar orqali muvaffaqiyatli chiqganligini bildiradi.
    """
    logout(r)  # Foydalanuvchini tizimdan chiqarish
    m.success(r, "Tizimdan muvaffaqiyatli chiqdingiz.")  # Xabar qo'shish
    return redirect('uy')  # Bosh sahifaga yo'naltirish