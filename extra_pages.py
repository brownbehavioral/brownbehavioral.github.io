# Extra pages: FAQ, Good Faith Estimate, Notice of Privacy Practices
import json as _json, re as _re
def _fill(t): return t.replace("{HOURS}",HOURS).replace("{HOURS_EXT}",HOURS_EXT)
FAQS = [
 ("Who can be seen at BBHS?","We welcome children, adolescents, adults, and older adults ages 5 and up. We serve patients throughout Tennessee and Mississippi in our Bolivar and Olive Branch offices, on our Mobile Health Clinic, and by secure telehealth."),
 ("How do I schedule my first appointment?","Book online anytime through <a href='/behavioral-health-request-an-appointment/'>healow</a> and choose <b>New Patient</b>, use the healow app with practice code ACGHDD, or call "+PHONE+"."),
 ("What are your office hours?","Our offices are open {HOURS} {HOURS_EXT}"),
 ("Do you offer telehealth?","Yes. Secure video visits are available for patients located in Tennessee or Mississippi at the time of the visit. You will need a private, quiet space and a phone, tablet, or computer with a camera and internet connection. Our team sends your video visit instructions before your appointment."),
 ("What insurance do you accept?","We accept Medicare, TennCare, Mississippi Medicaid, and most major commercial and Marketplace plans. See <a href='/insurance/'>Insurance Accepted</a> for the full list, explained in plain language, or call us to verify your coverage."),
 ("What if I do not have insurance?","No one will be denied access to services due to inability to pay. A discounted/sliding fee schedule is available based on family size and income. "+HRP_LINE+" Uninsured and self-pay patients also have the right to a <a href='/good-faith-estimate/'>Good Faith Estimate</a> of expected charges."),
 ("How do I pay my bill?","Pay your copay or balance online with <a href='"+SCRATCHPAY+"' target='_blank' rel='noopener'>Scratchpay</a>, finance care with CareCredit, or call "+PHONE+" to pay by phone. See <a href='/behavioral-health-care-payment/'>Payment Options</a>."),
 ("What should I bring to my first visit?","A photo ID, your insurance card if you have one, a list of your current medications and doses, and any prior records, evaluations, or school reports that may help your provider. If you receive an eClinicalWorks check-in link by text or email, please complete it before your visit."),
 ("How do I request a medication refill?","Send a refill request through the <a href='/behavioral-health-care-healow-patient-portal/'>patient portal</a> or the healow app, or call "+PHONE+". Please allow time for your provider to review the request, and do not wait until you are out of medication."),
 ("How do I cancel or reschedule?","Call "+PHONE+" as soon as you know you need to change your appointment so we can offer the time to another patient. You can also manage appointments in the healow app."),
 ("Do you offer services in Spanish?","Yes. "+LANG_EN+" <span lang='es'>"+LANG_ES+"</span>"),
 ("Is my information kept private?","Yes. We protect your health information under HIPAA, and records of substance use disorder treatment, including our MAT program, have additional protection under 42 C.F.R. Part 2. Read our <a href='/notice-of-privacy-practices/'>Notice of Privacy Practices</a>."),
 ("Do you see University of Memphis students?","Yes. BBHS providers see University of Memphis students at the Student Health and Counseling Center, 214 Wilder Tower, on Fridays from 9:00 a.m. to 4:00 p.m., in person or by telehealth. Students schedule by calling 901-678-2068."),
 ("How do providers refer a patient?","Use our <a href='/behavioral-health-care-send-your-referrals/'>referral form</a> or fax records to "+FAX+". For urgent referrals, please also call "+PHONE+"."),
 ("What should I do in a crisis?","If you are in danger, call 911. For a mental health or substance use crisis, call or text 988 (Suicide and Crisis Lifeline), call the Tennessee Statewide Crisis Line at 855-274-7471, or call the Mississippi Department of Mental Health Helpline at 1-877-210-8513. Help is free and available 24/7."),
]
_faq_ld = _json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":_re.sub(r"<[^>]+>","",_fill(a))}} for q,a in FAQS]})
_items = "".join("<details><summary>"+q+"</summary><p>"+_fill(a)+"</p></details>" for q,a in FAQS)
faq = ('<section><div class="wrap" style="max-width:900px"><div class="faq">'+_items+'</div>'
       '<p class="note" style="margin-top:26px">Still have a question? Call '+PHONE+' or <a href="/behavioral-health-care-contact-us/">contact us</a>.</p></div></section>'
       '<script type="application/ld+json">'+_faq_ld+'</script>'+CONNECT)
