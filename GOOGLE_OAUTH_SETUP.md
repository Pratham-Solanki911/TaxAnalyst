# 🔐 Google OAuth Setup Guide

## Complete Step-by-Step Guide to Enable Google Sign-In

This guide will walk you through setting up Google OAuth authentication for your Tax Analysis System.

---

## 📋 Prerequisites

- Google Account
- Access to Google Cloud Console
- 10 minutes of time

---

## 🚀 Step-by-Step Setup

### Step 1: Access Google Cloud Console

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account

### Step 2: Create a New Project

1. Click on the **project dropdown** at the top (next to "Google Cloud")
2. Click **"NEW PROJECT"**
3. Enter project details:
   - **Project name**: `Tax Analysis System` (or any name you prefer)
   - **Organization**: Leave as default or select your organization
4. Click **"CREATE"**
5. Wait for the project to be created (takes ~30 seconds)
6. Select your newly created project from the dropdown

### Step 3: Enable Required APIs

1. In the left sidebar, click **"APIs & Services"** > **"Library"**
2. Search for **"Google+ API"** or **"People API"**
3. Click on it and click **"ENABLE"**
4. Wait for it to enable

### Step 4: Configure OAuth Consent Screen

1. Go to **"APIs & Services"** > **"OAuth consent screen"**
2. Select **"External"** user type (unless you have a Google Workspace account)
3. Click **"CREATE"**

4. **Fill in the OAuth consent screen form:**

   **App Information:**
   - **App name**: `Indian Tax Analysis System`
   - **User support email**: Your email address
   - **App logo**: (Optional - you can skip this)

   **App domain:** (Optional - you can leave blank for now)
   - Application home page: `http://localhost:3000`
   - Application privacy policy link: (can skip)
   - Application terms of service link: (can skip)

   **Developer contact information:**
   - **Email addresses**: Your email address

5. Click **"SAVE AND CONTINUE"**

6. **Scopes screen:**
   - Click **"ADD OR REMOVE SCOPES"**
   - Select these scopes:
     - `openid`
     - `email`
     - `profile`
   - Or just skip this step (default scopes are sufficient)
   - Click **"SAVE AND CONTINUE"**

7. **Test users screen:**
   - Click **"ADD USERS"**
   - Add your email address (and any other test users)
   - Click **"ADD"**
   - Click **"SAVE AND CONTINUE"**

8. **Summary screen:**
   - Review your settings
   - Click **"BACK TO DASHBOARD"**

### Step 5: Create OAuth 2.0 Client ID

1. Go to **"APIs & Services"** > **"Credentials"**
2. Click **"CREATE CREDENTIALS"** at the top
3. Select **"OAuth client ID"**

4. **Configure the OAuth client:**
   - **Application type**: Select **"Web application"**
   - **Name**: `Tax Analysis Web Client` (or any name)

5. **Authorized JavaScript origins:**
   - Click **"ADD URI"**
   - Add: `http://localhost:3000`
   - For production, also add your production URL (e.g., `https://yourdomain.com`)

6. **Authorized redirect URIs:**
   - Click **"ADD URI"**
   - Add these URIs:
     ```
     http://localhost:3000
     http://localhost:3000/login
     ```

7. Click **"CREATE"**

### Step 6: Copy Your Client ID

1. A popup will appear with your credentials
2. **Copy the Client ID** - it looks like:
   ```
   123456789-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com
   ```
3. **Important**: Keep this Client ID safe (but it's not a secret - it's meant to be public)
4. Click **"OK"**

### Step 7: Configure Your Application

1. **Open your project folder:**
   ```
   cd "H:\Tax project\frontend"
   ```

