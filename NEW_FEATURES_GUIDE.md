# New Features Guide - Chatbot & Dynamic Rule Generation

## 🆕 What's New?

### 1. **AI Tax Chatbot (Context-Aware)**
A conversational AI assistant that knows your tax details and can answer personalized questions.

### 2. **Dynamic Tax Rule Generator**
Fully dynamic agent that fetches LIVE data from government sources instead of using hardcoded rules.

---

## 🤖 Feature 1: AI Tax Chatbot

### What is it?

A context-aware chatbot powered by Google Gemini that:
- **Remembers your tax calculation** from the frontend form
- Answers personalized tax questions based on YOUR data
- Provides tailored tax-saving suggestions
- Explains calculations in simple terms
- Available 24/7 for tax queries

### How Does It Work?

#### Architecture Flow:

```
User fills Tax Calculator form
         ↓
Tax calculation happens
         ↓
Results saved to localStorage
         ↓
User navigates to Chatbot page
         ↓
Chatbot reads localStorage
         ↓
Sends context to backend API (/chatbot/set-context)
         ↓
TaxChatbotAgent stores user's tax details in memory
         ↓
User asks questions
         ↓
Chatbot uses context + Gemini AI to answer
         ↓
Personalized responses based on user's actual numbers!
```

### Key Features:

1. **Context Awareness**
   - Knows your gross income
   - Knows which regime you chose
   - Knows your deductions
   - Knows your tax amount
   - Knows your risk level
   - Knows any red flags

2. **Personalized Responses**
   ```
   User: "Can I save more tax?"

   Chatbot: "Based on your income of ₹12,00,000 in OLD regime
   with ₹111,800 tax, you could save by..."
   ```

3. **Conversation Memory**
   - Remembers last 4 messages for context
   - Natural conversation flow

4. **Smart Suggestions**
   - AI generates 5 personalized tax-saving tips
   - Based on your specific situation
   - Actionable recommendations

### API Endpoints:

#### 1. Set Chatbot Context
```http
POST /chatbot/set-context

Body:
{
  "gross_income": 1200000,
  "regime": "old",
  "deductions": {...},
  "taxable_income": 975000,
  "total_tax": 111800,
  "risk_score": 0.0,
  "risk_level": "LOW",
  "compliance_score": 100,
  "flags": []
}

Response:
{
  "status": "success",
  "message": "Chatbot context updated. I'm now aware of your tax details!",
  "context_summary": {...}
}
```

#### 2. Chat with Bot
```http
POST /chatbot/chat

Body:
{
  "message": "Can you explain my tax calculation?"
}

Response:
{
  "status": "success",
  "user_message": "...",
  "bot_response": "Based on your income of ₹12,00,000...",
  "timestamp": "...",
  "has_context": true
}
```

#### 3. Get Personalized Suggestions
```http
GET /chatbot/suggestions

Response:
{
  "status": "success",
  "suggestions": [
    "1. Switch to the New Tax Regime...",
    "2. Utilize Section 80CCD(1B)...",
    ...
  ]
}
```

#### 4. Clear Context
```http
POST /chatbot/clear

Response:
{
  "status": "success",
  "message": "Chatbot context and history cleared"
}
```

### Frontend Usage:

1. **Calculate Tax**
   - Go to Tax Calculator
   - Fill income & deductions
   - Click "Calculate Tax"
   - Results automatically saved to localStorage

2. **Chat with Assistant**
   - Go to "💬 Chat Assistant" page
   - Chatbot automatically loads your tax context
   - Ask anything!

3. **Quick Questions**
   - Pre-built question buttons
   - Click to ask instantly

4. **Personalized Tips**
   - AI-generated suggestions
   - Based on your calculation
   - Click to ask chatbot about them

### Example Conversation:

```
USER: "How was my tax calculated?"

BOT: "Hello! Based on your details with Old Regime
and Gross Income of ₹12,00,000:

Step 1: Calculate Taxable Income
- Gross Income: ₹12,00,000
- Standard Deduction: -₹50,000
- Section 80C: -₹1,50,000
- Section 80D: -₹25,000
= Taxable Income: ₹9,75,000

Step 2: Apply Tax Slabs
- Up to ₹2.5L: ₹0
- ₹2.5L-5L: ₹12,500 (5%)
- ₹5L-9.75L: ₹95,000 (20%)
= Base Tax: ₹1,07,500

Step 3: Add Cess
- 4% Cess: ₹4,300

TOTAL TAX: ₹1,11,800 (9.32% effective rate)"
```

---

## 🌐 Feature 2: Dynamic Tax Rule Generator

### What Changed?

#### BEFORE (Old Version):
```python
# agents/tax_rule_generator.py
def generate_rule_file():
    # Use predefined comprehensive data (STATIC)
    # Comment says: "as live crawling may not always work"
    return HARDCODED_RULES  # ❌ Not truly dynamic
```

