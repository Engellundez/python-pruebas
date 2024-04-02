import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

def main():
    # window to see
    window = tk.Tk()
    window.geometry("700x550")
    window.title("Engellundez Pokedex Tutorial")
    window.config(padx=10, pady=10)

    # TEXT RESPONSE DATA
    title_label = tk.Label(window, text="Engellundez Pokedex")
    title_label.config(font=("Arial", 32))
    title_label.pack(padx=10, pady=10)

    pokemon_image = tk.Label(window)
    pokemon_image.config(font=("Arial", 60))
    pokemon_image.pack(padx=10, pady=10)

    pokemon_information = tk.Label(window)
    pokemon_information.config(font=("Arial", 20))
    pokemon_information.pack(padx=10, pady=10)

    pokemon_types = tk.Label(window)
    pokemon_types.config(font=("Arial", 20))
    pokemon_types.pack(padx=10, pady=10)

    # FUNCTION OF APPLICATION
    
    def load_pokemon():
        try:
            pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
            http = urllib3.PoolManager()
            response = http.request('GET', pokemon.sprites.front.get('default'))
            image = PIL.Image.open(BytesIO(response.data))

            img = PIL.ImageTk.PhotoImage(image)
            pokemon_image.config(image=img)
            pokemon_image.image = img

            pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
            pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
        except Exception as e:
            pokemon_image.image = None
            pokemon_information.config(text="???".title())
            pokemon_types.config(text="???".title())
        
    label_id_name = tk.Label(window, text="ID or Name")
    label_id_name.config(font=("Arial", 20))
    label_id_name.pack(padx=10, pady=10)

    text_id_name = tk.Text(window, height=1)
    text_id_name.config(font=("Arial", 20))
    text_id_name.pack(padx=10, pady=10)

    btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
    btn_load.config(font=("Arial", 20))
    btn_load.pack(padx=10, pady=10)

    window.mainloop()


main()
