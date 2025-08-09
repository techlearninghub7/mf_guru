# MF Guru — Sprint 0

## Goal
Sprint 0 skeleton: FastAPI backend, Supabase-ready Postgres, basic AMFI seed, Vercel serverless config.

## Prereqs
- Python 3.11
- pip
- Git
- (Optional) Docker
- Supabase project & DATABASE_URL

## Local setup (Windows)
1. Copy `.env.example` -> `.env` and set `DATABASE_URL`.
2. Run `run_local.bat`. This will:
   - create venv (if missing),
   - install requirements,
   - start uvicorn on 127.0.0.1:8000

3. Verify:
   - `GET http://127.0.0.1:8000/` => root message.
   - `GET http://127.0.0.1:8000/api/v1/health`
   - `POST http://127.0.0.1:8000/api/v1/funds/seed` to seed sample funds (calls AMFI).

## Deploy
- Push repository to GitHub.
- Connect to Vercel and set environment variable `DATABASE_URL` (Supabase connection).
- Vercel will build using `vercel.json`.

## Next steps
- Add Alembic-based migrations
- Replace seeder with robust AMFI parser + backfill historical NAV
- Add LLM summarizer (LangChain / HF) and caching
- Add risk profiler & recommendation engine
