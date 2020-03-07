import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.base import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.logger import Logger

Builder.load_string("""
<rootwi>:
    size: root.size
    width: root.width
    heigth: root.height
    canvas:
        Color:
            # #263238
            rgb: 0x26 / 255.0, 0x32 / 255.0, 0x38 / 255.0
        Rectangle:
            size: self.size
    Widget:
        canvas:
            Color: 
                rgba: 0, 0, 0, 1
            Rectangle:
                pos:  30, self.y + 220
                size: self.width - 60, self.height - 460

    PathButton:
        on_press: fichier.text = self.get_path_file()
        text: 'Sélectionner le fichier initial'
        size_hint: .30, .05
        pos: root.width/10, root.heigth/2
    # PathButton:
    #     on_press: dossier.text = self.get_path_folder()
    #     text: 'Sélectionner le dossier de destination'
    #     size_hint: .35, .05
    #     pos: root.width/10, root.heigth/2-50
    PathButton:
        on_press: resultat.text = self.clean(fichier.text)
        text: 'Nettoyer et sauvegarder'
        size_hint: .30, .05
        pos_hint:{'center_x':.5,'center_y':.3}

    Label:
        id: fichier
        size_hint: None, None
        pos_hint:{'x':.6,'y':.45}

    Label:
        id: resultat
        size_hint: None, None
        pos_hint:{'center_x':.5,'y':.37}


""")

class PathButton(Button):
    @staticmethod
    def get_path_file():
        root = tk.Tk()
        root.withdraw()
        value= filedialog.askopenfilename()
        Logger.info('value : '+value)
        return value

    @staticmethod
    def get_path_folder():
        root = tk.Tk()
        root.withdraw()
        value= filedialog.askdirectory()
        Logger.info('value : '+value)
        return value

    @staticmethod
    def clean(fichier):
        Logger.info('fichier : '+fichier)

        root = tk.Tk()
        root.withdraw()
        fichier1= filedialog.asksaveasfilename(defaultextension=".dat")

        Logger.info('fichier1 : '+fichier1)

        fileFirst = open(fichier, "r")
        fileFinal = open(fichier1, "w")
        for line in fileFirst:
            Logger.info('1. line : '+line)
            newline=line.replace("\',\'",";")
            Logger.info('2. line : '+line)
            newline=newline.replace("\'\'"," ")
            Logger.info('3. line : '+newline)
            newline=newline.replace(";","\',\'")
            Logger.info('4. line : '+newline)
            fileFinal.write(newline)
        fileFinal.close()
        fileFirst.close()

        return "Enregistré dans "+fichier1

class rootwi(RelativeLayout):
    pass


class MyApp(App):
    title = 'Automatisation de nettoyage'
    def build(self):
        return rootwi()

if __name__ == '__main__':
    MyApp().run()