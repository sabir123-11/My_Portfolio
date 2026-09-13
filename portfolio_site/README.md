# Sk Sabir Raja — Portfolio Website

A single-page portfolio built with **Django** (backend, templating, static
files, resume download, contact form) and hand-written **HTML/CSS/JS**
(frontend). No database records are required to run it — all your resume
content (education, skills, projects, experience, certifications,
achievements) lives in one place: `portfolio/views.py`.

## What's inside

- `portfolio_site/` — Django project settings/urls
- `portfolio/` — the one app that renders everything
  - `views.py` — **all your content lives here** (edit this to update the site)
  - `templates/portfolio/index.html` — the page markup
  - `static/portfolio/css/style.css` — all styling
  - `static/portfolio/js/main.js` — mobile nav + active-section highlighting
  - `static/portfolio/img/profile.jpg` — your photo
  - `static/portfolio/resume/Sk_Sabir_Raja_Resume.pdf` — your resume, servable
    for viewing/downloading straight from the site

## Run it locally

```bash
# 1. create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 2. install Django
pip install -r requirements.txt

# 3. apply Django's built-in migrations (auth/sessions tables only —
#    the portfolio itself needs no database)
python manage.py migrate

# 4. run the dev server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

## Updating your content

Everything is in `portfolio/views.py` as plain Python lists/dicts:
`PROFILE`, `EDUCATION`, `SKILLS`, `EXPERIENCE`, `PROJECTS`,
`CERTIFICATIONS`, `ACHIEVEMENTS`. Add a new project by adding one more
dictionary to the `PROJECTS` list — the template loops over it
automatically, no HTML changes needed.

To swap your photo or resume, just replace the files at
`portfolio/static/portfolio/img/profile.jpg` and
`portfolio/static/portfolio/resume/Sk_Sabir_Raja_Resume.pdf` (keep the same
filenames, or update the paths in `views.py` / `index.html`).

## Contact form

The contact form currently prints submitted messages to your terminal
(via Django's console email backend) and shows a confirmation message on
the page. To actually receive messages by email, open
`portfolio_site/settings.py` and replace `EMAIL_BACKEND` with your SMTP
provider's settings (Gmail, SendGrid, etc.), then send the message inside
`contact_submit()` in `portfolio/views.py` using Django's `send_mail()`.

## Deploying

Before putting this on a real server:

1. Set `DEBUG = False` in `portfolio_site/settings.py`.
2. Replace `SECRET_KEY` with a new, private value.
3. Set `ALLOWED_HOSTS` to your actual domain.
4. Run `python manage.py collectstatic` and serve the `staticfiles/`
   folder through your host (or WhiteNoise/Nginx).

Any host that runs Django (Railway, Render, PythonAnywhere, a VPS with
Gunicorn+Nginx) will work.
