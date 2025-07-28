# TaskUnit Logbook (SQLite-pohjainen)

Tämä projekti on osa ICT-varusmieshaun valintatehtävää. Se on yksinkertainen sovellus, joka tallentaa ja näyttää partiointi-/vartiointilokeja.

## 🔧 Miksi SQLite?

Halusin käyttää SQL-palvelinta (kuten PostgreSQL), mutta minulla ei ollut tarpeeksi aikaa. Siksi valitsin **SQLite**:n, koska se on kevyt ja nopea ottaa käyttöön ilman erillistä palvelinta.

## 🛠️ Käytetyt teknologiat

- **FastAPI** – Backend-sovelluskehys
- **SQLite** – Paikallinen tietokanta
- **SQLAlchemy** – ORM SQLite:lle
- **Uvicorn** – Sovelluspalvelin
- **Render.com** – Julkinen hostaus

## 🗂 Hakemistorakenne

TaskUnit_Logbook_With_SQLite/ │ ├── main.py                # FastAPI-sovelluksen päälogiikka ├── database.py            # SQLite-yhteys ja tietokantamalli ├── models.py              # SQLAlchemy-mallit ├── schemas.py             # Pydantic-tietomallit ├── requirements.txt       # Riippuvuudet └── sample-data/           # Esimerkkitietoa

## 🚀 Kuinka suorittaa paikallisesti

1. Asenna riippuvuudet:

```bash
pip install -r requirements.txt

2. Käynnistä palvelin:



uvicorn main:app --reload

3. Avaa selain:



http://127.0.0.1:8000/docs

Voit testata REST-rajapintaa interaktiivisesti Swagger UI:n kautta.

🌐 Testaus Render.com-palvelussa

Sovellus on julkaistu Render.comissa:

🔗 https://test-ictconscript-admission-h6o6.onrender.com

Kokeile API:a täällä:

https://test-ictconscript-admission-h6o6.onrender.com/docs

✅ Esimerkki POST /entries

Luo uusi lokimerkintä:

{
  "title": "Yöpartiointi valmis",
  "body": "Kaikki kunnossa pääportilla.",
  "lat": 60.1503,
  "lon": 25.0293
}

⏱️ Huom: Sovellus lisää automaattisesti id-kentän ja isoTime-ajan.

🧪 Testaus Postmanilla

1. Avaa Postman.


2. Luo uusi POST-pyyntö osoitteeseen:



https://test-ictconscript-admission-h6o6.onrender.com/entries

3. Valitse välilehti Body → raw → JSON ja lisää JSON-data (katso yllä).


4. Paina Send.



📎 Linkit

Repo: test-ictconscript-admission

Tehtävä: TaskUnit_Logbook_With_SQLite-kansio

---

Kiitos mahdollisuudesta! 🙏

YT.Abdulhadi Labanie
