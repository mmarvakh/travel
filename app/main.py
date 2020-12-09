from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
from sqlalchemy import *
from app.config import Config
from app.models import *

import csv

root = Tk()
db_connection = Config.db_connection
db = create_engine(db_connection)

root['bg'] = '#bae3e8'
root.title("Импорт данных")
root.wm_attributes('-alpha', 1)
root.geometry('450x150')

root.resizable(width=False, height=False)


def load_from_csv():
    with open(pathInput.get(), "r") as csvfile:
        tbl_reader = csv.reader(csvfile, delimiter=';')

        for row in tbl_reader:
            print(row)


def choose_handler():
    filename = askopenfilename()
    pathInput.insert(0, filename)


canvas = Canvas(root, width=450, height=150)
canvas.pack()

frame = Frame(root, bg='#fff')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

pathInput = Entry(frame, bg='#eee', width=23)
pathInput.grid(row=1, column=1, padx=50, pady=30)

btn_choose = Button(frame, text='Выбрать файл', bg='#eee', width=20, height=1, command=choose_handler)
btn_choose.grid(row=1, column=2)

typeSelect = Combobox(frame, height=1, width=20, state="readonly")
typeSelect['values'] = ('Тип импорта данных', 'Отели', 'Договоры', 'Бронирования', 'Туристы')
typeSelect.current(0)
typeSelect.grid(row=2, column=1)

btn_import = Button(frame, text='Импортировать', bg='#eee', width=20, height=1, command=load_from_csv)
btn_import.grid(row=2, column=2)


if __name__ == "__main__":
    root.mainloop()