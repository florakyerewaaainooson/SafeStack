# ai_explainer.py
def explain_findings(findings: dict) -> str:
    msgs = []
    if findings.get("owner_withdraw"):
        msgs.append("This contract contains a withdrawal function that may allow the owner to remove funds.")
    if findings.get("no_timelock"):
        msgs.append("There is no apparent time-lock on withdrawals, which increases risk of sudden fund removals.")
    if findings.get("suspicious_primitives"):
        msgs.append("Detected suspicious patterns: " + ", ".join(findings["suspicious_primitives"]))
    if not msgs:
        return "No obvious high-risk patterns detected in this basic scan."
    return " ".join(msgs)
