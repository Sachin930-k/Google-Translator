from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Function to handle translation
def change(text="type", src="en", dest="hi"):
    translator = GoogleTranslator(source=src, target=dest)
    translation = translator.translate(text)
    return translation

# Function to handle button click and data retrieval
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

# GUI Setup
root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='Sky blue')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold")) 
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Sky blue") 
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language selection for source and destination
languages = ['en', 'hi', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'ru']  # Sample list of languages (change as needed)

comb_sor = ttk.Combobox(frame, values=languages)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("en")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, values=languages)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("hi")

lab_txt = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Sky blue") 
lab_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Run the Tkinter main loop
root.mainloop()
