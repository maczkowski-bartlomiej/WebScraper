# ?? Webscraper - Skaner Stron Internetowych ??

Projekt przygotowany na uczelnie.

## ?? Opis projektu

Webscraper to narz?dzie umo?liwiaj?ce u?ytkownikom skanowanie stron internetowych w celu pozyskania kluczowych danych, takich jak tytu?y stron, adresy e-mail, liczba link車w wewn?trznych, struktura organizacyjna czy statystyki tag車w HTML. Aplikacja sk?ada si? z trzech g?車wnych modu?車w: interfejsu u?ytkownika, silnika skanowania oraz bazy danych, kt車re wsp車?dzia?aj? w harmonijny spos車b. ???

## ? G?車wne funkcjonalno?ci

- **Wprowadzanie adres車w URL ??:** U?ytkownik mo?e wprowadzi? list? adres車w URL (oddzielonych przecinkami) za pomoc? intuicyjnego interfejsu.
- **Asynchroniczne skanowanie ?:** Szybkie i wydajne przetwarzanie wielu stron dzi?ki asynchronicznym ??daniom HTTP.
- **Przegl?danie wynik車w ??:** Dane wy?wietlane w czytelnej formie tabelarycznej, zawieraj?cej szczeg車?y ka?dej zeskanowanej witryny.
- **Trwa?e przechowywanie danych ??:** Wyniki zapisywane w bazie MongoDB, co umo?liwia ich p車?niejsze wykorzystanie.

## ?? Struktura projektu

Projekt zosta? podzielony na trzy modu?y:

- **webscraper-interface ???:** Interfejs u?ytkownika oparty na frameworku Flask. Umo?liwia wprowadzanie adres車w URL i przegl?danie wynik車w w przejrzystej formie.
- **webscraper-engine ??:** Silnik skanowania oparty na FastAPI. Odpowiada za asynchroniczne pobieranie i analiz? stron przy u?yciu bibliotek BeautifulSoup i aiohttp.
- **mongo ???:** Modu? integracji z baz? danych MongoDB, wykorzystuj?cy asynchroniczny sterownik motor do przechowywania i pobierania danych.

## ?? Zbierane dane

Aplikacja gromadzi nast?puj?ce informacje z ka?dej zeskanowanej strony:

- **Tytu? strony ??:** Pobierany z tagu <title>.
- **Adresy e-mail ??:** Wyodr?bniane za pomoc? wyra?e里 regularnych.
- **Liczba link車w wewn?trznych ??:** Zliczane na podstawie odno?nik車w w obr?bie tej samej domeny.
- **Struktura organizacyjna ??:** Okre?lana na podstawie nag?車wk車w.
- **Liczba tag車w HTML ???:** Statystyki wyst?pie里 poszczeg車lnych tag車w w kodzie strony.

## ??? U?yte technologie

- **Python:** J?zyk programowania zapewniaj?cy czytelno?? i elastyczno??.
- **Flask:** Lekki framework webowy do tworzenia interfejsu u?ytkownika.
- **FastAPI:** Asynchroniczny framework do budowy wydajnego API.
- **BeautifulSoup:** Biblioteka do parsowania kodu HTML.
- **aiohttp:** Asynchroniczne ??dania HTTP dla szybkiego pobierania stron.
- **MongoDB:** NoSQL-owa baza danych do przechowywania wynik車w.
- **motor:** Asynchroniczny sterownik dla MongoDB.
- **Docker:** Konteneryzacja zapewniaj?ca sp車jne ?rodowisko uruchomieniowe.

## ??? Architektura

Aplikacja dzia?a w oparciu o architektur? klient-serwer:
- **Interfejs** (Flask) komunikuje si? z silnikiem (FastAPI) poprzez RESTful API.
- **Silnik** przetwarza ??dania, skanuje strony i zapisuje wyniki do bazy MongoDB.
- **Docker** zapewnia izolacj? i ?atwe uruchamianie wszystkich komponent車w w sieci scraper-network.

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

3. **Otw車rz przegl?dark?** i przejd? na adres:
   ```
   http://localhost:5000
   ```

?? Struktura katalog車w
```plaintext
webscraper/
念岸岸 interface/          # Kod modu?u interfejsu (Flask)
念岸岸 engine/             # Kod modu?u silnika (FastAPI)
念岸岸 docker-compose.yml  # Konfiguracja Dockera
弩岸岸 README.md           # Ten plik
```