#### AFTER (New Version):
```python
# agents/tax_rule_generator_dynamic.py
def generate_dynamic_rules():
    # Step 1: Crawl LIVE government websites ✅
    # Step 2: Extract with Gemini AI + Google Search ✅
    # Step 3: Generate JSON from real data ✅
    return LIVE_RULES  # ✅ Fully dynamic!
```

### How It Works Now:

```
1. Agent starts
    ↓
2. Crawls incometax.gov.in (LIVE)
    ↓
3. Fetches budget documents
    ↓
4. Sends content to Gemini AI
    ↓
5. Gemini uses Google Search for latest info
    ↓
6. Extracts: slabs, deductions, rebates, surcharges, cess
    ↓
7. Generates structured JSON
    ↓
8. Saves with timestamp & source URLs
```

### Key Features:

1. **Live Web Scraping**
   - Fetches from incometax.gov.in
   - Fetches from indiabudget.gov.in
   - Uses BeautifulSoup for parsing

2. **Domain Validation**
   - ONLY trusts .gov.in / .nic.in domains
   - Rejects private blogs/forums
   - Security built-in

3. **AI + Google Search**
   - Gemini analyzes live content
   - Uses Google Search tool for latest rules
   - Cross-references multiple sources

4. **Metadata Tracking**
   ```json
   {
     "generation_method": "DYNAMIC_LIVE_CRAWLING",
     "source_urls": ["https://incometax.gov.in/..."],
     "last_updated": "2026-01-01T..."
   }
   ```

### Usage:

```python
from agents.tax_rule_generator_dynamic import DynamicTaxRuleGeneratorAgent

agent = DynamicTaxRuleGeneratorAgent()

# Generate rules from LIVE sources
rules = agent.generate_dynamic_rules('old', '2024-25')

# Output: rules/india_tax_2024_25_old_dynamic.json
```

### Comparison:

| Feature | Old (Static) | New (Dynamic) |
|---------|--------------|---------------|
| Data Source | Hardcoded | Live websites |
| Update Method | Manual code edit | Auto fetch |
| Gemini AI | Rule formatting only | Extraction + Search |
| Google Search | ❌ No | ✅ Yes |
| Trustworthiness | Good | Excellent |
| Metadata | Basic | Detailed |

### Run It:

```bash
python agents/tax_rule_generator_dynamic.py
```

Output:
```
🔴 DYNAMIC RULE GENERATION (LIVE CRAWLING)
Regime: OLD | FY: 2024-25

STEP 1: Crawling government websites...
🌐 Fetching LIVE data from: https://incometax.gov.in/...
   ✓ Fetched 15,234 characters of live data
✓ Combined data from 2 sources

STEP 2: Using Gemini AI with Google Search for latest data...
🤖 Analyzing with Gemini AI (Dynamic Extraction)...
✓ Successfully extracted rules dynamically

✅ DYNAMIC rules generated: rules/india_tax_2024_25_old_dynamic.json
   Method: LIVE CRAWLING + GEMINI AI + GOOGLE SEARCH
   Slabs: 4
   Deductions: 7
```

---

## 📦 Installation

### Chatbot (No extra packages needed!)
Already included in existing requirements.txt:
- google-genai ✅
- fastapi ✅
- pydantic ✅

### Dynamic Generator
Same as above - all dependencies already installed!

---

## 🧪 Testing

### Test Chatbot:
```bash
python agents/tax_chatbot.py
```

Expected: 4 Q&A conversations with personalized responses

### Test Dynamic Generator:
```bash
python agents/tax_rule_generator_dynamic.py
```

Expected: Live crawling + JSON generation

### Test API:
```bash
# Start backend
python -m uvicorn api.main:app --reload

# In another terminal
curl -X POST http://localhost:8000/chatbot/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello!"}'
```

---

## 🎯 Summary

### Chatbot Highlights:
- ✅ Context-aware (remembers your tax details)
- ✅ Personalized answers
- ✅ Conversation memory
- ✅ AI-powered suggestions
- ✅ 4 new API endpoints
- ✅ Full frontend integration

### Dynamic Generator Highlights:
- ✅ Live web scraping from .gov.in
- ✅ Gemini AI + Google Search
- ✅ No hardcoded fallbacks
- ✅ Source URLs tracked
- ✅ Generation method logged
- ✅ 100% dynamic data

---

## 📞 Next Steps

1. ✅ Test chatbot in frontend (http://localhost:3000/chatbot)
2. ✅ Try dynamic rule generation
3. ✅ Compare old vs new rules
4. ✅ Add more quick questions
5. ✅ Enhance chatbot prompts

---

**Both features are production-ready and fully documented!**
