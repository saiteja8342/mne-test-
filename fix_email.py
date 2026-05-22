import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

# Insert the error popup HTML
error_html = """
        <div class="cf-success" id="cfSuccess">
          <div class="cfs-icon">✓</div>
          <h3>Message received!</h3>
          <p>We'll get back to you within 24 hours.</p>
        </div>

        <div class="cf-error" id="cfError" style="display:none; color:#ef4444; margin-top:16px; font-weight:600; padding:12px; background:rgba(239,68,68,0.1); border-radius:8px; border:1px solid rgba(239,68,68,0.2);">
          Mail is wrong! Please enter a valid email address.
        </div>
"""

html = re.sub(r'<div class="cf-success" id="cfSuccess">.*?</div>\s*</div>', error_html, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)


# 2. Update JS
with open('js/app.js', 'r') as f:
    js = f.read()

js_replacement = """
  function initContactForm() {
    const form    = document.getElementById('ctaForm');
    const success = document.getElementById('cfSuccess');
    const error   = document.getElementById('cfError');
    const submitBtn = document.getElementById('cfSubmit');
    const emailInput = document.getElementById('cfEmail');
    if (!form) return;

    form.addEventListener('submit', async e => {
      e.preventDefault();
      
      if (error) error.style.display = 'none';

      // Custom Email Format Validation
      const emailVal = emailInput ? emailInput.value.trim() : '';
      const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
      if (!emailRegex.test(emailVal)) {
        if (error) error.style.display = 'block';
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        const sp = submitBtn.querySelector('span');
        if (sp) sp.textContent = 'Sending…';
      }

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' }
        });

        if (res.ok) {
          form.style.display = 'none';
          if (success) success.style.display = 'block';
        } else {
          resetBtn('Error — try WhatsApp');
        }
      } catch {
        resetBtn('Network error');
      }
    });

    function resetBtn(msg) {
      if (!submitBtn) return;
      submitBtn.disabled = false;
      const sp = submitBtn.querySelector('span');
      if (sp) sp.textContent = msg || 'Send Message';
      setTimeout(() => { if (sp) sp.textContent = 'Send Message'; }, 3000);
    }
  }
"""

js = re.sub(r'function initContactForm\(\)\s*\{.*?\}\n\s*(?=\n\s*/\* =+)', js_replacement, js, flags=re.DOTALL)

with open('js/app.js', 'w') as f:
    f.write(js)
