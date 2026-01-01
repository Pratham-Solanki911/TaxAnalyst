# Setup Instructions for New Features

This document provides setup instructions for the three new features added to the Indian Tax Analysis System:

## 🔐 Feature 1: User Authentication with Google OAuth

### Setup Steps:

1. **Get Google OAuth Credentials:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Navigate to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client ID"
   - Configure the OAuth consent screen if prompted
   - Select "Web application" as the application type
   - Add authorized JavaScript origins:
     - `http://localhost:5173` (for development)
     - Your production domain (if applicable)
   - Add authorized redirect URIs:
     - `http://localhost:5173` (for development)
   - Copy the Client ID

2. **Configure Frontend Environment:**
   - Create a `.env` file in the `frontend` directory
   - Add your Google Client ID:
     ```
     VITE_API_URL=http://localhost:8000
     VITE_GOOGLE_CLIENT_ID=your-actual-client-id.apps.googleusercontent.com
     ```

3. **Install Dependencies:**
   ```bash
   cd frontend
   npm install
   ```

### How It Works:
- Users must sign in with their Google account to access the application
- User profile (name, email, picture) is stored in localStorage
- Authentication token is validated on each session
- Logout clears all user data and tax calculations

---

## 📊 Feature 2: Dashboard Analytics Charts

### What's New:
The Dashboard now displays interactive charts when you have tax calculation data:

1. **Tax Overview Stats**
   - Gross Income
   - Total Tax
   - Effective Tax Rate
   - Risk Level

2. **Tax Regime Slabs Chart**
   - Visual bar chart showing tax slabs for your selected regime
   - Easy comparison of tax rates across income brackets

3. **Tax Breakdown Pie Chart**
   - Shows distribution of Base Tax, Surcharge, and Cess
   - Interactive tooltips with exact amounts

4. **Deductions Chart**
   - Horizontal bar chart of all your claimed deductions
   - Easy visualization of where your deductions come from

### How to Use:
1. Sign in to the application
2. Go to "Tax Calculator"
3. Calculate your tax
4. Return to Dashboard to see the charts populated with your data

---

## 📈 Feature 3: Transaction Analyzer (CSV/Excel Upload)

### Setup Steps:

1. **Install Backend Dependencies:**
   ```bash
   cd "H:\Tax project"
   pip install -r requirements.txt
   ```

   The new dependencies include:
   - `python-multipart` - For file uploads
   - `openpyxl` - For Excel file processing
   - `pandas` - Already installed, used for data analysis

2. **Ensure Gemini API Key:**
   - The transaction analyzer uses Gemini AI for analysis
   - Make sure your `GEMINI_API_KEY` is set in the `.env` file at the project root:
     ```
     GEMINI_API_KEY=your-gemini-api-key
     ```

### How to Use:

1. **Prepare Your Transaction File:**

   Your CSV or Excel file should contain transaction data with columns like:
   - **Date** - Transaction date (e.g., "2024-01-15", "15/01/2024")
   - **Description/Narration** - Transaction details
   - **Amount** - Transaction amount
   - **Category** - (Optional) Expense category
   - **Type** - (Optional) Debit/Credit or Income/Expense

   Example CSV:
   ```csv
   Date,Description,Amount,Category,Type
   2024-01-15,Salary Credit,100000,Salary,Credit
   2024-01-16,Rent Payment,25000,Rent,Debit
   2024-01-20,Medical Insurance,15000,Insurance,Debit
   2024-02-01,PPF Deposit,12500,Investment,Debit
   ```

2. **Upload and Analyze:**
   - Navigate to "Transactions" page (📊 Transactions in the menu)
   - Click "Choose File" and select your CSV or Excel file
   - Click "Analyze Transactions"
   - Wait for AI analysis (usually 10-30 seconds)

3. **Review Results:**

   You'll receive:
   - **Transaction Summary**: Total transactions, date range, total amount, categories
   - **AI Insights**: Key patterns and spending trends
   - **Detailed Analysis**: Comprehensive breakdown of your transactions
   - **Tax Implications**: Potential deductions under Indian Income Tax Act
     - Which expenses qualify for 80C, 80D, etc.
     - Income sources to report
     - Compliance recommendations

### Supported File Formats:
- CSV (.csv)
- Excel (.xlsx, .xls)
- Maximum file size: 10MB (can be adjusted)

### Example Use Cases:
- **Salary Slips**: Upload to identify taxable components
- **Bank Statements**: Analyze spending and find deductible expenses
- **Investment Statements**: Track 80C investments
- **Medical Bills**: Identify 80D deductible amounts
- **Rent Receipts**: Calculate HRA exemption eligibility

---

## 🚀 Running the Application

### Backend:
```bash
cd "H:\Tax project"
python -m uvicorn api.main:app --reload
```
The API will be available at `http://localhost:8000`

### Frontend:
```bash
cd "H:\Tax project\frontend"
npm run dev
```
The frontend will be available at `http://localhost:5173`

---

## 📝 Notes

### Security:
- User authentication is client-side only (suitable for demo purposes)
- For production, implement server-side session management
- Never commit `.env` files with real credentials to git

### Data Privacy:
- All tax calculations are stored in browser localStorage
- Uploaded transaction files are processed in-memory and deleted immediately
- No user data is stored on the server
- Google OAuth only accesses basic profile information

### Performance:
- Transaction analysis uses Gemini AI and may take 10-30 seconds
- Large files (>5MB) may take longer to process
- Charts render using Recharts library (already optimized)

---

## 🐛 Troubleshooting

### Google OAuth Not Working:
- Verify your Client ID is correct in `.env`
- Check that `http://localhost:5173` is in authorized origins
- Clear browser cache and try again

### Charts Not Showing:
- Make sure you've calculated tax first
- Check browser console for errors
- Verify localStorage has `lastTaxCalculation` data

### Transaction Upload Fails:
- Verify file format is CSV or Excel
- Check that file has proper column headers
- Ensure GEMINI_API_KEY is set in backend `.env`
- Check backend console for detailed error messages

### File Upload Issues:
- Ensure backend dependencies are installed: `pip install python-multipart openpyxl`
- Check that the backend server is running
- Verify file size is under 10MB

---

## 🎯 Future Enhancements

Potential improvements for these features:

1. **Authentication**:
   - Add email/password authentication option
   - Implement server-side session management
   - Add user profile management page

2. **Dashboard**:
   - Add year-over-year comparison charts
   - Historical tax data tracking
   - Export charts as images

3. **Transaction Analyzer**:
   - Support for PDF bank statements (with OCR)
   - Batch file upload
   - Save analysis history
   - Export analysis as PDF report
   - Custom category mapping
   - Integration with popular accounting software

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the browser console for frontend errors
3. Check the terminal running the backend for API errors
4. Verify all environment variables are set correctly
