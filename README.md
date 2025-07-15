Dynamic Movie Website Generator

Eine Python-basierte Webanwendung, die eine dynamische Film-Website generiert, indem sie Filmdaten über die OMDb API abruft und in einer lokalen SQLite-Datenbank speichert. Das Projekt automatisiert die Datenerfassung, Filterung und HTML-Erzeugung zur effizienten Verwaltung von Filmsammlungen.

Funktionen

OMDb API-Integration
Ruft Filmdetails wie Poster, Bewertungen, Genres und Zusammenfassungen über eine öffentliche API ab.

Persistente Speicherung
Speichert abgerufene Filmdaten in einer SQLite-Datenbank für effizientes Nachladen und Wiederverwendung.

Such- und Filterfunktionen
Ermöglicht das Suchen von Filmen nach Titel und das Filtern nach IMDb-Bewertungen.

Automatische HTML-Erzeugung
Erstellt dynamisch responsive Webseiten, die Filmsammlungen mit Bildern und Metadaten ansprechend darstellen.

Optimierte Benutzerfreundlichkeit
Reduziert manuellen Aufwand und sorgt dafür, dass die Website automatisch mit neuen oder aktualisierten Inhalten aktualisiert wird.

Technologien

Python 3

SQLite

OMDb API

HTML5 / CSS3

Flask

Requests

Installation und Einrichtung:

Repository klonen:
git clone https://github.com/n2fabi/Movie_Project.git

Abhängigkeiten installieren:
pip install -r requirements.txt

OMDb API-Schlüssel einrichten:
Einen API-Schlüssel auf omdbapi.com/apikey.aspx anfordern und in einer .env-Datei oder in der Konfiguration hinterlegen.

Anwendung starten:
python main.py

Generierte Website anzeigen:
Die Datei index.html im Browser öffnen, um die Filmsammlung zu betrachten.

Anwendungsfälle:

- Verwaltung einer persönlichen Filmsammlung

- Statische Seitengenerierung für Filmarchive oder Fanprojekte

- Technische Demo für API-Integration, Datenpersistenz und dynamische Inhaltserstellung
