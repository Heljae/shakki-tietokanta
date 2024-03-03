# shakki-tietokanta
## Ohjeet sovelluksen käyttämiseen
Lataa sovellus koneellesi git clone komennon avulla.  
Luo sovelluksen juurikansioon .env niminen tiedosto. Kirjoita tiedostoon seuraava:  
```
DATABASE_URL=<tietokannan osoite>
```
Luo sovellukselle virtuaaliympäristö komennolla  
```
python3 -m venv venv
```
Siirry virtuaaliympäristöön.
```
source venv/bin/activate
```
Lataa sovellukseen vaadittavat riippuvuudet.
```
pip install -r ./requirements.txt
```
Päivitä sovelluksen tietokanta
```
psql < schema.sql
```
Käynnistä sovellus!!
```
flask run
```
## Loppupalautus
Sovelluksella on seuraavat ominaisuudet:
- Käyttäjä  pystyy lisäämään pelin
- Käyttäjä pystyy selaamaan pelejä
- Käyttäjä pystyy katsomaan yksittäisen pelin tiedot
- Käyttäjä pystyy selaamaan pelaajia
- Käyttäjä pystyy katsomaan yksittäisen pelaajan tiedot
- Käyttäjä pystyy hakemaan pelaajaa nimellä

## Palautus n
- Sovellus tulostaa nyt myös siirrot pelin omalla sivulla
- Sovellus näyttää pelaajan tiedoissa kaikkien pelattujen pelien määrän
- Sovelluksella voi nyt etsiä tietyn pelaajan tiedot
- Pelaajan tiedoissa näkyy kaikki pelit

## Palautus 3
- Tietokanta toimii!
- Käyttäjä voi lisätä uuden pelin
- Käyttäjä voi printata kaikki pelit melko luettavassa muodossa
- Käyttäjä pystyy listaamaan kaikki pelaajat
- Jokaisella pelaajalla on nyt sivu, jossa näkyy pelaajan tiedot. Jokaisen pelaajan sivulle on linkki kun listaa pelaajat.
- Jokaiselle pelille on nyt oma sivu, jossa näkyy pelin tiedot
- Nyt peliä lisätessä käyttäjä voi kirjoittaa pelin siirrot ylös ja siirrot lisätään tietokantaan.

## Palautus 2
- Sovellus aukeaa
- Sovelluksella on tietokanta, mutta en ole onnistunut saamaan sinne vielä lisättyä mitään

## Miten sovellus tulee toimimaan?

Tavoitteenani on luoda tietokanta, jonne pystyy tallentamaan shakkipelejä ja josta pystyy etsimään pelejä annettujen kriteerien avulla. Sovelluksessa tulee olemaan ainakin seuraavat ominaisuudet:  
- Käyttäjä pystyy kirjautumaan sisään
- Käyttäjä pystyy tallentamaan pelin tietokantaan
- Käyttäjä pystyy hakemaan pelejä esimerkiksi, vuosiluvun, pelaajan nimen tai pelin lopputuloksen mukaan.
- Käyttäjä pystyy selaamaan kaikkia tietokannassa olevia pelejä.
- Pelit tallennetaan merkkijonona

## Mahdollisia kehitysideoita:
- Käyttäjä pystyy selaamaan pelejä ilman kirjautumista sisään.
- Kun käyttäjä kirjautuu sisään, hän pystyy tallentamaan pelejä yksityiseksi, jolloin vain hän pystyy näkemään ne.
