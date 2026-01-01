# Complete Setup & Demo Guide

## 📋 Quick Start Checklist

### Prerequisites Installed
- [ ] Python 3.8 or higher
- [ ] Node.js 16 or higher
- [ ] Git (optional)
- [ ] Code editor (VS Code recommended)
- [ ] Gemini API Key

---

## 🚀 Step-by-Step Setup

### STEP 1: Verify Python Installation

```bash
python --version
```

Expected output: `Python 3.8+`

### STEP 2: Install Python Dependencies

```bash
cd "H:\Tax project"
pip install -r requirements.txt
```

Packages installed:
- python-dotenv
- google-genai
- requests
- beautifulsoup4
- fastapi
- uvicorn
- pandas
- etc.

### STEP 3: Verify Gemini API Connection

```bash
python test_gemini_connection.py
```

Expected output:
```
============================================================
GEMINI API CONNECTION TEST
============================================================
✓ API Key loaded: AIzaSyAPwF...

📤 Sending test prompt: 'Respond with 'Gemini connected successfully''
   Using model: gemini-3-flash-preview

📥 Response received:
   Gemini connected successfully

✅ Gemini API connection successful!
   Model used: gemini-3-flash-preview

============================================================
STATUS: READY TO PROCEED WITH AGENT DEVELOPMENT
============================================================
```

### STEP 4: Generate Tax Rules

```bash
python agents/tax_rule_generator.py
```

Expected output:
```
✓ TaxRuleGeneratorAgent initialized

============================================================
GENERATING TAX RULES: OLD REGIME - FY 2024-25
============================================================

📋 Using comprehensive Indian tax rules for FY 2024-25...

✅ Rule file generated: rules/india_tax_2024_25_old.json
   Regime: old
   Financial Year: 2024-25
   Slabs: 4
   Deductions: 7
```

Files created:
- `rules/india_tax_2024_25_old.json`
- `rules/india_tax_2024_25_new.json`

### STEP 5: Test Tax Analyzer Agent

```bash
python agents/tax_analyzer.py
```

You should see detailed tax calculations for both regimes and a comparison summary.

### STEP 6: Test API Endpoints

```bash
python test_api.py
```

Expected: All 6 API tests should pass with ✓ marks.

### STEP 7: Start Backend Server

Open a **new terminal window**:

