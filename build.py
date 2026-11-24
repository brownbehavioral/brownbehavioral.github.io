#!/usr/bin/env python3
"""Builds the Brown Behavioral Health Services static site.
Edit page content in this file, then run:  python3 build.py
Each page is written to <slug>/index.html so the old web addresses keep working."""
import os

SITE = "https://www.brownbehavioral.com"
PHONE, PHONE_LINK = "731-228-9068", "tel:+17312289068"
FAX = "901-425-9773"
EMAIL = "contact@brownbehavioral.com"
FORM_ENDPOINT = "https://formsubmit.co/" + EMAIL  # free form-to-email service
HEALOW_BOOK = "https://healow.com/apps/practice/brown-behavioral-health-services-pllc-bolivar-tn-30836?v=2&t=1"
PORTAL = "https://mycw248.ecwcloud.com/portal28692/jsp/100mp/login_otp.jsp"
REFERRAL = "https://form.jotform.com/233037233370144"
CARECREDIT = "https://www.carecredit.com/go/747MJQ/"
SCRATCHPAY = "https://scratchbilling.com/w/Brown_Behavioral_Health_Services/kOQJtmXyyvrrL2naiv0H"
FACEBOOK = "https://www.facebook.com/BrownBehavioralHealthServices"
PSYTODAY = "https://www.psychologytoday.com/profile/964592"
MAP = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d104263.03865848006!2d-89.0880990914496!3d35.2507832727626!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887e890c9f6c52eb%3A0xcf5c97b24fc74906!2sBolivar%2C%20TN%2038008%2C%20USA!5e0!3m2!1sen!2sph!4v1650263622702!5m2!1sen!2sph"

def ico(name, size=22):
    p = {
     "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.8 2z"/>',
     "cal":'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
     "portal":'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
     "card":'<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
     "send":'<path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/>',
     "heart":'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>',
     "mail":'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
     "pin":'<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
     "video":'<path d="m23 7-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/>',
     "fax":'<path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
     "fb":'<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
     "user":'<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
     "brief":'<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
     "brain":'<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24A2.5 2.5 0 0 0 14.5 2z"/>',
     "steth":'<path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6 6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"/><path d="M8 15v1a6 6 0 0 0 6 6 6 6 0 0 0 6-6v-4"/><circle cx="20" cy="10" r="2"/>',
     "leaf":'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
     "shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
     "check":'<path d="M20 6 9 17l-5-5"/>',
     "clock":'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
     "file":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
     "life":'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.9 4.9 4.3 4.3M14.8 14.8l4.3 4.3M14.8 9.2l4.3-4.3M4.9 19.1l4.3-4.3"/>',
    }[name]
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

NAV = [
 ("Home","/",None),
 ("About",None,[("Our Practice","/behavioral-health-care-about-us/"),("Our Team","/behavioral-health-care-meet-our-professionals/"),("Funding","/funding/"),("Center of Integrated Health (Nonprofit)","/center-of-integrated-health/"),("Careers","/behavioral-health-care-careers/"),("Request for Proposals","/behavioral-health-care-careers/request-for-proposals/")]),
 ("Services",None,[("All Services","/behavioral-health-care-services/"),("Psychiatric Evaluation","/behavioral-health-care-psychiatric-evaluation/"),("Medical Services","/behavioral-health-care-medical-services/"),("MS Medical Card Certification","/docs/MS-Cannabis-Certification.pdf")]),
 ("Patients",None,[("Patient Center","/patient-center/"),("Request an Appointment","/behavioral-health-request-an-appointment/"),("Insurance Accepted","/insurance/"),("Patient Portal","/behavioral-health-care-healow-patient-portal/"),("Pay Your Bill","/behavioral-health-care-payment/")]),
 ("Referrals","/behavioral-health-care-send-your-referrals/",None),
 ("Contact","/behavioral-health-care-contact-us/",None),
]

def nav_html(active):
    out=[]
    for label,href,sub in NAV:
        if sub:
            on=any(h==active for _,h in sub)
            items="".join(f'<li><a href="{h}"{" class=active" if h==active else ""}>{l}</a></li>' for l,h in sub)
            out.append(f'<li><button class="dd{" active" if on else ""}" aria-expanded="false">{label}</button><ul class="sub">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{href}"{" class=active" if href==active else ""}>{label}</a></li>')
    out.append(f'<li class="cta"><a href="/behavioral-health-request-an-appointment/">Book an Appointment</a></li>')
    return "<ul>"+"".join(out)+"</ul>"

def page(path, title, desc, body, phero=None):
    hero = ""
    if phero:
        h1, sub, crumb = phero
        hero = f'''<section class="phero"><div class="wrap"><div class="crumbs"><a href="/">Home</a> / {crumb}</div><h1>{h1}</h1>{f"<p>{sub}</p>" if sub else ""}</div></section>'''
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/images/favicon-32.png">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{SITE}/images/logo-270.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MedicalClinic","name":"Brown Behavioral Health Services, PLLC","url":"{SITE}","telephone":"+1-{PHONE}","faxNumber":"+1-{FAX}","email":"{EMAIL}","logo":"{SITE}/images/logo-270.png","areaServed":["Tennessee","Mississippi"],"address":[{{"@type":"PostalAddress","addressLocality":"Bolivar","addressRegion":"TN","postalCode":"38008","addressCountry":"US"}},{{"@type":"PostalAddress","addressLocality":"Olive Branch","addressRegion":"MS","postalCode":"38654","addressCountry":"US"}}],"sameAs":["{FACEBOOK}","{PSYTODAY}"]}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <div class="tb-left"><a href="{PHONE_LINK}">{ico("phone",15)} {PHONE}</a><a class="hide-sm" href="mailto:{EMAIL}">{ico("mail",15)} {EMAIL}</a><span class="hide-sm">Serving Tennessee and Mississippi, in person and by telehealth</span></div>
  <div class="tb-right"><a href="{CARECREDIT}" target="_blank" rel="noopener">We accept CareCredit</a><a class="crisis" href="tel:988">In crisis? Call or text 988</a></div>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="/"><img src="/images/logo-270.png" alt="Brown Behavioral Health Services logo" width="58" height="58"><span><b>Brown Behavioral<br>Health Services</b><small>PLLC</small></span></a>
  <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="main" aria-label="Main">{nav_html(path)}</nav>
</div></header>
<main id="main">
{hero}
{body}
</main>
<div class="crisis-band"><div class="wrap">
  <div class="ic">{ico("life",26)}</div>
  <p><b>In an emergency, call 911.</b> If you or someone you love is in a mental health or substance use crisis, free and confidential help is available 24 hours a day, 7 days a week, 365 days a year.</p>
  <div class="nums"><a href="tel:988">Call or Text 988: Suicide &amp; Crisis Lifeline</a><a href="tel:18552747471">TN Statewide Crisis Line: 855-CRISIS-1 (855-274-7471)</a><a href="tel:18772108513">MS Dept. of Mental Health Helpline: 1-877-210-8513</a><a href="sms:741741">Crisis Text Line: Text HOME to 741741</a><a href="tel:988">Veterans: Dial 988, then Press 1</a></div>
