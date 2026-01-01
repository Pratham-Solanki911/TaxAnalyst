# Quick Reference Card

## 🚀 Quick Start Commands

### Test Everything
```bash
# 1. Test Gemini API
python test_gemini_connection.py

# 2. Generate tax rules
python agents/tax_rule_generator.py

# 3. Test agents
python agents/tax_analyzer.py

# 4. Test API
python test_api.py

# 5. Run demo
python run_demo.py
```

### Start Backend
```bash
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend
```bash
cd frontend
npm install  # First time only
npm run dev
```

---

## 📍 Important URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |
| API Docs (ReDoc) | http://localhost:8000/redoc |

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `agents/tax_rule_generator.py` | Agent 1 - Rule generation |
| `agents/tax_analyzer.py` | Agent 2 - Tax analysis & fraud detection |
| `api/main.py` | FastAPI backend |
| `frontend/src/App.jsx` | React main app |
| `rules/*.json` | Tax rules database |
| `postman_collection.json` | API testing collection |
| `run_demo.py` | Complete demo script |

---

## 🎯 Demo Scenarios

### Scenario 1: Normal User
```json
{
  "gross_income": 1200000,
  "regime": "old",
  "deductions": {
    "80C": 150000,
    "80D": 25000,
    "Standard Deduction": 50000
  }
}
```
**Expected:** Tax ₹111,800 | Risk: LOW

### Scenario 2: High Risk
```json
{
  "gross_income": 800000,
  "regime": "old",
  "deductions": {
    "80C": 150000,
    "80D": 75000,
    "80G": 100000,
    "24(b)": 200000,
    "Standard Deduction": 50000
  }
}
```
**Expected:** Risk: HIGH | Multiple flags

### Scenario 3: Invalid Regime
```json
{
  "gross_income": 1000000,
  "regime": "new",
  "deductions": {
    "80C": 150000,
    "80D": 25000
  }
}
```
**Expected:** Risk: MEDIUM | Invalid deduction flags

---

## 🔍 API Endpoints Cheat Sheet

```bash
# Health check
GET /

# Get rules
GET /rules/current?regime=old&financial_year=2024-25

# Analyze tax
POST /analyze-tax
Body: { gross_income, regime, deductions }

# Compare regimes
POST /compare-regimes
Body: { gross_income, deductions_old, deductions_new }

# Generate report
POST /generate-report
Body: { gross_income, regime, deductions }

# Simulate
POST /simulate-scenario
Body: { base_income, income_increments, regime, deductions }

# Generate rules
POST /generate-rules?regime=both
```

---

## 💰 Tax Slabs Quick Ref (FY 2024-25)

### Old Regime
- 0-2.5L: 0%
- 2.5L-5L: 5%
- 5L-10L: 20%
- 10L+: 30%

### New Regime
- 0-3L: 0%
- 3L-7L: 5%
- 7L-10L: 10%
- 10L-12L: 15%
- 12L-15L: 20%
- 15L+: 30%

---

## 🔧 Troubleshooting

### Backend won't start
```bash
pip install --upgrade fastapi uvicorn
```

### Frontend errors
```bash
cd frontend
rm -rf node_modules
npm install
```

### Rules not found
```bash
python agents/tax_rule_generator.py
```

### API connection failed
- Check backend running on port 8000
- Check .env has GEMINI_API_KEY
- Disable firewall temporarily

---

## 📊 Project Statistics

- **Agents:** 2 (RuleGenerator, Analyzer)
- **API Endpoints:** 8
- **Frontend Pages:** 4
- **Tax Regimes:** 2
- **Fraud Checks:** 5
- **Lines of Code:** 3,500+
- **Technologies:** 10+

---

## ✅ Pre-Demo Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Tax rules generated in /rules
- [ ] Gemini API key working
- [ ] Postman collection imported
- [ ] Demo scenarios tested
- [ ] Screenshots ready
- [ ] Presentation prepared

---

## 🎓 Key Points for Presentation

1. **Multi-Agent Architecture** - Two specialized AI agents
2. **Gemini AI Integration** - Latest Google AI model
3. **Fraud Detection** - 5 pattern checks with risk scoring
4. **Both Regimes** - Old and New tax regime support
5. **Professional UI** - Modern fintech design
6. **Complete API** - 8 RESTful endpoints
7. **Real Data** - FY 2024-25 accurate rules
8. **Testing** - Comprehensive Postman collection

---

## 📞 Quick Help

**Documentation:**
- README.md - Full docs
- SETUP_GUIDE.md - Step-by-step setup
- PROJECT_SUMMARY.md - Complete overview

**Scripts:**
- test_gemini_connection.py - Test AI
- test_api.py - Test all endpoints
- run_demo.py - Full demonstration

---

**Status: ✅ READY FOR DEMO**
