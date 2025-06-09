# 馃寪 Webscraper - Skaner Stron Internetowych 馃殌

Projekt przygotowany na uczelnie.

## 馃搵 Opis projektu

**Webscraper** to narz臋dzie umo偶liwiaj膮ce u偶ytkownikom skanowanie stron internetowych w celu pozyskania kluczowych danych, takich jak tytu艂y stron, adresy e-mail, liczba link贸w wewn臋trznych, struktura organizacyjna czy statystyki tag贸w HTML. Aplikacja sk艂ada si臋 z trzech g艂贸wnych modu艂贸w: interfejsu u偶ytkownika, silnika skanowania oraz bazy danych, kt贸re wsp贸艂dzia艂aj膮 w harmonijny spos贸b. 馃洜锔?
## 鉁?G艂贸wne funkcjonalno艣ci

- **Wprowadzanie adres贸w URL** 馃摑: U偶ytkownik mo偶e wprowadzi膰 list臋 adres贸w URL (oddzielonych przecinkami) za pomoc膮 intuicyjnego interfejsu.
- **Asynchroniczne skanowanie** 鈿? Szybkie i wydajne przetwarzanie wielu stron dzi臋ki asynchronicznym 偶膮daniom HTTP.
- **Przegl膮danie wynik贸w** 馃搳: Dane wy艣wietlane w czytelnej formie tabelarycznej, zawieraj膮cej szczeg贸艂y ka偶dej zeskanowanej witryny.
- **Trwa艂e przechowywanie danych** 馃捑: Wyniki zapisywane w bazie MongoDB, co umo偶liwia ich p贸藕niejsze wykorzystanie.

## 馃З Struktura projektu

Projekt zosta艂 podzielony na trzy modu艂y, z kt贸rych ka偶dy pe艂ni unikaln膮 rol臋:

- **webscraper-interface** 馃枼锔? Interfejs u偶ytkownika oparty na frameworku Flask. Umo偶liwia wprowadzanie adres贸w URL i przegl膮danie wynik贸w w przejrzystej formie.
- **webscraper-engine** 馃攳: Silnik skanowania oparty na FastAPI. Odpowiada za asynchroniczne pobieranie i analiz臋 stron przy u偶yciu bibliotek BeautifulSoup i aiohttp.
- **mongo** 馃梽锔? Modu艂 integracji z baz膮 danych MongoDB, wykorzystuj膮cy asynchroniczny sterownik `motor` do przechowywania i pobierania danych.

## 馃搱 Zbierane dane

Aplikacja gromadzi nast臋puj膮ce informacje z ka偶dej zeskanowanej strony:

- **Tytu艂 strony** 馃摐: Pobierany z tagu `<title>`.
- **Adresy e-mail** 鉁夛笍: Wyodr臋bniane za pomoc膮 wyra偶e艅 regularnych.
- **Liczba link贸w wewn臋trznych** 馃敆: Zliczane na podstawie odno艣nik贸w w obr臋bie tej samej domeny.
- **Struktura organizacyjna** 馃搼: Okre艣lana na podstawie nag艂贸wk贸w (`<h1>`, `<h2>`, `<h3>`).
- **Liczba tag贸w HTML** 馃彿锔? Statystyki wyst膮pie艅 poszczeg贸lnych tag贸w w kodzie strony.

## 馃洜锔?U偶yte technologie

Projekt opiera si臋 na nowoczesnym stosie technologicznym:

- **Python** 馃悕: J臋zyk programowania zapewniaj膮cy czytelno艣膰 i elastyczno艣膰.
- **Flask** 馃寪: Lekki framework webowy do tworzenia interfejsu u偶ytkownika.
- **FastAPI** 馃殌: Asynchroniczny framework do budowy wydajnego API.
- **BeautifulSoup** 馃Ч: Biblioteka do parsowania kodu HTML.
- **aiohttp** 馃實: Asynchroniczne 偶膮dania HTTP dla szybkiego pobierania stron.
- **MongoDB** 馃梼锔? NoSQL-owa baza danych do przechowywania wynik贸w.
- **motor** 馃攲: Asynchroniczny sterownik dla MongoDB.
- **Docker** 馃惓: Konteneryzacja zapewniaj膮ca sp贸jne 艣rodowisko uruchomieniowe.

## 馃彈锔?Architektura

Aplikacja dzia艂a w oparciu o architektur臋 klient-serwer:
- **Interfejs** (Flask) komunikuje si臋 z **silnikiem** (FastAPI) poprzez RESTful API.
- **Silnik** przetwarza 偶膮dania, skanuje strony i zapisuje wyniki do bazy **MongoDB**.
- **Docker** zapewnia izolacj臋 i 艂atwe uruchamianie wszystkich komponent贸w w sieci `scraper-network`.

## 馃殌 Jak uruchomi膰?

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/<twoje-nazwa-uzytkownika>/webscraper.git
   cd webscraper
   ```

2. **Uruchom za pomoc膮 Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Otw贸rz przegl膮dark臋** i przejd藕 na adres:
   ```
   http://localhost:5000
   ```

4. Wprowad藕 adresy URL, kliknij "Skanuj" i przegl膮daj wyniki! 馃帀

## 馃搨 Struktura katalog贸w

```plaintext
webscraper/
鈹溾攢鈹€ interface/          # Kod modu艂u interfejsu (Flask)
鈹溾攢鈹€ engine/            # Kod modu艂u silnika (FastAPI)
鈹溾攢鈹€ docker-compose.yml  # Konfiguracja Dockera
鈹斺攢鈹€ README.md          # Ten plik
```

## 馃 Jak mog臋 pom贸c?

Chcesz doda膰 now膮 funkcj臋 lub zg艂osi膰 b艂膮d? 馃挕 Otw贸rz **issue** lub wy艣lij **pull request**! Wszelkie uwagi i sugestie s膮 mile widziane. 馃槉

## 馃摐 Licencja

Projekt jest dost臋pny na licencji MIT. Szczeg贸艂y znajdziesz w pliku `LICENSE`.

---

**Webscraper** to idealne narz臋dzie dla ka偶dego, kto chce szybko i efektywnie analizowa膰 strony internetowe. Do艂膮cz do nas i odkryj moc web scrapingu! 馃専