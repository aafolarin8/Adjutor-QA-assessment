# Adjutor API Test Automation Setup and Execution

## Overview

This document provides instructions on setting up and running automated test scripts using Postman collections and Selenium scripts. It also includes a summary of the test results.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aafolarin8/Adjutor-QA-assessment.git
cd Adjutor-QA-Assessment
```

### 2. Install Dependencies

Make sure you have the necessary tools installed:

- **Node.js**: [Download and install Node.js](https://nodejs.org/)
- **Postman CLI (Newman)**: Install Newman globally using npm:

  ```bash
  npm install -g newman
  ```

- **Selenium WebDriver**: Ensure you have the appropriate WebDriver for your browser. You can download WebDriver binaries from the following links:
  - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
  - [GeckoDriver (for Firefox)](https://github.com/mozilla/geckodriver/releases)

### 3. Generate API Key

1. Getting Your Postman API Key
- Go to [Postman API Keys](https://go.postman.co/settings/me/api-keys).
- Click Generate API Key.
- Enter a name for your key and click Generate API Key.
- Copy the key and save it securely.
2. Save this API Key as a secret in GitHub under your repository settings.

### 4. Configure GitHub Actions

1. Create a YAML file for GitHub Actions in the `.github/workflows` directory of your repository.
2. Paste the generated CLI command into this YAML file. This command will look something like:

   ```yaml
   name: Run Postman Collection

   on:
     push:
       branches:
         - main

   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Run Postman Collection
           run: newman run <collection-file.json> --api-key ${{ secrets.POSTMAN_API_KEY }}
   ```

3. Ensure that the Postman collection JSON file is in the repository.

### 5. Push Changes to GitHub

```bash
git add .
git commit -m "Add automation scripts and GitHub Actions configuration"
git push origin main
```

### 6. Monitor GitHub Actions

- Go to the GitHub Actions tab in your repository to monitor the execution of your workflows.

## Test Results Summary

### Test Execution Details

- **Total Iterations:** 1
- **Total Requests:** 29
- **Total Test Scripts:** 46
- **Total Pre-request Scripts:** 29
- **Total Assertions:** 74
- **Total Run Duration:** 1 minute 17.8 seconds
- **Total Data Received:** 30.54 KB (approx)
- **Average Response Time:** 2.5 seconds [Min: 72ms, Max: 1 minute 0.1s, Std Dev: 10.9s]

### Test Results

#### **Passed:**
- All iterations were executed without errors.
- All requests were successfully processed.
- Endpoints perform as expected.

#### **Failed:**
1. **JSONError**
   - **Detail:** Unexpected token '<' at 1:1
   - **Location:** Validation / Get Accounts for a BVN / Initialize BVN Accounts Consent

2. **Assertion Errors (Status Code)**
   - **Detail:** Expected status code 200 but got 402
   - **Locations:**
     - Credit Bureaus / Get Credit Report from CRC Credit Bureau
     - Credit Bureaus / Get Credit Report from FirstCentral Credit Bureau

3. **Assertion Errors (Response Time)**
   - **Detail:** Expected response time to be below 1000ms
   - **Locations:**
     - Embedded Loans and Payments / Pay with wallet / Initialize Payment (1319ms)
     - Operational Services / Profile / Get Adjutor Services Pricing (5305ms)
     - Operational Services / Miscellaneous / Get List of Banks (1696ms)
     - Direct Debit / Banks / Verify Bank Account Number (1421ms)    
