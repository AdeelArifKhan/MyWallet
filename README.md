# MyWallet
MyWallet – Smart Contract Wallet on Algorand
Slogen:
Secure. Scalable. Decentralized.
A lightweight on-chain wallet solution built with AlgoPy, currently in its testnet phase.

Description:
MyWallet is a decentralized smart contract wallet developed using the ARC4 standard on the Algorand blockchain. It offers users the ability to deposit and withdraw funds with personalized metadata, securely stored using box storage. Each deposit is tagged with the user's input (such as their GitHub handle or name) and associated with their wallet address.

This contract is designed to be simple, efficient, and extendable for future real-world applications like DeFi gateways, token vaults, or identity-based asset tracking.

Project Status:
✅ Currently Deployed on Testnet
✅ Initial features live: deposit() and withdraw()
🔜 Future updates: asset transfers, payment routing, and user dashboard integration

How It Works:
Deposit
The user calls deposit(name) with their name or identifier.
This data is stored on-chain using box storage, uniquely tied to the sender’s wallet address.

Withdraw
The user calls withdraw(name) to initiate a withdrawal request.
The contract confirms the request with a personalized message.

Launch on testnet
https://lora.algokit.io/testnet/application/740574648

ID is 740574648