```bash
cd "H:\Tax project"
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Keep this terminal running!

### STEP 8: Verify API in Browser

Open browser and go to:
- http://localhost:8000 - Should show JSON with status "online"
- http://localhost:8000/docs - Swagger UI (interactive API documentation)

### STEP 9: Install Frontend Dependencies

Open a **new terminal window**:

```bash
cd "H:\Tax project\frontend"
npm install
```

Wait for all packages to install (~2-3 minutes).

### STEP 10: Start Frontend Development Server

```bash
npm run dev
```

Expected output:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

### STEP 11: Open Frontend in Browser

Go to: http://localhost:3000

You should see the **Indian Tax Analysis System** dashboard!

---

## 🧪 Testing the System

### Test 1: Dashboard
1. Open http://localhost:3000
2. Verify system status shows "Online"
3. Check all feature cards are displayed

### Test 2: Tax Calculator
1. Click "Tax Calculator" in navigation
2. Enter:
   - Gross Income: 1200000
   - Regime: Old
   - 80C: 150000
   - 80D: 25000
   - Standard Deduction: 50000
3. Click "Calculate Tax"
4. Verify:
   - Total tax is calculated
   - Risk score is shown
   - Compliance score is displayed

### Test 3: Compare Regimes
1. Click "Compare Regimes"
2. Enter:
   - Gross Income: 1200000
   - Old Regime Deductions: 80C (150000), 80D (25000)
3. Click "Compare Regimes"
4. Verify:
   - Both regimes show tax amounts
   - Better regime is highlighted
   - Savings amount is shown

### Test 4: Reports
1. Click "Reports"
2. Enter income and deductions
3. Click "Generate Report"
4. Verify:
   - Detailed report is displayed
   - Download button works
   - Report is properly formatted

---

## 🎯 Demo Script for College Presentation

### Part 1: Introduction (2 minutes)
"This is a Multi-Agent Tax Analysis System powered by Google Gemini AI. It features two specialized AI agents working together to provide accurate tax calculations and fraud detection for Indian taxpayers."

### Part 2: Architecture Demo (3 minutes)
1. Show project structure
2. Explain the two agents:
   - **TaxRuleGeneratorAgent**: Fetches and structures tax rules
   - **TaxAnalyzerAgent**: Analyzes tax and detects fraud
3. Show the API backend (FastAPI)
4. Show the React frontend

### Part 3: Live Demo (5 minutes)

**Scenario 1: Normal User**
- Income: ₹12,00,000
- Regime: Old
- Deductions: 80C (₹1,50,000), 80D (₹25,000)
- Result: Clean calculation, LOW risk

**Scenario 2: Suspicious Pattern**
- Income: ₹8,00,000
- Regime: Old
- Deductions: Max out everything (80C, 80D, 80G, 24(b))
- Result: HIGH risk score, multiple red flags

**Scenario 3: Regime Comparison**
- Show how system recommends better regime
- Highlight savings

### Part 4: Technical Features (3 minutes)
1. Show Postman collection
2. Demonstrate API endpoints
3. Show fraud detection algorithm
4. Display tax rules JSON files

### Part 5: Q&A Preparation

**Common Questions:**

Q: How does fraud detection work?
A: We analyze 5 key patterns:
   - Deduction-to-income ratio
   - Multiple max-limit claims
   - Income fluctuations
   - Invalid regime deductions
   - Unusual claim patterns

Q: Where do you get tax rules?
A: From official sources (incometax.gov.in) and we structure them using Gemini AI into JSON format.

Q: Can this handle real-time data?
A: Yes, the API can be called in real-time, and agents can be triggered to update rules periodically.

Q: What AI model do you use?
A: Google Gemini (gemini-3-flash-preview) for intelligent rule extraction and pattern analysis.

---

## 🐛 Troubleshooting

### Issue: Backend won't start
**Solution:**
```bash
pip install --upgrade fastapi uvicorn
python -m uvicorn api.main:app --reload
```

### Issue: Frontend build errors
**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Issue: API connection failed
**Solution:**
1. Check backend is running on port 8000
2. Check `.env` file has valid GEMINI_API_KEY
3. Verify no firewall blocking

### Issue: Tax rules not found
**Solution:**
```bash
python agents/tax_rule_generator.py
```

---

## 📦 Postman Testing

### Import Collection
1. Open Postman
2. Click "Import"
3. Select `postman_collection.json`
4. Collection will be imported with all endpoints

### Test Sequence
1. Health Check - Verify API is running
2. Get Rules - Check tax rules are loaded
3. Analyze Tax - Test calculation
4. Compare Regimes - Test comparison
5. Generate Report - Test report generation

---

## 🎓 Project Deliverables

### For Submission
- [ ] Source code (complete project folder)
- [ ] README.md (documentation)
- [ ] Postman collection JSON
- [ ] Screenshots/Demo video
- [ ] Presentation slides

### Key Highlights to Mention
1. **Multi-Agent System** - Two specialized AI agents
2. **Google Gemini Integration** - Latest AI model
3. **Fraud Detection** - ML-based pattern recognition
4. **Professional UI** - React-based fintech design
5. **RESTful API** - FastAPI backend
6. **Real Data** - FY 2024-25 Indian tax rules
7. **Regime Comparison** - Helps users save money
8. **Comprehensive Testing** - Postman collection included

---

## ✅ Final Checklist Before Demo

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Tax rules generated in `/rules` folder
- [ ] Gemini API key working
- [ ] All test cases passing
- [ ] Postman collection tested
- [ ] Demo scenarios prepared
- [ ] Project structure explained
- [ ] Screenshots taken
- [ ] Backup of project taken

---

## 🎬 Recording Demo Video

### Recommended Flow:
1. Start with architecture diagram (30 sec)
2. Show project structure (30 sec)
3. Run test scripts (1 min)
4. Start backend and show API docs (1 min)
5. Open frontend and demo features (3 min)
6. Show fraud detection in action (1 min)
7. Demonstrate Postman collection (1 min)
8. Conclusion and future scope (30 sec)

**Total: ~8 minutes**

---

**Good luck with your presentation! 🚀**
