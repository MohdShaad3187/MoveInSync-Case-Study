import json
from pathlib import Path
from app import find_answer


def main():
    path = Path("eval.jsonl")
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    passed = 0
    for line in lines:
        row = json.loads(line)
        actual = find_answer(row["input"])
        ok = actual == row["expected"]
        if ok:
            passed += 1
        print(f"id={row['id']} pass={ok} actual={actual!r}")
    print(f"total={len(lines)} passed={passed}")


if __name__ == "__main__":
    main()
