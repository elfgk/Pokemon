import requests
import gradio as gr

def tum_pokemon_isimleri():
    pokemon_isimleri = []
    url = "https://pokeapi.co/api/v2/pokemon?limit=100"  # İlk 1000 Pokémon'u alıyoruz (örneğin)

    while url:
        response = requests.get(url)
        data = response.json()

        for pokemon in data["results"]:
            pokemon_isimleri.append(pokemon["name"])

        # Bir sonraki sayfaya geçiyoruz
        url = data["next"]

    return pokemon_isimleri

pokemon_isimleri= tum_pokemon_isimleri()

for isim in pokemon_isimleri:
    print(isim)
def pokemon_bilgisi(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        veri = response.json()
        isim = veri["name"]
        tipler = [tip["type"]["name"] for tip in veri["types"]]
        istatistikler = {stat["stat"]["name"]: stat["base_stat"] for stat in veri["stats"]}
        resim_url = veri["sprites"]["front_default"]  # Pokémon resminin URL'si
        # Hem metin hem de resim URL'sini döndürüyoruz
        pokemon_bilgisi = f"İsim: {isim}\nTipler: {', '.join(tipler)}\nİstatistikler: {istatistikler}"
        return pokemon_bilgisi, resim_url  # İki çıkış döndürüyoruz
    else:
        return "Pokémon bulunamadı veya API isteği başarısız oldu.",None

##gradio
with gr.Blocks() as demo:
    pokemon = gr.Dropdown(label="Pokémon Adı", choices=pokemon_isimleri)  # Pokémon listesinden seçim
    pokemon_bilgisi_output = gr.Textbox(label="Pokémon Bilgisi", interactive=False)  # Bilgiyi göstermek için Textbox
    pokemon_resim_output = gr.Image(label="Pokémon Resmi", interactive=False)  # Pokémon resmini göstermek için Image widget'ı

    # Pokémon adı seçildiğinde bilgiyi ve resmi göster
    pokemon.select(pokemon_bilgisi, inputs=pokemon, outputs=[pokemon_bilgisi_output, pokemon_resim_output])
demo.launch(share=True)