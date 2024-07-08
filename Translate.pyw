import asyncio
from googletrans import Translator, LANGUAGES
from CTkRightClickMenu import CTkRightClickMenu
from pywinstyles import apply_style
from hPyT import all_stuffs
from async_tkinter_loop import async_handler, async_mainloop
from os import path
from webbrowser import open as open_web
from CTkScrollableDropdown import *
    
class TranslatorApp:
    def __init__(self):
        script = path.dirname(path.abspath(__file__))

        
        import customtkinter as ctk
        self.tk = ctk
        self.CTkRightClickMenu = CTkRightClickMenu
        self.apply_style = apply_style
        self.all_stuffs = all_stuffs
        self.LANGUAGES = LANGUAGES
        self.tk.set_default_color_theme(path.join(script,"extreme.json"))
        self.root = self.tk.CTk()
        self.root.title("Translate")
        self.root.geometry("270x120")
        self.root.resizable(0,0)

        self.create_widgets()
        self.apply_styles()
        self.root.bind('<Control-t>', self.on_shortcut_exit)

        async_mainloop(self.root)
    def on_shortcut_exit(self,event=None):
        self.root.destroy()
        exit()
        

    def create_widgets(self):
        self.label1 = self.tk.CTkLabel(self.root, text="Text:")
        self.label1.grid(column=0, row=1, pady=5, padx=5)

        self.input = self.tk.CTkEntry(self.root)
        self.input.grid(column=1, row=1, pady=5, padx=5)

        self.label2 = self.tk.CTkLabel(self.root, text="Target language:")
        self.label2.grid(column=0, row=2, pady=5, padx=5)

        self.linput = self.tk.CTkEntry(self.root)#, values=list(self.LANGUAGES.values())
        self.linput.grid(column=1, row=2, pady=5, padx=5)
        
        self.output_text = self.tk.CTkEntry(self.root)
        self.output_text.grid(column=0, columnspan=2, row=3, pady=5, padx=5, sticky="nsew")

        self.input.bind("<KeyPress>", async_handler(self.translate_text))
        self.linput.bind("<Button-1>",async_handler(self.translate_text))
        CTkScrollableDropdown(self.linput, values=list(self.LANGUAGES.values()), command=lambda e: self.insert_method(e),
                      autocomplete=True,topmost=True)
        self.linput.insert(self.tk.END, "English")
        self.linput.bind("<KeyPress>", async_handler(self.translate_text))
        self.linput.bind("<Motion>", async_handler(self.translate_text))
        self.output_text.bind("<Motion>", async_handler(self.translate_text))
        self.menu=CTkRightClickMenu(self.root,topmost=True,width=200)
        self.menu.add_button("Exit/Reopen: CTRL   T  ",command=self.on_shortcut_exit)
        self.menu.add_button("Author: MustafaHilmiYAVUZHAN ",command=lambda:open_web("https://github.com/MustafaHilmiYAVUZHAN"))


    def apply_styles(self):
        self.root.attributes("-topmost", 1)
        self.all_stuffs.hide(self.root)
        self.apply_style(self.root, "acrylic")

    async def translate_text(self, event=None):
        text = self.input.get()
        if not text:
            return
        dest_lang = self.linput.get()
        try:
            translation = await TranslateApp.translateThis(text, dest_lang)
            self.output_text.delete(0, self.tk.END)
            self.output_text.insert(self.tk.END, translation)
        except Exception as e:
            print(f"Hata: Çeviri başarısız oldu: {e}")

    def insert_method(self,e):
        self.linput.delete(0, 'end')
        self.linput.insert(0, e)
        async_handler(self.translate_text)
    

class TranslateApp:
    @staticmethod
    async def translateThis(text, dest_lang):
        loop = asyncio.get_event_loop()
        translator = Translator()
        translation = await loop.run_in_executor(None, translator.translate, text, dest_lang)
        return translation.text


if __name__ == "__main__":
    app = TranslatorApp()
