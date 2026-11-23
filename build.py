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
     "life":'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.9 4.9 4.3 4.3M14.8 14.8l4.3 4.3M14.8 9.2l4.3-4.3M4.9 19.1l4.3-4.3"/>',
    }[name]
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

NAV = [
 ("Home","/",None),
 ("About",None,[("About Us","/behavioral-health-care-about-us/"),("Meet Our Professionals","/behavioral-health-care-meet-our-professionals/")]),
 ("Services",None,[("Behavioral Health Services","/behavioral-health-care-services/"),("Psychiatric Evaluation","/behavioral-health-care-psychiatric-evaluation/"),("Medical Services","/behavioral-health-care-medical-services/"),("MS Medical Card Certification","/docs/MS-Cannabis-Certification.pdf")]),
 ("Patients",None,[("Request an Appointment","/behavioral-health-request-an-appointment/"),("Healow Patient Portal","/behavioral-health-care-healow-patient-portal/"),("Payment Options","/behavioral-health-care-payment/"),("Send Your Referrals","/behavioral-health-care-send-your-referrals/")]),
 ("Careers",None,[("Join Our Team","/behavioral-health-care-careers/"),("Request for Proposals","/behavioral-health-care-careers/request-for-proposals/")]),
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
  <p><b>If you have an emergency or need immediate assistance, please call 911.</b> The Tennessee Statewide Crisis Line, available 24 hours a day, 365 days a year, is a free resource for anyone experiencing a mental health crisis. All calls are routed to a trained crisis counselor in your area, who will provide support and guidance and work to connect you with appropriate community supports.</p>
  <div class="nums"><a href="tel:18552747471">TN Crisis Line: 1-855-CRISIS-1 (1-855-274-7471)</a><a href="tel:988">988 Suicide &amp; Crisis Lifeline (formerly 1-800-273-TALK)</a></div>
</div></div>
<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div><a class="brand" href="/" style="color:#fff"><img src="/images/logo-270.png" alt="" width="58" height="58"><span><b style="color:#fff">Brown Behavioral<br>Health Services, PLLC</b></span></a>
      <p style="margin-top:16px">If you need our services or want to learn more, you can reach out to us anytime.</p>
      <div class="fee"><b>No one will be denied access to services due to inability to pay.</b> There is a discounted/sliding fee schedule available based on family size and income.</div>
      <div class="social"><a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{ico("fb",18)}</a><a href="{PSYTODAY}" target="_blank" rel="noopener" aria-label="Psychology Today profile">{ico("user",18)}</a></div>
    </div>
    <div><h4>Navigation</h4><ul><li><a href="/">Home</a></li><li><a href="/behavioral-health-care-about-us/">About Us</a></li><li><a href="/behavioral-health-care-meet-our-professionals/">Meet Our Professionals</a></li><li><a href="/behavioral-health-care-services/">Services</a></li><li><a href="/behavioral-health-care-medical-services/">Medical Services</a></li><li><a href="/behavioral-health-care-careers/">Careers</a></li><li><a href="/behavioral-health-care-contact-us/">Contact Us</a></li></ul></div>
    <div><h4>Patients</h4><ul><li><a href="/behavioral-health-request-an-appointment/">Request an Appointment</a></li><li><a href="/behavioral-health-care-healow-patient-portal/">Healow Patient Portal</a></li><li><a href="/behavioral-health-care-payment/">Payment Options</a></li><li><a href="{REFERRAL}" target="_blank" rel="noopener">Referral Form</a></li><li><a href="/sitemap/">Sitemap</a></li></ul></div>
    <div><h4>Contact Information</h4><ul>
      <li><b style="color:#fff">Service Areas:</b> Accept patients in the State of Tennessee and Mississippi</li>
      <li>Bolivar, TN 38008<br>Olive Branch, MS 38654</li><li>Also Offer Telehealth Visits</li>
      <li>Phone: <a href="{PHONE_LINK}">{PHONE}</a><br>Fax: {FAX}<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
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
home = f'''
<section class="hero"><div class="slides">
  <img class="on" src="/images/slider-1.jpg" alt="man listening to his psychiatrist">
  <img src="/images/slider-2.jpg" alt="medical personnel and a woman chatting" loading="lazy">
  <img src="/images/slider-3.jpg" alt="medical personnel comforting a woman" loading="lazy">
  <img src="/images/slider-4.jpg" alt="man sharing in front of the group" loading="lazy">
  <img src="/images/slider-5.jpg" alt="mother and her daughter listening to the psychiatrist" loading="lazy">
</div><div class="wrap">
  <span class="pill">{ico("video",16)} In-person in Bolivar, TN and Olive Branch, MS, plus telehealth</span>
  <h1>One Small Crack Does Not Mean You&rsquo;re Broken.</h1>
  <p>Let us help you restore and improve your lives with our help and expertise.</p>
  <div class="actions"><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">{ico("cal",18)} Request an Appointment</a><a class="btn btn-ghost" href="/behavioral-health-care-about-us/">Find Out More</a></div>
</div></section>

<div class="quick"><div class="wrap"><div class="grid">
  <a class="qcard" href="/behavioral-health-request-an-appointment/"><span class="ic">{ico("cal")}</span><span><b>Request an Appointment</b><span>Book online, any time</span></span></a>
  <a class="qcard" href="/behavioral-health-care-healow-patient-portal/"><span class="ic">{ico("portal")}</span><span><b>Healow Patient Portal</b><span>Records, messages and more</span></span></a>
  <a class="qcard" href="/behavioral-health-care-payment/"><span class="ic">{ico("card")}</span><span><b>Payment Options</b><span>CareCredit and Scratchpay</span></span></a>
  <a class="qcard" href="{REFERRAL}" target="_blank" rel="noopener"><span class="ic">{ico("send")}</span><span><b>Referral Form</b><span>Send us a referral</span></span></a>
</div></div></div>

<section><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Welcome to</span><h2>Brown Behavioral Health Services, PLLC</h2>
    <p class="lead">It is our duty to provide support and advocacy for individuals and families to help promote healthy mental well-being.</p>
    <p>There are many treatment options available for those seeking care for themselves or a loved one who may be experiencing everyday challenges or suffering from mental health concerns. Let us be your first choice.</p>
    <ul class="chips" style="margin:22px 0 28px"><li>Ages 5 and up</li><li>Tennessee &amp; Mississippi</li><li>Telehealth visits</li><li>Sliding fee scale</li></ul>
    <a class="btn btn-teal" href="/behavioral-health-care-about-us/">Find Out More</a></div>
  <div class="media arch reveal"><img src="/images/main-img.png" alt="psychiatrist comforting her emotional client"><div class="badge-float"><b>Let&rsquo;s Get Started</b>Begin your journey with us now.</div></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="center"><span class="eyebrow">What We Offer</span><h2>Care Designed Around You</h2><p class="lead">Our behavioral health care services are available for individuals aging 5 and up.</p></div>
  <div class="cards">
    <div class="card reveal"><img src="/images/btm1-box0.jpg" alt="cannabis" loading="lazy"><div class="body"><h3>Medical Card Certification</h3><p>Get certification for MS Cannabis.</p><a class="more" href="/docs/MS-Cannabis-Certification.pdf">Click Here</a></div></div>
    <div class="card reveal"><img src="/images/btm1-box1.jpg" alt="medical personnel giving medicine to a woman" loading="lazy"><div class="body"><h3>Medication Management</h3><p>Let us help manage your medications and their effectiveness.</p><a class="more" href="/behavioral-health-care-services/#medication-management">Click Here</a></div></div>
    <div class="card reveal"><img src="/images/btm1-box2.jpg" alt="parents comforting their daughter" loading="lazy"><div class="body"><h3>Psychiatric Evaluation</h3><p>Schedule an evaluation to understand your cognitive status.</p><a class="more" href="/behavioral-health-care-psychiatric-evaluation/">Click Here</a></div></div>
    <div class="card reveal"><img src="/images/btm1-box3.jpg" alt="psychiatrist and a woman chatting" loading="lazy"><div class="body"><h3>View More Services</h3><p>Find out more behavioral health care services we offer you.</p><a class="more" href="/behavioral-health-care-services/">Click Here</a></div></div>
  </div>
</div></section>

<section><div class="wrap split rev">
  <div class="media reveal"><img src="/images/btm2-img.jpg" alt="man with a hoodie listening to his psychiatrist" loading="lazy"></div>
  <div class="reveal"><span class="eyebrow">Let&rsquo;s Get Started</span><h2>Begin your journey with us now.</h2>
    <p class="lead">We hope to contribute to making a positive change in your and others&rsquo; lives.</p>
    <div class="two" style="margin-top:26px">
      <div class="panel"><h3>Meet Our Professionals</h3><p class="note">Get to know the professionals who are available to help and support you anytime.</p><a class="more" style="font-weight:600;text-decoration:none" href="/behavioral-health-care-meet-our-professionals/">Click Here &rarr;</a></div>
      <div class="panel gold"><h3>Send Your Referrals</h3><p class="note">Help us extend our reach to other people who can benefit from our services.</p><a style="font-weight:600;text-decoration:none" href="{REFERRAL}" target="_blank" rel="noopener">Click Here &rarr;</a></div>
    </div></div>
</div></section>

<section class="band"><div class="wrap" style="max-width:900px;position:relative">
  <span class="eyebrow gold">We Are Committed</span><h2>Our Mission Statement</h2>
  <blockquote>The mission of Brown Behavioral Health Services is to provide proficient and competent care related to diagnosing and treating psychiatric illnesses in pediatrics and adults while improving overall health status. BBHS is committed to the mental health population and is eager to serve each individual holistically while enhancing mental health awareness, promoting individual empowerment, and increasing access to treatment and services for persons living with mental illnesses.</blockquote>
  <p style="margin-top:28px"><a class="btn btn-gold" href="/behavioral-health-care-about-us/#mission">About Us</a></p>
</div></section>

<section><div class="wrap split">
  <div><span class="eyebrow">Reach Out to Us</span><h2>Send Us a Message</h2><p class="lead">Share your thoughts, questions, and concerns with us by leaving us a message.</p>
    <div class="panel" style="margin-top:20px">{contact_form("New message from brownbehavioral.com (home page)")}</div></div>
  <div><iframe class="map" src="{MAP}" title="Map of Bolivar, TN" loading="lazy" style="height:520px"></iframe></div>
</div></section>
'''
page("/", "Brown Behavioral Health Services, PLLC | Behavioral Health Care in Tennessee and Mississippi",
     "Psychiatric evaluation, medication management, therapy, MAT, primary care and more for ages 5 and up. Offices in Bolivar, TN and Olive Branch, MS, plus telehealth.", home)

# ---------------- ABOUT ----------------
about = f'''
<section><div class="wrap split">
 <div><span class="eyebrow">Who We Are</span><h2>Accessible care for rural communities</h2>
 <p class="lead">Brown Behavioral Health Services, PLLC takes pride in offering mental health, minor medical, weight loss, substance abuse treatment, and IV hydration services across the state of Tennessee and Mississippi.</p>
 <p>Our in person and telehealth capabilities provide a more accessible approach to healthcare across rural communities. We encourage you to choose a premiere clinic such as ours to help facilitate your mental health needs as well as other medical services.</p>
 <ul class="chips" style="margin-top:20px"><li>Mental Health</li><li>Minor Medical</li><li>Weight Loss</li><li>Substance Abuse Treatment</li><li>IV Hydration</li></ul></div>
 <div class="media arch"><img src="/images/main-img.png" alt="psychiatrist comforting her emotional client"></div>
</div></section>
<section class="alt" id="mission"><div class="wrap two">
 <div class="panel"><span class="eyebrow">Our Mission</span><p>The mission of Brown Behavioral Health Services is to provide proficient and competent care related to diagnosing and treating psychiatric illnesses in pediatrics and adults while improving overall health status. BBHS is committed to the mental health population and is eager to serve each individual holistically while enhancing mental health awareness, promoting individual empowerment, and increasing access to treatment and services for persons living with mental illnesses.</p></div>
 <div class="panel deep"><span class="eyebrow gold">Our Vision</span><p style="font-family:var(--serif);font-size:1.1rem;color:#f1f6f4">&ldquo;To provide client-centered, expert mental health services such as evaluations, patient advocacy, and medication management to the medically underserved communities with an aim to treat conditions such as Schizophrenia, Bipolar Disorders, ADHD, Depression, Anxiety, Substance Abuse, and many more.&rdquo;</p><p style="margin:0;color:var(--gold)">Dr. Avanti Brown, DNP, PMHNP-BC</p></div>
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
    return f'''<article class="person reveal"><img src="/images/{img}" alt="image of {name.split(",")[0]}"><div><h3>{name}</h3><div class="role">{role}</div><div class="cred">{cred}</div><p>{first}</p>{more}{f'<span class="tag">{tag}</span>' if tag else ""}</div></article>'''
providers = "".join([
 person("Dr-Avanti-Brown.jpg","Dr. Avanti Brown, APRN, DNP, PMHNP-BC, CARN-AP, NRCME","CEO | Provider | Educator &amp; Community Advocate","Board-Certified Psychiatric Mental Health Practitioner | Addictions Advanced Practice Provider",[
  "Dr. Avanti Brown, a native of West Tennessee, has been serving the mental health community since 2013. She is the CEO of Brown Behavioral Health Services, a Director on the University of Tennessee Health Science Center (UTHSC) Alumni Board, and a Healthcare Stakeholder for the Community Advisory Council (CAC) for the ACCESS (Achieving Cancer Care Equity and Systematic Solutions) Study.",
  "Dr. Brown earned her Bachelor of Science in Nursing in 2015 and worked as a Registered Nurse for many years. In 2021, she completed her Doctor of Nursing Practice at UTHSC, specializing as a Psychiatric Mental Health Nurse Practitioner, and became ANCC board-certified. During her graduate studies, she received multiple awards, including the Chancellor Diversity Scholarship Award, University Scholar Diversity Scholarship, HRSA ANEW Grant, and the Grace S. Wallace Scholarship Award.",
  "In 2022, she became a certified Medical Examiner for the Federal Motor Carrier Safety Administration, providing DOT (Department of Transportation) physical exams for CDL drivers and students. In 2025, she achieved dual certification as a Certified Addictions Advanced Practice Provider, expanding her expertise in MAT and MOUD treatment.",
  "With extensive experience treating children, adolescents, adults, and geriatrics across telehealth, outpatient, and inpatient settings, Dr. Brown combines clinical excellence with compassion to ensure her patients receive the best possible care."]),
 person("Dr-Kayla-Williams.jpg","Dr. Kayla Williams, APRN, DNP, PMHNP-BC","Psychiatric Mental Health Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse Practitioner",[
  "Dr. Kayla Williams is a board-certified Psychiatric Mental Health Nurse Practitioner committed to delivering comprehensive, patient-centered care across the lifespan. She earned her Doctor of Nursing Practice from the University of Tennessee Health Science Center in 2024, following her Bachelor of Science in Nursing from Baptist College of Health Sciences in 2019.",
  "She provides evidence-based treatment for children, adolescents, adults, and older adults facing a wide range of mental health conditions, including mood disorders, anxiety, ADHD, and trauma-related concerns. Dr. Williams is passionate about reducing stigma and promoting early intervention in mental health care.",
  "Her goal is to empower patients and families through education, individualized treatment planning, and ongoing support."]),
 person("Dr-Jessica-Allen.jpg","Dr. Jessica Allen, MSN, DNP, FNP-BC, PMHNP-BC","Psychiatric and Family Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse and Family Nurse Practitioner",[
  "Dr. Jessica Allen is a board-certified Psychiatric-Mental Health and Family Nurse Practitioner with a focus on providing client-centered, expert mental health and medical services, including medical consultations, psychiatric evaluations, and medication management to all communities. Dr. Allen treats individuals age 5 years and above. She offers flexible &amp; affordable telehealth, mobile, &amp; in-person appointments, with some evenings &amp; weekends available."],"Evenings &amp; weekends available"),
 person("Dr-DiYana-Fisher.jpg","Dr. Di&rsquo;Yana Fisher, APRN, DNP, PMHNP-BC","Psychiatric Mental Health Nurse Practitioner","Board-Certified Psychiatric Mental Health Nurse Practitioner",[
  "Dr. Di&rsquo;Yana Fisher, DNP, PMHNP-BC is a board-certified Psychiatric Mental Health Nurse Practitioner at BBHS, providing evidence-based psychiatric care to adolescents and adults across Tennessee and Mississippi.",
  "Dr. Fisher is committed to ensuring every patient feels heard, supported, and understood. She takes a collaborative, whole-person approach to care, recognizing the connection between mind, body, and life experiences. She develops individualized treatment plans for conditions including anxiety, depression, ADHD, bipolar disorder, trauma, and other mental health concerns.",
  "Known for her warm, nonjudgmental style, Dr. Fisher creates a welcoming space where patients feel comfortable asking questions and actively participating in their care. She offers both in-office and secure telehealth appointments and is dedicated to expanding access to high-quality mental health services throughout Tennessee and Mississippi."],"Now accepting new patients. Weekend appointments available."),
])
leaders = "".join([
 person("Destiny-Shaw.jpg","Destiny Shaw, BS, MBA","Practice Administrator | Chief of Operations","",[
  "Destiny Shaw serves as Practice Administrator and Chief of Operations at Brown Behavioral Health Services, where she oversees daily clinic operations and ensures patients experience seamless, coordinated care.",
  "With a five-year background in clinical mental health, rural health policy, and patient advocacy, Destiny brings both operational expertise and a deep commitment to expanding access to care in rural communities. She also serves as the Special Grant Projects Team Manager, leading initiatives that strengthen and grow the services BBHS provides."]),
 person("Brook-Pittman.jpg","Brook Pittman, CMA","Clinical Lead Medical Assistant | Community Health Coordinator","",[
  "With 15 years of dedicated work in the medical field, Brook Pittman serves compassionately as the Clinical Lead Medical Assistant at Brown Behavioral Health Services, supporting providers and patients across the clinic&rsquo;s behavioral health and primary care services.",
  "Brook also serves as the MA Student Rotation Coordinator, mentoring the next generation of medical assistants, and as Community Health Coordinator under the Healthcare Resiliency Program grant, connecting patients with resources throughout the community."]),
 person("Andreina-Acuna.jpg","Andreina Acuna, CMA","School Health Coordinator | Medical Assistant","",[
  "Andreina Acuna serves as the School Health Coordinator and Medical Assistant on the BBHS Clinical Administration team.",
  "With three years of experience in medical and legal translation services, Andreina transitioned into a front-facing healthcare role at BBHS after completing her rural student rotation with the clinic in the fall of 2025. She is excited to assist patients in both English and Spanish, helping expand accessible, welcoming care for every family BBHS serves."],"Se habla espa&ntilde;ol"),
])
team = f'''<section><div class="wrap"><div class="center"><span class="eyebrow">Clinical Providers</span><h2>Meet Our Providers</h2></div><div class="team">{providers}</div></div></section>
<section class="alt"><div class="wrap"><div class="center"><span class="eyebrow">Our People</span><h2>Meet Our Clinical and Leadership Team</h2></div><div class="team">{leaders}</div></div></section>{CONNECT}'''
page("/behavioral-health-care-meet-our-professionals/","Meet Our Professionals | Brown Behavioral Health Services","Meet the board-certified psychiatric nurse practitioners and clinical team at Brown Behavioral Health Services.",team,("Meet Our Professionals","Get to know the professionals who are available to help and support you anytime.","Meet Our Professionals"))

# ---------------- SERVICES ----------------
svc = ["Psychiatric Evaluation|/behavioral-health-care-psychiatric-evaluation/","Medication Management|#medication-management","Genetic Testing","Psychotherapy","ADHD Testing","DOT Physicals","Medical Card Certification|/docs/MS-Cannabis-Certification.pdf","Slim Program","MAT (Medication Assisted Treatment) Program","Alcohol and Drug: DUI School"]
def li(x):
    if "|" in x: t,h=x.split("|"); return f'<li><a href="{h}">{t}</a></li>'
    return f"<li>{x}</li>"
cond=["Major Depressive Disorders","Generalized Anxiety Disorder","PTSD","ADHD","Disruptive Mood Dysregulation Disorder","Conduct Disorders","Postpartum Depression","Bipolar Disorders","Schizophrenic Disorders","Medication Assisted Treatment for Substance Use Disorders","Many more"]
services = f'''<section><div class="wrap split">
<div><span class="eyebrow">Our Service Programs</span><h2>Behavioral health care for ages 5 and up</h2>
<p>If you want to avail any of them, we recommend you request an appointment and meet with our professionals. They will help you determine your situation and the services appropriate to address your concerns. We are here to support you.</p>
<ul class="svc" style="margin-top:24px">{"".join(li(x) for x in svc)}</ul></div>
<div class="media"><img src="/images/slider-1.jpg" alt="man listening to his psychiatrist" style="aspect-ratio:4/5;object-fit:cover"></div></div></section>
<section class="alt" id="medication-management"><div class="wrap two">
<div class="panel"><span class="eyebrow">Featured Service</span><h3>Medication Management</h3><p>Let us help manage your medications and their effectiveness.</p><a class="btn btn-outline" href="/behavioral-health-request-an-appointment/">Request an Appointment</a></div>
<div class="panel"><span class="eyebrow">Featured Service</span><h3>Psychiatric Evaluation</h3><p>Schedule an evaluation to understand your cognitive status.</p><a class="btn btn-outline" href="/behavioral-health-care-psychiatric-evaluation/">Learn More</a></div>
</div></section>
<section><div class="wrap"><div class="center"><span class="eyebrow">Conditions We Treat</span><h2>We treat a wide range of conditions</h2></div>
<ul class="chips" style="justify-content:center;margin-top:28px">{"".join(f"<li>{c}</li>" for c in cond)}</ul></div></section>{CONNECT}'''
page("/behavioral-health-care-services/","Services | Brown Behavioral Health Services","Psychiatric evaluation, medication management, genetic testing, psychotherapy, ADHD testing, MAT, DUI school and more.",services,("Services","Our behavioral health care services are available for individuals aging 5 and up.","Services"))

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
<aside><div class="media" style="margin-bottom:22px"><img src="/images/btm1-box2.jpg" alt="parents comforting their daughter"></div><div class="panel deep"><h3>Ready to talk?</h3><p>If you are interested in hearing more about our services, please feel free to reach out to us at any time.</p><a class="btn btn-gold" href="/behavioral-health-request-an-appointment/">Request an Appointment</a><p style="margin:16px 0 0">Or call <a style="color:#fff" href="{PHONE_LINK}">{PHONE}</a></p></div></aside>
</div></section>'''
page("/behavioral-health-care-psychiatric-evaluation/","Psychiatric Evaluation | Brown Behavioral Health Services","Comprehensive psychiatric evaluations for children, adolescents and adults in Tennessee and Mississippi.",pe,("Psychiatric Evaluation","Schedule an evaluation to understand your cognitive status.",'<a href="/behavioral-health-care-services/">Services</a> / Psychiatric Evaluation'))

# ---------------- MEDICAL ----------------
med=["Primary Care Services","DOT Physicals","Minor Medical Services","Slim Program","Mobile IV Hydration Service","Sports Physicals"]
medical = f'''<section><div class="wrap"><div class="cards three">{"".join(f'<div class="panel reveal"><span class="eyebrow">{ico("heart",16)}</span><h3>{m}</h3><a class="more" style="font-weight:600;text-decoration:none" href="/behavioral-health-request-an-appointment/">Request an Appointment &rarr;</a></div>' for m in med)}</div></div></section>{CONNECT}'''
page("/behavioral-health-care-medical-services/","Medical Services | Brown Behavioral Health Services","Primary care, DOT physicals, minor medical services, Slim Program, mobile IV hydration and sports physicals.",medical,("Medical Services","Primary care and medical services alongside our behavioral health care.","Medical Services"))

# ---------------- APPOINTMENT ----------------
appt = f'''<section><div class="wrap split">
<div><span class="eyebrow">Online Scheduling</span><h2>Book your next appointment online.</h2><p class="lead">No need to wait for our office to open the next day. Book online or through the app to schedule your appointment.</p>
<a class="btn btn-teal" href="{HEALOW_BOOK}" target="_blank" rel="noopener">{ico("cal",18)} Book Now</a>
<p style="margin-top:22px">Prefer to call? Reach us at <a href="{PHONE_LINK}">{PHONE}</a>.</p></div>
<div class="two">
<div class="panel"><span class="eyebrow">Tennessee</span><h3>TN Brown Behavioral Health Services</h3><p class="note">Bolivar, TN 38008</p><p class="note">Medical Provider Only</p><a class="btn btn-outline" href="{HEALOW_BOOK}" target="_blank" rel="noopener">Book in TN</a></div>
<div class="panel"><span class="eyebrow">Mississippi</span><h3>MS Brown Behavioral Health Services</h3><p class="note">Olive Branch, MS 38654</p><p class="note">&nbsp;</p><a class="btn btn-outline" href="{HEALOW_BOOK}" target="_blank" rel="noopener">Book in MS</a></div>
</div></div></section>
<section class="alt"><div class="wrap center"><h2>New to BBHS?</h2><p class="lead">No one will be denied access to services due to inability to pay. There is a discounted/sliding fee schedule available based on family size and income.</p><a class="btn btn-outline" href="/behavioral-health-care-payment/">See Payment Options</a></div></section>'''
page("/behavioral-health-request-an-appointment/","Request an Appointment | Brown Behavioral Health Services","Book your appointment online with Brown Behavioral Health Services in Tennessee or Mississippi.",appt,("Request an Appointment","Book online or through the app to schedule your appointment.","Request an Appointment"))

# ---------------- PORTAL ----------------
portal = f'''<section><div class="wrap split">
<div><span class="eyebrow">Healow App</span><h2>Set up the healow smartphone app in four easy steps!</h2>
<ol class="steps" style="margin-top:22px">
<li><span>Download the healow&trade; app from the App Store (iPhone) or Google Play (Android Phone).</span></li>
<li><span>Search our practice by entering practice code. Practice Code: <span class="code">ACGHDD</span></span></li>
<li><span>Enter your portal username and password to log in.</span></li>
<li><span>Set up your PIN to securely access your health records.</span></li></ol></div>
<div class="panel deep center"><div style="width:64px;height:64px;border-radius:16px;background:rgba(196,154,60,.2);color:var(--gold);display:grid;place-items:center;margin:0 auto 18px">{ico("portal",30)}</div><h3>Already have an account?</h3><p>Log in to view records, message your care team, and more.</p><a class="btn btn-gold" href="{PORTAL}" target="_blank" rel="noopener">Go to Patient Portal</a></div>
</div></section>'''
page("/behavioral-health-care-healow-patient-portal/","Healow Patient Portal | Brown Behavioral Health Services","Access the Brown Behavioral Health Services patient portal through the healow app. Practice code ACGHDD.",portal,("Healow Patient Portal","Securely access your health records anytime.","Healow Patient Portal"))

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

# ---------------- REFERRALS ----------------
ref = f'''<section><div class="wrap" style="max-width:820px"><div class="panel center"><div style="width:64px;height:64px;border-radius:16px;background:var(--teal-l);color:var(--teal);display:grid;place-items:center;margin:0 auto 18px">{ico("send",30)}</div>
<h2>Allow us to help others by sending your referrals.</h2><p class="lead">Help us extend our reach to other people who can benefit from our services.</p><a class="btn btn-teal" href="{REFERRAL}" target="_blank" rel="noopener">Open Referral Form</a><p class="note" style="margin-top:16px">Providers may also fax referrals to {FAX}.</p></div></div></section>'''
page("/behavioral-health-care-send-your-referrals/","Send Your Referrals | Brown Behavioral Health Services","Refer a patient to Brown Behavioral Health Services.",ref,("Send Your Referrals","Allow us to help others by sending your referrals.","Send Your Referrals"))

# ---------------- CAREERS ----------------
careers = f'''<section><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">Careers</span><h2>Join our team</h2><p class="lead">Join our team of professionals and share your expertise with those who need your help. Apply now!</p>
<div class="media" style="margin-top:24px"><img src="/images/slider-2.jpg" alt="medical personnel and a woman chatting" style="aspect-ratio:4/3;object-fit:cover"></div></div>
<div class="panel"><h3>Careers Form</h3><p class="note"><span class="req" style="color:#b4441c">*</span> Required Information</p>
<form action="{FORM_ENDPOINT}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="New job application from brownbehavioral.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{SITE}/thank-you/"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="row"><div><label for="c1">First Name <span class="req">*</span></label><input id="c1" name="First_Name" required></div><div><label for="c2">Last Name <span class="req">*</span></label><input id="c2" name="Last_Name" required></div></div>
<div class="row"><div><label for="c3">Email <span class="req">*</span></label><input id="c3" type="email" name="Email" required></div><div><label for="c4">Phone Number <span class="req">*</span></label><input id="c4" type="tel" name="Phone_Number" required></div></div>
<div class="row"><div><label for="c5">Cell Number <span class="req">*</span></label><input id="c5" type="tel" name="Cell_Number" required></div><div><label for="c6">Position Applying For <span class="req">*</span></label><input id="c6" name="Position_Applying_For" required></div></div>
<label for="c7">Attach Resume</label><input id="c7" type="file" name="attachment" accept=".pdf,.doc,.docx">
<label for="c8">Message</label><textarea id="c8" name="Message"></textarea>
<button class="btn btn-teal" type="submit">{ico("brief",18)} Submit Application</button></form></div>
</div></section>
<section class="alt"><div class="wrap center"><h2>Are you a consultant or vendor?</h2><p class="lead">View our current and past Requests for Proposals.</p><a class="btn btn-outline" href="/behavioral-health-care-careers/request-for-proposals/">Request for Proposals</a></div></section>'''
page("/behavioral-health-care-careers/","Careers | Brown Behavioral Health Services","Join the team at Brown Behavioral Health Services. Apply online.",careers,("Careers","Join our team of professionals and share your expertise with those who need your help.","Careers"))

# ---------------- RFP ----------------
rfp = f'''<section><div class="wrap" style="max-width:900px"><div class="prose">
<span class="eyebrow">Request for Proposal (RFP)</span><h2 style="margin-top:0">Technical Assistance and Evaluation Advisor: Brown Behavioral Health Services</h2>
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
 <div class="panel"><span class="eyebrow">{ico("pin",16)} Service Areas</span><p style="margin:0">Accept patients in the State of Tennessee and Mississippi<br><b>Bolivar, TN 38008</b><br><b>Olive Branch, MS 38654</b><br>Also Offer Telehealth Visits</p></div>
</div>
<div class="split" style="align-items:start"><div class="panel"><h2>Contact Us Form</h2><p class="note">* Required Information</p>{contact_form("New message from brownbehavioral.com (contact page)")}</div>
<iframe class="map" src="{MAP}" title="Map of Bolivar, TN" loading="lazy" style="height:640px"></iframe></div></div></section>'''
page("/behavioral-health-care-contact-us/","Contact Us | Brown Behavioral Health Services","Contact Brown Behavioral Health Services. Phone 731-228-9068, fax 901-425-9773, contact@brownbehavioral.com.",contact,("Contact Us","Do you need help? Reach out to us anytime.","Contact Us"))

# ---------------- PRIVACY ----------------
priv = f'''<section><div class="wrap prose" style="max-width:860px">
<p><b>Effective Date: March 2024</b></p>
<p>Welcome to Brown Behavioral Health Services (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;). We are committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, share, and safeguard your data when you use our services. By using our services, you consent to the practices described in this Privacy Policy.</p>
<h2>Information We Collect</h2><p>We may collect the following types of information when you use our website creation services:</p><ul>
<li><b>Personal Information:</b> We may collect personal information, including your name, email address, phone number, and business information when you sign up for our services or communicate with us.</li>
<li><b>Payment Information:</b> We may collect payment data for purchases, orders, or service requests, including valid credit card numbers, brands, and expiration dates. We store only very limited, if any, payment information (e.g. payment accounts, bank accounts, credit cards, or cheques) that we collect. Otherwise, all financial information is stored by our payment processor, and you are encouraged to review their privacy policy and contact them directly for responses to your questions.</li>
<li><b>Website Information:</b> In creating websites, we may collect content, images, and other materials provided by you to design and customize your website.</li>
<li><b>Technical Information:</b> We collect information related to your website&rsquo;s usage, such as IP addresses, browser type, and access times.</li>
<li><b>Cookies and Tracking Technologies:</b> We use cookies and similar technologies to track user behavior on our website. You can manage your cookie preferences through your browser settings.</li></ul>
<h2>How We Use Your Information</h2><p>We use your information for the following purposes:</p><ul>
<li><b>Website Creation:</b> We use your provided data and materials to create and customize websites according to your specifications.</li>
<li><b>Communication:</b> We use your contact information to respond to your inquiries, provide support, and keep you updated on the progress of your website project.</li>
<li><b>Improvement of Services:</b> We may use your website usage data to enhance and optimize our services and user experience.</li>
<li><b>Legal Compliance:</b> We process your data to comply with legal obligations and protect our rights.</li></ul>
<h2>How We Share Your Information</h2><p>No mobile information will be shared with third parties/affiliates for marketing/promotional purposes. All other categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.</p>
<ul><li><b>Service Providers and Legal Requirements:</b> We may disclose your information if required by law or to protect and ensure your safety and our rights, privacy, safety, or property.</li></ul>
<h2>Security of Your Information</h2><p>We take appropriate measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction. We use encryption, access controls, and regular security assessments to safeguard your data.</p>
<h2>Your Choices and Rights</h2><ul><li><b>Access and Correction:</b> You have the right to access and correct your personal information. You can do this by contacting us at {PHONE}.</li><li><b>Opt-Out:</b> You can opt out of receiving promotional communications from us at any time by following the instructions provided in the communication.</li></ul>
<h2>Changes to this Privacy Policy</h2><p>We may update this Privacy Policy from time to time to reflect changes in our practices or for legal reasons. We will notify you of any significant changes via email or a notice on our website.</p>
<h2>Contact Us</h2><p>If you have any questions or concerns regarding this Privacy Policy, please contact us at {PHONE}.</p>
<div class="alert"><b>Disclaimer:</b> By providing a telephone number and submitting the form you are consenting to be contacted by SMS text message. Message and data rates may apply. Reply STOP to opt out of further messaging. Phone numbers we collect and the consent we received will not be shared with 3rd-party providers.</div>
</div></section>'''
page("/privacy-policy/","Privacy Policy | Brown Behavioral Health Services","Privacy Policy for Brown Behavioral Health Services.",priv,("Privacy Policy","","Privacy Policy"))

# ---------------- SITEMAP + THANK YOU + 404 ----------------
links = [("Home","/"),("About Us","/behavioral-health-care-about-us/"),("Meet Our Professionals","/behavioral-health-care-meet-our-professionals/"),("Services","/behavioral-health-care-services/"),("Psychiatric Evaluation","/behavioral-health-care-psychiatric-evaluation/"),("Medical Services","/behavioral-health-care-medical-services/"),("Request an Appointment","/behavioral-health-request-an-appointment/"),("Healow Patient Portal","/behavioral-health-care-healow-patient-portal/"),("Payment Options","/behavioral-health-care-payment/"),("Send Your Referrals","/behavioral-health-care-send-your-referrals/"),("Careers","/behavioral-health-care-careers/"),("Request for Proposals","/behavioral-health-care-careers/request-for-proposals/"),("Contact Us","/behavioral-health-care-contact-us/"),("Privacy Policy","/privacy-policy/")]
page("/sitemap/","Sitemap | Brown Behavioral Health Services","All pages on brownbehavioral.com.",f'<section><div class="wrap"><ul class="svc">{"".join(f"<li><a href={chr(34)}{h}{chr(34)}>{t}</a></li>" for t,h in links)}</ul></div></section>',("Sitemap","","Sitemap"))
page("/thank-you/","Thank You | Brown Behavioral Health Services","Thank you for contacting Brown Behavioral Health Services.",f'<section><div class="wrap center" style="max-width:700px"><h2>Thank you!</h2><p class="lead">Your submission has been received. Our team will get back to you as soon as possible.</p><p>If this is an emergency, please call 911.</p><a class="btn btn-teal" href="/">Back to Home</a></div></section>',("Thank You","","Thank You"))
page("/404/","Page Not Found | Brown Behavioral Health Services","Page not found.",f'<section><div class="wrap center"><h2>Sorry, we could not find that page.</h2><p class="lead">Try one of the links in the menu, or call us at {PHONE}.</p><a class="btn btn-teal" href="/">Back to Home</a></div></section>',("Page Not Found","","404"))
os.replace("404/index.html","404.html"); os.rmdir("404")

with open("sitemap.xml","w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{h}</loc></url>" for _,h in links)+"</urlset>\n")
with open("robots.txt","w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open("CNAME","w") as f: f.write("www.brownbehavioral.com\n")
print("Built.")
