import re

new_css = """  /* =========================================================
     HYRECABS PREMIER STANDARD HERO BANNER (Top-Tier UI/UX)
     ========================================================= */
  .std-hero {
    position: relative;
    margin-top: 78px;
    background: #050e18;
    color: #ffffff;
    padding: 42px 0 56px;
    overflow: visible;
    isolation: isolate;
  }
  .std-hero-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
  }
  .std-hero-bg-photo {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 36%;
    opacity: 0.16;
    filter: saturate(1.2) brightness(0.8);
    mask-image: radial-gradient(ellipse 90% 70% at 70% 35%, black 25%, transparent 82%);
    -webkit-mask-image: radial-gradient(ellipse 90% 70% at 70% 35%, black 25%, transparent 82%);
  }
  .std-hero-bg-glow-1 {
    position: absolute;
    top: -12%;
    right: 6%;
    width: 640px;
    height: 640px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(105, 200, 226, 0.22) 0%, rgba(20, 80, 115, 0.08) 45%, transparent 70%);
    filter: blur(54px);
  }
  .std-hero-bg-glow-2 {
    position: absolute;
    bottom: -15%;
    left: -5%;
    width: 540px;
    height: 540px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(15, 45, 75, 0.45) 0%, transparent 65%);
    filter: blur(60px);
  }
  .std-hero-grid-lines {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 52px 52px;
    mask-image: radial-gradient(ellipse 75% 65% at 50% 45%, black 25%, transparent 75%);
    -webkit-mask-image: radial-gradient(ellipse 75% 65% at 50% 45%, black 25%, transparent 75%);
  }

  .std-hero-inner {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    gap: 36px;
  }

  /* --- Top Stage: Story on Left, Car Podium on Right --- */
  .std-stage {
    display: grid;
    grid-template-columns: minmax(0, 1.15fr) minmax(460px, 1fr);
    gap: 40px 52px;
    align-items: center;
  }

  .std-copy {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  .std-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(105, 200, 226, 0.12);
    border: 1px solid rgba(105, 200, 226, 0.32);
    color: #7fd4ea;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .std-pill-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #69c8e2;
    box-shadow: 0 0 10px #69c8e2;
    animation: pulseDot 2s ease-in-out infinite;
  }
  @keyframes pulseDot {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.35); opacity: 0.6; }
  }

  .std-title {
    margin: 0 0 16px;
    font-size: clamp(34px, 4.4vw, 54px);
    font-weight: 850;
    letter-spacing: -1.3px;
    line-height: 1.08;
    color: #ffffff;
    text-wrap: balance;
  }
  .std-title-cyan {
    background: linear-gradient(135deg, #ffffff 15%, #92def1 50%, #69c8e2 85%, #3fb6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }

  .std-lead {
    margin: 0 0 24px;
    font-size: 15.5px;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.82);
    max-width: 530px;
  }

  .std-cta-group {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 22px;
  }
  .std-cta-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    min-height: 48px;
    padding: 0 26px;
    border-radius: 999px;
    background: linear-gradient(135deg, #8fe0f5 0%, #69c8e2 48%, #36b0ce 100%);
    color: #06111e;
    font-size: 14.5px;
    font-weight: 800;
    line-height: 1;
    box-shadow: 0 10px 24px rgba(105, 200, 226, 0.32);
    transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
    text-decoration: none;
  }
  .std-cta-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 16px 32px rgba(105, 200, 226, 0.44);
    background: linear-gradient(135deg, #a4e7f8 0%, #7fd4ea 50%, #46bcd9 100%);
  }
  .std-link-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    min-height: 48px;
    padding: 0 20px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.14);
    color: rgba(255, 255, 255, 0.9);
    font-size: 14px;
    font-weight: 700;
    text-decoration: none;
    transition: background 0.18s, border-color 0.18s, color 0.18s;
  }
  .std-link-btn:hover {
    background: rgba(255, 255, 255, 0.12);
    border-color: rgba(105, 200, 226, 0.4);
    color: #7fd4ea;
  }

  .std-social-proof {
    display: flex;
    align-items: center;
    gap: 12px;
    color: rgba(255, 255, 255, 0.72);
    font-size: 13px;
  }
  .std-star-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(245, 158, 11, 0.14);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #fbbf24;
    font-weight: 800;
    font-size: 12px;
  }
  .std-proof-text strong {
    color: #ffffff;
  }

  /* --- Right Stage: Showcase Vehicle --- */
  .std-showcase {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    width: 100%;
    min-width: 0;
  }
  .std-script {
    text-align: right;
    margin-bottom: -6px;
    z-index: 2;
  }
  .std-script-title {
    display: block;
    font-family: 'Great Vibes', cursive;
    font-size: clamp(38px, 4.4vw, 56px);
    line-height: 1.1;
    color: #7ec8e8;
    text-shadow: 0 4px 20px rgba(4, 20, 32, 0.4);
  }
  .std-script-sub {
    display: inline-block;
    margin-top: 4px;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.45);
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.88);
  }

  .std-car-podium {
    position: relative;
    width: 100%;
    max-width: 530px;
    min-height: 250px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .std-podium-glow {
    position: absolute;
    left: 50%;
    bottom: 22px;
    transform: translateX(-50%);
    width: 88%;
    height: 70px;
    border-radius: 50%;
    background: radial-gradient(ellipse, rgba(105, 200, 226, 0.32) 0%, rgba(20, 70, 100, 0.12) 50%, transparent 75%);
    filter: blur(16px);
    pointer-events: none;
  }
  .std-car-img-wrap {
    position: relative;
    z-index: 2;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .std-car-img {
    width: 100%;
    max-height: 240px;
    object-fit: contain;
    filter: drop-shadow(0 20px 24px rgba(0, 0, 0, 0.45));
    transition: opacity 0.25s ease, transform 0.25s ease;
  }
  .std-car-shadow {
    position: absolute;
    left: 50%;
    bottom: 12px;
    transform: translateX(-50%);
    width: 78%;
    height: 22px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.65);
    filter: blur(10px);
    z-index: 1;
  }

  .std-float-badge {
    position: absolute;
    z-index: 3;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 14px;
    border-radius: 14px;
    background: rgba(8, 20, 32, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.14);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    color: #ffffff;
    font-size: 12px;
    line-height: 1.25;
    animation: floatBadge 4.5s ease-in-out infinite;
  }
  .std-float-left {
    top: 24px;
    left: -8px;
    animation-delay: 0s;
  }
  .std-float-right {
    bottom: 24px;
    right: 4px;
    animation-delay: 2.25s;
  }
  @keyframes floatBadge {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
  .std-badge-icon {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: rgba(105, 200, 226, 0.18);
    color: #69c8e2;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .std-badge-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22c55e;
    box-shadow: 0 0 8px #22c55e;
    flex-shrink: 0;
  }
  .std-float-badge strong {
    display: block;
    font-size: 12px;
    font-weight: 700;
    color: #ffffff;
  }
  .std-float-badge span {
    display: block;
    font-size: 10.5px;
    color: rgba(255, 255, 255, 0.65);
  }

  .std-vehicle-switcher {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 6px;
    z-index: 2;
  }
  .std-switch-btn {
    border: none;
    background: transparent;
    color: rgba(255, 255, 255, 0.68);
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 999px;
    cursor: pointer;
    font-family: inherit;
    transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  }
  .std-switch-btn:hover {
    color: #ffffff;
  }
  .std-switch-btn.active {
    background: rgba(105, 200, 226, 0.18);
    color: #7fd4ea;
    box-shadow: inset 0 0 0 1px rgba(105, 200, 226, 0.4);
  }

  /* --- COMMAND BOOKING CONSOLE (Horizontal Bar) --- */
  .std-booking-console {
    width: 100%;
    position: relative;
    z-index: 10;
  }
  .std-booking-form {
    background: rgba(10, 22, 36, 0.9);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1.5px solid rgba(105, 200, 226, 0.24);
    border-radius: 22px;
    padding: 18px 22px 16px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.46), 0 0 0 1px rgba(255, 255, 255, 0.05);
  }

  .std-tabs-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }
  .std-tab {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: transparent;
    border: 1px solid transparent;
    border-radius: 999px;
    padding: 7px 16px;
    color: rgba(255, 255, 255, 0.68);
    font-size: 13px;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    transition: all 0.18s ease;
  }
  .std-tab:hover {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.05);
  }
  .std-tab.active {
    background: rgba(105, 200, 226, 0.16);
    border-color: rgba(105, 200, 226, 0.38);
    color: #7fd4ea;
  }

  /* Form Grid: 4 fields + 1 search button */
  .std-search-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr) auto minmax(0, 1.15fr) auto minmax(0, 1.15fr) auto;
    align-items: center;
    gap: 12px;
  }

  .std-cell {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.04);
    border: 1.5px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    min-height: 54px;
    transition: border-color 0.18s, background 0.18s, box-shadow 0.18s;
  }
  .std-cell:hover,
  .std-cell:focus-within {
    border-color: #69c8e2;
    background: rgba(105, 200, 226, 0.06);
    box-shadow: 0 0 0 3px rgba(105, 200, 226, 0.12);
  }
  .std-cell-icon {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: rgba(105, 200, 226, 0.14);
    color: #69c8e2;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .std-cell-content {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    text-align: left;
  }
  .std-cell-content label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.55);
    margin-bottom: 2px;
    line-height: 1;
    cursor: pointer;
  }
  .std-cell .picker-trigger {
    background: transparent;
    border: none;
    padding: 0;
    min-height: 26px;
    color: #ffffff;
    font-family: inherit;
    font-size: 14px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    width: 100%;
    cursor: pointer;
    text-align: left;
  }
  .std-cell .picker-trigger .picker-value {
    color: #ffffff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .std-cell .picker-caret {
    margin-left: auto;
    color: rgba(255, 255, 255, 0.45);
    flex-shrink: 0;
  }

  /* Date + Time combined cell */
  .std-cell-datetime .datetime-box {
    display: flex;
    align-items: center;
    gap: 6px;
    min-width: 0;
    background: transparent;
    border: none;
    padding: 0;
    min-height: 26px;
  }
  .std-cell-datetime .datetime-box .search-field {
    border: none;
    padding: 0;
    flex: 1 1 auto;
    min-width: 0;
  }
  .std-cell-datetime .datetime-box .search-field[data-picker="time"] {
    flex: 0 0 auto;
  }
  .std-dt-sep {
    color: rgba(255, 255, 255, 0.25);
    font-weight: 300;
    font-size: 13px;
  }

  .std-cell-divider {
    width: 1px;
    height: 34px;
    background: rgba(255, 255, 255, 0.08);
  }

  .std-search-action {
    display: flex;
    align-items: center;
  }
  .std-search-submit {
    min-height: 54px;
    padding: 0 24px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, #8fe0f5 0%, #69c8e2 50%, #36b0ce 100%);
    color: #06111e;
    font-family: inherit;
    font-size: 15px;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 0 8px 22px rgba(105, 200, 226, 0.35);
    transition: transform 0.18s, box-shadow 0.18s, background 0.18s;
  }
  .std-search-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(105, 200, 226, 0.48);
    background: linear-gradient(135deg, #a4e7f8 0%, #7fd4ea 50%, #46bcd9 100%);
  }

  /* Booking footer note strip */
  .std-booking-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 12.5px;
    color: rgba(255, 255, 255, 0.72);
  }
  .std-foot-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .std-foot-item svg { flex-shrink: 0; }
  .std-foot-center {
    color: rgba(255, 255, 255, 0.85);
  }
  .std-foot-right {
    color: rgba(255, 255, 255, 0.9);
    font-weight: 600;
  }

  /* --- 4 VALUE PILLARS (Clean Standard Cards) --- */
  .std-features-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    width: 100%;
  }
  .std-feat-card {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 18px 20px;
    border-radius: 18px;
    background: rgba(10, 22, 36, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }
  .std-feat-card:hover {
    transform: translateY(-3px);
    border-color: rgba(105, 200, 226, 0.35);
    box-shadow: 0 14px 32px rgba(0, 0, 0, 0.32);
  }
  .std-feat-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(105, 200, 226, 0.22) 0%, rgba(20, 90, 120, 0.3) 100%);
    border: 1px solid rgba(105, 200, 226, 0.28);
    color: #7fd4ea;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .std-feat-body {
    min-width: 0;
  }
  .std-feat-body strong {
    display: block;
    font-size: 14.5px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 2px;
  }
  .std-feat-body span {
    display: block;
    font-size: 11.5px;
    font-weight: 700;
    color: #69c8e2;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .std-feat-body p {
    margin: 0;
    font-size: 12px;
    line-height: 1.45;
    color: rgba(255, 255, 255, 0.65);
  }

  /* --- RESPONSIVE BREAKPOINTS --- */
  @media (max-width: 1160px) {
    .std-search-grid {
      grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
      row-gap: 12px;
    }
    .std-cell-divider:nth-of-type(2) {
      display: none;
    }
    .std-search-action {
      grid-column: span 3;
    }
    .std-search-submit {
      width: 100%;
    }
    .std-features-row {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 960px) {
    .std-stage {
      grid-template-columns: 1fr;
      gap: 24px;
    }
    .std-showcase {
      align-items: center;
      margin-top: 10px;
    }
    .std-script {
      text-align: center;
    }
    .std-car-podium {
      max-width: 440px;
      min-height: 220px;
    }
    .std-float-left { left: 0; top: 10px; }
    .std-float-right { right: 0; bottom: 10px; }
    .std-booking-footer {
      flex-direction: column;
      align-items: flex-start;
      gap: 8px;
    }
  }

  @media (max-width: 768px) {
    .std-hero {
      margin-top: 70px;
      padding: 26px 0 42px;
    }
    .std-title {
      font-size: 30px;
      letter-spacing: -0.8px;
    }
    .std-lead {
      font-size: 14.5px;
    }
    .std-booking-form {
      padding: 16px 14px 14px;
      border-radius: 18px;
    }
    .std-tabs-bar {
      overflow-x: auto;
      scrollbar-width: none;
      padding-bottom: 8px;
    }
    .std-tabs-bar::-webkit-scrollbar { display: none; }
    .std-tab {
      white-space: nowrap;
      padding: 6px 12px;
      font-size: 12px;
    }
    .std-search-grid {
      grid-template-columns: 1fr;
      gap: 10px;
    }
    .std-cell-divider {
      display: none;
    }
    .std-search-action {
      grid-column: span 1;
    }
    .std-search-submit {
      width: 100%;
      min-height: 48px;
    }
    .std-features-row {
      grid-template-columns: 1fr;
      gap: 12px;
    }
    .std-feat-card {
      padding: 14px 16px;
    }
    .std-float-badge {
      display: none;
    }
    .std-car-podium {
      max-width: 340px;
      min-height: 180px;
    }
    .std-car-img {
      max-height: 180px;
    }
    .std-vehicle-switcher {
      width: 100%;
      justify-content: center;
    }
    .std-switch-btn {
      flex: 1 1 auto;
      text-align: center;
      padding: 6px 8px;
      font-size: 11px;
    }
  }
"""

