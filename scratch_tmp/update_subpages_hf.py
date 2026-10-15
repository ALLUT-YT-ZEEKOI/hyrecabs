import re

UNIFIED_HEADER_CSS = """
  /* =========================================================
     HYRECABS UNIFIED LUXURY HEADER
     ========================================================= */
  header.site-header {
    background: rgba(5, 14, 24, 0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(105, 200, 226, 0.16);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
    position: sticky;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    transition: background 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
  }
  header.site-header.is-scrolled {
    background: rgba(4, 10, 18, 0.96);
    border-bottom: 1px solid rgba(105, 200, 226, 0.26);
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5), 0 0 20px rgba(105, 200, 226, 0.08);
  }
  .header-wrap {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 78px;
    gap: 16px;
  }
  .brand {
    display: flex;
    align-items: center;
    flex-shrink: 0;
    text-decoration: none;
  }
  .brand-logo {
    height: 44px;
    width: auto;
    display: block;
    object-fit: contain;
    transition: transform 0.22s ease;
  }
  .brand:hover .brand-logo {
    transform: scale(1.03);
  }
  .nav-links {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 13.5px;
    font-weight: 600;
    color: rgba(255, 255, 255, 0.86);
  }
  .nav-links a {
    padding: 8px 12px;
    border-radius: 8px;
    position: relative;
    transition: color 0.2s ease, background 0.2s ease;
    white-space: nowrap;
    text-decoration: none;
    color: rgba(255, 255, 255, 0.86);
  }
  .nav-links a:hover {
    color: #69c8e2;
    background: rgba(105, 200, 226, 0.08);
  }
  .nav-links a.active {
    color: #ffffff;
    font-weight: 700;
  }
  .nav-links a.active::after {
    content: "";
    position: absolute;
    left: 12px;
    right: 12px;
    bottom: -2px;
    height: 2.5px;
    border-radius: 2px;
    background: linear-gradient(90deg, #69c8e2, #7fd4ea);
    box-shadow: 0 0 10px rgba(105, 200, 226, 0.65);
  }
  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-shrink: 0;
  }
  .header-phone-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 14px;
    background: rgba(105, 200, 226, 0.08);
    border: 1px solid rgba(105, 200, 226, 0.25);
    border-radius: 999px;
    color: #e2f4f8;
    font-size: 12.5px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
  }
  .header-phone-badge:hover {
    background: rgba(105, 200, 226, 0.18);
    border-color: #69c8e2;
    color: #69c8e2;
    transform: translateY(-1px);
    box-shadow: 0 4px 14px rgba(105, 200, 226, 0.25);
  }
  .phone-pulse-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    animation: phonePulse 1.8s infinite;
  }
  @keyframes phonePulse {
    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { box-shadow: 0 0 0 7px rgba(16, 185, 129, 0); }
    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
  }
  .header-wa-btn {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(37, 211, 102, 0.12);
    border: 1px solid rgba(37, 211, 102, 0.35);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #25d366;
    transition: all 0.2s ease;
    text-decoration: none;
    flex-shrink: 0;
  }
  .header-wa-btn:hover {
    background: #25d366;
    color: #061018;
    transform: translateY(-1px) scale(1.05);
    box-shadow: 0 6px 18px rgba(37, 211, 102, 0.35);
  }
  .lang-currency-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    color: rgba(255, 255, 255, 0.85);
    font-size: 12px;
    font-weight: 600;
  }
  .btn-book-now {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: linear-gradient(135deg, #69c8e2 0%, #4fb2cd 100%);
    color: #050e18;
    font-size: 13.5px;
    font-weight: 700;
    padding: 10px 22px;
    border-radius: 999px;
    border: none;
    box-shadow: 0 4px 16px rgba(105, 200, 226, 0.32);
    transition: all 0.22s ease;
    white-space: nowrap;
    text-decoration: none;
  }
  .btn-book-now:hover {
    background: linear-gradient(135deg, #7fd4ea 0%, #5ec3de 100%);
    box-shadow: 0 6px 24px rgba(105, 200, 226, 0.55);
    transform: translateY(-1px);
    color: #040a12;
  }

  /* MOBILE NAV TOGGLE (HAMBURGER) */
  .nav-toggle-btn {
    display: none;
    width: 40px;
    height: 40px;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.35);
    background: rgba(255, 255, 255, 0.06);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    flex-shrink: 0;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .nav-toggle-btn:hover {
    background: rgba(105, 200, 226, 0.14);
    border-color: #69c8e2;
  }
  .nav-toggle-btn span {
    display: block;
    width: 18px;
    height: 2px;
    border-radius: 2px;
    background: #ffffff;
    transition: transform 0.28s ease, opacity 0.18s ease;
  }
  .nav-toggle-btn.open span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
  .nav-toggle-btn.open span:nth-child(2) { opacity: 0; }
  .nav-toggle-btn.open span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }

  .nav-backdrop {
    position: fixed;
    inset: 78px 0 0;
    background: rgba(4, 10, 18, 0.65);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 998;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.25s ease, visibility 0.25s ease;
  }
  .nav-backdrop.show {
    opacity: 1;
    visibility: visible;
  }
  .mobile-nav-cta {
    display: none;
  }

  /* =========================================================
     HYRECABS UNIFIED LUXURY FOOTER
     ========================================================= */
  footer.site-footer {
    background: radial-gradient(900px 340px at 50% 0%, rgba(105, 200, 226, 0.09), transparent 70%), linear-gradient(180deg, #050e18 0%, #03080e 100%);
    border-top: 1px solid rgba(105, 200, 226, 0.18);
    color: #e2f4f8;
    padding-top: 56px;
    padding-bottom: 28px;
    position: relative;
    overflow: hidden;
    margin-top: 40px;
  }
  footer.site-footer::before {
    content: "";
    position: absolute;
    top: 0;
    left: 10%;
    right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(105, 200, 226, 0.6), transparent);
  }
  .footer-grid-top {
    display: grid;
    grid-template-columns: minmax(260px, 1.45fr) repeat(3, minmax(160px, 1fr));
    gap: 44px;
    margin-bottom: 40px;
    align-items: start;
    text-align: left;
  }
  .footer-brand-logo {
    height: 48px;
    width: auto;
    display: block;
    margin-bottom: 14px;
    object-fit: contain;
  }
  .footer-brand-desc {
    font-size: 13px;
    line-height: 1.7;
    color: rgba(226, 244, 248, 0.78);
    max-width: 330px;
    margin-bottom: 16px;
  }
  .footer-trust-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 18px;
  }
  .footer-chip {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    background: rgba(105, 200, 226, 0.08);
    border: 1px solid rgba(105, 200, 226, 0.2);
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    color: #69c8e2;
  }
  .footer-social-links {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .footer-social-links a {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba(255, 255, 255, 0.85);
    transition: all 0.2s ease;
    text-decoration: none;
  }
  .footer-social-links a:hover {
    background: rgba(105, 200, 226, 0.18);
    border-color: #69c8e2;
    color: #69c8e2;
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(105, 200, 226, 0.25);
  }
  .footer-col-h {
    font-size: 13px;
    font-weight: 800;
    color: #69c8e2;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .footer-links-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .footer-links-list li {
    margin-bottom: 11px;
    font-size: 13px;
    color: rgba(226, 244, 248, 0.8);
    line-height: 1.5;
  }
  .footer-links-list a {
    font-size: 13px;
    color: rgba(226, 244, 248, 0.8);
    text-decoration: none;
    transition: color 0.18s ease, transform 0.18s ease;
    display: inline-block;
  }
  .footer-links-list a:hover {
    color: #69c8e2;
    transform: translateX(3px);
  }
  .footer-contact-list li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }
  .footer-contact-list svg {
    flex-shrink: 0;
    margin-top: 3px;
  }
  .footer-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 14px;
    padding: 6px 14px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.28);
    border-radius: 999px;
    font-size: 11.5px;
    font-weight: 600;
    color: #10b981;
  }
  .footer-badge-pill .badge-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10b981;
  }
  .footer-bottom-bar {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    font-size: 12px;
    color: rgba(226, 244, 248, 0.65);
    flex-wrap: wrap;
  }
  .footer-copy {
    margin: 0;
    line-height: 1.6;
  }
  .footer-legal-links {
    display: flex;
    gap: 18px;
    flex-shrink: 0;
    flex-wrap: wrap;
  }
  .footer-legal-links a {
    color: rgba(226, 244, 248, 0.7);
    text-decoration: none;
    transition: color 0.18s ease;
  }
  .footer-legal-links a:hover {
    color: #69c8e2;
  }

  /* Responsive Rules */
  @media (max-width: 1024px) {
    .footer-grid-top {
      grid-template-columns: repeat(2, 1fr);
      gap: 36px;
    }
  }
  @media (max-width: 900px) {
    .header-phone-badge { display: none; }
    .lang-currency-badge { display: none; }
    .btn-book-now { display: none; }
    .nav-toggle-btn { display: flex; }

    .nav-links {
      position: fixed;
      top: 78px;
      left: 0;
      right: 0;
      flex-direction: column;
      align-items: stretch;
      gap: 0;
      padding: 12px 24px 24px;
      background: rgba(5, 14, 24, 0.98);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(105, 200, 226, 0.22);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
      color: #ffffff;
      font-size: 15px;
      max-height: calc(100vh - 78px);
      overflow-y: auto;
      transform: translateY(-100%);
      visibility: hidden;
      transition: transform 0.32s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.32s;
      z-index: 999;
    }
    .nav-links.open {
      transform: translateY(0);
      visibility: visible;
    }
    .nav-links a {
      padding: 14px 4px;
      border-radius: 0;
      color: rgba(255, 255, 255, 0.9);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      font-size: 15px;
    }
    .nav-links a:hover, .nav-links a.active {
      color: #69c8e2;
      background: transparent;
    }
    .nav-links a.active::after { display: none; }
    .mobile-nav-cta {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 16px;
      padding-top: 12px;
    }
    .mobile-nav-phone {
      display: flex !important;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px !important;
      border-radius: 12px !important;
      background: rgba(105, 200, 226, 0.1) !important;
      border: 1px solid rgba(105, 200, 226, 0.3) !important;
      color: #69c8e2 !important;
      font-weight: 600;
    }
    .mobile-nav-wa {
      display: flex !important;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px !important;
      border-radius: 12px !important;
      background: #25d366 !important;
      color: #061018 !important;
      font-weight: 700;
    }
    .mobile-nav-book {
      display: flex !important;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px !important;
      border-radius: 12px !important;
      background: linear-gradient(135deg, #69c8e2 0%, #4fb2cd 100%) !important;
      color: #050e18 !important;
      font-weight: 700;
    }
  }
  @media (max-width: 600px) {
    .footer-grid-top {
      grid-template-columns: 1fr;
      gap: 30px;
    }
    .footer-bottom-bar {
      flex-direction: column;
      align-items: flex-start;
      gap: 12px;
    }
  }
"""

