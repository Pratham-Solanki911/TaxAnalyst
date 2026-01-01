# Fixing Google OAuth "origin_mismatch" Error

## Quick Solution: Use Development Mode

I've added a **"Continue as Developer (Testing Mode)"** button on the login page that bypasses Google OAuth entirely. This allows you to test all features immediately without setting up OAuth.

**To use it:**
1. Go to http://localhost:5173/login
2. Click **"Continue as Developer (Testing Mode)"**
3. You'll be logged in as "Developer User"
4. Test all features: Dashboard charts, Tax Calculator, Transaction Analyzer, etc.

---

## Permanent Solution: Fix OAuth Configuration

The "origin_mismatch" error happens when the redirect URI in Google Cloud Console doesn't match your app's URL exactly.

### Step-by-Step Fix:

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/apis/credentials

2. **Find Your OAuth Client**
   - Click on your OAuth 2.0 Client ID (the one you created)

3. **Check Authorized JavaScript Origins**

   Make sure you have EXACTLY this:
   ```
   http://localhost:5173
   ```

   Common mistakes:
   - ❌ `http://localhost:5173/` (with trailing slash)
   - ❌ `https://localhost:5173` (https instead of http)
   - ❌ `http://localhost:5174` (wrong port)

   Correct:
   - ✅ `http://localhost:5173` (no trailing slash, http, port 5173)

4. **Check Authorized Redirect URIs**

   Add these URIs:
   ```
   http://localhost:5173
   http://localhost:5173/
   http://localhost:5173/login
   ```

   Having multiple is fine - Google will use the first match.

5. **Save Changes**
   - Click **"SAVE"** at the bottom
   - Wait 5 minutes for changes to propagate

6. **Update Your .env File**

   Make sure your `frontend/.env` has:
   ```env
   VITE_API_URL=http://localhost:8000
   VITE_GOOGLE_CLIENT_ID=YOUR-ACTUAL-CLIENT-ID.apps.googleusercontent.com
   ```

7. **Restart Frontend**
   ```bash
   cd "H:\Tax project\frontend"
   npm run dev
   ```

8. **Test OAuth Login**
   - Go to http://localhost:5173/login
   - Try "Sign in with Google" button
   - Should work now!

---

## Alternative: Vite Dev Server Port

If you're still having issues, check what port Vite is actually using:

1. When you run `npm run dev`, check the terminal output:
   ```
   VITE v5.0.8  ready in 500 ms

   ➜  Local:   http://localhost:5173/
   ➜  Network: use --host to expose
   ```

2. If it shows a different port (like 5174), update Google Console with that port.

---

## Testing Checklist

After fixing:

- [ ] Google OAuth button appears on login page
- [ ] Clicking "Sign in with Google" opens Google popup
- [ ] Selecting account redirects back to app
- [ ] User is logged in (see name/picture in header)
- [ ] Can access all pages
- [ ] Can logout successfully

---

## Common Issues

### Issue: "Popup blocked"
**Solution:** Allow popups for localhost in browser settings

### Issue: "Invalid Client ID"
**Solution:**
- Check your Client ID is correct in `.env`
- Make sure you copied the entire ID
- Restart dev server after changing `.env`

### Issue: "Access blocked: This app's request is invalid"
**Solution:**
- Complete OAuth consent screen configuration
- Add your email to test users if using "Testing" mode
- Or publish the app (make it "In production")

### Issue: Still getting origin_mismatch
**Solution:**
- Clear browser cache
- Try incognito/private mode
- Wait 5-10 minutes after saving Google Console changes
- Double-check for typos in URLs (trailing slashes, http vs https)

---

## Production Deployment

When deploying to production:

1. Add your production URL to Google Console:
   ```
   https://yourdomain.com
   https://www.yourdomain.com
   ```

2. Update `.env` (or environment variables) with production URL:
   ```env
   VITE_API_URL=https://api.yourdomain.com
   VITE_GOOGLE_CLIENT_ID=your-client-id
   ```

3. Make sure your domain uses HTTPS (required for OAuth)

---

## Need Help?

1. **Use Development Mode** (already added) - bypasses OAuth entirely
2. **Check Google Console errors** - Often shows exact mismatch
3. **Browser DevTools** - Check console for detailed error messages
4. **Google's OAuth Playground** - Test your credentials at https://developers.google.com/oauthplayground/

The Development Mode button is perfect for testing and development. You can set up proper OAuth later when you're ready to deploy or need to test the actual Google login flow.