new_html = """  <!-- HERO BANNER (Standard Luxury UI/UX) -->
  <section class="std-hero" aria-label="HyreCabs Kerala Cab Rentals">
    <div class="std-hero-bg" aria-hidden="true">
      <img src="images/hero-kerala-scenic.jpg" alt="" class="std-hero-bg-photo" />
      <div class="std-hero-bg-glow-1"></div>
      <div class="std-hero-bg-glow-2"></div>
      <div class="std-hero-grid-lines"></div>
    </div>

    <div class="container std-hero-inner">
      <!-- TOP STAGE: Headline & Story on Left + Car Showcase on Right -->
      <div class="std-stage">
        <div class="std-copy">
          <div class="std-pill">
            <span class="std-pill-dot"></span>
            <span>Premium Cab Rentals • Kerala</span>
          </div>

          <h1 class="std-title">
            More Than a Ride.<br />
            <span class="std-title-cyan">It’s a Kerala Experience.</span>
          </h1>

          <p class="std-lead">
            From misty hills to coastal towns, HyreCabs makes every journey across Kerala smooth, safe and memorable.
          </p>

          <div class="std-cta-group">
            <a href="#heroSearchForm" class="std-cta-btn">
              <span>Explore Our Services</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
            </a>
            <a href="#howitworks" class="std-link-btn">
              <span>How It Works</span>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
            </a>
          </div>

          <div class="std-social-proof">
            <div class="std-avatars">
              <span class="std-star-badge">★ 4.9/5</span>
            </div>
            <div class="std-proof-text">
              <strong>Trusted by 25,000+ travelers</strong> across Kerala
            </div>
          </div>
        </div>

        <!-- CAR SHOWCASE ON RIGHT -->
        <div class="std-showcase">
          <div class="std-script" aria-hidden="true">
            <span class="std-script-title">Kerala Awaits</span>
            <span class="std-script-sub">TRAVEL WITH HYRECABS</span>
          </div>

          <div class="std-car-podium">
            <div class="std-podium-glow" aria-hidden="true"></div>
            <div class="std-car-img-wrap">
              <img src="images/hero_car.png" alt="HyreCabs Premium SUV" id="stdCarImg" class="std-car-img" />
            </div>
            <div class="std-car-shadow" aria-hidden="true"></div>

            <!-- Floating Trust Badges on Vehicle -->
            <div class="std-float-badge std-float-left">
              <div class="std-badge-icon" aria-hidden="true">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>
              </div>
              <div>
                <strong>Verified Chauffeur</strong>
                <span>Sanitized &amp; GPS Tracked</span>
              </div>
            </div>

            <div class="std-float-badge std-float-right">
              <div class="std-badge-dot" aria-hidden="true"></div>
              <div>
                <strong id="stdCarTitle">Toyota Innova Hycross</strong>
                <span id="stdCarPrice">From ₹2,499/day</span>
              </div>
            </div>
          </div>

          <!-- Vehicle switcher pills -->
          <div class="std-vehicle-switcher" role="tablist" aria-label="Select vehicle preview">
            <button type="button" class="std-switch-btn active" data-car="suv" onclick="selectStdCar('suv')">
              <span>Premium SUV</span>
            </button>
            <button type="button" class="std-switch-btn" data-car="sedan" onclick="selectStdCar('sedan')">
              <span>Executive Sedan</span>
            </button>
            <button type="button" class="std-switch-btn" data-car="taxi" onclick="selectStdCar('taxi')">
              <span>City Taxi</span>
            </button>
          </div>
        </div>
      </div>

      <!-- COMMAND BOOKING ENGINE BAR -->
      <div class="std-booking-console">
        <form action="search-results.html" method="GET" class="std-booking-form" id="heroSearchForm">
          <!-- Service Type Tabs -->
          <div class="std-tabs-bar">
            <button type="button" class="std-tab active" data-mode="outstation" onclick="setTripMode('outstation')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 17h14v-5l-2-5H7L5 12v5z"/><circle cx="7.5" cy="17.5" r="1.5"/><circle cx="16.5" cy="17.5" r="1.5"/></svg>
              <span>Outstation Cab</span>
            </button>
            <button type="button" class="std-tab" data-mode="airport" onclick="setTripMode('airport')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>
              <span>Airport Transfer</span>
            </button>
            <button type="button" class="std-tab" data-mode="local" onclick="setTripMode('local')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
              <span>Hourly Rental</span>
            </button>
          </div>

          <!-- The 4 Search Field Blocks + CTA in horizontal bar -->
          <div class="std-search-grid">
            <!-- Field 1: Pickup Location -->
            <div class="std-cell search-field" data-picker="place">
              <div class="std-cell-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </div>
              <div class="std-cell-content">
                <label>Pick-up Location</label>
                <button type="button" class="picker-trigger" aria-haspopup="listbox" aria-expanded="false">
                  <span class="picker-value" data-display>Kochi — Kaloor</span>
                  <svg class="picker-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <input type="hidden" name="pickup" value="Kochi — Kaloor" data-hidden />
                <div class="picker-panel place-panel" role="listbox" aria-label="Choose pickup location"></div>
              </div>
            </div>

            <div class="std-cell-divider" aria-hidden="true"></div>

            <!-- Field 2: Drop-off Location -->
            <div class="std-cell search-field" data-picker="place">
              <div class="std-cell-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
              </div>
              <div class="std-cell-content">
                <label>Drop-off Location</label>
                <button type="button" class="picker-trigger" aria-haspopup="listbox" aria-expanded="false">
                  <span class="picker-value" data-display>Kottayam</span>
                  <svg class="picker-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <input type="hidden" name="dropoff" value="Kottayam" data-hidden />
                <div class="picker-panel place-panel" role="listbox" aria-label="Choose drop-off location"></div>
              </div>
            </div>

            <div class="std-cell-divider" aria-hidden="true"></div>

            <!-- Field 3: Pickup Date & Time -->
            <div class="std-cell std-cell-datetime search-datetime">
              <div class="std-cell-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
              </div>
              <div class="std-cell-content">
                <label>Pick-up Date &amp; Time</label>
                <div class="datetime-box">
                  <div class="search-field" data-picker="date">
                    <button type="button" class="picker-trigger" aria-haspopup="dialog" aria-expanded="false">
                      <span class="picker-value" data-display>10 Sep 2026</span>
                    </button>
                    <input type="hidden" name="startDate" value="2026-09-10" data-hidden />
                    <div class="picker-panel date-panel" role="dialog" aria-label="Choose start date"></div>
                  </div>
                  <span class="std-dt-sep">|</span>
                  <div class="search-field" data-picker="time">
                    <button type="button" class="picker-trigger" aria-haspopup="listbox" aria-expanded="false">
                      <span class="picker-value" data-display>10:00 AM</span>
                      <svg class="picker-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
                    </button>
                    <input type="hidden" name="startTime" value="10:00 AM" data-hidden />
                    <div class="picker-panel time-panel" role="listbox" aria-label="Choose start time"></div>
                  </div>
                </div>
              </div>
            </div>

            <div class="std-cell-divider" aria-hidden="true"></div>

            <!-- Field 4: Drop-off Date & Time -->
            <div class="std-cell std-cell-datetime search-datetime">
              <div class="std-cell-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
              </div>
              <div class="std-cell-content">
                <label>Drop-off Date &amp; Time</label>
                <div class="datetime-box">
                  <div class="search-field" data-picker="date">
                    <button type="button" class="picker-trigger" aria-haspopup="dialog" aria-expanded="false">
                      <span class="picker-value" data-display>13 Sep 2026</span>
                    </button>
                    <input type="hidden" name="endDate" value="2026-09-13" data-hidden />
                    <div class="picker-panel date-panel" role="dialog" aria-label="Choose end date"></div>
                  </div>
                  <span class="std-dt-sep">|</span>
                  <div class="search-field" data-picker="time">
                    <button type="button" class="picker-trigger" aria-haspopup="listbox" aria-expanded="false">
                      <span class="picker-value" data-display>10:00 AM</span>
                      <svg class="picker-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
                    </button>
                    <input type="hidden" name="endTime" value="10:00 AM" data-hidden />
                    <div class="picker-panel time-panel" role="listbox" aria-label="Choose end time"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- CTA Button -->
            <div class="std-search-action">
              <button type="submit" class="std-search-submit">
                <span>Find My Cab</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
              </button>
            </div>
          </div>

          <!-- Footnote Strip -->
          <div class="std-booking-footer">
            <div class="std-foot-item">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
              <span>Driver age: <strong>21+</strong></span>
            </div>
            <div class="std-foot-item std-foot-center">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Free cancellation up to 6 hours before pickup</span>
            </div>
            <div class="std-foot-item std-foot-right">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" color="#69c8e2" aria-hidden="true"><path d="M12 21c-.4 0-4-2.2-5.8-6.1C4.7 11.6 5.2 8.4 7 7.2c1.1-.7 2.4-.4 3.2.4.3-.9 1-2.3 2.4-3.1 1.7-1 3.5-.3 4.4 1.1.8 1.2.8 2.9.1 4.5 1.5-.1 2.7.7 3.1 2 .6 1.9-.5 4.1-2.9 5.4C15.2 19.5 12.4 21 12 21z"/><path d="M12 10v11" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
              <span>Trusted by thousands across Kerala</span>
            </div>
          </div>
        </form>
      </div>

      <!-- THE 4 VALUE PILLARS (Clean Standard Cards) -->
      <div class="std-features-row">
        <div class="std-feat-card">
          <div class="std-feat-icon" aria-hidden="true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>
          </div>
          <div class="std-feat-body">
            <strong>Safe &amp; Reliable</strong>
            <span>Verified Drivers</span>
            <p>Police-cleared &amp; courteous local drivers for total peace of mind.</p>
          </div>
        </div>

        <div class="std-feat-card">
          <div class="std-feat-icon" aria-hidden="true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 17h14v-5l-2-5H7L5 12v5z"/><circle cx="7.5" cy="17.5" r="1.5"/><circle cx="16.5" cy="17.5" r="1.5"/></svg>
          </div>
          <div class="std-feat-body">
            <strong>Wide Range</strong>
            <span>Sedans to SUVs</span>
            <p>Hatchbacks, Executive Sedans, Innova Hycross &amp; Luxury Vans.</p>
          </div>
        </div>

        <div class="std-feat-card">
          <div class="std-feat-icon" aria-hidden="true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
          </div>
          <div class="std-feat-body">
            <strong>On-Time Pickup</strong>
            <span>Always on Schedule</span>
            <p>Punctual arrivals at your door or airport terminal, 24/7/365.</p>
          </div>
        </div>

        <div class="std-feat-card">
          <div class="std-feat-icon" aria-hidden="true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div class="std-feat-body">
            <strong>Across Kerala</strong>
            <span>Major Cities &amp; Towns</span>
            <p>Cochin Airport, Kottayam, Kollam, Munnar &amp; all 14 districts.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

new_js = """
  // Standard Hero Vehicle Switcher
  function selectStdCar(type) {
    const img = document.getElementById('stdCarImg');
    const title = document.getElementById('stdCarTitle');
    const price = document.getElementById('stdCarPrice');
    const btns = document.querySelectorAll('.std-switch-btn');
    
    btns.forEach(b => b.classList.toggle('active', b.getAttribute('data-car') === type));
    
    if (img) {
      img.style.opacity = '0';
      img.style.transform = 'scale(0.96) translateY(4px)';
      setTimeout(() => {
        if (type === 'suv') {
          img.src = 'images/hero_car.png';
          img.alt = 'HyreCabs Toyota Innova Hycross';
          if (title) title.textContent = 'Toyota Innova Hycross';
          if (price) price.textContent = 'From ₹2,499/day';
        } else if (type === 'sedan') {
          img.src = 'images/car_luxury.png';
          img.alt = 'HyreCabs Executive Sedan';
          if (title) title.textContent = 'Executive Luxury Sedan';
          if (price) price.textContent = 'From ₹1,999/day';
        } else if (type === 'taxi') {
          img.src = 'images/car_sedan.png';
          img.alt = 'HyreCabs City Taxi';
          if (title) title.textContent = 'HyreCabs City Taxi';
          if (price) price.textContent = 'From ₹1,499/day';
        }
        img.style.opacity = '1';
        img.style.transform = 'scale(1) translateY(0)';
      }, 160);
    }
  }

  // Trip Mode Selector (Outstation, Airport, Local)
  function setTripMode(mode) {
    document.querySelectorAll('.std-tab').forEach(t => {
      t.classList.toggle('active', t.getAttribute('data-mode') === mode);
    });
    const dropField = document.querySelectorAll('.search-field[data-picker="place"]')[1];
    if (dropField) {
      const display = dropField.querySelector('[data-display]');
      const hidden = dropField.querySelector('[data-hidden]');
      if (mode === 'airport') {
        if (display) display.textContent = 'Cochin Airport (COK)';
        if (hidden) hidden.value = 'Cochin Airport (COK)';
      } else if (mode === 'outstation') {
        if (display && display.textContent === 'Cochin Airport (COK)') {
          display.textContent = 'Kottayam';
          if (hidden) hidden.value = 'Kottayam';
        }
      }
    }
  }
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
css_start = content.find('/* Live UX hero — Kerala experience banner */')
css_end = content.find('.hero-visual-slot {')
assert css_start != -1 and css_end != -1, 'CSS markers not found'
content = content[:css_start] + new_css + content[css_end:]

# 2. Replace HTML
html_start = content.find('<!-- HERO — live Kerala UX banner -->')
html_end = content.find('<!-- Benefits — How It Works -->')
assert html_start != -1 and html_end != -1, 'HTML markers not found'
content = content[:html_start] + new_html + content[html_end:]

# 3. Clean up the debug script at bottom if present
debug_script = """<script>
(function () {
  var w = document.documentElement.clientWidth;
  var rows = [];
  document.querySelectorAll('body *').forEach(function (el) {
    var r = el.getBoundingClientRect();
    if (r.width > 440) {
      var name = (el.className && el.className.toString ? el.className.toString() : el.tagName).slice(0, 48);
      rows.push(Math.round(r.width) + ' ' + name);
    }
  });
  rows.sort();
  document.title = 'CW' + w + ' ' + rows.slice(-8).join(' || ');
})();
</script>"""
content = content.replace(debug_script, "")

# 4. Insert new JS before </script> at the end
last_script_end = content.rfind('</script>')
assert last_script_end != -1, 'closing script tag not found'
content = content[:last_script_end] + new_js + content[last_script_end:]

# 5. Fix <body class="ux-banner"> to <body class="std-banner-page">
content = content.replace('<body class="ux-banner">', '<body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html successfully!')