def generate_header_html(active_item="fleet"):
    home_act = ' class="active"' if active_item == "home" else ''
    fleet_act = ' class="active"' if active_item == "fleet" else ''
    blog_act = ' class="active"' if active_item == "blog" else ''
    contact_act = ' class="active"' if active_item == "contact" else ''

    return f"""<!-- HEADER -->
<header class="site-header" id="siteHeader">
  <div class="container header-wrap">
    <a href="index.html" class="brand" aria-label="HyreCabs Kerala — Premium Cab &amp; Car Rentals">
      <img src="images/logo-cars.png" alt="HyreCabs Kerala" class="brand-logo" />
    </a>

    <nav class="nav-links" id="primaryNav">
      <a href="index.html"{home_act}>Home</a>
      <a href="search-results.html"{fleet_act}>Cab Fleet</a>
      <a href="search-results.html?service=airport">Airport Taxi</a>
      <a href="index.html#howitworks">How it Works</a>
      <a href="index.html#faq">FAQ</a>
      <a href="blog.html"{blog_act}>Travel Blog</a>
      <a href="contact.html"{contact_act}>Contact</a>

      <div class="mobile-nav-cta">
        <a href="tel:+917034060000" class="mobile-nav-phone">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>24/7 Helpline: +91 70340 60000</span>
        </a>
        <a href="https://wa.me/917034060000?text=Hi%20HyreCabs,%20I%20would%20like%20to%20book%20a%20cab%20in%20Kerala." target="_blank" rel="noopener" class="mobile-nav-wa">
          <span>Chat on WhatsApp</span>
        </a>
        <a href="search-results.html" class="mobile-nav-book">Book a Cab Online →</a>
      </div>
    </nav>

    <div class="header-actions">
      <a href="tel:+917034060000" class="header-phone-badge" title="24/7 Kerala Helpline">
        <span class="phone-pulse-dot" aria-hidden="true"></span>
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span>+91 70340 60000</span>
      </a>

      <a href="https://wa.me/917034060000?text=Hello%20HyreCabs,%20I%20would%20like%20to%20book%20a%20cab%20in%20Kerala." target="_blank" rel="noopener" class="header-wa-btn" aria-label="WhatsApp 24/7 Support" title="Chat on WhatsApp">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.02L7.55 18.84L4.44 19.66L5.27 16.63L5.07 16.31C4.24 15 3.8 13.48 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67M9.04 7.69C8.86 7.69 8.57 7.76 8.32 8.03C8.07 8.3 7.37 8.96 7.37 10.29C7.37 11.62 8.34 12.91 8.48 13.1C8.62 13.29 10.39 16.03 13.1 17.2C13.75 17.47 14.25 17.64 14.65 17.77C15.3 17.97 15.89 17.94 16.36 17.87C16.88 17.79 17.96 17.22 18.18 16.58C18.41 15.94 18.41 15.4 18.34 15.28C18.27 15.17 18.09 15.1 17.82 14.96C17.54 14.82 16.2 14.16 15.95 14.07C15.7 13.98 15.52 13.93 15.33 14.21C15.15 14.48 14.64 15.1 14.48 15.28C14.33 15.46 14.17 15.48 13.9 15.35C13.62 15.21 12.45 14.83 11.07 13.6C10 12.64 9.32 11.46 9.18 11.23C9.04 11 9.16 10.88 9.3 10.74C9.43 10.62 9.58 10.42 9.72 10.26C9.86 10.1 9.9 9.98 10 9.78C10.1 9.58 10.05 9.42 9.98 9.28C9.91 9.14 9.36 7.79 9.13 7.25C8.91 6.72 8.68 6.8 8.52 6.79C8.36 6.78 8.18 6.78 8 6.78"/></svg>
      </a>

      <div class="lang-currency-badge" title="Kerala, India • INR">
        <span class="flag-icon" aria-hidden="true">🇮🇳</span>
        <span>₹ INR</span>
      </div>

      <a href="search-results.html" class="btn-book-now">
        <span>Book Cab</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>

      <button class="nav-toggle-btn" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="nav-backdrop" id="navBackdrop"></div>"""

