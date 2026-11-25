# Case Study B - Commute Policy Assistant

## How to run

Option 1 (Docker):
```bash
docker compose up
```

Option 2 (Local `.venv`):
```powershell
.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Run evaluation script:
```powershell
.venv\Scripts\python.exe eval.py
```

## Design decisions
- Used FastAPI with a single `/ask` POST endpoint and a plain HTML page at `/`.
- Policy text is kept in a plain text file (`policies.txt`) and matched by simple keyword check instead of Chroma, embeddings, or an LLM.
- No JWT, company filtering, policy versioning, or citation formatting is implemented.

## Trade-offs
- Keyword matching on a static text file avoids LLM API setup, latency, and database dependencies, at the cost of not handling paraphrases, multi-company isolation, or missing-policy cases properly.
