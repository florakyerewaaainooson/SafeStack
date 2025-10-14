# ⚙️ Phase 2 — SafeStack Build & Design

## Project Overview
SafeStack helps DeFi investors detect malicious smart contracts on the Stacks blockchain using AI.  
It analyzes smart contract code, predicts potential risks, and assigns a **Safety Score** with an AI-generated explanation.

## Goals of Phase 2
- Design the system architecture  
- Create the initial project structure  
- Prepare a basic prototype to simulate the workflow  

## Flow of the System
1. User pastes a smart contract address.
2. SafeStack retrieves contract data from the blockchain.
3. AI analyzes the code for vulnerabilities.
4. A Safety Score and short explanation are returned.

## Example (Concept)
Input:  
`contract_id: SP2C2GVR..XYZ123`  

Output:  
`Safety Score: 84/100`  
`Explanation: The contract uses verified libraries and secure token-handling logic.`

## Next Steps
- Connect real blockchain API data  
- Build browser extension for instant analysis  
- Integrate with Stacks wallets
