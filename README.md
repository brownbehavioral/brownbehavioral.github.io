# brownbehavioral.com website

Static website for Brown Behavioral Health Services, PLLC. Hosted free on GitHub Pages.

## How updates work
- All page text lives in `build.py`. Styles are in `assets/site.css`. Images are in `images/`.
- After any edit, run `python3 build.py` to regenerate the pages, then commit and push. GitHub Pages republishes in about a minute.
- Page addresses match the old WordPress site (for example `/behavioral-health-care-about-us/`), so existing links and Google results keep working.

## Forms
Contact and Careers forms send to contact@brownbehavioral.com through FormSubmit (free). The very first submission triggers an activation email to that inbox; click the link once to turn the forms on.

## Going live on www.brownbehavioral.com
1. In the GitHub repository: Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`. Custom domain: `www.brownbehavioral.com`. Tick "Enforce HTTPS" once it is available.
2. At the domain's DNS provider, change ONLY these records (do not touch MX, TXT/SPF, DKIM or autodiscover records, which run your Microsoft 365 email):
   - `www`  CNAME  `<your-github-username>.github.io`
   - `@` (root) A records: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
3. Wait for DNS to update (usually under an hour, up to 24 hours), then cancel the old Proweaver hosting.
