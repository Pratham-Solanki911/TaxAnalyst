# Indian Tax Analysis System - Multi-Agent AI Platform

A comprehensive multi-agent tax analysis system powered by Google Gemini AI for Indian income tax calculation, fraud detection, and regime comparison for Financial Year 2024-25.

## 🎯 Project Overview

This system implements a **multi-agent architecture** with THREE specialized AI agents:

1. **TaxRuleGeneratorAgent** - Crawls official Indian government sources and generates structured tax rules (now with DYNAMIC live fetching!)
2. **TaxAnalyzerAgent** - Analyzes user financial data, calculates tax, and detects fraud patterns
3. **TaxChatbotAgent** 🆕 - Context-aware AI chatbot that answers tax questions based on your calculation

## ✨ Key Features

### Tax Calculation
- ✅ Accurate slab-based tax computation for both OLD and NEW regimes
- ✅ Support for all major deductions (80C, 80D, 80G, 80E, 24(b), etc.)
- ✅ Automatic rebate calculation (Section 87A)
- ✅ Surcharge and Health & Education Cess computation
- ✅ Effective tax rate calculation

### AI-Powered Fraud Detection
- 🔍 Deduction-to-income ratio analysis
- 🔍 Pattern anomaly detection (repeated max-limit claims)
- 🔍 Income fluctuation monitoring
- 🔍 Invalid regime deduction detection
- 🔍 Risk scoring (0-1 scale) with LOW/MEDIUM/HIGH levels
- 🔍 Compliance score (0-100%)
- 🔍 Actionable recommendations

### Regime Comparison
- 📊 Side-by-side OLD vs NEW regime comparison
- 📊 Automatic best regime recommendation
- 📊 Savings calculation
- 📊 Risk assessment for both regimes

### Professional UI
- 🎨 Clean, professional fintech design
- 🎨 Light theme with high contrast
- 🎨 Responsive layout
- 🎨 Interactive dashboards
- 🎨 Real-time calculations

### 🆕 AI Tax Chatbot (NEW!)
- 💬 **Floating chat bubble** - Available on ALL pages
- 💬 Context-aware conversational AI
- 💬 Remembers your tax calculation details
- 💬 Personalized answers based on YOUR data
- 💬 AI-powered tax-saving suggestions
- 💬 Conversation memory for natural flow
- 💬 Quick question buttons
- 💬 Beautiful animations & modern UI
- 💬 Minimizable & mobile responsive

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    React Frontend                        │
│  (Dashboard, Calculator, Comparison, Reports)            │
└────────────────────┬────────────────────────────────────┘
                     │ REST API
┌────────────────────▼────────────────────────────────────┐
│                  FastAPI Backend                         │
│  (Endpoints: /analyze-tax, /compare-regimes, etc.)      │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼──────────┐    ┌────────▼─────────────┐
│ TaxRuleGenerator │    │   TaxAnalyzerAgent   │
│      Agent       │    │  - Tax Calculation   │
│  - Web Crawling  │───▶│  - Fraud Detection   │
│  - Rule Extract  │    │  - Risk Scoring      │
│  - JSON Schema   │    │  - Report Generation │
└──────────────────┘    └──────────────────────┘
        │                         │
        │                         │
┌───────▼─────────────────────────▼───────────┐
│        rules/india_tax_2024_25_*.json       │
│     (Structured Tax Rules Database)         │
└─────────────────────────────────────────────┘
```

## 📁 Project Structure

```
Tax project/
├── agents/
│   ├── tax_rule_generator.py    # Agent 1: Rule generation
│   └── tax_analyzer.py          # Agent 2: Tax analysis & fraud detection
├── api/
│   └── main.py                  # FastAPI backend
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── TaxCalculator.jsx
│   │   │   ├── CompareRegimes.jsx
│   │   │   └── Reports.jsx
│   │   ├── utils/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── rules/
│   ├── india_tax_2024_25_old.json
│   └── india_tax_2024_25_new.json
├── schemas/
│   └── tax_rule_schema.json
├── test_gemini_connection.py
├── test_api.py
├── postman_collection.json
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Google Gemini API Key

### Step 1: Clone and Setup Environment

```bash
cd "H:\Tax project"
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create `.env` file (already exists):
```
GEMINI_API_KEY=your_api_key_here
```

### Step 4: Generate Tax Rules

```bash
python agents/tax_rule_generator.py
```

This will create:
- `rules/india_tax_2024_25_old.json`
- `rules/india_tax_2024_25_new.json`

### Step 5: Test API Connection

```bash
python test_gemini_connection.py
python test_api.py
```

### Step 6: Start Backend Server

```bash
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Step 7: Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Step 8: Start Frontend Development Server

```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## 📡 API Endpoints

### Health Check
```
GET /
```

### Get Tax Rules
```
GET /rules/current?regime={old|new}&financial_year=2024-25
```

### Analyze Tax
```
POST /analyze-tax
Content-Type: application/json

{
  "gross_income": 1200000,
  "regime": "old",
  "financial_year": "2024-25",
  "deductions": {
    "80C": 150000,
    "80D": 25000,
    "Standard Deduction": 50000
  },
  "previous_year_income": 1000000
}
```

### Compare Regimes
```
POST /compare-regimes
Content-Type: application/json

