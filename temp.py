import tkinter as tk

# Hesap makinesi fonksiyonları
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())  # Kullanıcının girdiği matematiksel ifadeyi hesapla
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Modern Hesap Makinesi")
root.geometry("400x500")  # Pencere boyutunu ayarla
root.config(bg="#2d2d2d")

# Giriş kutusunu (entry) ekle
entry = tk.Entry(root, font=("Helvetica", 20), justify="right", bd=5, relief="sunken", bg="#444444", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Butonları oluştur
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Butonlara işlevler ekle
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=("Helvetica", 16), command=button_clear, bg="#444444", fg="#ffffff", relief="raised")
    elif text == '=':
        button = tk.Button(root, text=text, font=("Helvetica", 16), command=button_equal, bg="#666666", fg="#ffffff", relief="raised")
    else:
        button = tk.Button(root, text=text, font=("Helvetica", 16), command=lambda t=text: button_click(t), bg="#444444", fg="#ffffff", relief="raised")
    button.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew", padx=5, pady=5)

# Satır ve sütun boyutlarını esnek yap
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Pencereyi çalıştır
root.mainloop()
