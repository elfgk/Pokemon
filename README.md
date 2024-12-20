# Pokémon Bilgisi Uygulaması

Bu Python uygulaması, [PokéAPI](https://pokeapi.co/) kullanarak Pokémon'lar hakkında bilgi edinmenize ve her Pokémon'un resmiyle birlikte detaylı bilgilerini görmenize olanak sağlar. Kullanıcı, bir Pokémon seçtikten sonra o Pokémon'un adı, türleri, istatistikleri ve resmini görüntüleyebilir.-->https://huggingface.co/spaces/elfgk/Pokemon

## Özellikler

- **Pokémon Seçimi**: Pokémon listesinden herhangi birini seçebilirsiniz.
- **Pokémon Bilgisi**: Seçilen Pokémon hakkında detaylı bilgi (adı, türler, istatistikler) görüntülenir.
- **Pokémon Resmi**: Seçilen Pokémon'un resmi uygulama ekranında yer alır.

## Teknolojiler

- **Python**: Uygulama Python ile yazılmıştır.
- **Gradio**: Kullanıcı arayüzü için Gradio kütüphanesi kullanılmıştır.
- **PokéAPI**: Pokémon bilgilerini almak için PokéAPI kullanılır.

## Ekran Görüntüleri

![Pokémon Bilgisi Uygulaması](screenshot.png)

## Kurulum

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### Gereksinimler

- Python 3.x
- `requests` ve `gradio` kütüphaneleri

### Adımlar

1. Python ve gerekli kütüphaneleri yükleyin:

    ```bash
    pip install requests gradio
    ```

2. Proje dosyasını indirin veya klonlayın:

    ```bash
    git clone https://github.com/kullanici-adiniz/pokemon-bilgisi-uygulamasi.git
    cd pokemon-bilgisi-uygulamasi
    ```

3. `pokemon_uygulamasi.py` dosyasını çalıştırın:

    ```bash
    python pokemon_uygulamasi.py
    ```

4. Uygulama başarıyla çalıştığında, web tarayıcınızda Pokémon bilgilerini görüntüleyebilirsiniz.

### Kullanım

1. **Pokémon Seçin**: Gradio arayüzü üzerinden bir Pokémon adı seçin.
2. **Pokémon Bilgileri Görüntülenir**: Seçtiğiniz Pokémon'un adı, türleri ve istatistikleri ekranda görünür.
3. **Pokémon Resmi**: Pokémon'un resmi arayüzde yer alır.

## Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkılarınızı bekliyoruz! Lütfen katkı yapmadan önce `CONTRIBUTING.md` dosyasını okuyun.

### Hata Bildirme

Herhangi bir hata ile karşılaşırsanız, [Issues](https://github.com/kullanici-adiniz/pokemon-bilgisi-uygulamasi/issues) bölümünü kullanarak bildirebilirsiniz.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

## Kaynaklar

- **PokéAPI**: [https://pokeapi.co/](https://pokeapi.co/)
- **Gradio**: [https://gradio.app/](https://gradio.app/)
