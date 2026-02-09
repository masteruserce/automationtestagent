import os
import json
from pathlib import Path
from openai import OpenAI

client = OpenAI()

ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_DIR = ROOT / "automation"
UI_DIR = AUTOMATION_DIR / "ui"
API_DIR = AUTOMATION_DIR / "api"
UTILS_DIR = AUTOMATION_DIR / "utils"
PIPELINE_FILE = ROOT / ".github/workflows/automation.yml"


# ---------------------------
# Utilities
# ---------------------------
def safe_write(path: Path, content: str):
    if path.exists():
        print(f"{path} already exists- overriding")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[CREATED] {path}")

    path.write_text(content, encoding="utf-8")
    print(f"[updated] {path}")


def llm_generate(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You generate ONLY runnable code. No explanations.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


# ---------------------------
# UI Test Generator
# ---------------------------
def generate_ui_test(base_url: str, flow: str):
    prompt = f"""
Generate Playwright Python test using pytest.

Rules:
- No explanations
- No markdown
- Use sync_playwright
- Deterministic waits
- Base URL: {base_url}

Test flow:
{flow}
"""
    code = llm_generate(prompt)
    clean_code = strip_markdown_fences(code)
    safe_write(UI_DIR / f"test_{flow}_ui.py", clean_code)


# ---------------------------
# API Test Generator
# ---------------------------
def generate_api_test(base_url: str, endpoints: list):
    prompt = f"""
Generate pytest API tests using requests.

Rules:
- No explanations
- Validate status code and JSON keys
- Base URL: {base_url}

Endpoints:
{json.dumps(endpoints, indent=2)}
"""
    code = llm_generate(prompt)
    clean_code = strip_markdown_fences(code)
    safe_write(API_DIR / "test_api.py", clean_code)


# ---------------------------
# Common Files
# ---------------------------
def ensure_common_files():
    safe_write(UTILS_DIR / "config.py", """BASE_URL = """ "")

    safe_write(
        AUTOMATION_DIR / "requirements.txt",
        """pytest
pytest-html
requests
playwright
""",
    )

    safe_write(AUTOMATION_DIR / "conftest.py", """import pytest""")


# ---------------------------
# GitHub Actions Pipeline
# ---------------------------
def ensure_pipeline():
    if not PIPELINE_FILE.exists():
        PIPELINE_FILE.parent.mkdir(parents=True, exist_ok=True)

    PIPELINE_FILE.write_text(
        """name: Automation Tests

on:
  push:
  workflow_dispatch:

jobs:
  automation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r automation/requirements.txt
          playwright install --with-deps

      - name: Run tests
        run: |
          pytest automation --html=report.html --self-contained-html

      - name: Publish report
        uses: actions/upload-artifact@v4
        with:
          name: automation-report
          path: report.html
""",
        encoding="utf-8",
    )
    print("[CREATED] GitHub Actions pipeline")


# ---------------------------
# Main Agent Entry
# ---------------------------
def run_agent(spec: dict):
    base_url = spec["base_url"]

    ensure_common_files()
    ensure_pipeline()

    for flow in spec.get("ui_flows", []):
        generate_ui_test(base_url, flow)

    generate_api_test(base_url, spec.get("api_endpoints", []))

    print("\n✅ Automation agent completed successfully")


def strip_markdown_fences(code: str) -> str:
    code = code.strip()

    # Remove triple-backtick fences
    if code.startswith("```"):
        code = code.split("```", 1)[1]

    if code.endswith("```"):
        code = code.rsplit("```", 1)[0]

    code = code.strip()

    # Remove a leading language tag like "python"
    first_line = code.splitlines()[0].strip().lower()
    if first_line in {"python", "py"}:
        code = "\n".join(code.splitlines()[1:])

    return code.strip()


# ---------------------------
# Run directly
# ---------------------------
if __name__ == "__main__":
    SPEC = {
        "base_url": "https://example.com",
        "ui_flows": ["login"],
        "api_endpoints": [
            {"method": "GET", "path": "/api/users"},
            {"method": "POST", "path": "/api/login"},
        ],
    }

    run_agent(SPEC)
