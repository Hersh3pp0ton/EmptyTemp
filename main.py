from win11toast import toast
import os

dir = "C:/Windows/Temp/"

elementiIgnorati = False

for file in os.listdir(dir):
    try:
        os.remove(os.path.join(dir, file))
    except PermissionError:
        elementiIgnorati = True
    except FileNotFoundError:
        pass

stringa = "Temp svuotato con successo.\nAlcuni elementi sono stati ignorati." if elementiIgnorati else "Temp svuotato con successo."

toast(
    'EmptyTemp',
    stringa,
    icon='C:/Users/MSI/PycharmProjects/EmptyTemp/icon.png'
)
