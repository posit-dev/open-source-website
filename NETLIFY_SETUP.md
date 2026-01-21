# Netlify Deployment Setup

This guide helps you set up Netlify deployment with GitHub Actions.

## Prerequisites

- GitHub repository with the Hugo site
- Netlify account (free at https://netlify.com)

## Setup Steps

### 1. Create a Netlify Site

1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Connect to GitHub and select this repository
4. **Important**: In build settings, you can leave defaults or set:
   - Build command: `echo 'Build happens in GitHub Actions'`
   - Publish directory: `public`
5. Click "Deploy site"
6. Wait for the initial deploy (it will fail or be empty - that's OK)

### 2. Get Your Netlify Site ID

1. In your Netlify site dashboard, go to "Site configuration" → "General"
2. Under "Site information", copy the **Site ID** (looks like: `abc123def-4567-89gh-ijkl-mnopqrstuvwx`)

### 3. Create a Netlify Personal Access Token

1. Go to https://app.netlify.com/user/applications
2. Click "New access token"
3. Give it a name like "GitHub Actions Deploy"
4. Click "Generate token"
5. **Copy the token immediately** (you won't see it again)

### 4. Add Secrets to GitHub Repository

1. Go to your GitHub repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add two secrets:

   **Secret 1:**
   - Name: `NETLIFY_AUTH_TOKEN`
   - Value: [paste your Netlify personal access token]

   **Secret 2:**
   - Name: `NETLIFY_SITE_ID`
   - Value: [paste your Netlify site ID]

### 5. Enable GitHub Actions (if needed)

1. Go to your repository Settings → Actions → General
2. Ensure "Allow all actions and reusable workflows" is selected
3. Save if you made changes

### 6. Trigger Deployment

Once the secrets are added, you can trigger a deployment by:

- Pushing to the `main` branch
- Opening a pull request (creates a preview deployment)
- Manually running the workflow in Actions tab

## Expected Behavior

- **Push to main**: Deploys to production at your Netlify site URL
- **Pull requests**: Creates a unique preview URL and posts it as a comment on the PR
- **Manual trigger**: Can manually deploy from the Actions tab

## Troubleshooting

### Build fails with "NETLIFY_AUTH_TOKEN not set"
- Make sure you've added the secret correctly in GitHub Settings
- Secret names are case-sensitive

### Deploy succeeds but site is empty
- Check that `hugo --minify` builds successfully locally
- Verify `public/` directory contains the built site

### Preview URLs not appearing on PRs
- Check that `enable-pull-request-comment: true` is set in the workflow
- Ensure GitHub Actions has permission to comment on PRs

## Testing Locally

To test the build process locally:

```bash
# Install dependencies
npm ci

# Build Tailwind CSS
npm run build-tailwind

# Build Hugo site
hugo --minify

# Check the public/ directory
ls -la public/
```

## Custom Domain (Optional)

To use a custom domain:

1. Go to your Netlify site dashboard
2. Navigate to "Domain management"
3. Click "Add custom domain"
4. Follow Netlify's instructions for DNS configuration
5. Update `baseURL` in `hugo.toml` to your custom domain
