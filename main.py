from crypto_main import NEW_KEY_YNS, NEW_KEY_YS, encryptedtext, decryptedtext, encryptedfile, decryptedfile
from tools_main import spliter_mail_hash, connector_mail_hash, fast_hex_tu_utf, hex_tu_utf, gluing_files, breakdown_files
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#граф интерфейс
#window - menu_frame, text_frame
window = tk.Tk()
window.title("Suslo.v1")
window.geometry("700x750")
#
menu_frame = tk.Frame(window, bg="#1e1e1e")
text_frame = tk.Frame(window, bg="#1e1e1e")
file_crypt_frame = tk.Frame(window, bg="#1e1e1e")
key_frame = tk.Frame(window, bg="#1e1e1e")
main_menu_frame = tk.Frame(window, bg="#1e1e1e")
tools_menu_frame = tk.Frame(window, bg="#1e1e1e")

spliter_mail_hash_ = tk.Frame(window, bg="#1e1e1e")
connector_mail_hash_ = tk.Frame(window, bg="#1e1e1e")
hex_tu_utf_ = tk.Frame(window, bg="#1e1e1e")
gluing_files_ = tk.Frame(window, bg="#1e1e1e")
breakdown_files_ = tk.Frame(window, bg="#1e1e1e")
login_frame = tk.Frame(window, bg="#1e1e1e")



def open_screen(current_frame, target_frame):
    current_frame.pack_forget()
    target_frame.pack(fill="both", expand=True)

def back_to_frame(current_frame, target_frame):
    current_frame.pack_forget()
    target_frame.pack(fill="both", expand=True)


#
## граница быстрого шифрования\дешифрования
#шифрование
label_title = tk.Label(text_frame, text="Быстрое шифрование текста", fg = "#e8e8e8", bg ="#1e1e1e", font=("Arial", 18, "bold"))
label_title.pack()

ttk.Separator(text_frame, orient="horizontal").pack(fill="x")

label_title1 = tk.Label(text_frame, text="вставьте ключ", fg = "#e8e8e8", bg ="#1e1e1e")
label_title1.pack()


