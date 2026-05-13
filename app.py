import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="India Daily Dispatch",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default header/footer/menu so the UI stays like the original HTML page.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_code = r'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>India Daily Dispatch</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: #f7f4ef;
      color: #222;
      line-height: 1.6;
    }

    header {
      background: #111;
      color: white;
      padding: 18px 8%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }

    header h2 {
      font-size: 24px;
      letter-spacing: 1px;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin-left: 18px;
      font-size: 14px;
    }

    .hero {
      padding: 70px 8%;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 35px;
      align-items: center;
    }

    .hero h1 {
      font-size: 46px;
      line-height: 1.1;
      margin-bottom: 20px;
    }

    .hero p {
      font-size: 18px;
      margin-bottom: 25px;
      color: #444;
    }

    .btn {
      display: inline-block;
      background: #111;
      color: white;
      padding: 14px 24px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: bold;
    }

    .preview-card {
      background: white;
      padding: 28px;
      border-radius: 16px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.08);
      border-top: 6px solid #111;
    }

    .preview-card h2 {
      margin-bottom: 8px;
    }

    .preview-card h3 {
      margin-top: 18px;
      color: #111;
    }

    .preview-card p {
      font-size: 14px;
      color: #555;
      margin-top: 5px;
    }

    section {
      padding: 55px 8%;
    }

    .section-title {
      text-align: center;
      font-size: 32px;
      margin-bottom: 30px;
    }

    .features {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 22px;
    }

    .feature {
      background: white;
      padding: 24px;
      border-radius: 14px;
      box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    }

    .feature h3 {
      margin-bottom: 10px;
    }

    .subscribe {
      background: #111;
      color: white;
      text-align: center;
      border-radius: 20px;
      margin: 40px 8%;
      padding: 45px 20px;
    }

    .subscribe h2 {
      font-size: 32px;
      margin-bottom: 12px;
    }

    .subscribe p {
      margin-bottom: 22px;
      color: #ddd;
    }

    form {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    input[type="email"] {
      padding: 14px;
      width: 280px;
      border: none;
      border-radius: 8px;
      font-size: 15px;
    }

    button {
      padding: 14px 22px;
      border: none;
      border-radius: 8px;
      background: #f4c542;
      font-weight: bold;
      cursor: pointer;
    }

    footer {
      text-align: center;
      padding: 25px;
      color: #666;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <header>
    <h2>📰 India Daily Dispatch</h2>
    <nav>
      <a href="#features">Features</a>
      <a href="#sample">Sample</a>
      <a href="#subscribe">Subscribe</a>
    </nav>
  </header>

  <section class="hero">
    <div>
      <h1>Your AI-powered daily India newspaper.</h1>
      <p>Get a clean, 1-minute daily digest covering politics, IPL, business, technology, education, and entertainment — delivered straight to your inbox.</p>
      <a href="#subscribe" class="btn">Subscribe for Free</a>
    </div>

    <div class="preview-card" id="sample">
      <h2>Daily News Preview</h2>
      <p>🌤 Hubli Weather | 📈 Market Snapshot | 🕒 Today</p>
      <h3>Politics</h3>
      <p>Top political updates from verified Indian news sources.</p>
      <h3>Sports</h3>
      <p>IPL and cricket highlights summarized in a readable format.</p>
      <h3>Business</h3>
      <p>Market and economy updates for the day.</p>
    </div>
  </section>

  <section id="features">
    <h2 class="section-title">Why Subscribe?</h2>
    <div class="features">
      <div class="feature">
        <h3>⚡ Quick Digest</h3>
        <p>Read important news in under 1 minute without opening many websites.</p>
      </div>
      <div class="feature">
        <h3>🏏 IPL & Sports</h3>
        <p>Daily sports updates with cricket and IPL highlights.</p>
      </div>
      <div class="feature">
        <h3>🤖 AI Organized</h3>
        <p>News is automatically categorized into clean newspaper sections.</p>
      </div>
      <div class="feature">
        <h3>📧 Email Delivery</h3>
        <p>Receive the digest automatically in your inbox every day.</p>
      </div>
    </div>
  </section>

  <div class="subscribe" id="subscribe">
    <h2>Subscribe to the Daily Dispatch</h2>
    <p>Enter your email to receive the AI-curated India news digest.</p>

    <form id="subscribeForm">
      <input type="email" id="email" name="email" placeholder="Enter your email" required />
      <button type="submit">Subscribe</button>
    </form>

    <br><br>

    <button id="demoBtn" type="button">Send Today’s Demo Newspaper</button>

    <p id="demoMessage" style="margin-top:15px;font-size:14px;"></p>

    <p id="message" style="margin-top:15px;font-size:14px;"></p>

    <script>
      const form = document.getElementById('subscribeForm');
      const message = document.getElementById('message');

      form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const email = document.getElementById('email').value;

        try {
          const response = await fetch('https://chaitrab.app.n8n.cloud/webhook/subscribe', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email })
          });

          if (response.ok) {
            message.textContent = '✅ Subscribed successfully! You will receive the daily newspaper by email.';
            form.reset();
          } else {
            message.textContent = '❌ Something went wrong. Please try again.';
          }
        } catch (error) {
          message.textContent = '❌ Network error. Please try again later.';
        }
      });
      const demoBtn = document.getElementById('demoBtn');
      const demoMessage = document.getElementById('demoMessage');

      demoBtn.addEventListener('click', async function () {
      demoMessage.textContent = '⏳ Generating today’s newspaper...';

  try {
    const response = await fetch('https://chaitrab.app.n8n.cloud/webhook/send-demo-news', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        demo: true
      })
    });

    if (response.ok) {
      demoMessage.textContent = '✅ Today’s newspaper has been sent to your email.';
    } else {
      demoMessage.textContent = '❌ Could not send demo newspaper.';
    }
  } catch (error) {
    demoMessage.textContent = '❌ Network error. Please try again.';
  }
});
    </script>
  </div>

  <footer>
    Built using n8n + Groq + News APIs | AI News Automation Project
  </footer>
</body>
</html>
'''

components.html(html_code, height=1100, scrolling=True)