</div></div>
<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div><a class="brand" href="/" style="color:#fff"><img src="/images/logo-270.png" alt="" width="58" height="58"><span><b style="color:#fff">Brown Behavioral<br>Health Services, PLLC</b></span></a>
      <p style="margin-top:16px">If you need our services or want to learn more, you can reach out to us anytime.</p>
      <div class="fee"><b>No one will be denied access to services due to inability to pay.</b> There is a discounted/sliding fee schedule available based on family size and income.</div>
      <p style="margin-top:14px">Phone: <a href="{PHONE_LINK}">{PHONE}</a><br>Fax: {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p><div class="social"><a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{ico("fb",18)}</a><a href="{PSYTODAY}" target="_blank" rel="noopener" aria-label="Psychology Today profile">{ico("user",18)}</a></div>
    </div>
    <div><h4>Navigation</h4><ul><li><a href="/">Home</a></li><li><a href="/behavioral-health-care-about-us/">About Us</a></li><li><a href="/behavioral-health-care-meet-our-professionals/">Meet Our Professionals</a></li><li><a href="/behavioral-health-care-services/">Services</a></li><li><a href="/behavioral-health-care-medical-services/">Medical Services</a></li><li><a href="/behavioral-health-care-send-your-referrals/">Referrals</a></li><li><a href="/behavioral-health-care-careers/">Careers</a></li><li><a href="/behavioral-health-care-contact-us/">Contact Us</a></li></ul></div>
    <div><h4>Patients</h4><ul><li><a href="/patient-center/">Patient Center</a></li><li><a href="/behavioral-health-request-an-appointment/">Request an Appointment</a></li><li><a href="/behavioral-health-care-healow-patient-portal/">Patient Portal (healow)</a></li><li><a href="/insurance/">Insurance Accepted</a></li><li><a href="/behavioral-health-care-payment/">Payment Options</a></li><li><a href="/funding/">Funding</a></li><li><a href="/center-of-integrated-health/">Center of Integrated Health</a></li><li><a href="/sitemap/">Sitemap</a></li></ul></div>
    <div><h4>Our Offices</h4><ul>
      <li>Accepting patients throughout Tennessee and Mississippi</li>
      <li><b style="color:#fff">Tennessee Office</b><br>793 Tennessee Street<br>Bolivar, TN 38008</li>
      <li><b style="color:#fff">Mississippi Office</b><br>9851 Hwy 178, Suite B<br>Olive Branch, MS 38654</li><li>Telehealth visits available throughout TN and MS</li>
      </ul></div>
  </div>
  <div class="bottom"><span>&copy; 2022 - <span id="yr">2026</span> Brown Behavioral Health Services, PLLC. All rights reserved.</span><span><a href="/privacy-policy/">Privacy Policy</a> &nbsp;|&nbsp; <a href="/behavioral-health-care-about-us/#nondiscrimination">Nondiscrimination Policy</a></span></div>
</div></footer>
<script src="/assets/site.js"></script>
</body></html>'''
    d = path.strip("/")
    os.makedirs(d, exist_ok=True) if d else None
    with open(os.path.join(d, "index.html") if d else "index.html", "w") as f:
        f.write(html)

CONNECT = f'''<section class="alt"><div class="wrap"><div class="panel deep" style="display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap">
<div><h2 style="margin-bottom:6px">Connect with Us</h2><p style="margin:0">Learn more about us and our services. Contact us.</p></div>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">Request an Appointment</a><a class="btn btn-ghost" href="/behavioral-health-care-contact-us/">Contact Us</a></div></div></div></section>'''

def contact_form(subject):
    return f'''<form action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="{subject}"><input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{SITE}/thank-you/"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="row"><div><label for="fn">Full Name <span class="req">*</span></label><input id="fn" name="Full_Name" required></div>
<div><label for="em">Email Address <span class="req">*</span></label><input id="em" type="email" name="Email_Address" required></div></div>
<div class="row"><div><label for="ph">Phone <span class="req">*</span></label><input id="ph" type="tel" name="Phone" required></div>
<div><label for="ad">Address <span class="req">*</span></label><input id="ad" name="Address" required></div></div>
<label for="qc">Question / Comment</label><textarea id="qc" name="Question_or_Comment"></textarea>
<label class="check"><input type="checkbox" name="Privacy_Policy" value="Agreed" required> <span>By submitting this form you agree to the terms of the <a href="/privacy-policy/">Privacy Policy</a>.</span></label>
<label class="check"><input type="checkbox" name="SMS_Consent" value="Agreed"> <span>By providing a telephone number and submitting this form you are consenting to be contacted by SMS text message. Message &amp; data rates may apply. You can reply STOP to opt-out of further messaging.</span></label>
<p class="note">Please do not include private medical details in this form. For medical concerns, call {PHONE} or use the patient portal.</p>
<button class="btn btn-teal" type="submit">{ico("send",18)} Send Message</button></form>'''

# ---------------- HOME ----------------
BOLIVAR_MAP = "https://www.google.com/maps?q=793+Tennessee+Street,+Bolivar,+TN+38008&output=embed"
OLIVE_MAP = "https://www.google.com/maps?q=9851+Hwy+178+Ste+B,+Olive+Branch,+MS+38654&output=embed"

CATS = [
 ("brain","Behavioral Health","Psychiatric care for children, adolescents, and adults.",
  [("Psychiatric Evaluation","/behavioral-health-care-psychiatric-evaluation/"),("Medication Management","/behavioral-health-care-services/#behavioral"),("Psychotherapy","/behavioral-health-care-services/#behavioral"),("ADHD Testing","/behavioral-health-care-services/#behavioral"),("Genetic Testing","/behavioral-health-care-services/#behavioral")],"/behavioral-health-care-services/#behavioral"),
 ("shield","Addiction &amp; Recovery","Compassionate, evidence-based support for recovery.",
  [("MAT (Medication Assisted Treatment) Program","/behavioral-health-care-services/#recovery"),("Alcohol and Drug: DUI School","/behavioral-health-care-services/#recovery")],"/behavioral-health-care-services/#recovery"),
 ("steth","Primary &amp; Medical Care","Everyday medical care under the same roof.",
  [("Primary Care Services","/behavioral-health-care-medical-services/"),("Minor Medical Services","/behavioral-health-care-medical-services/"),("DOT Physicals","/behavioral-health-care-medical-services/"),("Sports Physicals","/behavioral-health-care-medical-services/"),("Mobile IV Hydration Service","/behavioral-health-care-medical-services/")],"/behavioral-health-care-medical-services/"),
 ("leaf","Wellness &amp; Specialty","Programs that support your whole-person health.",
  [("Slim Program","/behavioral-health-care-services/#wellness"),("MS Medical Card Certification","/docs/MS-Cannabis-Certification.pdf")],"/behavioral-health-care-services/#wellness"),
]
def cats_html():
    out=[]
    for ic,t,d,items,href in CATS:
        lis="".join(f'<li><a href="{h}">{n}</a></li>' for n,h in items)
        out.append(f'<div class="cat reveal"><div class="ci">{ico(ic,24)}</div><h3>{t}</h3><p class="note">{d}</p><ul>{lis}</ul><a class="more" href="{href}">Explore &rarr;</a></div>')
    return '<div class="cats">'+"".join(out)+'</div>'

LOCS = f'''<div class="locs">
 <div class="loc"><iframe src="{BOLIVAR_MAP}" title="Map of Bolivar, TN office" loading="lazy"></iframe><div class="lb"><span class="eyebrow">Tennessee</span><h3>Bolivar Office</h3><p>793 Tennessee Street<br>Bolivar, TN 38008</p><p class="note">Medicare-Certified Rural Health Clinic</p></div></div>
 <div class="loc"><iframe src="{OLIVE_MAP}" title="Map of Olive Branch, MS office" loading="lazy"></iframe><div class="lb"><span class="eyebrow">Mississippi</span><h3>Olive Branch Office</h3><p>9851 Hwy 178, Suite B<br>Olive Branch, MS 38654</p></div></div>
 <div class="loc"><div class="tele">{ico("video",56)}</div><div class="lb"><span class="eyebrow">Anywhere in TN &amp; MS</span><h3>Secure Telehealth</h3><p>Private video visits from the comfort of home for patients throughout Tennessee and Mississippi.</p></div></div>
</div>'''

home = f'''
<section class="hero"><div class="slides">
  <img class="on" src="/images/hero-ribbon-cutting.jpg" alt="BBHS team and community members at the Mobile Health Clinic ribbon cutting">
  <img src="/images/counseling-session.jpg" alt="A therapist meeting with a client" loading="lazy">
  <img src="/images/mobile-clinic.jpg" alt="The Brown Behavioral Health Services Mobile Health Clinic" loading="lazy">
  <img src="/images/mental-health-awareness.jpg" alt="BBHS team celebrating Mental Health Awareness Month" loading="lazy">
</div><div class="wrap">
  <span class="pill">{ico("video",16)} Tennessee &amp; Mississippi &middot; In Office and Secure Telehealth</span>
  <h1>Exceptional Behavioral Health Care, Delivered With Distinction.</h1>
  <p>Board-certified psychiatric care, integrated primary care, and addiction medicine for children, adolescents, and adults, provided with discretion, compassion, and clinical excellence.</p>
  <p class="tag-line">One small crack does not mean you&rsquo;re broken.</p>
  <div class="actions"><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">{ico("cal",18)} Schedule a Consultation</a><a class="btn btn-ghost" href="/behavioral-health-care-services/">Explore Our Services</a></div>
</div></section>

<div class="quick"><div class="wrap"><div class="grid">
  <a class="qcard" href="/behavioral-health-request-an-appointment/"><span class="ic">{ico("cal")}</span><span><b>Schedule Online</b><span>Book anytime on healow</span></span></a>
  <a class="qcard" href="/behavioral-health-care-healow-patient-portal/"><span class="ic">{ico("portal")}</span><span><b>Patient Portal</b><span>eClinicalWorks &amp; healow app</span></span></a>
  <a class="qcard" href="/behavioral-health-care-payment/"><span class="ic">{ico("card")}</span><span><b>Pay Your Bill</b><span>Flexible financing available</span></span></a>
  <a class="qcard" href="/behavioral-health-care-send-your-referrals/"><span class="ic">{ico("send")}</span><span><b>Provider Referrals</b><span>Refer a patient with confidence</span></span></a>
</div></div></div>

<div class="trust"><div class="wrap"><span>Doctoral-Prepared, Board-Certified Providers</span><span>Children, Adolescents, Adults &amp; Older Adults</span><span>In Office &amp; Secure Telehealth</span><span>Medicare-Certified Rural Health Clinic</span></div></div>

<section><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Welcome to Brown Behavioral Health Services, PLLC</span><h2>A Higher Standard of Mental Health Care</h2>
    <p class="lead">We partner with individuals and families to restore balance, strengthen resilience, and promote lasting mental well-being.</p>
    <p>Our practice pairs doctoral-prepared, board-certified clinicians with a deeply personal approach to care. Whether you are navigating everyday challenges or a complex diagnosis, for yourself or for someone you love, every treatment plan is designed around you. We would be honored to be your first choice in care.</p>
    <ul class="chips" style="margin:22px 0 28px"><li>Ages 5 and older</li><li>Tennessee &amp; Mississippi</li><li>Secure telehealth</li><li>Sliding fee scale available</li></ul>
    <a class="btn btn-teal" href="/behavioral-health-care-about-us/">Discover Our Practice</a></div>
  <div class="media arch reveal"><img src="/images/community-outreach.jpg" alt="BBHS team members at a community outreach event with the Mobile Health Clinic" style="aspect-ratio:4/5;object-fit:cover;width:100%"><div class="badge-float"><b>Your Care Begins Here</b>The same attentive care, in office or online.</div></div>
</div></section>

<section class="mist"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Our Expertise</span><h2 style="margin:0">Comprehensive Care, Thoughtfully Delivered</h2></div><p class="lead">Specialized psychiatric, medical, and recovery services for individuals ages 5 and older, all coordinated by one dedicated team.</p></div>
  {cats_html()}
</div></section>

<section><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Our Providers</span><h2 style="margin:0">Board-Certified. Deeply Committed.</h2></div><a class="btn btn-outline" href="/behavioral-health-care-meet-our-professionals/">Meet the Full Team</a></div>
  <div class="pgrid">
   <a class="pcard reveal" href="/behavioral-health-care-meet-our-professionals/"><img src="/images/home-Dr-Avanti-Cross-Brown.jpg" alt="Dr. Avanti Cross-Brown" loading="lazy"><div><b>Dr. Avanti Cross-Brown, APRN, DNP, PMHNP-BC, CARN-AP, NRCME</b><span>Founder &amp; CEO | Provider | Educator &amp; Community Advocate<br>Board-Certified Psychiatric Mental Health Practitioner | Addictions Advanced Practice Provider</span></div></a>
   <a class="pcard reveal" href="/behavioral-health-care-meet-our-professionals/"><img src="/images/home-Dr-Kayla-Williams.jpg" alt="Dr. Kayla Williams" loading="lazy"><div><b>Dr. Kayla Williams, APRN, DNP, PMHNP-BC</b><span>Board-Certified Psychiatric Mental Health Nurse Practitioner</span></div></a>
   <a class="pcard reveal" href="/behavioral-health-care-meet-our-professionals/"><img src="/images/Dr-Jessica-Allen.jpg" alt="Dr. Jessica Allen" loading="lazy"><div><b>Dr. Jessica Allen, MSN, DNP, FNP-BC, PMHNP-BC</b><span>Board-Certified Psychiatric Mental Health Nurse and Family Nurse Practitioner</span></div></a>
   <a class="pcard reveal" href="/behavioral-health-care-meet-our-professionals/"><img src="/images/home-Dr-DiYana-Fisher.jpg" alt="Dr. Di&rsquo;Yana Fisher" loading="lazy"><div><b>Dr. Di&rsquo;Yana Fisher, APRN, DNP, PMHNP-BC</b><span>Board-Certified Psychiatric Mental Health Nurse Practitioner</span></div></a>
  </div>
</div></section>

<section class="band"><div class="wrap" style="position:relative">
  <div class="sec-head"><div><span class="eyebrow gold">Getting Started</span><h2 style="margin:0">Three Simple Steps to Care</h2></div><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">Schedule a Consultation</a></div>
  <div class="hsteps">
    <div class="hstep"><h3>Request Your Appointment</h3><p>Book online anytime through healow, or call {PHONE}. Choose &ldquo;New Patient&rdquo; for your first visit.</p></div>
    <div class="hstep"><h3>Meet Your Provider</h3><p>Visit us in Bolivar or Olive Branch, or connect by secure telehealth from home.</p></div>
    <div class="hstep"><h3>Receive a Personalized Plan</h3><p>Together we set short-term and long-term goals and support you every step of the way.</p></div>
  </div>
</div></section>

<section class="mist"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">In the Community</span><h2 style="margin:0">Bringing Care to Where You Are</h2></div><p class="lead">Our Mobile Health Clinic travels to rural communities so more families can get care close to home.</p></div>
  <div class="gallery">
   <figure class="g-big reveal"><img src="/images/hero-ribbon-cutting.jpg" alt="Mobile Health Clinic ribbon cutting with the BBHS team and community leaders" loading="lazy"><figcaption>Mobile Health Clinic ribbon cutting</figcaption></figure>
   <figure class="reveal"><img src="/images/mobile-clinic.jpg" alt="BBHS Mobile Health Clinic" loading="lazy"><figcaption>Our Mobile Health Clinic</figcaption></figure>
   <figure class="reveal"><img src="/images/mental-health-awareness.jpg" alt="BBHS team and partners during Mental Health Awareness Month" loading="lazy"><figcaption>Mental Health Awareness Month</figcaption></figure>
   <figure class="reveal"><img src="/images/community-outreach.jpg" alt="BBHS staff at a community outreach event" loading="lazy" style="object-position:center 60%"><figcaption>Community outreach events</figcaption></figure>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Locations</span><h2 style="margin:0">Serving Tennessee and Mississippi</h2></div><p class="lead">We accept patients throughout the State of Tennessee and Mississippi, in office and by telehealth.</p></div>
  {LOCS}
</div></section>

<section class="mist"><div class="wrap" style="max-width:920px;text-align:center">
  <span class="eyebrow">Our Commitment</span><h2>Our Mission</h2>
  <p style="font-family:var(--serif);font-size:clamp(1.1rem,2vw,1.35rem);line-height:1.7;color:var(--deep)">The mission of Brown Behavioral Health Services is to provide proficient and competent care related to diagnosing and treating psychiatric illnesses in pediatrics and adults while improving overall health status. BBHS is committed to the mental health population and is eager to serve each individual holistically while enhancing mental health awareness, promoting individual empowerment, and increasing access to treatment and services for persons living with mental illnesses.</p>
  <a class="btn btn-teal" href="/behavioral-health-care-about-us/#mission">Learn About Our Practice</a>
</div></section>

<section style="padding-bottom:0"><div class="wrap"><div class="panel" style="display:grid;grid-template-columns:1.4fr 1fr;gap:26px;align-items:center">
  <div><span class="eyebrow">Our Nonprofit Partner</span><h2 style="margin-bottom:8px">Center of Integrated Health</h2><p style="margin:0">Our 501(c)(3) nonprofit extends care beyond the clinic through youth sports and wellness, youth mental health, and community partnerships across rural Tennessee and Mississippi.</p></div>
  <div style="text-align:right"><a class="btn btn-teal" href="/center-of-integrated-health/">Learn About the Center</a></div>
</div></div></section>

<section><div class="wrap"><div class="panel gold payband">
  <div><span class="eyebrow">Accessible Care</span><h2 style="margin-bottom:10px">Care for Every Family</h2><p style="margin:0"><b>No one will be denied access to services due to inability to pay.</b> A discounted/sliding fee schedule is available based on family size and income, and we proudly accept CareCredit and Scratchpay financing.</p><p style="margin:12px 0 0"><b>We accept Medicare, TennCare, Mississippi Medicaid, and most major private and Marketplace plans.</b></p></div>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end"><a class="btn btn-teal" href="/insurance/">Insurance Accepted</a><a class="btn btn-teal" href="/behavioral-health-care-payment/">Payment Options</a><a class="btn btn-outline" href="{CARECREDIT}" target="_blank" rel="noopener">Apply for CareCredit</a></div>
</div></div></section>

<section class="mist"><div class="wrap split" style="align-items:start">
  <div><span class="eyebrow">Connect With Us</span><h2>We Welcome Your Inquiry</h2><p class="lead">Share your questions or concerns, and a member of our team will respond promptly and confidentially.</p>
    <div class="panel deep" style="margin-top:24px"><ul class="ilist">
      <li>{ico("phone",18)}<span>Phone: <a style="color:#fff" href="{PHONE_LINK}">{PHONE}</a></span></li>
      <li>{ico("fax",18)}<span>Fax: {FAX}</span></li>
      <li>{ico("mail",18)}<span><a style="color:#fff" href="mailto:{EMAIL}">{EMAIL}</a></span></li>
      <li>{ico("pin",18)}<span>Bolivar, TN &amp; Olive Branch, MS<br>Telehealth throughout TN &amp; MS</span></li></ul></div></div>
  <div class="formcard">{contact_form("New message from brownbehavioral.com (home page)")}</div>
</div></section>
'''
page("/", "Brown Behavioral Health Services, PLLC | Behavioral Health Care in Tennessee and Mississippi",
     "Board-certified psychiatric care, primary care, and addiction medicine for ages 5 and up. Offices in Bolivar, TN and Olive Branch, MS, plus secure telehealth.", home)

# ---------------- ABOUT ----------------
about = f'''
<section><div class="wrap split">
 <div><span class="eyebrow">Who We Are</span><h2>Accessible care for rural communities</h2>
 <p class="lead">Brown Behavioral Health Services, PLLC takes pride in offering mental health, minor medical, weight loss, substance abuse treatment, and IV hydration services across the state of Tennessee and Mississippi.</p>
 <p>Our in person and telehealth capabilities provide a more accessible approach to healthcare across rural communities. We encourage you to choose a premiere clinic such as ours to help facilitate your mental health needs as well as other medical services.</p>
 <ul class="chips" style="margin-top:20px"><li>Mental Health</li><li>Minor Medical</li><li>Weight Loss</li><li>Substance Abuse Treatment</li><li>IV Hydration</li></ul></div>
 <div class="media"><img src="/images/hero-ribbon-cutting.jpg" alt="BBHS team and community members at the Mobile Health Clinic ribbon cutting" style="aspect-ratio:4/3;object-fit:cover;width:100%"></div>
</div></section>
<section class="alt" id="mission"><div class="wrap two">
 <div class="panel"><span class="eyebrow">Our Mission</span><p>The mission of Brown Behavioral Health Services is to provide proficient and competent care related to diagnosing and treating psychiatric illnesses in pediatrics and adults while improving overall health status. BBHS is committed to the mental health population and is eager to serve each individual holistically while enhancing mental health awareness, promoting individual empowerment, and increasing access to treatment and services for persons living with mental illnesses.</p></div>
 <div class="panel deep"><span class="eyebrow gold">Our Vision</span><p style="font-family:var(--serif);font-size:1.1rem;color:#f1f6f4">&ldquo;To provide client-centered, expert mental health services such as evaluations, patient advocacy, and medication management to the medically underserved communities with an aim to treat conditions such as Schizophrenia, Bipolar Disorders, ADHD, Depression, Anxiety, Substance Abuse, and many more.&rdquo;</p><p style="margin:0;color:var(--gold)">Dr. Avanti Cross-Brown, DNP, PMHNP-BC</p></div>
</div></section>
<section id="nondiscrimination"><div class="wrap" style="max-width:900px"><span class="eyebrow">Policy</span><h2>Nondiscrimination Policy</h2>
<p>It is the policy of Brown Behavioral Health Services (BBHS), under Title VI of the Civil Rights Act of 1964 and related statutes, to ensure that no person be excluded from participation in, be denied the benefits of, or be otherwise subjected to discrimination under any program or activity, on the grounds of race, religion, sex, color, age, disability, national origin, or any other protected class status. Equal opportunity will be provided to all members, program participants, service recipients, volunteers, contractors, employees, and subcontractors.</p>
<p>BBHS further assures that every effort will be made to ensure nondiscrimination in all programs and activities, regardless of how they are funded. It is also the policy of BBHS to comply with state and local laws governing nondiscrimination. BBHS prohibits any form of harassment based on race, religion, sex, color, age, disability, national origin, or any other protected class status applicable to federal, state, or local law.</p></div></section>
{CONNECT}'''
page("/behavioral-health-care-about-us/","About Us | Brown Behavioral Health Services","Mission, vision and nondiscrimination policy of Brown Behavioral Health Services, serving Tennessee and Mississippi.",about,("About Us","Mental health, minor medical, weight loss, substance abuse treatment, and IV hydration services across Tennessee and Mississippi.","About Us"))

# ---------------- TEAM ----------------
def person(img,name,role,cred,paras,tag=""):
    first,rest=paras[0],paras[1:]
    more = f'<details><summary>Read full bio</summary>{"".join(f"<p>{p}</p>" for p in rest)}</details>' if rest else ""
    ini="".join(w[0] for w in name.split(",")[0].replace("Dr. ","").split()[:2])
    pic=f'<img src="/images/{img}" alt="image of {name.split(",")[0]}">' if img else f'<div class="avatar" aria-hidden="true">{ini}</div>'
    return f'''<article class="person reveal">{pic}<div><h3>{name}</h3><div class="role">{role}</div><div class="cred">{cred}</div><p>{first}</p>{more}{f'<span class="tag">{tag}</span>' if tag else ""}</div></article>'''
_prov = ([
 person("Dr-Avanti-Brown.jpg","Dr. Avanti Cross-Brown, APRN, DNP, PMHNP-BC, CARN-AP, NRCME","Founder &amp; CEO | Provider | Educator &amp; Community Advocate","Board-Certified Psychiatric Mental Health Practitioner | Addictions Advanced Practice Provider",[
  "Dr. Avanti Cross-Brown is the Founder and CEO of Brown Behavioral Health Services (BBHS), a CMS certified Rural Health Clinic based in Bolivar, Tennessee and Olive Branch, Mississippi that serves urban and rural residents across both states. A native of West Tennessee, she has been serving the mental health community since 2013.",
  "Under her leadership, BBHS holds facility licenses in Office-Based Opioid Treatment, Outpatient Mental Health, Alcohol and Drug Detox, and DUI School. The practice delivers behavioral health, primary care, addictions treatment, school-based telehealth, correctional health, and mobile clinic services, as well as free care for uninsured patients.",
  "Dr. Cross-Brown earned her Bachelor of Science in Nursing from the University of Memphis in 2015 and worked as a Registered Nurse for many years. In 2021, she completed her Doctor of Nursing Practice at the University of Tennessee Health Science Center (UTHSC), specializing as a Psychiatric Mental Health Nurse Practitioner, and became ANCC board-certified. During graduate school, she received more than five competitive scholarships, including the Chancellor Diversity Scholarship Award, University Scholar Diversity Scholarship, and Grace S. Wallace Scholarship Award, as well as the fully funded HRSA ANEW Award.",
  "In 2022, she became a certified Medical Examiner for the Federal Motor Carrier Safety Administration, providing DOT (Department of Transportation) physical exams for CDL drivers and students. In 2025, she achieved dual certification as a Certified Addictions Advanced Practice Provider, expanding her expertise in MAT and MOUD treatment.",
  "At UTHSC, she serves as a Director on the Alumni Board and as a board member and Healthcare Stakeholder for the Community Advisory Council (CAC) of the ACCESS (Achieving Cancer Care Equity and Systematic Solutions) Study.",
  "A passionate grant writer, Dr. Cross-Brown has secured funding across Tennessee and Mississippi, including the Healthcare Rural Resiliency Program award (2025); the End Zone Chronic Disease Prevention award (2026), which funds the Blue Plate Project she developed alongside her Practice Administrator; and the Mississippi Rural Health Transformation Program workforce award (MENTOR MS, 2026). BBHS was also one of five organizations nationally selected for the Rural Healthcare Provider Transition Project.",
  "In 2026, Cynthia Daniels &amp; Co. named her one of the Top 40 Under 40 Urban Elite Professionals.",
  "With extensive experience treating children, adolescents, adults, and geriatrics across telehealth, outpatient, and inpatient settings, Dr. Cross-Brown combines clinical excellence with compassion to ensure her patients receive the best possible care."]),
 person("Dr-Kayla-Williams.jpg","Dr. Kayla Williams, APRN, DNP, PMHNP-BC","Psychiatric Mental Health Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse Practitioner",[
  "Dr. Kayla Williams is a board-certified Psychiatric Mental Health Nurse Practitioner committed to delivering comprehensive, patient-centered care across the lifespan. She earned her Doctor of Nursing Practice from the University of Tennessee Health Science Center in 2024, following her Bachelor of Science in Nursing from Baptist College of Health Sciences in 2019.",
  "She provides evidence-based treatment for children, adolescents, adults, and older adults facing a wide range of mental health conditions, including mood disorders, anxiety, ADHD, and trauma-related concerns. Dr. Williams is passionate about reducing stigma and promoting early intervention in mental health care.",
  "Her goal is to empower patients and families through education, individualized treatment planning, and ongoing support."],"Now accepting new patients. Weekend appointments available."),
 person("Dr-Jessica-Allen.jpg","Dr. Jessica Allen, MSN, DNP, FNP-BC, PMHNP-BC","Psychiatric and Family Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse and Family Nurse Practitioner",[
  "Dr. Jessica Allen is a board-certified Psychiatric-Mental Health and Family Nurse Practitioner with a focus on providing client-centered, expert mental health and medical services, including medical consultations, psychiatric evaluations, and medication management to all communities. Dr. Allen treats individuals age 5 years and above. She offers flexible &amp; affordable telehealth, mobile, &amp; in-person appointments, with some evenings &amp; weekends available."],"Evenings &amp; weekends available"),
 person("Dr-DiYana-Fisher.jpg","Dr. Di&rsquo;Yana Fisher, APRN, DNP, PMHNP-BC","Psychiatric Mental Health Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse Practitioner",[
  "Dr. Di&rsquo;Yana Fisher, DNP, PMHNP-BC is a board-certified Psychiatric Mental Health Nurse Practitioner at BBHS, providing evidence-based psychiatric care to adolescents and adults across Tennessee and Mississippi.",
  "Dr. Fisher is committed to ensuring every patient feels heard, supported, and understood. She takes a collaborative, whole-person approach to care, recognizing the connection between mind, body, and life experiences. She develops individualized treatment plans for conditions including anxiety, depression, ADHD, bipolar disorder, trauma, and other mental health concerns.",
  "Known for her warm, nonjudgmental style, Dr. Fisher creates a welcoming space where patients feel comfortable asking questions and actively participating in their care. She offers both in-office and secure telehealth appointments and is dedicated to expanding access to high-quality mental health services throughout Tennessee and Mississippi."],"Now accepting new patients. Weekend appointments available."),
])
_lead = ([
 person("Destiny-Shaw.jpg","Destiny Shaw, BS, MBA","Chief Operating Officer (COO) | Practice Administrator","",[
  "Destiny Shaw serves as Chief Operating Officer and Practice Administrator at Brown Behavioral Health Services, where she oversees daily clinic operations and ensures patients experience seamless, coordinated care.",
  "With a five-year background in clinical mental health, rural health policy, and patient advocacy, Destiny brings both operational expertise and a deep commitment to expanding access to care in rural communities. She also serves as the Special Grant Projects Team Manager, leading initiatives that strengthen and grow the services BBHS provides."]),
 person("Brook-Pittman.jpg","Brook Pittman, CMA","Clinical Lead Medical Assistant | Community Health Coordinator","",[
  "With 15 years of dedicated work in the medical field, Brook Pittman serves compassionately as the Clinical Lead Medical Assistant at Brown Behavioral Health Services, supporting providers and patients across the clinic&rsquo;s behavioral health and primary care services.",
  "Brook also serves as the MA Student Rotation Coordinator, mentoring the next generation of medical assistants, and as Community Health Coordinator under the Healthcare Resiliency Program grant, connecting patients with resources throughout the community."]),
 person("Andreina-Acuna.jpg","Andreina Acuna, CMA","School Health Coordinator | Medical Assistant","",[
  "Andreina Acuna serves as the School Health Coordinator and Medical Assistant on the BBHS Clinical Administration team.",
  "With three years of experience in medical and legal translation services, Andreina transitioned into a front-facing healthcare role at BBHS after completing her rural student rotation with the clinic in the fall of 2025. She is excited to assist patients in both English and Spanish, helping expand accessible, welcoming care for every family BBHS serves."],"Se habla espa&ntilde;ol"),
])
THERAPISTS = [
 ("Bernice Lofties","Therapist"),
 ("Broderick Webster","Therapist"),
 ("Cameron Brown, MSW, MBA","Therapist"),
 ("Rodques Jones, MSW","Therapist"),
]
_ther = "".join(person(None,n,r,"Behavioral Health Therapy",[f"{n.split(',')[0]} provides individual psychotherapy as part of the BBHS behavioral health team, supporting patients in building coping skills, insight, and resilience."]) for n,r in THERAPISTS)
def tsec(eyebrow,title,body,alt=False):
    return f'''<section class="{'mist' if alt else ''}"><div class="wrap"><div class="center"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2></div><div class="team">{body}</div></div></section>'''
team = (tsec("Leadership","Executive Leadership",_prov[0]+_lead[0])
      + tsec("Clinical Providers","Our Providers","".join(_prov[1:]),True)
      + tsec("Behavioral Health","Our Therapists",_ther)
      + tsec("Clinical Support","Medical Assistant Team","".join(_lead[1:]),True) + CONNECT)
page("/behavioral-health-care-meet-our-professionals/","Meet Our Professionals | Brown Behavioral Health Services","Meet the leadership, board-certified providers, therapists, and clinical team at Brown Behavioral Health Services.",team,("Meet Our Professionals","Get to know the professionals who are available to help and support you anytime.",'<a href="/behavioral-health-care-about-us/">About</a> / Our Team'))

# ---------------- SERVICES ----------------
SVC = {
 "behavioral":("brain","Behavioral Health",[
   ("Psychiatric Evaluation","A comprehensive assessment that brings clarity to diagnosis and direction to treatment.","/behavioral-health-care-psychiatric-evaluation/"),
   ("Medication Management","Ongoing, evidence-based oversight so every medication works safely and effectively for you.",None),
   ("Psychotherapy","Talk therapy with licensed professionals to build coping skills, insight, and resilience.",None),
   ("ADHD Testing","Thorough testing for children, adolescents, and adults to guide an accurate diagnosis.",None),
   ("Genetic Testing","Testing that can help personalize your treatment plan.",None)]),
 "recovery":("shield","Addiction &amp; Recovery",[
   ("MAT (Medication Assisted Treatment) Program","Medication combined with counseling and support for substance use disorders.",None),
   ("Alcohol and Drug: DUI School","Required alcohol and drug education delivered in a respectful, supportive setting.",None)]),
 "medical":("steth","Primary &amp; Medical Care",[
   ("Primary Care Services","Everyday medical care that works hand in hand with your behavioral health care.","/behavioral-health-care-medical-services/"),
   ("DOT Physicals","Department of Transportation physical exams for CDL drivers and students.","/behavioral-health-care-medical-services/"),
   ("Minor Medical Services","Prompt care for common, non-emergency medical needs.","/behavioral-health-care-medical-services/"),
   ("Sports Physicals","Pre-participation physicals for student athletes.","/behavioral-health-care-medical-services/"),
   ("Mobile IV Hydration Service","IV hydration brought to you.","/behavioral-health-care-medical-services/")]),
 "wellness":("leaf","Wellness &amp; Specialty",[
   ("Slim Program","Medically guided weight-loss support.",None),
   ("Medical Card Certification","Mississippi medical cannabis certification.","/docs/MS-Cannabis-Certification.pdf")]),
}
def svc_sections():
    out=[]
    for i,(key,(ic,title,items)) in enumerate(SVC.items()):
        cards="".join(f'<div class="panel reveal"><h3>{n}</h3><p class="note" style="margin:0 0 {"12px" if h else "0"}">{d}</p>{f"<a class=more style=font-weight:600;text-decoration:none href={chr(34)}{h}{chr(34)}>Learn More &rarr;</a>" if h else ""}</div>' for n,d,h in items)
        out.append(f'<section id="{key}" class="{"mist" if i%2 else ""}"><div class="wrap"><div class="sec-head"><div style="display:flex;gap:18px;align-items:center"><div class="icw"><div class="ci" style="margin:0">{ico(ic,24)}</div></div><h2 style="margin:0">{title}</h2></div></div><div class="cards three" style="margin-top:0">{cards}</div></div></section>')
    if True:
        out.insert(1,"")
    return "".join(out)
cond=["Major Depressive Disorders","Generalized Anxiety Disorder","PTSD","ADHD","Disruptive Mood Dysregulation Disorder","Conduct Disorders","Postpartum Depression","Bipolar Disorders","Schizophrenic Disorders","Medication Assisted Treatment for Substance Use Disorders","Many more"]
services = f'''<section style="padding-bottom:40px"><div class="wrap" style="max-width:900px;text-align:center"><p class="lead">Our behavioral health care services are available for individuals aging 5 and up. If you want to avail any of them, we recommend you request an appointment and meet with our professionals. They will help you determine your situation and the services appropriate to address your concerns. We are here to support you.</p>
<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px"><a class="btn btn-outline" href="#behavioral">Behavioral Health</a><a class="btn btn-outline" href="#recovery">Addiction &amp; Recovery</a><a class="btn btn-outline" href="#medical">Primary &amp; Medical</a><a class="btn btn-outline" href="#wellness">Wellness &amp; Specialty</a></div></div></section>
<span id="medication-management"></span>{svc_sections()}
<section class="band"><div class="wrap center" style="position:relative"><span class="eyebrow gold">Conditions We Treat</span><h2>Expert Care for a Wide Range of Conditions</h2>
<ul class="chips" style="justify-content:center;margin-top:28px">{"".join(f'<li style="background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.18)">{c}</li>' for c in cond)}</ul></div></section>{CONNECT}'''
page("/behavioral-health-care-services/","Services | Brown Behavioral Health Services","Behavioral health, addiction and recovery, primary care, and wellness services for ages 5 and up in Tennessee and Mississippi.",services,("Our Services","Behavioral health, recovery, medical, and wellness services, coordinated by one dedicated team.","Services"))

# ---------------- PSYCH EVAL ----------------
pe = f'''<section><div class="wrap split" style="align-items:start"><div class="prose">
<p class="lead">A comprehensive psychiatric evaluation is needed to properly diagnose and treat emotional, behavioral, or developmental disorders. This may include evaluating problems with relationships with friends or family members, work, school, sleeping, eating, substance abuse, emotional expression, development, coping, attentiveness, and responsiveness.</p>
<h2>An evaluation may include:</h2>
<ul><li>Description of behaviors</li><li>Description of symptoms (physical and psychiatric symptoms)</li>
<li>Effects of behaviors or symptoms related to:<ul><li>Work performance</li><li>School performance</li><li>Relationships and social interactions with others</li><li>Family involvement</li><li>Activity involvement</li></ul></li>
<li>Psychiatric interview with mental status exam</li><li>Personal and family history of emotional, behavioral, or developmental disorders</li>
<li>Complete medical history, including description of the person&rsquo;s overall physical health, list of any other illnesses or conditions present, and any current treatments</li>
<li>Lab tests including:<ul><li>Blood tests</li><li>Radiology studies to look for abnormalities, particularly in the brain structures</li><li>Educational assessments</li><li>Speech and language assessments</li><li>Psychological assessments</li></ul></li></ul>
<p>After reviewing the evaluation and formulating a diagnosis, we will work with you to establish long-term and short-term treatment goals.</p></div>
<aside><div class="media" style="margin-bottom:22px"><img src="/images/therapy-notes.jpg" alt="A provider taking notes during an evaluation" style="aspect-ratio:4/3;object-fit:cover;width:100%"></div><div class="panel deep"><h3>Ready to talk?</h3><p>If you are interested in hearing more about our services, please feel free to reach out to us at any time.</p><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">Request an Appointment</a><p style="margin:16px 0 0">Or call <a style="color:#fff" href="{PHONE_LINK}">{PHONE}</a></p></div></aside>
</div></section>'''
page("/behavioral-health-care-psychiatric-evaluation/","Psychiatric Evaluation | Brown Behavioral Health Services","Comprehensive psychiatric evaluations for children, adolescents and adults in Tennessee and Mississippi.",pe,("Psychiatric Evaluation","Schedule an evaluation to understand your cognitive status.",'<a href="/behavioral-health-care-services/">Services</a> / Psychiatric Evaluation'))

# ---------------- MEDICAL ----------------
med=["Primary Care Services","DOT Physicals","Minor Medical Services","Slim Program","Mobile IV Hydration Service","Sports Physicals"]
medical = f'''<section><div class="wrap"><div class="cards three">{"".join(f'<div class="panel reveal"><span class="eyebrow">{ico("heart",16)}</span><h3>{m}</h3><a class="more" style="font-weight:600;text-decoration:none" href="/behavioral-health-request-an-appointment/">Request an Appointment &rarr;</a></div>' for m in med)}</div></div></section>{CONNECT}'''
page("/behavioral-health-care-medical-services/","Medical Services | Brown Behavioral Health Services","Primary care, DOT physicals, minor medical services, Slim Program, mobile IV hydration and sports physicals.",medical,("Medical Services","Primary care and medical services alongside our behavioral health care.","Medical Services"))

# ---------------- APPOINTMENT ----------------
appt = f'''<section><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">Online Scheduling with healow</span><h2>Book your next appointment online.</h2><p class="lead">No need to wait for our office to open the next day. BBHS uses <b>eClinicalWorks</b>, and appointments are booked online through <b>healow</b>, eClinicalWorks&rsquo; secure scheduling and patient app.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap;margin:6px 0 20px"><a class="btn btn-teal" href="{HEALOW_BOOK}" target="_blank" rel="noopener">{ico("cal",18)} Book Now on healow</a><a class="btn btn-outline" href="{PHONE_LINK}">{ico("phone",16)} Call {PHONE}</a></div>
<h3>How to book on healow</h3>
<ol class="steps">
<li><span>Click <b>Book Now on healow</b>. Our practice page on healow.com opens in a new window.</span></li>
<li><span>Choose your <b>provider</b> and <b>visit reason</b>. Select <b>New Patient</b> if this is your first visit with BBHS, or <b>Established Patient</b> if you have been seen before.</span></li>
<li><span>Pick an available <b>date and time</b>, in office or by telehealth.</span></li>
<li><span>Enter your <b>name, date of birth, phone, email, and insurance</b>. healow will send a verification code by text or email to confirm it is you.</span></li>
<li><span>Watch for your <b>confirmation</b> by text or email. Before your visit you may also receive an eClinicalWorks <b>check-in link</b> to complete your forms, insurance, and consents from your phone.</span></li>
</ol></div>
<div>
<div class="two" style="margin-bottom:22px">
<div class="panel"><span class="eyebrow">Tennessee</span><h3>TN Brown Behavioral Health Services</h3><p class="note">793 Tennessee Street, Bolivar, TN 38008</p><p class="note">Medical Provider Only</p><a class="btn btn-outline" href="{HEALOW_BOOK}" target="_blank" rel="noopener">Book in TN</a></div>
<div class="panel"><span class="eyebrow">Mississippi</span><h3>MS Brown Behavioral Health Services</h3><p class="note">9851 Hwy 178, Suite B, Olive Branch, MS 38654</p><p class="note">&nbsp;</p><a class="btn btn-outline" href="{HEALOW_BOOK}" target="_blank" rel="noopener">Book in MS</a></div>
</div>
<div class="panel deep"><span class="eyebrow gold">Prefer the App?</span><h3>Book in the healow App</h3><ul class="ilist">
<li>{ico("check",18)}<span>Download the free <b>healow&trade;</b> app from the App Store or Google Play.</span></li>
<li>{ico("check",18)}<span>Search for our practice using practice code <b style="color:var(--gold)">ACGHDD</b>.</span></li>
<li>{ico("check",18)}<span>Tap <b>Book Appointment</b>, then choose your provider, visit reason, and time.</span></li>
<li>{ico("check",18)}<span>Telehealth visits: our team will send your secure video visit instructions before your appointment.</span></li></ul></div>
</div></div></section>
<section class="mist"><div class="wrap center" style="max-width:820px"><span class="eyebrow">New Patients</span><h2>New to BBHS?</h2><p class="lead">We are welcoming new patients ages 5 and up at our Bolivar and Olive Branch offices and by secure telehealth. Book your first visit on healow in minutes and choose <b>New Patient</b> as your visit type, or call {PHONE} and our team will schedule you and set up your eClinicalWorks patient portal.</p><div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn btn-teal" href="{HEALOW_BOOK}" target="_blank" rel="noopener">{ico("cal",18)} Book a New Patient Appointment</a><a class="btn btn-outline" href="/insurance/">Check Insurance Accepted</a></div><p class="note" style="margin-top:18px">No one will be denied access to services due to inability to pay. A sliding fee schedule is available based on family size and income.</p></div></section>'''
page("/behavioral-health-request-an-appointment/","Request an Appointment | Brown Behavioral Health Services","Book your appointment online through healow (eClinicalWorks) with Brown Behavioral Health Services in Tennessee or Mississippi.",appt,("Request an Appointment","Book online through healow, in the healow app, or by phone.",'<a href="/patient-center/">Patients</a> / Request an Appointment'))

# ---------------- PORTAL ----------------
portal = f'''<section><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">eClinicalWorks Patient Portal</span><h2>Your health records, anytime.</h2><p class="lead">Our patient portal is powered by <b>eClinicalWorks</b>. Use it on the web or in the <b>healow</b> app to view visit summaries and lab results, message your care team, request refills, update your information, and manage appointments.</p>
<h3>First time logging in?</h3>
<ol class="steps">
<li><span>Ask our front desk at {PHONE} for a <b>portal invitation</b> if you did not receive one at your visit. It arrives by email or text with your <b>username</b> and a temporary password.</span></li>
<li><span>Open the <b>Go to Patient Portal</b> button on this page, or download the <b>healow&trade;</b> app from the App Store (iPhone) or Google Play (Android).</span></li>
<li><span>In the healow app, search our practice by entering practice code <span class="code">ACGHDD</span>.</span></li>
<li><span>Enter your portal username and password to log in, then create a new password.</span></li>
<li><span>Set up your PIN to securely access your health records.</span></li></ol>
<p class="note" style="margin-top:16px">Forgot your password? Use the &ldquo;Forgot Password&rdquo; link on the login screen or call our office for a reset.</p></div>
<div class="panel deep center sidecard"><div style="width:64px;height:64px;border-radius:16px;background:rgba(224,168,74,.2);color:var(--gold);display:grid;place-items:center;margin:0 auto 18px">{ico("portal",30)}</div><h3>Already have an account?</h3><p>Log in to the eClinicalWorks patient portal to view records, message your care team, and more.</p><a class="btn btn-gold" href="{PORTAL}" target="_blank" rel="noopener">Go to Patient Portal</a><p style="margin:18px 0 0">healow app practice code: <b style="color:var(--gold)">ACGHDD</b></p><p class="note" style="color:#d7ebe8;margin:10px 0 0">The portal is for non-urgent communication. In an emergency, call 911.</p></div>
</div></section>'''
page("/behavioral-health-care-healow-patient-portal/","Patient Portal (eClinicalWorks and healow) | Brown Behavioral Health Services","Access the Brown Behavioral Health Services eClinicalWorks patient portal on the web or in the healow app. Practice code ACGHDD.",portal,("Patient Portal","Powered by eClinicalWorks and the healow app. Practice code ACGHDD.",'<a href="/patient-center/">Patients</a> / Patient Portal'))

# ---------------- PAYMENT ----------------
pay = f'''<section><div class="wrap three">
<div class="panel"><span class="eyebrow">Option 1</span><h3>Debit/Credit Card</h3><p>To pay your balance by debit or credit card, please call our office and our team will process your payment and email you a confirmation.</p><a class="btn btn-outline" href="{PHONE_LINK}">{ico("phone",16)} Call {PHONE}</a></div>
<div class="panel gold"><span class="eyebrow">Option 2</span><h3>CareCredit Card</h3><p><b>Pay online with the CareCredit credit card.</b> We proudly accept the CareCredit credit card to help you finance your healthcare needs. Now you can pay online with CareCredit to help pay at the time of care, when you get a post-care bill, or up to 30 days before your appointment, quickly and securely. Special financing options are available.*</p>
<p><a class="btn btn-teal" href="{CARECREDIT}" target="_blank" rel="noopener">Pay with CareCredit</a></p><p class="note">Don&rsquo;t have CareCredit? Get prequalified! <a href="{CARECREDIT}" target="_blank" rel="noopener">Apply here or learn more</a> today.</p></div>
<div class="panel"><span class="eyebrow">Option 3</span><h3>Scratch Pay</h3><p>We now offer Scratchpay to make financing easy for everyone! With higher approval rates, friendly terms, and a simple application process, Scratchpay lets you get the care you need now and worry about payments later. Learn more at <a href="https://www.scratchpay.com" target="_blank" rel="noopener">www.scratchpay.com</a>.</p><a class="btn btn-outline" href="{SCRATCHPAY}" target="_blank" rel="noopener">Apply today!</a></div>
</div>
<div class="wrap" style="margin-top:28px"><p class="note">*Subject to credit approval. Minimum monthly payments required. Promotional financing options are available on purchases of $200 or more. Standard Account Terms apply to purchases of less than $200. Promotional financing options available through Pay My Provider may differ from options available in-office. See <a href="http://www.carecredit.com" target="_blank" rel="noopener">www.carecredit.com</a> for details.</p>
<div class="alert">No one will be denied access to services due to inability to pay. There is a discounted/sliding fee schedule available based on family size and income.</div></div></section>'''
page("/behavioral-health-care-payment/","Payment Options | Brown Behavioral Health Services","Pay by debit/credit card, CareCredit, or Scratchpay. Sliding fee scale available.",pay,("Payment Options","Flexible ways to pay for your care.","Payment Options"))

# ---------------- PATIENT CENTER ----------------
pc = f'''<section><div class="wrap"><div class="cards" style="margin-top:0">
 <div class="panel reveal"><div class="icw"><div class="ci">{ico("cal",24)}</div></div><h3>Request an Appointment</h3><p class="note">Book online at any hour through healow (eClinicalWorks), in the healow app with practice code <span class="code">ACGHDD</span>, or call {PHONE}.</p><a class="btn btn-teal" href="/behavioral-health-request-an-appointment/">Schedule</a></div>
 <div class="panel reveal"><div class="icw"><div class="ci">{ico("portal",24)}</div></div><h3>Patient Portal</h3><p class="note">Your eClinicalWorks portal on the web or in the healow app. Practice code <span class="code">ACGHDD</span>.</p><a class="btn btn-teal" href="/behavioral-health-care-healow-patient-portal/">Open Portal</a></div>
 <div class="panel reveal"><div class="icw"><div class="ci">{ico("card",24)}</div></div><h3>Pay Your Bill</h3><p class="note">Copays, balances, and financing through CareCredit and Scratchpay.</p><a class="btn btn-teal" href="/behavioral-health-care-payment/">Payment Options</a></div>
 <div class="panel reveal"><div class="icw"><div class="ci">{ico("file",24)}</div></div><h3>Insurance Accepted</h3><p class="note">Medicare, TennCare, Mississippi Medicaid, and most major private plans, explained in plain language.</p><a class="btn btn-teal" href="/insurance/">View Plans</a></div>
</div></div></section>
<section class="mist"><div class="wrap two">
 <div class="panel"><span class="eyebrow">Before Your Visit</span><h3>What to Bring</h3><ul class="ilist">
  <li>{ico("check",18)}<span>Complete your eClinicalWorks check-in link if you receive one by text or email</span></li>
  <li>{ico("check",18)}<span>A photo ID and your insurance card, if you have insurance</span></li>
  <li>{ico("check",18)}<span>A list of your current medications and doses</span></li>
  <li>{ico("check",18)}<span>Any prior records, evaluations, or school reports that may help your provider</span></li>
  <li>{ico("check",18)}<span>For telehealth: a quiet, private space and a charged phone, tablet, or computer</span></li></ul></div>
 <div class="panel deep"><span class="eyebrow gold">Financial Assistance</span><h3>Care for Every Family</h3><p>No one will be denied access to services due to inability to pay. There is a discounted/sliding fee schedule available based on family size and income.</p><p>Ask our front desk about the sliding fee schedule at {PHONE}.</p></div>
</div></section>{CONNECT}'''
page("/patient-center/","Patient Center | Brown Behavioral Health Services","Appointments, patient portal, bill pay, and visit information for patients of Brown Behavioral Health Services.",pc,("Patient Center","Everything you need for your care, in one place.","Patient Center"))

# ---------------- REFERRALS ----------------
REF_ENDPOINT = FORM_ENDPOINT  # see note in README: use a HIPAA-covered form service before go-live
def radios(name, opts, req=False):
    return '<div class="radios">'+"".join(f'<label><input type="radio" name="{name}" value="{o}"{" required" if req and i==0 else ""}> {o}</label>' for i,o in enumerate(opts))+'</div>'
ref = f'''<section><div class="wrap split" style="grid-template-columns:1.6fr 1fr;align-items:start">
<div class="formcard"><h2 style="margin-bottom:6px">Patient Referral Form</h2><p class="note">Fields marked <span class="req" style="color:#b4441c">*</span> are required. Our team will contact the patient to schedule.</p>
<form action="{REF_ENDPOINT}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="New patient referral from brownbehavioral.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{SITE}/thank-you/"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<fieldset><legend>Referring Provider or Agency</legend>
<div class="row"><div><label for="r1">Your Name <span class="req">*</span></label><input id="r1" name="Referring_Name" required></div><div><label for="r2">Organization / Practice <span class="req">*</span></label><input id="r2" name="Referring_Organization" required></div></div>
<div class="row3"><div><label for="r3">Phone <span class="req">*</span></label><input id="r3" type="tel" name="Referring_Phone" required></div><div><label for="r4">Fax</label><input id="r4" type="tel" name="Referring_Fax"></div><div><label for="r5">Email <span class="req">*</span></label><input id="r5" type="email" name="Referring_Email" required></div></div>
<label for="r6">Referral Source Type</label><select id="r6" name="Referral_Source_Type"><option>Physician / Provider Office</option><option>Hospital / Emergency Department</option><option>School / School Counselor</option><option>Court / Probation / Drug Court</option><option>Community Agency</option><option>Employer</option><option>Family Member / Self-Referral</option><option>Other</option></select>
</fieldset>
<fieldset><legend>Patient Information</legend>
<div class="row3"><div><label for="p1">Patient Full Name <span class="req">*</span></label><input id="p1" name="Patient_Name" required></div><div><label for="p2">Date of Birth <span class="req">*</span></label><input id="p2" type="date" name="Patient_DOB" required></div><div><label for="p3">Patient Phone <span class="req">*</span></label><input id="p3" type="tel" name="Patient_Phone" required></div></div>
<div class="row"><div><label for="p4">Parent / Guardian (if under 18)</label><input id="p4" name="Guardian_Name"></div><div><label for="p5">Insurance</label><select id="p5" name="Insurance"><option value="">Select...</option><option>TennCare</option><option>Mississippi Medicaid</option><option>Medicare</option><option>Commercial Insurance</option><option>Self-Pay / Uninsured</option><option>Unknown</option></select></div></div>
</fieldset>
<fieldset><legend>Referral Details</legend>
<label>Services Requested <span class="req">*</span></label>
<div class="radios"><label><input type="checkbox" name="Services[]" value="Psychiatric Evaluation"> Psychiatric Evaluation</label><label><input type="checkbox" name="Services[]" value="Medication Management"> Medication Management</label><label><input type="checkbox" name="Services[]" value="Psychotherapy"> Psychotherapy</label><label><input type="checkbox" name="Services[]" value="ADHD Testing"> ADHD Testing</label><label><input type="checkbox" name="Services[]" value="MAT Program"> MAT Program</label><label><input type="checkbox" name="Services[]" value="DUI School"> DUI School</label><label><input type="checkbox" name="Services[]" value="Primary Care"> Primary Care</label><label><input type="checkbox" name="Services[]" value="Other"> Other</label></div>
<label>Preferred Visit Type</label>{radios("Preferred_Visit",["Bolivar, TN Office","Olive Branch, MS Office","Telehealth","No Preference"])}
<label>Urgency</label>{radios("Urgency",["Routine","Soon (within 2 weeks)","Urgent"])}
<label for="d1">Reason for Referral <span class="req">*</span></label><textarea id="d1" name="Reason_for_Referral" required placeholder="Briefly describe presenting concerns and any relevant history."></textarea>
<label for="d2">Attach Records (optional)</label><input id="d2" type="file" name="attachment" accept=".pdf,.doc,.docx,.jpg,.png">
</fieldset>
<label class="check"><input type="checkbox" name="Consent" value="Confirmed" required> <span>I confirm the patient (or guardian) is aware of and agrees to this referral, and the information provided is accurate to the best of my knowledge.</span></label>
<button class="btn btn-teal" type="submit" style="margin-top:8px">{ico("send",18)} Submit Referral</button></form></div>
<aside class="sidecard"><div class="panel deep"><span class="eyebrow gold">For Referral Partners</span><h3>Thank You for Trusting Us</h3><p>Allow us to help others by sending your referrals. We contact every referred patient promptly to schedule care.</p><ul class="ilist">
<li>{ico("clock",18)}<span>Urgent referrals: please also call {PHONE}</span></li>
<li>{ico("fax",18)}<span>Prefer to fax? Send records to {FAX}</span></li>
<li>{ico("shield",18)}<span>Psychiatric, medical, and recovery services for ages 5 and up</span></li>
<li>{ico("pin",18)}<span>Bolivar, TN, Olive Branch, MS, and telehealth throughout TN and MS</span></li></ul>
<p class="note" style="color:#c9d3e0;margin:14px 0 0">If the patient is in crisis, call 911 or direct them to the 988 Suicide &amp; Crisis Lifeline.</p></div></aside>
</div></section>'''
page("/behavioral-health-care-send-your-referrals/","Send Your Referrals | Brown Behavioral Health Services","Refer a patient to Brown Behavioral Health Services for psychiatric, medical, or recovery care in Tennessee and Mississippi.",ref,("Patient Referrals","Help us extend our reach to people who can benefit from our services.","Referrals"))

# ---------------- CAREERS ----------------
careers = f'''<section><div class="wrap split" style="grid-template-columns:1fr 1.6fr;align-items:start">
<aside class="sidecard"><span class="eyebrow">Careers</span><h2>Join Our Team</h2><p class="lead">Join our team of professionals and share your expertise with those who need your help. Apply now!</p>
<div class="media" style="margin:22px 0"><img src="/images/mental-health-awareness.jpg" alt="The BBHS team at a Mental Health Awareness Month event" style="aspect-ratio:4/3;object-fit:cover"></div>
<div class="panel"><h3>Why BBHS</h3><ul class="ilist">
<li>{ico("check",18)}<span>Mission-driven care for rural and underserved communities</span></li>
<li>{ico("check",18)}<span>Integrated team across behavioral health, primary care, and recovery</span></li>
<li>{ico("check",18)}<span>In-office and telehealth settings in Tennessee and Mississippi</span></li>
<li>{ico("check",18)}<span>Clinical training site partnerships and student rotations</span></li></ul></div>
<p style="margin-top:18px"><a href="/behavioral-health-care-careers/request-for-proposals/">Consultants and vendors: view our Requests for Proposals &rarr;</a></p></aside>
<div class="formcard"><h2 style="margin-bottom:6px">Employment Application</h2><p class="note">Fields marked <span class="req" style="color:#b4441c">*</span> are required.</p>
<form action="{FORM_ENDPOINT}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="New job application from brownbehavioral.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{SITE}/thank-you/"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<fieldset><legend>Your Information</legend>
<div class="row"><div><label for="c1">First Name <span class="req">*</span></label><input id="c1" name="First_Name" required></div><div><label for="c2">Last Name <span class="req">*</span></label><input id="c2" name="Last_Name" required></div></div>
<div class="row3"><div><label for="c3">Email <span class="req">*</span></label><input id="c3" type="email" name="Email" required></div><div><label for="c4">Phone Number <span class="req">*</span></label><input id="c4" type="tel" name="Phone_Number" required></div><div><label for="c5">Cell Number</label><input id="c5" type="tel" name="Cell_Number"></div></div>
<div class="row"><div><label for="c6">City</label><input id="c6" name="City"></div><div><label for="c7">State</label><select id="c7" name="State"><option>Tennessee</option><option>Mississippi</option><option>Other</option></select></div></div>
</fieldset>
<fieldset><legend>Position</legend>
<div class="row"><div><label for="c8">Position Applying For <span class="req">*</span></label><select id="c8" name="Position_Applying_For" required><option value="">Select...</option><option>Psychiatric Mental Health Nurse Practitioner (PMHNP)</option><option>Family Nurse Practitioner (FNP)</option><option>Therapist / Counselor (LCSW, LPC, LMFT, LMSW)</option><option>Registered Nurse (RN)</option><option>Licensed Practical Nurse (LPN)</option><option>Certified Medical Assistant (CMA)</option><option>Front Desk / Patient Services</option><option>Billing / Administrative</option><option>Student Rotation / Internship</option><option>Other</option></select></div>
<div><label for="c9">License or Certification</label><input id="c9" name="License_or_Certification" placeholder="e.g., APRN, LCSW, CMA"></div></div>
<label>Preferred Location</label><div class="radios"><label><input type="checkbox" name="Preferred_Location[]" value="Bolivar, TN"> Bolivar, TN</label><label><input type="checkbox" name="Preferred_Location[]" value="Olive Branch, MS"> Olive Branch, MS</label><label><input type="checkbox" name="Preferred_Location[]" value="Telehealth / Remote"> Telehealth / Remote</label></div>
<label>Availability</label><div class="radios"><label><input type="radio" name="Availability" value="Full-Time"> Full-Time</label><label><input type="radio" name="Availability" value="Part-Time"> Part-Time</label><label><input type="radio" name="Availability" value="PRN"> PRN</label><label><input type="radio" name="Availability" value="Contract (1099)"> Contract (1099)</label></div>
<div class="row"><div><label for="c10">Earliest Start Date</label><input id="c10" type="date" name="Start_Date"></div><div><label for="c11">How did you hear about us?</label><select id="c11" name="How_Heard"><option value="">Select...</option><option>Indeed</option><option>LinkedIn</option><option>School / Clinical Rotation</option><option>Employee Referral</option><option>Social Media</option><option>Other</option></select></div></div>
</fieldset>
<fieldset><legend>Resume and Message</legend>
<label for="c12">Attach Resume <span class="req">*</span></label><input id="c12" type="file" name="attachment" accept=".pdf,.doc,.docx" required>
<label for="c13">Message</label><textarea id="c13" name="Message" placeholder="Tell us about your experience and what draws you to BBHS."></textarea>
</fieldset>
<button class="btn btn-teal" type="submit">{ico("brief",18)} Submit Application</button></form></div>
</div></section>'''
page("/behavioral-health-care-careers/","Careers | Brown Behavioral Health Services","Join the team at Brown Behavioral Health Services. Apply online for clinical and administrative positions in Tennessee and Mississippi.",careers,("Careers","Join our team of professionals and share your expertise with those who need your help.",'<a href="/behavioral-health-care-about-us/">About</a> / Careers'))

# ---------------- INSURANCE ----------------
# Each group: (eyebrow, title, intro, [(plan, plain-language explanation, also-known-as)])
INS_GROUPS = [
 ("Medicare","Medicare and Medicare Advantage",
  "Medicare is federal health insurance for people 65 and older and for some younger people with disabilities. Medicare Advantage plans are Medicare plans offered by private companies.",
  [("Original Medicare","The red, white, and blue Medicare card from the federal government. Covers people 65 and older and some people with disabilities.","Medicare Part B"),
   ("Railroad Medicare","Medicare for retired railroad workers and their families. Your card will say &ldquo;Railroad Retirement Board.&rdquo;","RRB Medicare"),
   ("Dual Special Needs Plans (D-SNP)","Medicare Advantage plans for people who have <b>both</b> Medicare and Medicaid (TennCare or Mississippi Medicaid).","D-SNP, Dual Eligible plans"),
   ("BlueCare Plus","A BlueCross BlueShield of Tennessee plan for people who have both Medicare and TennCare.","BlueCare Plus (HMO D-SNP)"),
   ("Wellcare","Medicare Advantage and Medicare prescription plans offered by Centene.","A Centene company"),
   ("Cigna Healthspring","Cigna&rsquo;s Medicare Advantage plans.",""),
   ("Humana","Medicare Advantage plans, plus employer and individual plans.",""),
   ("Devoted Health","A Medicare Advantage plan for people with Medicare.","Devoted")]),
 ("Tennessee Medicaid","TennCare",
  "TennCare is Tennessee&rsquo;s Medicaid program for eligible children, families, pregnant women, and adults. TennCare members choose or are assigned a health plan, and the plan name appears on your card.",
  [("BlueCare Tennessee","A TennCare health plan offered by BlueCross BlueShield of Tennessee.","BlueCare"),
   ("TennCare Select","A TennCare plan mainly for children in state custody and some children with special health care needs.","Offered by BlueCross BlueShield of Tennessee"),
   ("Wellpoint","A TennCare health plan, formerly called Amerigroup. Wellpoint also offers Medicare and other plans.","Formerly Amerigroup"),
   ("UnitedHealthcare Community Plan","A TennCare health plan offered by UnitedHealthcare.","UHC Community Plan")]),
 ("Mississippi Medicaid","Mississippi Medicaid",
  "Mississippi Medicaid covers eligible children, families, pregnant women, and adults. Many members are enrolled in a MississippiCAN or CHIP health plan, and the plan name appears on your card.",
  [("Magnolia Health","A Mississippi Medicaid (MississippiCAN and CHIP) health plan.","A Centene company"),
   ("Molina Healthcare","A Mississippi Medicaid (MississippiCAN and CHIP) health plan. Molina also offers Marketplace plans.","Molina"),
   ("TrueCare","A Mississippi Medicaid (MississippiCAN) health plan.","TrueCare Mississippi")]),
 ("Private Insurance","Employer, Individual, and Marketplace Plans",
  "These are plans you get through a job, buy on your own, or purchase through the Health Insurance Marketplace (HealthCare.gov).",
  [("UnitedHealthcare","Employer, individual, and Medicare Advantage plans from UnitedHealth Group, including UMR and Optum behavioral health plans.","UnitedHealth Group, UHC, UMR, Optum"),
   ("BlueCross BlueShield of Tennessee","Employer and individual plans for Tennessee residents.","BCBST"),
   ("BlueCross BlueShield of Mississippi","Employer and individual plans for Mississippi residents.","BCBSMS"),
   ("BlueAdvantage","BlueCross BlueShield of Tennessee&rsquo;s Medicare Advantage plan.","BCBST Medicare Advantage"),
   ("BlueCard (Out-of-State Blue Plans)","BlueCross BlueShield plans from other states, accepted through the national BlueCard program. Look for the suitcase logo on your card.","BlueCard"),
   ("BCBS Federal Employee Program","BlueCross BlueShield coverage for federal employees, retirees, and their families.","FEP Blue"),
   ("Aetna","Employer, individual, and Medicare Advantage plans from CVS Health.","CVS Health"),
   ("Cigna","Employer and individual plans.","Cigna and Evernorth"),
   ("Ambetter","Individual and family plans sold on the Health Insurance Marketplace.","A Centene company"),
   ("Oscar","Individual and family plans sold on the Health Insurance Marketplace.","Oscar Health"),
   ("Alliant Health Plans","Individual, family, and employer plans.","Alliant")]),
 ("Additional Coverage","Other Plans We Accept",
  "We also work with these plans and behavioral health networks.",
  [("TRICARE","Health coverage for active-duty service members, retirees, and their families.",""),
   ("Anthem","Employer and individual plans.",""),
   ("Carelon Behavioral Health","A behavioral health network that manages mental health benefits for some plans.","Formerly Beacon Health Options"),
   ("Magellan","A behavioral health network that manages mental health benefits for some plans.","Magellan Healthcare")]),
]
ORDER = [3,0,1,2,4]  # Private first, then Medicare, TennCare, MS Medicaid, Other
SHORT = {3:"Commercial &amp; Marketplace",0:"Medicare &amp; Medicare Advantage",1:"TennCare (TN Medicaid)",2:"Mississippi Medicaid",4:"Other Plans"}
def ins_lists():
    ICONS={3:"brief",0:"shield",1:"heart",2:"heart",4:"check"}
    cols="".join(f'<div class="inscard reveal"><div class="inshead"><span class="insic">{ico(ICONS[k],20)}</span><h3>{SHORT[k]}</h3></div><ul>{"".join(f"<li>{ico(chr(99)+chr(104)+chr(101)+chr(99)+chr(107),15)}<span>{p}</span></li>" for p,_,_ in INS_GROUPS[k][3])}</ul></div>' for k in ORDER)
    return f'<div class="inscols">{cols}</div>'
def ins_explain():
    out=[]
    for k in ORDER:
        eb,title,intro,plans=INS_GROUPS[k]
        rows="".join(f'<li><b>{p}:</b> {d}</li>' for p,d,_ in plans)
        out.append(f'<details class="faq"><summary>{SHORT[k]}: what these plans are</summary><p>{intro}</p><ul>{rows}</ul></details>')
    return "".join(out)
ins = f'''<section style="padding-top:56px;padding-bottom:40px"><div class="wrap">
<p class="lead" style="margin-bottom:26px">We accept the plans below at our Bolivar, TN and Olive Branch, MS offices and by telehealth. Don&rsquo;t see your plan? Call <a href="{PHONE_LINK}">{PHONE}</a> and we will check for you.</p>
{ins_lists()}
</div></section>
<section class="mist" style="padding:56px 0"><div class="wrap two" style="align-items:start">
<div><span class="eyebrow">Plain-Language Guide</span><h2>Not Sure What Your Plan Is?</h2><p>Look at the front of your insurance card. In Tennessee, Medicaid is called <b>TennCare</b>. In Mississippi, Medicaid plans are often called <b>MississippiCAN</b>. If you have both Medicare and Medicaid, you may be in a <b>D-SNP</b> or <b>BlueCare Plus</b> plan. Tap a group to learn more.</p>
<div class="panel" style="padding:22px;margin-top:18px"><p style="margin:0"><b>No insurance?</b> No one will be denied access to services due to inability to pay. A sliding fee schedule, CareCredit, and Scratchpay are available. <a href="/behavioral-health-care-payment/">Payment options &rarr;</a></p><p class="note" style="margin:10px 0 0">Self-pay programs (DOT physicals, Slim Program, DUI School, and MS medical card certification) are not billed to insurance.</p></div></div>
<div>{ins_explain()}</div>
</div></section>'''
page("/insurance/","Insurance Accepted | Brown Behavioral Health Services","Brown Behavioral Health Services accepts Medicare, Railroad Medicare, D-SNP plans, TennCare (BlueCare, TennCare Select, Wellpoint), Mississippi Medicaid (Magnolia, Molina, TrueCare), and major commercial and Marketplace plans.",ins,("Insurance Accepted","Medicare, TennCare, Mississippi Medicaid, and major private plans, explained in plain language.",'<a href="/patient-center/">Patients</a> / Insurance'))

# ---------------- FUNDING ----------------
# Set show=True only after the award may be announced publicly.
GRANTS = [
 dict(show=True, state="Tennessee", funder="Tennessee Department of Health", program="Healthcare Rural Resiliency Program", amount="$3,577,860", term="2025 to 2028",
      body="Expands primary care, mental health, and substance use services in Hardeman County, Tennessee, including a mobile medical unit serving communities across the county, school-based telehealth, behavioral health services for Whiteville Correctional Facility, remote patient monitoring, added licensed counselors, and an annual Rural Health Fair each October.",
      highlights=["Hosted the Rural Community Health Fair in Bolivar (July 2026): 578 attendees and 227 children and adolescents screened for depression, anxiety, and substance use",
                  "Mobile clinic services and screenings across Hardeman County",
                  "Presented on the HRP panel at the West Tennessee Regional Health Council (August 2026)",
                  "Trained staff in addiction and psychiatric medication treatment (August 2026)",
                  "Opened a third location through a University of Memphis partnership (September 2026)",
                  "Advanced suicide prevention and pediatric care through TSPN and the Cumberland Pediatric Foundation"]),
 dict(show=True, state="Tennessee", funder="Tennessee Department of Health", program="Creating Healthier Rural Communities Through the End Zone for Chronic Disease Prevention: The Blue Plate Project", amount="$1,500,000", term="2026 to 2030",
      body="A community food access and chronic disease prevention initiative in Hardeman County featuring a community garden, a food pantry network serving Bolivar, Hickory Valley, Whiteville, Toone, and Grand Junction, and recurring nutrition and chronic disease education classes."),
 dict(show=True, state="Mississippi", funder="Mississippi State Department of Health, Rural Health Transformation Program", program="Workforce Expansion Initiative: Project MENTOR MS", amount="$448,140", term="2026 to 2027",
      body="Builds the rural behavioral health workforce in North Mississippi through preceptor development, clinical rotations for students, apprenticeships, and mobile clinic training sites in Marshall, Tate, Benton, Alcorn, and Tippah counties."),
 dict(show=True, state="Tennessee", funder="Tennessee Department of Health", program="Perinatal Behavioral Health Workforce Development: BLOOM Perinatal Fellowship", amount="$43,000", term="2026",
      body="Supports supervision, training, and specialty certification for clinicians serving mothers and families during the perinatal period."),
 dict(show=True, state="National", funder="National Rural Health Resource Center, funded by HRSA&rsquo;s Federal Office of Rural Health Policy", program="Rural Healthcare Provider Transition Project", amount="National Selection", term="2026 to 2027",
      body="BBHS was one of five organizations selected nationally to receive technical assistance that prepares rural providers for value-based care."),
 dict(show=True, state="Tennessee", funder="Good Sports", program="Youth Sports Equipment Grant: Center of Integrated Health", amount="In-Kind Award", term="2026 to 2028",
      body="Provides new sports equipment, apparel, and footwear for youth sports programs serving Hardeman County schools, awarded to <a href=\"/center-of-integrated-health/\">Center of Integrated Health</a>, the nonprofit founded by Dr. Avanti Cross-Brown."),
]
def hl(g):
    if not g.get("highlights"): return ""
    return '<p class="aka" style="margin-top:16px">2026 Highlights</p><ul class="hl">'+"".join(f'<li>{ico("check",15)}<span>{x}</span></li>' for x in g["highlights"])+'</ul>'
def grant_cards():
    out=[]
    for g in [g for g in GRANTS if g["show"]]:
        out.append(f'''<article class="formcard reveal" style="padding:30px;margin-bottom:22px;display:grid;grid-template-columns:220px 1fr;gap:30px;align-items:start">
<div><span class="eyebrow">{g["state"]}</span><div style="font-family:var(--serif);font-size:2rem;color:var(--deep);line-height:1.1">{g["amount"]}</div><p class="note" style="margin:6px 0 0">{g["term"]}</p></div>
<div><p class="note" style="margin:0 0 4px;color:var(--teal);font-weight:600">{g["funder"]}</p><h3>{g["program"]}</h3><p style="margin:0">{g["body"]}</p>{hl(g)}</div></article>''')
    return "".join(out)
funding = f'''<section><div class="wrap split" style="grid-template-columns:1fr 1.7fr;align-items:start">
<aside class="sidecard"><span class="eyebrow">Investing in Rural Health</span><h2>Public Partnerships That Expand Access</h2><p class="lead">Public funding allows Brown Behavioral Health Services to reach more patients, grow our workforce, and bring care directly into rural communities across Tennessee and Mississippi.</p>
<div class="panel deep" style="margin-top:20px"><h3>Funding Acknowledgment</h3><p style="margin:0">Programs described on this page are supported in whole or in part by the funding agencies listed. The contents are the responsibility of Brown Behavioral Health Services, PLLC and do not necessarily represent the official views of the funding agencies.</p></div>
<p class="note" style="margin-top:18px">For funding partnerships or program inquiries, contact <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE}.</p></aside>
<div>{grant_cards()}</div>
</div></section>
<section class="mist"><div class="wrap center"><span class="eyebrow">Partner With Us</span><h2>Collaborating for Healthier Communities</h2><p class="lead">We welcome partnerships with schools, health systems, community organizations, and funders who share our commitment to rural health.</p><a class="btn btn-teal" href="/behavioral-health-care-contact-us/">Contact Our Team</a></div></section>'''
page("/funding/","Funding | Brown Behavioral Health Services","State funding supporting rural behavioral health, primary care, workforce, and chronic disease prevention programs at Brown Behavioral Health Services.",funding,("Funding","Public investment that expands access to care in rural Tennessee and Mississippi.",'<a href="/behavioral-health-care-about-us/">About</a> / Funding'))

# ---------------- NONPROFIT ----------------
COI_EMAIL = EMAIL  # replace with the Center's own email when provided
COI_SVCS = [
 ("heart","Youth Sports and Wellness","A youth sports program serving Hardeman County students for five years, equipped through a Good Sports in-kind award so cost is never a barrier to playing."),
 ("brain","Youth Mental Health","Wellness education and mental health support for young people, coordinated with Brown Behavioral Health Services."),
 ("shield","Free Care for Uninsured Patients","Helping uninsured neighbors access behavioral health and primary care through Brown Behavioral Health Services."),
 ("video","Mobile Health Outreach","Bringing screenings, education, and care to rural communities through the Brown Behavioral Health Services Mobile Health Clinic."),
 ("portal","School-Based Health and Telehealth","Supporting school health programs and school-based telehealth so students can get care without leaving campus."),
 ("check","Community Health Fairs and Screenings","Free health fairs and mental health screenings that connect families with care, benefits, and local resources."),
 ("leaf","Food Access and Nutrition","Community food access, gardens, and nutrition education that support chronic disease prevention."),
 ("life","Substance Use Recovery Support","Recovery resources, education, and peer support that complement addiction treatment and help people stay well."),
 ("pin","Reentry and Correctional Health Support","Supporting people returning home from incarceration with connections to health care, recovery, and community resources."),
]
coi_cards="".join(f'<div class="panel reveal"><div class="icw"><div class="ci">{ico(ic,24)}</div></div><h3>{t}</h3><p class="note" style="margin:0">{d}</p></div>' for ic,t,d in COI_SVCS)
coi = f'''<div class="coi">
<section class="phero"><div class="wrap"><div class="crumbs"><a href="/">Home</a> / <a href="/behavioral-health-care-about-us/">About</a> / Center of Integrated Health</div><h1>Center of Integrated Health</h1><p>Our 501(c)(3) nonprofit partner, extending care and opportunity to rural communities.</p></div></section>
<section><div class="wrap split">
<div><span class="eyebrow">Our Nonprofit Partner</span><h2>Center of Integrated Health</h2>
<p class="lead">Center of Integrated Health is a Tennessee nonprofit and 501(c)(3) public charity founded by Dr. Avanti Cross-Brown to extend health, wellness, and opportunity to rural and underserved families beyond the walls of the clinic.</p>
<p>Working hand in hand with Brown Behavioral Health Services, the Center pursues grants, community partnerships, and charitable support for programs that strengthen youth, families, and communities across West Tennessee and North Mississippi.</p>
<ul class="chips" style="margin-top:18px"><li>501(c)(3) Public Charity</li><li>Founded 2023</li><li>Bolivar, Tennessee</li></ul>
<p style="margin-top:18px"><b>Founder and Executive Director:</b> Dr. Avanti Cross-Brown, APRN, DNP, PMHNP-BC, CARN-AP, NRCME</p></div>
<div class="media"><img src="/images/mental-health-awareness.jpg" alt="Community members and BBHS team during a Mental Health Awareness Month event" style="aspect-ratio:4/3;object-fit:cover;width:100%"></div>
</div></section>
<section class="mist"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">What We Do</span><h2 style="margin:0">Programs and Services</h2></div><p class="lead">Delivered in partnership with Brown Behavioral Health Services.</p></div>
<div class="cards three" style="margin-top:0">{coi_cards}</div></div></section>
<section><div class="wrap"><div class="panel deep" style="display:grid;grid-template-columns:1.4fr 1fr;gap:26px;align-items:center">
<div><span class="eyebrow gold">Get Involved</span><h2 style="color:#fff;margin-bottom:8px">Partner, Volunteer, or Give</h2><p style="margin:0">We welcome partnerships with funders, schools, faith communities, and local organizations who share our commitment to healthier rural communities. Center of Integrated Health is a 501(c)(3) public charity, and contributions may be tax-deductible as allowed by law.</p></div>
<div style="text-align:right"><a class="btn btn-gold" href="mailto:{COI_EMAIL}?subject=Center%20of%20Integrated%20Health">Contact the Center</a><p class="note" style="color:#f3e3d6;margin:12px 0 0">{COI_EMAIL} &middot; {PHONE}</p></div>
</div></div></section>
</div>'''
page("/center-of-integrated-health/","Center of Integrated Health | Nonprofit Partner of Brown Behavioral Health Services","Center of Integrated Health is a 501(c)(3) nonprofit founded by Dr. Avanti Cross-Brown, supporting youth, families, and rural communities in partnership with Brown Behavioral Health Services.",coi)

# ---------------- RFP ----------------
rfp = f'''<section><div class="wrap" style="max-width:900px"><div class="prose">
<div class="alert" style="margin-bottom:24px"><b>Status: Closed.</b> This Request for Proposal closed on July 8, 2025, and is no longer accepting submissions. Future opportunities will be posted on this page.</div><span class="eyebrow">Request for Proposal (RFP)</span><h2 style="margin-top:0">Technical Assistance and Evaluation Advisor: Brown Behavioral Health Services</h2>
<h3>Overview</h3>
<p>The mission of Brown Behavioral Health Services (BBHS) is to provide proficient and competent care related to diagnosing and treating psychiatric illnesses in pediatrics and adults while improving overall health status. BBHS is committed to the mental health population and is eager to serve everyone holistically while enhancing mental health awareness, promoting individual empowerment, and increasing access to treatment and services for people living with mental illnesses.</p>
<p>Brown Behavioral Health&rsquo;s Bolivar location received Rural Health Clinic status by the Centers for Medicare and Medicaid Services (CMS) in April 2025. At the same time, BBHS was awarded a Rural Health Resiliency grant from the Tennessee Department of Health to expand primary and behavioral health services in Hardeman County, Tennessee. We are looking for a technical assistance partner who can help us build a solid foundation by supporting adoption of our new Electronic Health Record (EHR) eClinicalWorks, build workflows and automation between our Office Manager and back-office billing and coding provider, and analyze our patient population needs and service offerings.</p>
<h3>Project Goals</h3><ul><li>Establish baseline patient and service line data;</li><li>Deliver integrated, high-quality, comprehensive prevention and healthcare services;</li><li>Develop innovative delivery models that are evidence informed;</li><li>Improve access to primary and mental health care in Hardeman County;</li><li>Support an increase of staffing to offer additional services;</li><li>Establish referral agreements with outside agencies such as Hardeman County Schools, West Tennessee Healthcare - Bolivar, and others as may be needed.</li><li>Establish a mobile unit that will be self-sustained by the end of the grant period</li></ul>
<h3>Expected Outcomes</h3><ul><li>Development of workflows between providers, partners, and mobile unit</li><li>Tracking of clinical outcomes such as reductions in mental health symptoms, substance abuse treatment adherence, etc.</li><li>Support training new staff in the use of EHR, QuickBooks, and/or specific service lines</li><li>Prepare a comprehensive report at the end of the grant period.</li></ul>
<h3>Project Timeline</h3><p>August 2025 to June 2026; Follow-up report Fall 2027</p>
<h3>RFP Requirements and Submission Guidelines</h3><ul><li>Interested administrators should have demonstrated experience working with federally designated Rural Health Clinics and/or Mental and Behavioral Health Services</li><li>Ideal firm will have its own data management platform (as opposed to engaging an additional/separate vendor)</li><li>Proposals should be addressed to Dr. Avanti Cross-Brown and Destiny Shaw and submitted to <a href="mailto:{EMAIL}">{EMAIL}</a> by Friday, July 8, 2025, 12 pm Central.</li><li>Brown Behavioral Health Services will notify the selected technical assistance partner by Friday, July 25, 2025.</li></ul>
</div></div></section>'''
page("/behavioral-health-care-careers/request-for-proposals/","Request for Proposals | Brown Behavioral Health Services","RFP: Technical Assistance and Evaluation Advisor for Brown Behavioral Health Services.",rfp,("Request for Proposals","Technical Assistance and Evaluation Advisor",'<a href="/behavioral-health-care-careers/">Careers</a> / Request for Proposals'))

# ---------------- CONTACT ----------------
contact = f'''<section><div class="wrap">
<div class="three" style="margin-bottom:40px">
 <div class="panel"><span class="eyebrow">{ico("phone",16)} Call</span><h3><a href="{PHONE_LINK}" style="text-decoration:none">{PHONE}</a></h3><p class="note" style="margin:0">Fax: {FAX}</p></div>
 <div class="panel"><span class="eyebrow">{ico("mail",16)} Email</span><h3 style="font-size:1.05rem;word-break:break-all"><a href="mailto:{EMAIL}" style="text-decoration:none">{EMAIL}</a></h3><p class="note" style="margin:0">We will respond as soon as possible.</p></div>
 <div class="panel"><span class="eyebrow">{ico("pin",16)} Our Offices</span><p style="margin:0"><b>793 Tennessee Street</b><br>Bolivar, TN 38008<br><b>9851 Hwy 178, Suite B</b><br>Olive Branch, MS 38654<br>Telehealth throughout TN and MS</p></div>
</div>
<div class="split" style="align-items:start"><div class="panel"><h2>Contact Us Form</h2><p class="note">* Required Information</p>{contact_form("New message from brownbehavioral.com (contact page)")}</div>
<iframe class="map" src="{MAP}" title="Map of Bolivar, TN" loading="lazy" style="height:640px"></iframe></div></div></section>'''
page("/behavioral-health-care-contact-us/","Contact Us | Brown Behavioral Health Services","Contact Brown Behavioral Health Services. Phone 731-228-9068, fax 901-425-9773, contact@brownbehavioral.com.",contact,("Contact Us","Do you need help? Reach out to us anytime.","Contact Us"))

# ---------------- PRIVACY ----------------
priv = f'''<section><div class="wrap prose" style="max-width:860px">
<p><b>Effective Date: March 2024. Last Updated: November 2026</b></p>
<p>Welcome to Brown Behavioral Health Services (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;). We are committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, share, and safeguard your data when you use our services. By using our services, you consent to the practices described in this Privacy Policy.</p>
<h2>Information We Collect</h2><p>We may collect the following types of information when you use our website or contact us:</p><ul>
<li><b>Personal Information:</b> We may collect personal information, including your name, email address, phone number, and business information when you submit a form, request an appointment, or otherwise communicate with us.</li>
<li><b>Payment Information:</b> We may collect payment data for purchases, orders, or service requests, including valid credit card numbers, brands, and expiration dates. We store only very limited, if any, payment information (e.g. payment accounts, bank accounts, credit cards, or cheques) that we collect. Otherwise, all financial information is stored by our payment processor, and you are encouraged to review their privacy policy and contact them directly for responses to your questions.</li>
<li><b>Form Submissions:</b> Information you choose to provide through our contact, referral, and careers forms, including any files you attach.</li>
<li><b>Technical Information:</b> We collect information related to your website&rsquo;s usage, such as IP addresses, browser type, and access times.</li>
<li><b>Cookies and Tracking Technologies:</b> We use cookies and similar technologies to track user behavior on our website. You can manage your cookie preferences through your browser settings.</li></ul>
<h2>How We Use Your Information</h2><p>We use your information for the following purposes:</p><ul>
<li><b>Providing Care and Services:</b> We use the information you provide to respond to appointment requests, referrals, and employment applications.</li>
<li><b>Communication:</b> We use your contact information to respond to your inquiries, provide support, and keep you informed about your request.</li>
<li><b>Improvement of Services:</b> We may use your website usage data to enhance and optimize our services and user experience.</li>
<li><b>Legal Compliance:</b> We process your data to comply with legal obligations and protect our rights.</li></ul>
<h2>How We Share Your Information</h2><p>No mobile information will be shared with third parties/affiliates for marketing/promotional purposes. All other categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.</p>
<ul><li><b>Service Providers and Legal Requirements:</b> We may disclose your information if required by law or to protect and ensure your safety and our rights, privacy, safety, or property.</li></ul>
<h2>Your Health Information</h2><p>Protected health information you share as a patient is handled in accordance with HIPAA and our Notice of Privacy Practices, which is available at our offices or upon request. Please do not send private medical details through our general contact form.</p>
<h2>Security of Your Information</h2><p>We take appropriate measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction. We use encryption, access controls, and regular security assessments to safeguard your data.</p>
<h2>Your Choices and Rights</h2><ul><li><b>Access and Correction:</b> You have the right to access and correct your personal information. You can do this by contacting us at {PHONE}.</li><li><b>Opt-Out:</b> You can opt out of receiving promotional communications from us at any time by following the instructions provided in the communication.</li></ul>
<h2>Changes to this Privacy Policy</h2><p>We may update this Privacy Policy from time to time to reflect changes in our practices or for legal reasons. We will notify you of any significant changes via email or a notice on our website.</p>
<h2>Contact Us</h2><p>If you have any questions or concerns regarding this Privacy Policy, please contact us at {PHONE}.</p>
<div class="alert"><b>Disclaimer:</b> By providing a telephone number and submitting the form you are consenting to be contacted by SMS text message. Message and data rates may apply. Reply STOP to opt out of further messaging. Phone numbers we collect and the consent we received will not be shared with 3rd-party providers.</div>
</div></section>'''
page("/privacy-policy/","Privacy Policy | Brown Behavioral Health Services","Privacy Policy for Brown Behavioral Health Services.",priv,("Privacy Policy","","Privacy Policy"))

# ---------------- SITEMAP + THANK YOU + 404 ----------------
links = [("Home","/"),("About Us","/behavioral-health-care-about-us/"),("Meet Our Professionals","/behavioral-health-care-meet-our-professionals/"),("Services","/behavioral-health-care-services/"),("Psychiatric Evaluation","/behavioral-health-care-psychiatric-evaluation/"),("Medical Services","/behavioral-health-care-medical-services/"),("Patient Center","/patient-center/"),("Request an Appointment","/behavioral-health-request-an-appointment/"),("Patient Portal (eClinicalWorks / healow)","/behavioral-health-care-healow-patient-portal/"),("Insurance Accepted","/insurance/"),("Payment Options","/behavioral-health-care-payment/"),("Funding","/funding/"),("Center of Integrated Health","/center-of-integrated-health/"),("Send Your Referrals","/behavioral-health-care-send-your-referrals/"),("Careers","/behavioral-health-care-careers/"),("Request for Proposals","/behavioral-health-care-careers/request-for-proposals/"),("Contact Us","/behavioral-health-care-contact-us/"),("Privacy Policy","/privacy-policy/")]
page("/sitemap/","Sitemap | Brown Behavioral Health Services","All pages on brownbehavioral.com.",f'<section><div class="wrap"><ul class="svc">{"".join(f"<li><a href={chr(34)}{h}{chr(34)}>{t}</a></li>" for t,h in links)}</ul></div></section>',("Sitemap","","Sitemap"))
page("/thank-you/","Thank You | Brown Behavioral Health Services","Thank you for contacting Brown Behavioral Health Services.",f'<section><div class="wrap center" style="max-width:700px"><h2>Thank you!</h2><p class="lead">Your submission has been received. Our team will get back to you as soon as possible.</p><p>If this is an emergency, please call 911.</p><a class="btn btn-teal" href="/">Back to Home</a></div></section>',("Thank You","","Thank You"))
page("/404/","Page Not Found | Brown Behavioral Health Services","Page not found.",f'<section><div class="wrap center"><h2>Sorry, we could not find that page.</h2><p class="lead">Try one of the links in the menu, or call us at {PHONE}.</p><a class="btn btn-teal" href="/">Back to Home</a></div></section>',("Page Not Found","","404"))
os.replace("404/index.html","404.html"); os.rmdir("404")

with open("sitemap.xml","w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{h}</loc></url>" for _,h in links)+"</urlset>\n")
with open("robots.txt","w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
# CNAME is added at launch: with open("CNAME","w") as f: f.write("www.brownbehavioral.com\n")
print("Built.")