entry_key = tk.Entry(text_frame, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
entry_key.pack()

label_title2 = tk.Label(text_frame, text="вставьте текст", fg = "#e8e8e8", bg ="#1e1e1e")
label_title2.pack()

open_text = tk.Text(text_frame, height=5, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
open_text.pack()

label_title3 = tk.Label(text_frame, text="шифрованный текст", fg = "#e8e8e8", bg ="#1e1e1e")
label_title3.pack()

text_input = tk.Text(text_frame, height=5, width=60, fg = "#e8e8e8", bg ="#1e1e1e")
text_input.pack()

def enter_encrypt_text():
    INPUT_CHOICE_key = entry_key.get()
    byte_encrypt_text = open_text.get('1.0', tk.END).strip()
    text_input.delete("1.0", tk.END)
    text_input.insert("1.0", encryptedtext(INPUT_CHOICE_key, byte_encrypt_text))

button_encrypt = tk.Button(text_frame, text="Зашифровать", fg = "#e8e8e8", bg ="#1e1e1e", command=enter_encrypt_text)
button_encrypt.pack(pady=10)
#шифрование
#дешифрования

ttk.Separator(text_frame, orient="horizontal").pack(fill="x")

label_decrypt = tk.Label(text_frame, text="Быстрое дешифрование текста", fg = "#e8e8e8", bg ="#1e1e1e", font=("Arial", 18, "bold"))
label_decrypt.pack()

ttk.Separator(text_frame, orient="horizontal").pack(fill="x")

label_title5 = tk.Label(text_frame, text="вставьте ключ", fg = "#e8e8e8", bg ="#1e1e1e")
label_title5.pack()

entry_key2 = tk.Entry(text_frame, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
entry_key2.pack()

label_iinfo = tk.Label(text_frame, text="вставьте шифрованый текст сюда", fg = "#e8e8e8", bg ="#1e1e1e")
label_iinfo.pack()

byte_text_input = tk.Text(text_frame, height=5, width=60, fg = "#e8e8e8", bg ="#1e1e1e")
byte_text_input.pack()

def enter_decrypt_text():
    INPUT_CHOICE_key = entry_key2.get()
    byte_decrypt_text = byte_text_input.get('1.0', tk.END).strip()
    byte_text_input.delete("1.0", tk.END)
    byte_text_input.insert("1.0", decryptedtext(INPUT_CHOICE_key, byte_decrypt_text))

button_decrypt = tk.Button(text_frame, text="дешифровать", fg = "#e8e8e8", bg ="#1e1e1e", command=enter_decrypt_text)
button_decrypt.pack(pady=10)


#дешифрования
label_title5 = tk.Label(text_frame, text="ваш ключ", fg = "#e8e8e8", bg ="#1e1e1e")
label_title5.pack()

def create_key():
    key1.delete("1.0", tk.END)
    key1.insert("1.0", NEW_KEY_YNS())

key1 = tk.Text(text_frame, height=3, width=45, fg = "#e8e8e8", bg ="#1e1e1e")
key1.pack()

button_key = tk.Button(text_frame, text="быстрый ключ", fg = "#e8e8e8", bg ="#1e1e1e", command=create_key)
button_key.pack(pady=10)

button_back_text = tk.Button(text_frame, text="Назад", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(text_frame, menu_frame))
button_back_text.pack(pady=10)
## граница быстрого шифрования\дешифрования

## граница создания своего ключа шифрования
def create_file_key():
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", NEW_KEY_YS())

label_titlekey = tk.Label(key_frame, text="создание вашего ключа шифрования", fg = "#e8e8e8", bg ="#1e1e1e")
label_titlekey.pack()

text_output = tk.Text(key_frame, height=1, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
text_output.pack()

button_key = tk.Button(key_frame, text="создать ключ в файле", fg = "#e8e8e8", bg ="#1e1e1e", command=create_file_key)
button_key.pack(pady=10)

button_back_text = tk.Button(key_frame, text="Назад", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(key_frame, menu_frame))
button_back_text.pack(pady=10)
## граница создания своего ключа шифрования

## граница шифрование\дешифрование файлов
#шифрование
label_title = tk.Label(file_crypt_frame, text="Шифрование файла", fg = "#e8e8e8", bg ="#1e1e1e", font=("Arial", 18, "bold"))
label_title.pack()

ttk.Separator(file_crypt_frame, orient="horizontal").pack(fill="x")

label_title6 = tk.Label(file_crypt_frame, text="вставьте ключ", fg = "#e8e8e8", bg ="#1e1e1e")
label_title6.pack()

entry_key3 = tk.Entry(file_crypt_frame, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
entry_key3.pack()

selected_file = ""
def open_input_file():
    global selected_file
    filename = filedialog.askopenfilename()
    selected_file = filename

file_name = tk.Button(file_crypt_frame, text="Выбрать файл", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file)
file_name.pack(pady=10)

label_title8 = tk.Label(file_crypt_frame, text="ответ программы", fg = "#e8e8e8", bg ="#1e1e1e")
label_title8.pack()

out_message = tk.Text(file_crypt_frame, height=1, width=30, fg = "#e8e8e8", bg ="#1e1e1e")
out_message.pack()

def create_file_crypt():
    INPUT_CHOICE_key = entry_key3.get()
    filename = selected_file
    out_message.delete("1.0", tk.END)
    out_message.insert("1.0", encryptedfile(INPUT_CHOICE_key, filename))

button_crypt = tk.Button(file_crypt_frame, text="зашифровать данные в файле", fg = "#e8e8e8", bg ="#1e1e1e", command=create_file_crypt)
button_crypt.pack(pady=10)


#шифрование

#дешифрования
ttk.Separator(file_crypt_frame, orient="horizontal").pack(fill="x")

label_decrypt = tk.Label(file_crypt_frame, text="Дешифрование файлов", fg = "#e8e8e8", bg ="#1e1e1e", font=("Arial", 18, "bold"))
label_decrypt.pack()

ttk.Separator(file_crypt_frame, orient="horizontal").pack(fill="x")

label_title6 = tk.Label(file_crypt_frame, text="вставьте ключ", fg = "#e8e8e8", bg ="#1e1e1e")
label_title6.pack()

entry_key4 = tk.Entry(file_crypt_frame, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
entry_key4.pack()

selected_file1 = ""
def open_input_file1():
    global selected_file1
    filename = filedialog.askopenfilename()
    selected_file1 = filename

file_name1 = tk.Button(file_crypt_frame, text="Выбрать файл", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file1)
file_name1.pack(pady=10)

label_title9 = tk.Label(file_crypt_frame, text="ответ программы", fg = "#e8e8e8", bg ="#1e1e1e")
label_title9.pack()

out_message1 = tk.Text(file_crypt_frame, height=1, width=30, fg = "#e8e8e8", bg ="#1e1e1e")
out_message1.pack()

def create_file_decrypt():
    input_choice_key = entry_key4.get()
    filename = selected_file1
    out_message1.delete("1.0", tk.END)
    out_message1.insert("1.0", decryptedfile(input_choice_key, filename))

button_crypt = tk.Button(file_crypt_frame, text="дешифровать данные в файле", fg = "#e8e8e8", bg ="#1e1e1e", command=create_file_decrypt)
button_crypt.pack(pady=10)

#дешифрования
button_back_text = tk.Button(file_crypt_frame, text="Назад", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(file_crypt_frame, menu_frame))
button_back_text.pack(pady=10)
## граница шифрование\дешифрование файлов

##граница главного меню шифрования-дешифрования-ключей

menu_title = tk.Label(menu_frame, text="Меню шифрования-дешифрования", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20) 

ttk.Separator( menu_frame, orient="horizontal").pack(fill="x")

label_title9 = tk.Label(menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=10, y=90, width=221, height=50)

big_button_text = tk.Button(menu_frame, text="Быстрое шифрование\дешифрования",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, relief="flat", bd=0, command=lambda: open_screen(menu_frame, text_frame))
big_button_text.place(x=13, y=93, width=215, height=44)

label_title9 = tk.Label(menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=237, y=90, width=221, height=50)

big_button_key = tk.Button(menu_frame, text="Создание ключа в файле",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(menu_frame, key_frame))
big_button_key.place(x=240, y=93, width=215, height=44)

label_title9 = tk.Label(menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=464, y=90, width=221, height=50)

big_button_file_crypt = tk.Button(menu_frame, text="Шифрование\дешифрование файлов",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(menu_frame, file_crypt_frame))
big_button_file_crypt.place(x=467, y=93, width=215, height=44)

button_back_text = tk.Button(menu_frame, text="Назад", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(menu_frame, main_menu_frame))
button_back_text.pack(pady=70)
##граница главного меню шифрования-дешифрования-ключей
##граница меню инструментов
menu_title = tk.Label(tools_menu_frame, text="Меню инструментов", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(tools_menu_frame, orient="horizontal").pack(fill="x")

label_title9 = tk.Label(tools_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=10, y=90, width=221, height=50)

button_text_split = tk.Button(tools_menu_frame, text="Разбивка файла mail:hash",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, relief="flat", bd=0, command=lambda: open_screen(tools_menu_frame, spliter_mail_hash_))
button_text_split.place(x=13, y=93, width=215, height=44)

label_title9 = tk.Label(tools_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=237, y=90, width=221, height=50)

big_button_key = tk.Button(tools_menu_frame, text="Склеивание файлов в mail:hash",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(tools_menu_frame, connector_mail_hash_))
big_button_key.place(x=240, y=93, width=215, height=44)

label_title9 = tk.Label(tools_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=464, y=90, width=221, height=50)

big_button_file_crypt = tk.Button(tools_menu_frame, text="Преобразование из hex в UTF-8",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(tools_menu_frame, hex_tu_utf_))
big_button_file_crypt.place(x=467, y=93, width=215, height=44)

label_title9 = tk.Label(tools_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=10, y=150, width=221, height=50)

big_button_text = tk.Button(tools_menu_frame, text="Склеивание файлов",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, relief="flat", bd=0, command=lambda: open_screen(tools_menu_frame, gluing_files_))
big_button_text.place(x=13, y=153, width=215, height=44)

label_title9 = tk.Label(tools_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=237, y=150, width=221, height=50)

big_button_breakdown = tk.Button(tools_menu_frame, text="Разбивка файлов",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(tools_menu_frame, breakdown_files_))
big_button_breakdown.place(x=240, y=153, width=215, height=44)


button_back_text1 = tk.Button(tools_menu_frame, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(tools_menu_frame, main_menu_frame))
button_back_text1.pack(pady=150)
##граница меню инструментов
#разбивка файлов mail:hash
menu_title = tk.Label(spliter_mail_hash_, text="Разбивка файлов mail:hash", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(spliter_mail_hash_, orient="horizontal").pack(fill="x")\

filename2 = ""
def open_input_file_hash():
    global filename2
    filename = filedialog.askopenfilename()
    filename2 = filename
    entry_file14.delete(0, tk.END)
    entry_file14.insert(0, filename)

file_name2 = tk.Button(spliter_mail_hash_, text="Выбрать файл", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_hash)
file_name2.pack(pady=10)

entry_file14 = tk.Entry(spliter_mail_hash_, width=50, fg = "#e8e8e8", bg ="#1e1e1e")
entry_file14.pack()

file_name2 = tk.Button(spliter_mail_hash_, text='Разбить на "mail - hash"', 
fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: spliter_mail_hash(filename2, separator=':'))
file_name2.pack(pady=10)

button_back_text1 = tk.Button(spliter_mail_hash_, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(spliter_mail_hash_, tools_menu_frame))
button_back_text1.pack(pady=150)
#разбивка файлов mail:hash
#склеивание файлов mail:hash
menu_title = tk.Label(connector_mail_hash_, text="Склеивание файлов в mail:hash", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(connector_mail_hash_, orient="horizontal").pack(fill="x")

file_mail = ""
def open_input_file_mail():
    global file_mail
    filename = filedialog.askopenfilename()
    file_mail = filename


file_name2 = tk.Button(connector_mail_hash_, text='Выбрать файл "mail"', fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_mail)
file_name2.pack(pady=5)

file_hash = ""
def open_input_file_hash1():
    global file_hash
    filename = filedialog.askopenfilename()
    file_hash = filename
    output_file_name.delete("1.0", tk.END)
    output_file_name.insert("1.0", file_mail + "\n" + file_hash)

file_name2 = tk.Button(connector_mail_hash_, text='Выбрать файл "hash"', fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_hash1)
file_name2.pack(pady=5)

output_file_name = tk.Text(connector_mail_hash_, width=70, height=3, fg = "#e8e8e8", bg ="#1e1e1e")
output_file_name.pack()

file_name2 = tk.Button(connector_mail_hash_, text='Склеить файлы', fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: connector_mail_hash(file_mail, file_hash, separator=':'))
file_name2.pack(pady=5)

button_back_text1 = tk.Button(connector_mail_hash_, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(connector_mail_hash_, tools_menu_frame))
button_back_text1.pack(pady=150)
#склеивание файлов mail:hash

#преобразование хекса в ютифишку
menu_title = tk.Label(hex_tu_utf_, text="Преобразование из hex в UTF-8", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(hex_tu_utf_, orient="horizontal").pack(fill="x")

file_hex = ""
def open_input_file_hex():
    global file_hex
    filename = filedialog.askopenfilename()
    file_hex = filename
    entry_file11.delete(0, tk.END)
    entry_file11.insert(0, filename)

file_name2 = tk.Button(hex_tu_utf_, text="Выбрать файл", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_hex)
file_name2.pack(pady=10)

entry_file11 = tk.Entry(hex_tu_utf_, width=60, fg = "#e8e8e8", bg ="#1e1e1e")
entry_file11.pack()

file_name51 = tk.Button(hex_tu_utf_, text="Преоброзовать в UTF-8", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: hex_tu_utf(file_hex))
file_name51.pack(pady=10)

#мне лень делать быстрое преобразование

button_back_text1 = tk.Button(hex_tu_utf_, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(hex_tu_utf_, tools_menu_frame))
button_back_text1.pack(pady=150)
#преобразование хекса в ютифишку


#склеивание файлов
menu_title = tk.Label(gluing_files_, text="Cклеивание файлов", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(gluing_files_, orient="horizontal").pack(fill="x")

files_split = ""
def open_input_file_split():
    global files_split
    filename = filedialog.askopenfilenames()
    files_split = filename
    output_file_.insert('1.0', files_split)

file = tk.Button(gluing_files_, text="Выбрать файлы", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_split)
file.pack(pady=5)

output_file_ = tk.Text(gluing_files_, width=70, height=5, fg = "#e8e8e8", bg ="#1e1e1e")
output_file_.pack()

menu_title = tk.Label(gluing_files_, text="Введите название исходного файла(в конце добавьте .txt)",
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

nam_file = tk.Entry(gluing_files_, width=60, fg = "#e8e8e8", bg ="#1e1e1e")
nam_file.pack()


filessplit = tk.Button(gluing_files_, text="Cклеить файлы", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: gluing_files(files_split, nam_file.get()))
filessplit.pack(pady=10)

button_back_text1 = tk.Button(gluing_files_, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(gluing_files_, tools_menu_frame))
button_back_text1.pack(pady=150)
#склеивание файлов
#разбивка файлов
menu_title = tk.Label(breakdown_files_, text="Разбивка файлов", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(breakdown_files_, orient="horizontal").pack(fill="x")

file_breakdown = ""
def open_input_file_breakdown():
    global file_breakdown
    filename = filedialog.askopenfilename()
    file_breakdown = filename

file = tk.Button(breakdown_files_, text="Выбрать файл", fg = "#e8e8e8", bg ="#1e1e1e", command=open_input_file_breakdown)
file.pack(pady=5)

count_title = tk.Label(breakdown_files_, text="Выберите колличество строк",
fg = "#e8e8e8", bg ="#1e1e1e")
count_title.pack(pady=5)

count_lines = tk.Entry(breakdown_files_, width=30, fg = "#e8e8e8", bg ="#1e1e1e")
count_lines.pack()

file_breakdown = tk.Button(breakdown_files_, text="Разбить файлы", fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: breakdown_files(file_breakdown, count_lines.get()))
file_breakdown.pack(pady=5)

button_back_text1 = tk.Button(breakdown_files_, text="Назад",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: back_to_frame(breakdown_files_, tools_menu_frame))
button_back_text1.pack(pady=150)

#разбивка файлов
###граница ультра главного меню

menu_title = tk.Label(main_menu_frame, text="Главное меню", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
menu_title.pack(pady=20)

ttk.Separator(main_menu_frame, orient="horizontal").pack(fill="x")

label_title9 = tk.Label(main_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=10, y=90, width=221, height=50)

big_button_crypt = tk.Button(main_menu_frame, text="шифрование-дешифрования",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(main_menu_frame, menu_frame))
big_button_crypt.place(x=13, y=93, width=215, height=44)

label_title9 = tk.Label(main_menu_frame, text="", bg ="#ff0000", bd=0)
label_title9.place(x=237, y=90, width=221, height=50)

big_button_key = tk.Button(main_menu_frame, text="Инструменты",
fg = "#e8e8e8", bg ="#303030", width=30, height=3, bd=0, command=lambda: open_screen(main_menu_frame, tools_menu_frame))
big_button_key.place(x=240, y=93, width=215, height=44)
###граница ультра главного меню
###граница входа в приложение
login_title = tk.Label(login_frame, text="SusloRebern", font=("Arial", 18, "bold"),
fg = "#e8e8e8", bg ="#1e1e1e")
login_title.pack(pady=20)

ttk.Separator(login_frame, orient="horizontal").pack(fill="x")

login_label = tk.Label(login_frame, text="Введите логин", fg = "#e8e8e8", bg ="#1e1e1e", bd=0)
login_label.pack()

login_line = tk.Entry(login_frame, width=30, fg = "#e8e8e8", bg ="#1e1e1e")
login_line.pack()

password_label = tk.Label(login_frame, text="Ввеите пароль", fg = "#e8e8e8", bg ="#1e1e1e", bd=0)
password_label.pack()

password_line = tk.Entry(login_frame, width=30, fg = "#e8e8e8", bg ="#1e1e1e")
password_line.pack()

button_vhod_in_main_menu = tk.Button(login_frame, text="Вход",
 fg = "#e8e8e8", bg ="#1e1e1e", command=lambda: open_screen(login_frame, main_menu_frame))
button_vhod_in_main_menu.pack()
###граница входа в приложение

login_frame.pack(fill="both", expand=True)
window.mainloop()