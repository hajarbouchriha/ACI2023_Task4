# ACI2023_Task4
This project is my fourth task as a cyber security intern at Alpha Coding Ignite
# Encryption Implementation

## Overview

This repository contains a Python implementation of encryption protocols for data in transit and data at rest. The code includes symmetric (AES) and asymmetric (RSA) encryption methods, key generation, documentation of the implementation process, and guidelines for ongoing management.

## Features

- **Symmetric Encryption (AES):**
  - Algorithm: Advanced Encryption Standard (AES)
  - Key Size: 256 bits
  - Mode: Cipher Feedback (CFB)

- **Asymmetric Encryption (RSA):**
  - Algorithm: Rivest–Shamir–Adleman (RSA)
  - Key Size: 2048 bits
  - Padding: Optimal Asymmetric Encryption Padding (OAEP)

- **Key Generation:**
  - AES Key: 256-bit key generated using a secure random number generator.
  - RSA Key Pair: 2048-bit private key and corresponding public key.

- **Implementation Process:**
  - Documentation providing insights into the encryption strategy, key management, integration, and security measures.

- **Ongoing Management Guidelines:**
  - Key Rotation: Rotate keys at specified intervals.
  - Incident Response: Define procedures for handling key compromises.
  - Audits: Regularly audit the encryption implementation.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/hajarbouchriha/encryption-implementation.git
   cd encryption-implementation
