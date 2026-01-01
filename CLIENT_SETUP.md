# 🚀 Client Setup Guide - Indian Tax Analysis System

## For Your Clients: One-Command Setup

Send this guide to your clients for easy installation of the Tax Analysis System.

---

## 📋 Prerequisites (Install These First)

Your client needs to install these before running the setup:

### 1. **Python 3.8 or higher**
- Download: https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Verify: Open terminal/cmd and type `python --version`

### 2. **Node.js 16 or higher**
- Download: https://nodejs.org/ (LTS version recommended)
- Verify: Open terminal/cmd and type `node --version`

### 3. **Git**
- Download: https://git-scm.com/downloads
- Verify: Open terminal/cmd and type `git --version`

---

## 🎯 One-Command Installation

### For Windows Users:

1. **Open Command Prompt** (Win + R, type `cmd`, press Enter)

2. **Navigate to desired folder:**
   ```cmd
   cd C:\Users\YourName\Documents
   ```

3. **Run this single command:**
   ```cmd
   git clone https://github.com/Pratham-Solanki911/TaxAnalyst.git && cd TaxAnalyst && setup.bat
   ```

4. **Wait for installation** (5-10 minutes)

5. **Done!** The setup script will:
   - Download the entire project
   - Install all Python dependencies
   - Install all Node.js dependencies
   - Create environment file templates
   - Generate start scripts

---

### For Mac/Linux Users:

1. **Open Terminal**

2. **Navigate to desired folder:**
   ```bash
   cd ~/Documents
   ```

3. **Run these commands:**
   ```bash
   git clone https://github.com/Pratham-Solanki911/TaxAnalyst.git
   cd TaxAnalyst
   chmod +x setup.sh
   ./setup.sh
   ```

4. **Wait for installation** (5-10 minutes)

5. **Done!**

---

## ⚙️ Configuration (5 Minutes)

After installation, you need to configure two things:

### 1. Get Gemini API Key (Required - Free)

1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Open `.env` file in project folder
5. Replace `your-gemini-api-key-here` with your actual key:
   ```
   GEMINI_API_KEY=paste-your-key-here
   ```
6. Save the file

### 2. Google OAuth (Optional)

**Option A: Skip OAuth (Recommended for Quick Start)**
- No setup needed!
- Just click "Continue as Developer" when you login
- Start using immediately

**Option B: Setup Google OAuth (For Production)**
- Follow detailed guide in `OAUTH_FIX.md`
- Or skip and use Development Mode

---

## 🎮 Running the Application

### Windows:

**Double-click:**
```
start-all.bat
```

Or open Command Prompt and run:
```cmd
cd path\to\TaxAnalyst
start-all.bat
```

### Mac/Linux:

Open Terminal and run:
```bash
cd path/to/TaxAnalyst
./start-all.sh
```

### Access the Application:

Wait 10-15 seconds for servers to start, then:

- **Open browser:** http://localhost:3000
- **Login:** Click "Continue as Developer (Testing Mode)"
- **Start using!**

---

## 📚 Quick User Guide

### First Time Using:

1. **Login**
   - Click "Continue as Developer" button

2. **Calculate Tax**
   - Go to "Tax Calculator"
   - Enter income: `1200000` (example)
   - Select regime: Old or New
   - Add deductions (optional)
   - Click "Calculate Tax"

3. **View Dashboard**
   - Return to Dashboard
   - See beautiful charts and analytics

4. **Try Transaction Analyzer**
   - Go to "📊 Transactions"
   - Upload a CSV file (sample format in documentation)
   - Get AI insights

5. **Ask the Chatbot**
   - Click chatbot bubble (bottom-right)
   - Ask: "How can I save more tax?"
   - Get personalized advice

---

## 🆘 Troubleshooting

### "Python is not recognized"
- Install Python and check "Add to PATH" during installation
- Restart terminal/cmd after installation

### "Node is not recognized"
- Install Node.js
- Restart terminal/cmd after installation

### "Setup failed"
- Make sure you have internet connection
- Make sure Python, Node.js, and Git are installed
- Try running setup script again

### "Cannot access http://localhost:3000"
- Wait 15-20 seconds after running start script
- Check if both backend and frontend started
- Try refreshing browser

### "Login not working"
- Click "Continue as Developer (Testing Mode)"
- Don't worry about Google OAuth for now

### Need More Help?
- Read `README.md` for detailed documentation
- Check `SETUP_INSTRUCTIONS.md` for troubleshooting
- Contact system administrator

---

## 🛑 Stopping the Application

### Windows:
- Press `Ctrl + C` in each command window
- Or close the windows

### Mac/Linux:
- Press `Ctrl + C` in terminal
- Application will shutdown gracefully

---

## 📊 Sample Data to Try

### Transaction CSV Example:

Create a file called `sample.csv`:

```csv
Date,Description,Amount,Category
2024-01-15,Salary Credit,100000,Income
2024-01-16,Rent Payment,25000,Expense
2024-01-20,Medical Insurance,15000,Insurance
2024-02-01,PPF Deposit,12500,Investment
2024-02-05,LIC Premium,20000,Insurance
2024-03-01,Home Loan EMI,30000,Loan
```

Upload this in Transaction Analyzer to see AI insights!

---

## ✨ Features Your Client Can Use

1. ✅ **Tax Calculation** - Accurate for FY 2024-25
2. ✅ **Fraud Detection** - AI-powered risk assessment
3. ✅ **Regime Comparison** - Old vs New regime
4. ✅ **Interactive Charts** - Visual tax breakdown
5. ✅ **Transaction Analysis** - Upload bank statements
6. ✅ **AI Chatbot** - Ask tax questions anytime
7. ✅ **Reports** - Download comprehensive reports

---

## 📞 Support

For technical support or questions:

1. Check documentation in project folder
2. Contact your system administrator
3. Visit: https://github.com/Pratham-Solanki911/TaxAnalyst

---

## 🔄 Updating to Latest Version

When you release updates, clients can update easily:

### Windows:
```cmd
cd TaxAnalyst
git pull origin main
setup.bat
```

### Mac/Linux:
```bash
cd TaxAnalyst
git pull origin main
./setup.sh
```

---

## 🎓 What to Tell Your Client

**Email Template:**

```
Subject: Tax Analysis System - Installation Guide

Hi [Client Name],

I've set up the Indian Tax Analysis System for you. Here's how to install it:

STEP 1: Install Prerequisites (one-time only)
- Python 3.8+: https://www.python.org/downloads/
- Node.js: https://nodejs.org/
- Git: https://git-scm.com/downloads

STEP 2: Install Tax System (one command)
Open Command Prompt and run:
git clone https://github.com/Pratham-Solanki911/TaxAnalyst.git && cd TaxAnalyst && setup.bat

STEP 3: Configure (5 minutes)
1. Get free API key: https://makersuite.google.com/app/apikey
2. Edit .env file and add your key

STEP 4: Run
Double-click: start-all.bat
Open browser: http://localhost:3000

Full guide: CLIENT_SETUP.md (included in project)

Let me know if you need any help!

Best regards,
[Your Name]
```

---

<div align="center">

**Setup takes 10-15 minutes total**

**System is ready to use immediately after setup**

</div>
