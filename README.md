# Reading Tracker

A personal reading tracker that helps users record books, track reading progress, write notes, and review completed books.

## Features

- Upload PDF version of the book to add books.
- Track current page and reading percentage, time and date of reading.
- Selecting quotes and write side notes for each book
- Mark the unknown vocab and provide its translation.
- Writing summary of the book

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Django
- Database: SQLite / PostgreSQL
- Version Control: Git + GitHub

## Project Structure

```text
ReadingTracker/
├── frontend/
│   ├── index.html
│   ├── shelf.html
│   ├── notes.html
│   ├── vocabulary.html
│   ├── styles.css
│   └── assets/
├── backend/
│   └── README.md
├── README.md
└── LICENSE
```

The current frontend pages are located in `frontend/`. Open `frontend/index.html` or run a local static server from the `frontend/` folder. The `backend/` folder is prepared for the future Django implementation.

## My Contribution

- Designed the book tracking system
- Built the progress tracking logic
- Implemented note-taking features
- Created the README and project documentation
- Managed GitHub issues and feature planning

## Future Improvements

- User login system
- Search and filter books
- Reading statistics dashboard
- Export notes as PDF