UNIFIED_FOOTER_HTML = """<!-- HYRECABS KERALA FOOTER -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid-top">
      <!-- Col 1: Brand & Kerala Promise -->
      <div class="footer-col-brand">
        <a href="index.html" class="footer-brand-link" aria-label="HyreCabs Kerala — Home">
          <img src="images/logo-cars.png" alt="HyreCabs Kerala" class="footer-brand-logo" />
        </a>
        <p class="footer-brand-desc">
          Kerala’s premier cab &amp; car rental network. Transparent fares, licensed drivers, and curated travel experiences across God’s Own Country.
        </p>
        <div class="footer-trust-chips">
          <span class="footer-chip">✨ 24/7 Available</span>
          <span class="footer-chip">🛡️ Zero Surge</span>
          <span class="footer-chip">⭐ 4.9/5 Rated</span>
        </div>
        <div class="footer-social-links">
          <a href="https://wa.me/917034060000" target="_blank" rel="noopener" aria-label="WhatsApp" title="WhatsApp">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.02L7.55 18.84L4.44 19.66L5.27 16.63L5.07 16.31C4.24 15 3.8 13.48 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67M9.04 7.69C8.86 7.69 8.57 7.76 8.32 8.03C8.07 8.3 7.37 8.96 7.37 10.29C7.37 11.62 8.34 12.91 8.48 13.1C8.62 13.29 10.39 16.03 13.1 17.2C13.75 17.47 14.25 17.64 14.65 17.77C15.3 17.97 15.89 17.94 16.36 17.87C16.88 17.79 17.96 17.22 18.18 16.58C18.41 15.94 18.41 15.4 18.34 15.28C18.27 15.17 18.09 15.1 17.82 14.96C17.54 14.82 16.2 14.16 15.95 14.07C15.7 13.98 15.52 13.93 15.33 14.21C15.15 14.48 14.64 15.1 14.48 15.28C14.33 15.46 14.17 15.48 13.9 15.35C13.62 15.21 12.45 14.83 11.07 13.6C10 12.64 9.32 11.46 9.18 11.23C9.04 11 9.16 10.88 9.3 10.74C9.43 10.62 9.58 10.42 9.72 10.26C9.86 10.1 9.9 9.98 10 9.78C10.1 9.58 10.05 9.42 9.98 9.28C9.91 9.14 9.36 7.79 9.13 7.25C8.91 6.72 8.68 6.8 8.52 6.79C8.36 6.78 8.18 6.78 8 6.78"/></svg>
          </a>
          <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="https://facebook.com" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </a>
        </div>
      </div>

      <!-- Col 2: Services -->
      <div>
        <div class="footer-col-h">Kerala Cab Services</div>
        <ul class="footer-links-list">
          <li><a href="search-results.html?service=airport">Cochin Airport (COK) Taxi</a></li>
          <li><a href="search-results.html?service=airport">Trivandrum (TRV) Airport Cabs</a></li>
          <li><a href="search-results.html?service=outstation">Outstation Round Trips &amp; One-Way</a></li>
          <li><a href="search-results.html">Hourly City Cab Rental</a></li>
          <li><a href="search-results.html">Munnar &amp; Hill Station Tours</a></li>
          <li><a href="search-results.html">Alleppey Backwater Transfers</a></li>
        </ul>
      </div>

      <!-- Col 3: Quick Navigation -->
      <div>
        <div class="footer-col-h">Quick Links</div>
        <ul class="footer-links-list">
          <li><a href="index.html">Home</a></li>
          <li><a href="search-results.html">Explore Cab Fleet</a></li>
          <li><a href="index.html#howitworks">How It Works</a></li>
          <li><a href="index.html#policies">Rental Policies &amp; FAQ</a></li>
          <li><a href="index.html#depots">Kerala Hubs &amp; Coverage</a></li>
          <li><a href="blog.html">Travel Blog &amp; Tips</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>

      <!-- Col 4: Contact HQ -->
      <div>
        <div class="footer-col-h">24/7 Kerala HQ</div>
        <ul class="footer-links-list footer-contact-list">
          <li>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#69c8e2" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>JNI Stadium Complex, Kaloor, Kochi, Kerala — 682017</span>
          </li>
          <li>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#69c8e2" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <a href="tel:+917034060000">+91 70340 60000</a>
          </li>
          <li>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#69c8e2" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            <a href="mailto:info@hyrecabs.com">info@hyrecabs.com</a>
          </li>
          <li>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#69c8e2" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20M2 12h20"/></svg>
            <a href="https://hyrecabs.com">www.hyrecabs.com</a>
          </li>
        </ul>
        <div class="footer-badge-pill">
          <span class="badge-dot"></span>
          <span>Verified Kerala Cab Network</span>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="footer-bottom-bar">
      <p class="footer-copy">© 2026 HyreCabs. All Rights Reserved. Crafted with excellence by Zeekoi Enterprise Solutions.</p>
      <div class="footer-legal-links">
        <a href="index.html#policies">Privacy Policy</a>
        <a href="index.html#policies">Terms of Service</a>
        <a href="index.html#policies">Rental Guidelines</a>
        <a href="contact.html">Support</a>
      </div>
    </div>
  </div>
</footer>
"""

