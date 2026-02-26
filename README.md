# 🗂️ Log Parser — Lesson 1

> A Python project for safely parsing structured log files line-by-line.  
> Built for cloud operations teams who need to filter, validate, and export log data.

---

## 📌 Table of Contents

- [Project Description](#-project-description)
- [Log Format](#-log-format)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [How to Run Each Task](#-how-to-run-each-task)
  - [Task 1 — Parse a Single Line](#task-1--parse-a-single-line)
  - [Task 2 — Parse a List of Lines](#task-2--parse-a-list-of-lines)
  - [Task 3 — Parse a Log File](#task-3--parse-a-log-file)
  - [Task 4 — Count Invalid Lines](#task-4--count-invalid-lines)
  - [Task 5 — Export to JSON](#task-5--export-to-json)
- [Run All Tasks at Once](#-run-all-tasks-at-once)
- [Expected Output](#-expected-output)
- [How the Parser Works](#-how-the-parser-works)
- [Author](#-author)

---

## 📖 Project Description

This project implements a **log line parser** for an operations team that receives large log files daily. Each file contains hundreds of lines — some are clean, some have extra whitespace, and some are completely broken.

The core function `parse_log_line()` safely processes each line and returns structured data or `None` if the line is invalid. This parsed data is then used to filter valid entries, count bad lines, and export results to JSON.

**Key goals:**
- Parse log lines into structured tuples
- Skip and count invalid/malformed lines without crashing
- Export clean data to JSON for downstream use

> ⚠️ **Lesson 1 scope:** Format validation only (exactly 4 fields). Level validation (e.g. ERROR, INFO) is added in Lesson 2.

---

## 📋 Log Format

A **valid** log line follows this exact structure:

```
timestamp | level | service | message
```

**Example:**
```
2026-02-05 08:11:20 | ERROR | db | DB timeout
```

| Field       | Description                        | Example                  |
|-------------|------------------------------------|--------------------------|
| `timestamp` | Date and time of the event         | `2026-02-05 08:11:20`    |
| `level`     | Severity level                     | `ERROR`, `INFO`, `WARN`  |
| `service`   | The service that generated the log | `db`, `api`, `auth`      |
| `message`   | Human-readable description         | `DB timeout`             |

**Invalid lines (will return `None`):**
```
BAD LINE WITHOUT SEPARATORS          ← no pipe separators
2026-02-05 | INFO | auth | ok | EXTRA  ← 5 fields instead of 4
                                      ← empty line
```

---

## 📁 Project Structure

```
log-parser-lesson1/
│
├── task1_parse_single.py     # Core parse function + 4 test cases
├── task2_parse_list.py       # Parse a Python list of lines
├── task3_parse_file.py       # Read and parse sample_logs.txt
├── task4_report_invalids.py  # Count valid vs invalid lines
├── task5_export_parsed_json.py  # Export results to JSON
│
├── sample_logs.txt           # Sample log file (input)
├── parsed_logs.json          # Generated output (created by Task 5)
│
└── README.md                 # This file
```

---

## ⚙️ Setup & Installation

### Requirements

- **Python 3.7+** (no external libraries needed — standard library only)
- **Git** (for pushing to GitHub)

### Step 1 — Clone or open in GitHub Codespaces

**Option A: GitHub Codespaces (recommended)**
1. Go to your repository on GitHub
2. Click the green **"Code"** button → **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait ~30 seconds for the environment to load

**Option B: Clone locally**
```bash
git clone https://github.com/YOUR_USERNAME/log-parser-lesson1.git
cd log-parser-lesson1
```

### Step 2 — Verify Python is installed

```bash
python --version
```

You should see `Python 3.x.x`. If not, install Python from [python.org](https://python.org).

### Step 3 — Confirm all files are present

```bash
ls
```

You should see:
```
task1_parse_single.py  task3_parse_file.py        task5_export_parsed_json.py
task2_parse_list.py    task4_report_invalids.py   sample_logs.txt   README.md
```

> ⚠️ If files are missing, upload them via the Codespaces file explorer (right-click → Upload).

---

## ▶️ How to Run Each Task

### Task 1 — Parse a Single Line

**File:** `task1_parse_single.py`  
**What it does:** Implements the core `parse_log_line()` function and runs 4 built-in test cases.

```bash
python task1_parse_single.py
```

**Expected output:**
```
Case 1 [PASS]: expected=('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout') got=('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout')
Case 2 [PASS]: expected=('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout') got=('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout')
Case 3 [PASS]: expected=None got=None
Case 4 [PASS]: expected=None got=None

All tests passed!
```

---

### Task 2 — Parse a List of Lines

**File:** `task2_parse_list.py`  
**What it does:** Runs `parse_log_line()` on a hardcoded Python list and prints all valid results.

```bash
python task2_parse_list.py
```

**Expected output:**
```
Parsed results:
('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout')
('2026-02-05 08:11:25', 'warn', 'api', 'Slow response (920ms)')

Total input lines : 4
Valid parsed lines : 2
Skipped (invalid) : 2
```

---

### Task 3 — Parse a Log File

**File:** `task3_parse_file.py`  
**What it does:** Reads `sample_logs.txt` line-by-line and prints the first 5 valid parsed tuples.

```bash
python task3_parse_file.py
```

**Expected output:**
```
First 5 valid parsed lines:
('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout')
('2026-02-05 08:11:21', 'INFO', 'auth', 'User login successful')
('2026-02-05 08:11:22', 'WARN', 'api', 'Slow response (920ms)')
('2026-02-05 08:11:23', 'ERROR', 'api', 'Connection refused')
('2026-02-05 08:11:24', 'INFO', 'db', 'Query completed in 12ms')

Total valid lines found: 17
```

> ⚠️ Requires `sample_logs.txt` in the same folder.

---

### Task 4 — Count Invalid Lines

**File:** `task4_report_invalids.py`  
**What it does:** Reads the log file and counts total, valid, and invalid lines.

```bash
python task4_report_invalids.py
```

**Expected output:**
```
Total lines: 21
Valid lines: 17
Invalid format lines: 4
```

> ⚠️ Requires `sample_logs.txt` in the same folder.

---

### Task 5 — Export to JSON

**File:** `task5_export_parsed_json.py`  
**What it does:** Reads the log file, parses all valid lines, and exports them to `parsed_logs.json`.

```bash
python task5_export_parsed_json.py
```

**Expected output:**
```
Wrote 17 records to parsed_logs.json
```

**Verify the JSON was created:**
```bash
cat parsed_logs.json
```

**JSON structure:**
```json
[
  {
    "timestamp": "2026-02-05 08:11:20",
    "level": "ERROR",
    "service": "db",
    "message": "DB timeout"
  },
  {
    "timestamp": "2026-02-05 08:11:21",
    "level": "INFO",
    "service": "auth",
    "message": "User login successful"
  }
]
```

> ⚠️ Requires `sample_logs.txt` in the same folder. Creates `parsed_logs.json` automatically.

---

## ⚡ Run All Tasks at Once

Paste this into your terminal to run all 5 tasks in sequence:

```bash
echo "=== TASK 1 ===" && python task1_parse_single.py && \
echo "=== TASK 2 ===" && python task2_parse_list.py && \
echo "=== TASK 3 ===" && python task3_parse_file.py && \
echo "=== TASK 4 ===" && python task4_report_invalids.py && \
echo "=== TASK 5 ===" && python task5_export_parsed_json.py
```

Then push everything to GitHub:

```bash
git add .
git commit -m "Complete all 5 log parser tasks - Lesson 1"
git push
```

---

## ✅ Expected Output Summary

| Task | File | Result |
|------|------|--------|
| Task 1 | `task1_parse_single.py` | 4/4 test cases PASS |
| Task 2 | `task2_parse_list.py` | 2 valid, 2 skipped |
| Task 3 | `task3_parse_file.py` | First 5 valid lines printed |
| Task 4 | `task4_report_invalids.py` | 21 total, 17 valid, 4 invalid |
| Task 5 | `task5_export_parsed_json.py` | `parsed_logs.json` with 17 records |

---

## 🔍 How the Parser Works

The core function `parse_log_line()` follows 6 steps:

```python
def parse_log_line(line: str):
    # Step 1: Strip leading/trailing whitespace
    line = line.strip()

    # Step 2: If empty after stripping → invalid
    if not line:
        return None

    # Step 3: Split by pipe character '|'
    parts = line.split('|')

    # Step 4: Strip whitespace from each field
    parts = [p.strip() for p in parts]

    # Step 5: Must have exactly 4 fields → otherwise invalid
    if len(parts) != 4:
        return None

    # Step 6: Return as a tuple (timestamp, level, service, message)
    return tuple(parts)
```

| Scenario | Result |
|----------|--------|
| `"2026-02-05 08:11:20 \| ERROR \| db \| DB timeout"` | ✅ Returns tuple |
| `"  line with spaces  "` after strip | ✅ Handles correctly |
| `""` or `"   "` | ❌ Returns `None` |
| `"no pipes here"` | ❌ Returns `None` |
| `"a \| b \| c \| d \| e"` (5 fields) | ❌ Returns `None` |

---

## 👤 Author

**ABS973**  
GitHub: [@ABS973](https://github.com/ABS973)  
Project: Log Parser — Lesson 1  
Language: Python 3  
