from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

POLICY_FILE = Path("policies.txt")


class QuestionRequest(BaseModel):
    question: str


HTML_PAGE = """<!DOCTYPE html>
<html>
<head>
<title>Commute Policy Assistant</title>
</head>
<body style="background-color: #ffffff; color: #000000; font-family: serif; margin: 0; padding: 0;">
<h1 style="background:#000; color:#fff; margin:0;">Commute Policy Assistant</h1>
<p>ask something about policy</p>
<form onsubmit="ask(event)">
<input id="q" type="text" placeholder="question" style="background:#fff; color:#000; border:2px solid #000;">
<br><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button type="submit" style="background:#000; color:#fff; border:1px solid #000;">Submit</button>
</form>
<br>
<div id="ans" style="border:1px solid #000; background:#fff; color:#000; width:300px; margin-left:47px;"></div>
<script>
async function ask(e) {
  e.preventDefault();
  const q = document.getElementById("q").value;
  const res = await fetch("/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({question: q})
  });
  const data = await res.json();
  document.getElementById("ans").innerText = data.answer;
}
</script>
</body>
</html>
"""


def find_answer(question: str) -> str:
    if not POLICY_FILE.exists():
        return "no policy file"
    lines = [line.strip() for line in POLICY_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
    words = [w.lower().strip("?.,!") for w in question.split() if len(w) > 2]
    for line in lines:
        lower_line = line.lower()
        if any(w in lower_line for w in words):
            return line
    return "not sure"


@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE


@app.post("/ask")
def ask_question(req: QuestionRequest):
    return {"answer": find_answer(req.question)}