2. **Create `.env` file** (if it doesn't exist):
   ```
   VITE_API_URL=http://localhost:8000
   VITE_GOOGLE_CLIENT_ID=paste-your-client-id-here
   ```

3. **Paste your Client ID:**
   Replace `paste-your-client-id-here` with the actual Client ID you copied.

   Example:
   ```
   VITE_API_URL=http://localhost:8000
   VITE_GOOGLE_CLIENT_ID=123456789-abc123xyz.apps.googleusercontent.com
   ```

4. **Save the file**

### Step 8: Restart Your Application

1. **Stop the frontend** (if it's running)
   - Press `Ctrl + C` in the terminal

2. **Start it again:**
   ```bash
   npm run dev
   ```

3. **Open browser:**
   ```
   http://localhost:3000/login
   ```

### Step 9: Test Google Sign-In

1. You should see the login page with:
   - Google "Sign in with Google" button
   - "Continue as Developer" button

2. Click **"Sign in with Google"**
3. Select your Google account
4. Grant permissions if asked
5. You should be redirected to the Dashboard!

---

## ✅ Verification Checklist

- [ ] Project created in Google Cloud Console
- [ ] OAuth consent screen configured
- [ ] OAuth 2.0 Client ID created
- [ ] Client ID copied
- [ ] `frontend/.env` file updated with Client ID
- [ ] Frontend restarted
- [ ] Google sign-in button appears
- [ ] Can successfully sign in with Google
- [ ] Redirected to Dashboard after sign-in
- [ ] User name and picture appear in header

---

## 🔧 Troubleshooting

### Error: "origin_mismatch"

**Problem**: The JavaScript origin doesn't match.

**Solution**:
1. Go back to [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials)
2. Click on your OAuth 2.0 Client ID
3. Check **Authorized JavaScript origins** has exactly:
   ```
   http://localhost:3000
   ```
   (No trailing slash, http not https, port 3000)
4. Save and wait 5 minutes for changes to propagate
5. Clear browser cache and try again

### Error: "Access blocked: This app's request is invalid"

**Problem**: OAuth consent screen not configured or app not verified.

**Solution**:
1. Make sure you completed Step 4 (OAuth consent screen)
2. Add your email to test users
3. If using external user type, app will show warning but still work for test users

### Error: "redirect_uri_mismatch"

**Problem**: Redirect URI not configured.

**Solution**:
1. Add both these to Authorized redirect URIs:
   ```
   http://localhost:3000
   http://localhost:3000/login
   ```

### Google button doesn't appear

**Problem**: Client ID not loaded or invalid.

**Solution**:
1. Check `frontend/.env` file exists
2. Verify Client ID is correct
3. Restart frontend server
4. Check browser console for errors

### "Popup blocked" error

**Solution**:
- Allow popups for localhost in browser settings
- Or click the popup icon in address bar

---

## 🌐 Production Deployment

When deploying to production:

1. **Update Authorized JavaScript origins:**
   ```
   https://yourdomain.com
   https://www.yourdomain.com
   ```

2. **Update Authorized redirect URIs:**
   ```
   https://yourdomain.com
   https://yourdomain.com/login
   https://www.yourdomain.com
   https://www.yourdomain.com/login
   ```

3. **Update `.env` file** (on production server):
   ```
   VITE_API_URL=https://api.yourdomain.com
   VITE_GOOGLE_CLIENT_ID=your-client-id
   ```

4. **Verify OAuth consent screen:**
   - Update app domain to production domain
   - Consider publishing the app (removes warning for users)

---

## 📊 OAuth Scopes Explained

The app requests these permissions:

- **`openid`**: Required for Google Sign-In
- **`email`**: To get user's email address
- **`profile`**: To get user's name and profile picture

These are **basic profile scopes** - minimal and safe.

---

## 🔒 Security Notes

### What's Safe to Share:
- ✅ Client ID (it's meant to be public)
- ✅ Redirect URIs (public information)
- ✅ JavaScript origins (public information)

### What to Keep Secret:
- ❌ Client Secret (if you have one - but we don't use it for frontend)
- ❌ User tokens
- ❌ Access tokens

### Best Practices:
- ✅ Use `.env` files for configuration
- ✅ Add `.env` to `.gitignore` (already done)
- ✅ Use different Client IDs for development and production
- ✅ Regularly review authorized apps in Google Account
- ✅ Monitor OAuth consent screen for suspicious activity

---

## 💡 Tips

1. **Development vs Production:**
   - Create separate OAuth clients for dev and prod
   - Use different Client IDs
   - Better security and easier debugging

2. **Test Users:**
   - Add multiple test users during development
   - Anyone not in test users list will see warning
   - Publish app to remove warnings (requires verification)

3. **Domain Verification:**
   - For production, verify your domain
   - Removes "unverified app" warning
   - Increases user trust

4. **Monitoring:**
   - Check Google Cloud Console > APIs & Services > Credentials
   - Monitor usage in Dashboard
   - Set up quotas if needed

---

## 🎯 Quick Reference

### Required URLs in Google Console:

**Authorized JavaScript origins:**
```
http://localhost:3000
```

**Authorized redirect URIs:**
```
http://localhost:3000
http://localhost:3000/login
```

### `.env` File Format:
```
VITE_API_URL=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=123456789-abc123xyz.apps.googleusercontent.com
```

---

## 📞 Still Need Help?

1. Check Google's official docs: https://developers.google.com/identity/gsi/web/guides/overview
2. Review error messages in browser console
3. Verify all steps completed
4. Wait 5-10 minutes after making changes (propagation delay)
5. Try incognito/private browsing mode

---

## 🎉 Success!

Once configured, your users can:
- ✅ Sign in with Google (one click)
- ✅ No password to remember
- ✅ Secure OAuth 2.0 authentication
- ✅ Automatic profile import (name, picture)
- ✅ Still have Development Mode as backup

**Your Tax Analysis System now has enterprise-grade authentication!** 🔐

---

<div align="center">

**Questions? Check the [Troubleshooting](#-troubleshooting) section**

[Back to Main README](README.md)

</div>