NAV_JS = """
  // Mobile navigation drawer toggle
  (function () {
    const toggle = document.getElementById('navToggle');
    const nav = document.getElementById('primaryNav');
    const backdrop = document.getElementById('navBackdrop');
    if (!toggle || !nav) return;

    function setOpen(open) {
      nav.classList.toggle('open', open);
      toggle.classList.toggle('open', open);
      if (backdrop) backdrop.classList.toggle('show', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.style.overflow = open ? 'hidden' : '';
    }

    toggle.addEventListener('click', () => setOpen(!nav.classList.contains('open')));
    if (backdrop) backdrop.addEventListener('click', () => setOpen(false));
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setOpen(false); });
    window.addEventListener('resize', () => { if (window.innerWidth > 900) setOpen(false); });
  })();
"""

def update_search_results():
    with open('search-results.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Append CSS before </style>
    content = content.replace('</style>', UNIFIED_HEADER_CSS + '\n</style>', 1)

    # Replace Header HTML
    header_pattern = r'<!-- HEADER -->\s*<header class="site-header">.*?</header>\s*<div class="nav-backdrop" id="navBackdrop"></div>'
    new_header = generate_header_html(active_item="fleet")
    content = re.sub(header_pattern, new_header, content, count=1, flags=re.DOTALL)

    # Replace Footer HTML
    footer_pattern = r'<!-- FOOTER -->\s*<footer class="site-footer">.*?</footer>'
    content = re.sub(footer_pattern, UNIFIED_FOOTER_HTML, content, count=1, flags=re.DOTALL)

    with open('search-results.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("search-results.html updated!")

def update_booking():
    with open('booking.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Append CSS before </style>
    content = content.replace('</style>', UNIFIED_HEADER_CSS + '\n</style>', 1)

    # Replace Header HTML
    header_pattern = r'<!-- HEADER -->\s*<header class="site-header">.*?</header>'
    new_header = generate_header_html(active_item="fleet")
    content = re.sub(header_pattern, new_header, content, count=1, flags=re.DOTALL)

    # Add Footer before </main> or after </main>
    assert '</main>' in content, "booking.html missing </main>"
    content = content.replace('</main>', '</main>\n' + UNIFIED_FOOTER_HTML, 1)

    # Add Nav JS before </script>
    content = content.replace('</script>', NAV_JS + '\n</script>', 1)

    with open('booking.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("booking.html updated!")

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace email
    content = content.replace('info@kottayamrentals.com', 'info@hyrecabs.com')

    # Append CSS before </style>
    content = content.replace('</style>', UNIFIED_HEADER_CSS + '\n</style>', 1)

    # Replace Header HTML
    header_pattern = r'<header class="site-header">.*?</header>\s*<div class="nav-backdrop" id="navBackdrop"></div>'
    new_header = generate_header_html(active_item="contact")
    content = re.sub(header_pattern, new_header, content, count=1, flags=re.DOTALL)

    # Replace Footer HTML
    footer_pattern = r'<footer class="site-footer">.*?</footer>'
    content = re.sub(footer_pattern, UNIFIED_FOOTER_HTML, content, count=1, flags=re.DOTALL)

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("contact.html updated!")

def update_blog():
    with open('blog.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Append CSS before </style>
    content = content.replace('</style>', UNIFIED_HEADER_CSS + '\n</style>', 1)

    # Replace Header HTML
    header_pattern = r'<header class="site-header">.*?</header>\s*<div class="nav-backdrop" id="navBackdrop"></div>'
    new_header = generate_header_html(active_item="blog")
    content = re.sub(header_pattern, new_header, content, count=1, flags=re.DOTALL)

    # Replace Footer HTML
    footer_pattern = r'<footer class="site-footer">.*?</footer>'
    content = re.sub(footer_pattern, UNIFIED_FOOTER_HTML, content, count=1, flags=re.DOTALL)

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("blog.html updated!")

if __name__ == '__main__':
    update_search_results()
    update_booking()
    update_contact()
    update_blog()
