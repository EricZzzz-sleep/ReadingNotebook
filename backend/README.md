# Backend

This Django backend serves the static frontend, saves uploaded PDFs to disk, stores book metadata in SQLite, and exposes the local API used by the reader.

## Run Locally

From the project root:

```bash
python3 -m pip install -r backend/requirements.txt
cd backend
python3 manage.py migrate
python3 manage.py runserver 8000
```

Uploaded PDFs are saved in:

```text
backend/uploads/pdfs/
```

The frontend expects the backend API on the same origin as the served pages. With the commands above, open `http://localhost:8000`.
