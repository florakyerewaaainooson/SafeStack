# stacks_connector.py
# For Phase 2 prototype this returns mock contract code for a given address.
# Replace with real Stacks API calls later.

def fetch_contract_code(address: str) -> str:
    # Mock sample Clarity-like contract text (simplified)
    mock_code = """
(define-public (withdraw-all)
  (begin
    (contract-call? .owner withdraw (get-balance))
    (ok true)))
;; admin: tx-sender is owner
(define-data-var owner principal 'SP123EXAMPLE)
"""
    return mock_code
