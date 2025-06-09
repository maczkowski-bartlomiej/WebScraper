🌐 Webscraper - Skaner Stron Internetowych 🚀

Projekt przygotowany na uczelnie

📋 Opis projektu

Webscraper to narzędzie umożliwiające użytkownikom skanowanie stron internetowych w celu pozyskania kluczowych danych, takich jak tytuły stron, adresy e-mail, liczba linków wewnętrznych, struktura organizacyjna czy statystyki tagów HTML. Aplikacja składa się z trzech głównych modułów: interfejsu użytkownika, silnika skanowania oraz bazy danych, które współdziałają w harmonijny sposób. 🛠️

✨ Główne funkcjonalności





Wprowadzanie adresów URL 📝: Użytkownik może wprowadzić listę adresów URL (oddzielonych przecinkami) za pomocą intuicyjnego interfejsu.



Asynchroniczne skanowanie ⚡: Szybkie i wydajne przetwarzanie wielu stron dzięki asynchronicznym żądaniom HTTP.



Przeglądanie wyników 📊: Dane wyświetlane w czytelnej formie tabelarycznej, zawierającej szczegóły każdej zeskanowanej witryny.



Trwałe przechowywanie danych 💾: Wyniki zapisywane w bazie MongoDB, co umożliwia ich późniejsze wykorzystanie.

🧩 Struktura projektu

Projekt został podzielony na trzy moduły, z których każdy pełni unikalną rolę:





webscraper-interface 🖥️: Interfejs użytkownika oparty na frameworku Flask. Umożliwia wprowadzanie adresów URL i przeglądanie wyników w przejrzystej formie.



webscraper-engine 🔍: Silnik skanowania oparty na FastAPI. Odpowiada za asynchroniczne pobieranie i analizę stron przy użyciu bibliotek BeautifulSoup i aiohttp.



mongo 🗄️: Moduł integracji z bazą danych MongoDB, wykorzystujący asynchroniczny sterownik motor do przechowywania i pobierania danych.

📈 Zbierane dane

Aplikacja gromadzi następujące informacje z każdej zeskanowanej strony:





Tytuł strony 📜: Pobierany z tagu <title>.



Adresy e-mail ✉️: Wyodrębniane za pomocą wyrażeń regularnych.



Liczba linków wewnętrznych 🔗: Zliczane na podstawie odnośników w obrębie tej samej domeny.



Struktura organizacyjna 📑: Określana na podstawie nagłówków (<h1>, <h2>, <h3>).



Liczba tagów HTML 🏷️: Statystyki wystąpień poszczególnych tagów w kodzie strony.

🛠️ Użyte technologie

Projekt opiera się na nowoczesnym stosie technologicznym:





Python 🐍: Język programowania zapewniający czytelność i elastyczność.



Flask 🌐: Lekki framework webowy do tworzenia interfejsu użytkownika.



FastAPI 🚀: Asynchroniczny framework do budowy wydajnego API.



BeautifulSoup 🧹: Biblioteka do parsowania kodu HTML.



aiohttp 🌍: Asynchroniczne żądania HTTP dla szybkiego pobierania stron.



MongoDB 🗃️: NoSQL-owa baza danych do przechowywania wyników.



motor 🔌: Asynchroniczny sterownik dla MongoDB.



Docker 🐳: Konteneryzacja zapewniająca spójne środowisko uruchomieniowe.

🏗️ Architektura

Aplikacja działa w oparciu o architekturę klient-serwer:





Interfejs (Flask) komunikuje się z silnikiem (FastAPI) poprzez RESTful API.



Silnik przetwarza żądania, skanuje strony i zapisuje wyniki do bazy MongoDB.



Docker zapewnia izolację i łatwe uruchamianie wszystkich komponentów w sieci scraper-network.

🚀 Jak uruchomić?





Sklonuj repozytorium:

git clone https://github.com/<twoje-nazwa-uzytkownika>/webscraper.git
cd webscraper



Uruchom za pomocą Docker Compose:

docker-compose up --build



Otwórz przeglądarkę i przejdź na adres:

http://localhost:5000



Wprowadź adresy URL, kliknij "Skanuj" i przeglądaj wyniki! 🎉

📂 Struktura katalogów

webscraper/
├── interface/          # Kod modułu interfejsu (Flask)
├── engine/            # Kod modułu silnika (FastAPI)
├── docker-compose.yml  # Konfiguracja Dockera
└── README.md          # Ten plik

🤝 Jak mogę pomóc?

Chcesz dodać nową funkcję lub zgłosić błąd? 💡 Otwórz issue lub wyślij pull request! Wszelkie uwagi i sugestie są mile widziane. 😊

📜 Licencja

Projekt jest dostępny na licencji MIT. Szczegóły znajdziesz w pliku LICENSE.



Webscraper to idealne narzędzie dla każdego, kto chce szybko i efektywnie analizować strony internetowe. Dołącz do nas i odkryj moc web scrapingu! 🌟