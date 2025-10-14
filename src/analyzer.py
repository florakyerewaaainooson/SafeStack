# analyzer.py
def analyze_code(code: str) -> dict:
    """Return findings as a dict of detected risk signatures."""
    findings = {"owner_withdraw": False, "no_timelock": False, "suspicious_primitives": []}

    lc = code.lower()
    if "withdraw-all" in lc or "withdraw" in lc:
        findings["owner_withdraw"] = True
        findings["suspicious_primitives"].append("unrestricted-withdraw")
    if "time-lock" not in lc and "timelock" not in lc and "lock" not in lc:
        findings["no_timelock"] = True
    # add simple pattern checks
    if "contract-call?" in lc and "owner" in lc:
        findings["suspicious_primitives"].append("owner-executes-withdrawals")

    return findings
