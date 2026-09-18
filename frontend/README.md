# READMEForge Frontend

React + Vite + Tailwind CSS frontend for `AnujrajShrestha/readme_file_maker`.

The UI is connected to the FastAPI endpoint:

- `GET /`
- `POST /maker`

The backend `/maker` expects:

```json
{
  "url": "https://github.com/user/repository",
  "project_name": "Project Name",
  "author_name": "Author Name",
  "github_id_url": "https://github.com/user"
}
```

## Setup

```bash
npm install
```

Create `.env` from `.env.example` if your backend is not running on port 8000.

```bash
npm run dev
```

Open the Vite URL shown in the terminal.

## Production build

```bash
npm run build
npm run preview
```

## Backend

From the backend directory:

```bash
uvicorn main:app --reload
```

The frontend defaults to `http://127.0.0.1:8000`. Override it with:

```env
VITE_API_URL=https://your-backend.example.com
```

## Design

- Dark responsive layout
- Tailwind CSS v4
- Animated SVG background
- Glassmorphism cards
- Mobile-friendly form
- Loading/error/success states
- Markdown README rendering
- Copy README action
- GitHub repository links
