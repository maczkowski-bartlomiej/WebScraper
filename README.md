# ?? Webscraper - Skaner Stron Internetowych ??

Projekt przygotowany na uczelnie.

## ?? Opis projektu

Webscraper to narz?dzie umo?liwiaj?ce u?ytkownikom skanowanie stron internetowych w celu pozyskania kluczowych danych, takich jak tytu?y stron, adresy e-mail, liczba linkow wewn?trznych, struktura organizacyjna czy statystyki tagow HTML. Aplikacja sk?ada si? z trzech g?ownych modu?ow: interfejsu u?ytkownika, silnika skanowania oraz bazy danych, ktore wspo?dzia?aj? w harmonijny sposob. ???

## ? G?owne funkcjonalno?ci

- **Wprowadzanie adresow URL ??:** U?ytkownik mo?e wprowadzi? list? adresow URL (oddzielonych przecinkami) za pomoc? intuicyjnego interfejsu.
- **Asynchroniczne skanowanie ?:** Szybkie i wydajne przetwarzanie wielu stron dzi?ki asynchronicznym ??daniom HTTP.
- **Przegl?danie wynikow ??:** Dane wy?wietlane w czytelnej formie tabelarycznej, zawieraj?cej szczego?y ka?dej zeskanowanej witryny.
- **Trwa?e przechowywanie danych ??:** Wyniki zapisywane w bazie MongoDB, co umo?liwia ich po?niejsze wykorzystanie.

## ?? Struktura projektu

Projekt zosta? podzielony na trzy modu?y:

- **webscraper-interface ???:** Interfejs u?ytkownika oparty na frameworku Flask. Umo?liwia wprowadzanie adresow URL i przegl?danie wynikow w przejrzystej formie.
- **webscraper-engine ??:** Silnik skanowania oparty na FastAPI. Odpowiada za asynchroniczne pobieranie i analiz? stron przy u?yciu bibliotek BeautifulSoup i aiohttp.
- **mongo ???:** Modu? integracji z baz? danych MongoDB, wykorzystuj?cy asynchroniczny sterownik motor do przechowywania i pobierania danych.

## ?? Zbierane dane

Aplikacja gromadzi nast?puj?ce informacje z ka?dej zeskanowanej strony:

- **Tytu? strony ??:** Pobierany z tagu <title>.
- **Adresy e-mail ??:** Wyodr?bniane za pomoc? wyra?e? regularnych.
- **Liczba linkow wewn?trznych ??:** Zliczane na podstawie odno?nikow w obr?bie tej samej domeny.
- **Struktura organizacyjna ??:** Okre?lana na podstawie nag?owkow.
- **Liczba tagow HTML ???:** Statystyki wyst?pie? poszczegolnych tagow w kodzie strony.

## ??? U?yte technologie

- **Python:** J?zyk programowania zapewniaj?cy czytelno?? i elastyczno??.
- **Flask:** Lekki framework webowy do tworzenia interfejsu u?ytkownika.
- **FastAPI:** Asynchroniczny framework do budowy wydajnego API.
- **BeautifulSoup:** Biblioteka do parsowania kodu HTML.
- **aiohttp:** Asynchroniczne ??dania HTTP dla szybkiego pobierania stron.
- **MongoDB:** NoSQL-owa baza danych do przechowywania wynikow.
- **motor:** Asynchroniczny sterownik dla MongoDB.
- **Docker:** Konteneryzacja zapewniaj?ca spojne ?rodowisko uruchomieniowe.

## ??? Architektura

Aplikacja dzia?a w oparciu o architektur? klient-serwer:
- **Interfejs** (Flask) komunikuje si? z silnikiem (FastAPI) poprzez RESTful API.
- **Silnik** przetwarza ??dania, skanuje strony i zapisuje wyniki do bazy MongoDB.
- **Docker** zapewnia izolacj? i ?atwe uruchamianie wszystkich komponentow w sieci scraper-network.

?? Jak uruchomi??

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/<twoje-nazwa-uzytkownika>/webscraper.git
   cd webscraper
   ```

2. **Uruchom za pomoc? Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Otworz przegl?dark?** i przejd? na adres:
   ```
   http://localhost:5000
   ```

?? Struktura katalogow
```plaintext
webscraper/
¢u¢w¢w interface/          # Kod modu?u interfejsu (Flask)
¢u¢w¢w engine/             # Kod modu?u silnika (FastAPI)
¢u¢w¢w docker-compose.yml  # Konfiguracja Dockera
¢|¢w¢w README.md           # Ten plik
```
