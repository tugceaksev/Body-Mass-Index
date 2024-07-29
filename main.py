import tkinter as tk
from tkinter import messagebox

def vki_hesapla(kilo, boy):
    return kilo / (boy ** 2)

def vki_durumu(vki):
    if vki < 18.5:
        return "Zayıf"
    elif 18.5 <= vki < 24.9:
        return "Normal kilolu"
    elif 25 <= vki < 29.9:
        return "Fazla kilolu"
    else:
        return "Obez"

def hesapla():
    try:
        kilo = float(entry_kilo.get())
        boy = float(entry_boy.get())
        vki = vki_hesapla(kilo, boy)
        durum = vki_durumu(vki)
        messagebox.showinfo("Sonuç", f"Vücut Kitle İndeksiniz: {vki:.2f}\nDurumunuz: {durum}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# Ana pencere
root = tk.Tk()
root.title("Vücut Kitle İndeksi Hesaplayıcı")
root.geometry("400x200")

# Kilo etiketi ve giriş kutusu
label_kilo = tk.Label(root, text="Kilonuzu (kg) girin:")
label_kilo.pack(pady=5)
entry_kilo = tk.Entry(root)
entry_kilo.pack(pady=5)

# Boy etiketi ve giriş kutusu
label_boy = tk.Label(root, text="Boyunuzu (metre) girin:")
label_boy.pack(pady=5)
entry_boy = tk.Entry(root)
entry_boy.pack(pady=5)

# Hesapla butonu
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
button_hesapla.pack(pady=20)

root.mainloop()