{
  "gross_income": 1200000,
  "financial_year": "2024-25",
  "deductions_old": {
    "80C": 150000,
    "80D": 25000,
    "Standard Deduction": 50000
  },
  "deductions_new": {
    "Standard Deduction": 50000
  }
}
```

### Generate Report
```
POST /generate-report
Content-Type: application/json

{
  "gross_income": 1500000,
  "regime": "old",
  "deductions": {...}
}
```

### Simulate Scenarios
```
POST /simulate-scenario
Content-Type: application/json

{
  "base_income": 500000,
  "income_increments": [500000, 1000000, 1500000, 2000000],
  "regime": "new",
  "deductions": {"Standard Deduction": 50000}
}
```

### Generate Rules
```
POST /generate-rules?regime=both&financial_year=2024-25
```

## 🧪 Testing with Postman

Import `postman_collection.json` into Postman:
1. Open Postman
2. Click Import
3. Select `postman_collection.json`
4. Update `base_url` variable if needed
5. Run requests

## 📊 Tax Rules (FY 2024-25)

### Old Regime
| Income Range | Tax Rate |
|--------------|----------|
| Up to ₹2.5L | 0% |
| ₹2.5L - ₹5L | 5% |
| ₹5L - ₹10L | 20% |
| Above ₹10L | 30% |

**Major Deductions:**
- 80C: ₹1,50,000
- 80D: ₹75,000
- 24(b) Home Loan: ₹2,00,000
- Standard Deduction: ₹50,000

### New Regime
| Income Range | Tax Rate |
|--------------|----------|
| Up to ₹3L | 0% |
| ₹3L - ₹7L | 5% |
| ₹7L - ₹10L | 10% |
| ₹10L - ₹12L | 15% |
| ₹12L - ₹15L | 20% |
| Above ₹15L | 30% |

**Deductions:**
- Standard Deduction: ₹50,000 (only)

### Common
- **Surcharge:** 0-37% based on income
- **Health & Education Cess:** 4%
- **Rebate 87A:** Up to ₹25,000 (new) / ₹12,500 (old)

## 🔒 Fraud Detection Features

### Risk Factors Analyzed
1. **High Deduction Ratio** (>50% of income)
2. **Multiple Max-Limit Claims** (3+ sections)
3. **Unusual 80C Claims** (high claim vs low income)
4. **Significant Income Changes** (>50% YoY)
5. **Invalid Regime Deductions** (claiming old regime deductions in new)

### Risk Levels
- **LOW** (0.0 - 0.3): No major issues
- **MEDIUM** (0.3 - 0.6): Review recommended
- **HIGH** (0.6 - 1.0): Detailed verification required

## 🎓 College Project Demo Checklist

- ✅ Multi-agent architecture implemented
- ✅ AI-powered agents (Gemini integration)
- ✅ Web crawling capabilities (trusted sources)
- ✅ Fraud detection with ML patterns
- ✅ RESTful API backend
- ✅ Professional React frontend
- ✅ Postman collection for testing
- ✅ Complete documentation
- ✅ Tax rules for FY 2024-25
- ✅ Regime comparison feature
- ✅ Report generation
- ✅ Risk scoring system

## 🛠️ Technology Stack

**Backend:**
- Python 3.12
- FastAPI
- Google Gemini AI (gemini-3-flash-preview)
- Pydantic
- BeautifulSoup4 (web scraping)
- Uvicorn

**Frontend:**
- React 18
- Vite
- Axios
- React Router
- Recharts (for visualizations)

**AI/ML:**
- Google Gemini API
- Pattern-based fraud detection
- Risk scoring algorithms

## 📝 Usage Examples

### Example 1: Calculate Tax (Old Regime)
```python
from agents.tax_analyzer import TaxAnalyzerAgent

agent = TaxAnalyzerAgent()
agent.load_rules('old', '2024-25')

user_data = {
    "gross_income": 1200000,
    "deductions": {
        "80C": 150000,
        "80D": 25000,
        "Standard Deduction": 50000
    }
}

result = agent.calculate_tax(user_data)
print(f"Total Tax: ₹{result['total_tax']:,.2f}")
```

### Example 2: Fraud Detection
```python
fraud_result = agent.detect_fraud(user_data, result)
print(f"Risk Score: {fraud_result['risk_score']}")
print(f"Risk Level: {fraud_result['risk_level']}")
print(f"Flags: {fraud_result['flags']}")
```

### Example 3: Compare Regimes
```python
comparison = agent.compare_regimes(user_data)
print(f"Better Regime: {comparison['comparison']['better_regime']}")
print(f"Savings: ₹{comparison['comparison']['savings']:,.2f}")
```

## 🔗 Official Sources

Tax rules are based on:
- Income Tax Department: https://www.incometax.gov.in
- CBDT Notifications
- Finance Ministry Circulars
- India Budget Portal

## 📄 License

This is a college project for educational purposes.

## 👥 Contact

For queries regarding this project, please refer to the documentation.

---

**Built with ❤️ for Indian Taxpayers | FY 2024-25**
