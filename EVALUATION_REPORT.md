# Evaluation Report - Case Study B

## Test scenarios
- Basic lookup for night drop approval rule.
- Basic lookup for weekend cab rule.
- Basic lookup for airport trip rule.

## Method
- Ran `eval.py` against `eval.jsonl` using exact string comparison on `find_answer`.

## Results
- 3 / 3 cases in `eval.jsonl` matched expected strings.

## Known failures
- Paraphrased questions fail to match keywords and return `"not sure"`.
- Cross-company queries, policy versioning, JWT auth, and citation checks are not implemented.

## Limitations
- Only one hardcoded plain-text policy exists (`policies.txt`).
- No Chroma vector store, no LLM, and no error/timeout handling.

## Trade-off
- Chose plain text keyword lookup over RAG + LLM to keep the setup minimal and avoid external dependencies, sacrificing semantic matching and policy isolation.
