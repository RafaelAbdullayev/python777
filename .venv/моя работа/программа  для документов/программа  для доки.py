import tkinter as tk
from tkinter import simpledialog, messagebox

# Переводы для разных языков
translations = {
    "en": {
        "add_store": "Add Store",
        "add_equipment": "Add Equipment",
        "create_invoice": "Create Invoice",
        "settings": "Settings",
        "choose_theme": "Choose Theme",
        "exit": "Exit",
        "about": "About",
    },
    "az": {
        "add_store": "Mağaza əlavə et",
        "add_equipment": "Avadanlıq əlavə et",
        "create_invoice": "Faktura yarat",
        "settings": "Parametrlər",
        "choose_theme": "Dizayn seçin",
        "exit": "Çıxış",
        "about": "Haqqında",
    }
}

# Текущий язык
current_language = "en"

# Функция для отображения информации о программе
def show_about():
    messagebox.showinfo("About", "Program created by: Rafael Abdullayev")

# Функция для изменения темы
def change_theme(theme):
    if theme == "dark":
        root.tk_setPalette(background="#2F2F2F", foreground="#FFFFFF")
    elif theme == "light":
        root.tk_setPalette(background="#FFFFFF", foreground="#000000")

# Функции для кнопок
def add_store():
    print("Store added")

def add_equipment():
    print("Equipment added")

def create_invoice():
    print("Invoice created")

def open_settings():
    print("Settings opened")

# Главное окно программы
root = tk.Tk()
root.title("Store Management Program")
root.geometry("500x500")

# Кнопки
button_add = tk.Button(root, text=translations[current_language]["add_store"], command=add_store)
button_add.pack(pady=10)

button_equipment = tk.Button(root, text=translations[current_language]["add_equipment"], command=add_equipment)
button_equipment.pack(pady=10)

button_invoice = tk.Button(root, text=translations[current_language]["create_invoice"], command=create_invoice)
button_invoice.pack(pady=10)

button_settings = tk.Button(root, text=translations[current_language]["settings"], command=open_settings)
button_settings.pack(pady=10)

button_theme = tk.Button(root, text=translations[current_language]["choose_theme"], command=lambda: change_theme("dark"))
button_theme.pack(pady=10)

button_exit = tk.Button(root, text=translations[current_language]["exit"], command=root.quit)
button_exit.pack(pady=10)

# Создание меню
menu = tk.Menu(root)
root.config(menu=menu)

# Файл
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label=translations[current_language]["add_store"], command=add_store)
file_menu.add_command(label=translations[current_language]["add_equipment"], command=add_equipment)
file_menu.add_command(label=translations[current_language]["create_invoice"], command=create_invoice)
file_menu.add_separator()
file_menu.add_command(label=translations[current_language]["exit"], command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

# Настройки
settings_menu = tk.Menu(menu, tearoff=0)
settings_menu.add_command(label=translations[current_language]["settings"], command=open_settings)
menu.add_cascade(label=translations[current_language]["settings"], menu=settings_menu)

# О программе
menu.add_command(label=translations[current_language]["about"], command=show_about)

# Запуск программы
root.mainloop()
