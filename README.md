# TK Mall

TK Mall is a Django website that presents information about a mall and the services it provides. The project uses Django views and templates for the site pages, static assets for styling and images, and SQLite for local development data.

## Tech Stack

- Python
- Django
- SQLite
- HTML templates
- CSS and static image assets

## Pages

- Home
- About
- Contact
- Main landing page

## Project Structure

```text
mysite/
  manage.py
  db.sqlite3
  mysite/
    settings.py
    urls.py
  Tk_mall/
    views.py
    urls.py
    templates/Tk_mall/
  static/Tk_mall/
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/lampi12/Tk_mall.git
cd Tk_mall/mysite
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install Django:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the app at `http://127.0.0.1:8000/`.

## Notes

The project includes local SQLite data and generated Python cache files. A future cleanup pass should add a `.gitignore` and remove generated files from version control.
