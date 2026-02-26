# Task 1 — Parse a single line (Lesson 1)
# Implement parse_log_line(line) and run the test cases.

def parse_log_line(line: str):
    """Return (timestamp, level, service, message) OR None if invalid format."""
    # 1) Strip the whole line
    line = line.strip()
    # 2) If empty -> return None
    if not line:
        return None
    # 3) Split by '|'
    parts = line.split('|')
    # 4) Strip each part
    parts = [p.strip() for p in parts]
    # 5) If not exactly 4 parts -> return None
    if len(parts) != 4:
        return None
    # 6) Return tuple of parts
    return tuple(parts)


def run_tests():
    cases = [
        ("2026-02-05 08:11:20 | ERROR | db | DB timeout",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("  2026-02-05 08:11:20|ERROR|db|DB timeout  \n",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("BAD LINE WITHOUT SEPARATORS", None),
        ("2026-02-05 | INFO | auth | ok | EXTRA", None),
    ]

    all_passed = True
    for i, (line, expected) in enumerate(cases, start=1):
        got = parse_log_line(line)
        status = "PASS" if got == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"Case {i} [{status}]: expected={expected} got={got}")

    print("\nAll tests passed!" if all_passed else "\nSome tests FAILED.")


if __name__ == "__main__":
    run_tests()
