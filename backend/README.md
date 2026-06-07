# QuoteBook Backend

This Django backend serves the static frontend, saves uploaded PDFs to disk, stores book metadata in SQLite, and exposes the local API used by the reader.

## Run Locally

From the project root:

```bash
python3 run.py
```

On Windows, use `python run.py`. The launcher creates `.venv`, installs dependencies, runs migrations, and starts the app at `http://localhost:8000`.

Uploaded PDFs are saved in:

```text
backend/uploads/pdfs/
```

The frontend expects the backend API on the same origin as the served pages. With the commands above, open `http://localhost:8000`.

For downloadable laptop apps, use the Electron/PyInstaller packaging flow from the project root. Desktop builds store each user's library in their OS app-data folder. The static PWA remains available for browser-based hosting.
