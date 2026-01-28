# Vercel Deployment Guide

## ✅ Issues Fixed

### 1. **Renamed `homepage.html` → `index.html`**

Vercel requires `index.html` as the entry point for static sites.

### 2. **Created `vercel.json`**

Added Vercel configuration file for proper routing.

### 3. **Updated All Navigation Links**

Updated 18 HTML files to reference `index.html` instead of `homepage.html`.

## 🚀 How to Deploy on Vercel

### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Go to [vercel.com](https://vercel.com)** and sign in
2. **Click "Add New Project"**
3. **Import your Git repository** (GitHub/GitLab/Bitbucket)
   - Or use "Import Third-Party Git Repository" if not connected
4. **Configure Project:**
   - Framework Preset: **Other** (static HTML)
   - Root Directory: `./` (leave as default)
   - Build Command: (leave empty)
   - Output Directory: `./` (leave as default)
5. **Click "Deploy"**

### Method 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to your project
cd "/Users/sniply/Desktop/KRAFTHAUS/KHEL SAHAYOG"

# Deploy
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (select your account)
# - Link to existing project? No
# - Project name? khel-sahayog (or your choice)
# - Directory? ./ (press Enter)
# - Override settings? No

# For production deployment
vercel --prod
```

## 📋 Pre-Deployment Checklist

- [x] `index.html` exists (entry point)
- [x] `vercel.json` configuration created
- [x] All internal links updated to use `index.html`
- [ ] All images in `/images` folder exist
- [ ] Git repository is up to date
- [ ] No broken links

## 🔍 Common Deployment Issues

### Issue: "404 - Page Not Found"

**Solution:** Ensure `index.html` is in the root directory (already fixed ✅)

### Issue: "Images not loading"

**Solution:** Check that all images are in the `/images` folder and paths are correct

### Issue: "CSS not loading"

**Solution:** Ensure all CSS files are in the root directory (already correct ✅)

### Issue: "Navigation links broken"

**Solution:** All links now use `index.html` (already fixed ✅)

## 📁 Project Structure

```
KHEL SAHAYOG/
├── index.html              ← Entry point (was homepage.html)
├── vercel.json             ← Vercel configuration
├── style.css               ← Global styles
├── about.html
├── athletics.html
├── badminton.html
├── ... (other HTML files)
├── images/                 ← Image assets
│   └── logo.png
└── ... (other CSS files)
```

## 🎯 Next Steps

1. **Commit changes to Git:**

   ```bash
   git add .
   git commit -m "Fix: Rename homepage.html to index.html for Vercel deployment"
   git push
   ```

2. **Deploy on Vercel** using Method 1 or 2 above

3. **Test your deployment:**
   - Check all pages load correctly
   - Verify dropdown menu works
   - Test all navigation links
   - Verify images load properly

## 🌐 Your Site Will Be Live At

After deployment, Vercel will provide a URL like:

- `https://khel-sahayog.vercel.app`
- Or your custom domain if configured

---

**Ready to deploy!** Your project is now configured correctly for Vercel. 🚀