page("/faq/","Frequently Asked Questions | Brown Behavioral Health Services","Answers about new patient appointments, hours, telehealth, insurance, uninsured care, billing, refills, privacy, and Spanish language services at BBHS.",faq,("Frequently Asked Questions","Quick answers about appointments, insurance, billing, and your care.",'<a href="/patient-center/">Patients</a> / FAQ'))

gfe = '''<section><div class="wrap prose" style="max-width:860px">
<h2>Your Right to Receive a Good Faith Estimate of Expected Charges</h2>
<p>Under the law, health care providers need to give patients who don&rsquo;t have insurance or who are not using insurance an estimate of the bill for medical items and services.</p>
<ul>
<li>You have the right to receive a Good Faith Estimate for the total expected cost of any non-emergency items or services. This includes related costs like medical tests, prescription drugs, equipment, and hospital fees.</li>
<li>Make sure your health care provider gives you a Good Faith Estimate in writing at least 1 business day before your medical service or item. You can also ask your health care provider, and any other provider you choose, for a Good Faith Estimate before you schedule an item or service.</li>
<li>If you receive a bill that is at least $400 more than your Good Faith Estimate, you can dispute the bill.</li>
<li>Make sure to save a copy or picture of your Good Faith Estimate.</li>
</ul>
<p>For questions or more information about your right to a Good Faith Estimate, visit <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">www.cms.gov/nosurprises</a> or call 1-800-985-3059.</p>
<h2>How to Request a Good Faith Estimate from BBHS</h2>
<p>If you are uninsured, or you choose not to use your insurance, tell our team when you schedule, or call PHONE_X. We will give you your Good Faith Estimate in writing:</p>
<ul>
<li>Within 1 business day after scheduling, if your service is scheduled at least 3 business days in advance.</li>
<li>Within 3 business days after scheduling, if your service is scheduled at least 10 business days in advance.</li>
<li>Within 3 business days after you ask for one, if you have not scheduled yet.</li>
</ul>
<p>For ongoing care such as therapy or medication management, your estimate may cover a series of visits for up to 12 months. If your expected care changes, we will give you an updated estimate.</p>
<h2>If Your Bill Is Higher Than Your Estimate</h2>
<p>If you are billed at least $400 more than your Good Faith Estimate, you may start a dispute through the federal patient-provider dispute resolution process within 120 calendar days of the date on your original bill. Please contact us first at PHONE_X so we can review the bill with you. You may also contact the U.S. Department of Health and Human Services at 1-800-985-3059.</p>
<div class="alert">No one will be denied access to services due to inability to pay. A discounted/sliding fee schedule is available based on family size and income. HRP_X</div>
</div></section>'''.replace("PHONE_X",PHONE).replace("HRP_X",HRP_LINE)
page("/good-faith-estimate/","Good Faith Estimate | Brown Behavioral Health Services","Your right to a Good Faith Estimate of expected charges if you are uninsured or not using insurance at Brown Behavioral Health Services.",gfe,("Good Faith Estimate","Your right to know your costs before you receive care.",'<a href="/patient-center/">Patients</a> / Good Faith Estimate'))

_npp = open("npp_fragment.html").read()
npp = ('<section><div class="wrap prose" style="max-width:880px">'
 '<p><b>Effective and updated February 2026, Version 1.0</b></p>'
 '<p><a class="btn btn-outline" href="/docs/Notice-of-Privacy-Practices.pdf" target="_blank" rel="noopener">Download or Print the Notice (PDF)</a></p>'
 + _npp +
 '<h2>Who to Contact</h2><p><b>Privacy Officer and Compliance Officer:</b> Dr. Avanti Cross-Brown, DNP, PMHNP-BC, CARN-AP, Chief Executive Officer and Compliance Officer<br>'
 'Telephone: <a href="'+PHONE_LINK+'">'+PHONE+'</a><br>Fax: '+FAX+'<br>Email: <a href="mailto:'+EMAIL+'">'+EMAIL+'</a><br>Mailing address: 793 Tennessee Street, Bolivar, TN 38008</p>'
 '<p>Original effective date: 01/02/2021. Updated: February 2026.</p>'
 '<div class="alert">A paper copy of this Notice is available at the front desk of either office. '+LANG_EN+' <span lang="es">'+LANG_ES+'</span></div>'
 '</div></section>')
page("/notice-of-privacy-practices/","Notice of Privacy Practices | Brown Behavioral Health Services","How Brown Behavioral Health Services may use and share your health information, protections for substance use disorder records under 42 CFR Part 2, and your privacy rights.",npp,("Notice of Privacy Practices","How your health information is used and protected, and your rights.",'<a href="/patient-center/">Patients</a> / Notice of Privacy Practices'))
