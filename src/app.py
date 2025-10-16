from flask import Flask, render_template, request, jsonify
from flask import Flask, request, jsonify
from stacks_connector import fetch_contract_code
from analyzer import analyze_code
from risk_scoring import compute_score
from ai_explainer import explain_findings

app = Flask(__name__)

# ---------------------------
# Homepage route
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")



# ---------------------------
# Analyzer route
# ---------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    code = data.get("code")
    address = data.get("address")

    if address and not code:
        code = fetch_contract_code(address)  # mock connector for now

    if not code:
        return jsonify({"error": "Please provide 'address' or 'code' in JSON body"}), 400

    findings = analyze_code(code)
    score = compute_score(findings)
    explanation = explain_findings(findings)

    return jsonify({
        "safety_score": score,
        "risk_level": ("Dangerous" if score < 40 else "Moderate" if score < 70 else "Safe"),
        "findings": findings,
        "explanation": explanation
    })


# ---------------------------
# Run Flask app
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
