# risk_scoring.py
def compute_score(findings: dict) -> int:
    score = 100
    if findings.get("owner_withdraw"):
        score -= 35
    if findings.get("no_timelock"):
        score -= 20
    score -= 10 * len(findings.get("suspicious_primitives", []))
    if score < 0:
        score = 0
    return score
