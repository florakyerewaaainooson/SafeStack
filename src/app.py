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
    return """
    <html>
        <head>
            <title>SafeStack</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background: #0d1117;
                    color: #f0f6fc;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    font-size: 2.5em;
                    color: #58a6ff;
                }
                p {
                    font-size: 1.2em;
                    color: #8b949e;
                }
            </style>
        </head>
        <body>
            <h1>✅ SafeStack is Live</h1>
            <p>Your AI-powered Bitcoin Security Analyzer is running smoothly.</p>
            <p>Use the <b>POST /analyze</b> endpoint to test your smart contract security.</p>
        </body>
    </html>
    """


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
