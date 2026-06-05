import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The start marker
start_marker = "  /* Premium Cinematic Hero */"
end_marker = "  /* Premium Trust Section */"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

new_hero = """  /* Premium Cinematic Hero */
  .premium-hero {
    position: relative;
    width: 100vw;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: #050816;
  }

  /* Background Elements */
  .ph-glow {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 80vw; height: 80vh;
    background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.15) 0%, rgba(124, 58, 237, 0.1) 40%, transparent 70%);
    z-index: 1;
    pointer-events: none;
  }
  
  .ph-particles {
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.3;
    z-index: 1;
    pointer-events: none;
  }

  /* Two Column Layout */
  .ph-container {
    position: relative;
    z-index: 10;
    width: 100%;
    max-width: 1400px;
    padding: 0 40px;
    margin-top: 60px; /* Offset for nav */
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 60px;
    align-items: center;
  }

  @media (max-width: 1024px) {
    .ph-container {
      grid-template-columns: 1fr;
      text-align: center;
      gap: 40px;
      margin-top: 100px;
    }
  }

  /* Left Column: Content */
  .ph-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  
  @media (max-width: 1024px) {
    .ph-content {
      align-items: center;
    }
  }

  .ph-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 100px;
    color: #fff;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 24px;
    opacity: 0;
    transform: translateY(20px);
  }

  .ph-badge-dot {
    width: 6px; height: 6px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 10px #10b981;
    animation: pulseDot 2s infinite;
  }
  
  @keyframes pulseDot {
    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
    70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
  }

  .ph-title {
    font-family: var(--ff-head, 'Bebas Neue', sans-serif);
    font-size: clamp(3.5rem, 5vw, 6rem);
    line-height: 0.95;
    color: #fff;
    margin-bottom: 24px;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: left;
  }

  @media (max-width: 1024px) {
    .ph-title { text-align: center; }
  }

  .ph-title-line {
    display: block;
    overflow: hidden;
  }
  
  .ph-title-inner {
    display: block;
    opacity: 0;
    transform: translateY(100%);
  }

  .ph-highlight {
    background: linear-gradient(135deg, #60a5fa, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }

  .ph-subtitle {
    font-size: clamp(1.1rem, 1.3vw, 1.25rem);
    color: rgba(255, 255, 255, 0.7);
    max-width: 500px;
    margin-bottom: 32px;
    line-height: 1.6;
    opacity: 0;
    transform: translateY(20px);
    text-align: left;
  }

  @media (max-width: 1024px) {
    .ph-subtitle { text-align: center; }
  }

  .ph-actions {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 40px;
    opacity: 0;
    transform: translateY(20px);
  }

  @media (max-width: 1024px) {
    .ph-actions {
      justify-content: center;
      flex-wrap: wrap;
    }
  }

  .ph-btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 18px 40px;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 100px;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 15px 30px rgba(99, 102, 241, 0.2), inset 0 1px 0 rgba(255,255,255,0.2);
    position: relative;
    overflow: hidden;
  }

  .ph-btn-secondary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 18px 40px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 100px;
    text-decoration: none;
    transition: all 0.4s ease;
  }

  /* Trust Metrics */
  .ph-metrics {
    display: flex;
    align-items: center;
    gap: 32px;
    opacity: 0;
    transform: translateY(20px);
  }

  @media (max-width: 1024px) {
    .ph-metrics {
      justify-content: center;
      flex-wrap: wrap;
    }
  }

  .ph-metric-item {
    display: flex;
    align-items: center;
    gap: 10px;
    color: rgba(255,255,255,0.8);
    font-size: 0.95rem;
    font-weight: 500;
  }

  .ph-metric-icon {
    color: #a855f7;
  }

  /* Right Column: Video Frame */
  .ph-right {
    position: relative;
    display: flex;
    justify-content: flex-end;
    opacity: 0;
    transform: scale(0.95);
  }

  @media (max-width: 1024px) {
    .ph-right {
      justify-content: center;
    }
  }

  .ph-video-frame {
    position: relative;
    width: 100%;
    max-width: 500px;
    aspect-ratio: 4/5;
    border-radius: 24px;
    background: #000;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(124, 58, 237, 0.3);
    overflow: hidden;
    animation: floatFrame 6s ease-in-out infinite;
  }

  @keyframes floatFrame {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
  }

  .ph-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 1; /* Crisp */
  }

  /* Subtle gradient overlay to match aesthetic without losing sharpness */
  .ph-video-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 50%, rgba(5, 8, 22, 0.6) 100%);
    pointer-events: none;
  }

</style>

<section class="premium-hero" id="hero" aria-label="Hero section">
  
  <div class="ph-glow"></div>
  <div class="ph-particles"></div>

  <div class="ph-container">
    <!-- LEFT SIDE: Content -->
    <div class="ph-content">
      <div class="ph-badge" id="phBadge">
        <div class="ph-badge-dot"></div>
        Available For Projects
      </div>

      <h1 class="ph-title" id="phTitle">
        <span class="ph-title-line"><span class="ph-title-inner">TURN RAW FOOTAGE</span></span>
        <span class="ph-title-line"><span class="ph-title-inner">INTO CONTENT THAT</span></span>
        <span class="ph-title-line"><span class="ph-title-inner ph-highlight">DRIVES RESULTS</span></span>
      </h1>

      <p class="ph-subtitle" id="phSubtitle">
        Professional video editing for creators, brands and businesses.<br>
        Fast turnaround. Premium quality. Built for growth.
      </p>

      <div class="ph-actions" id="phActions">
        <a href="#contact" class="ph-btn-primary magnetic-btn">Get Free Quote</a>
        <a href="#showreel" class="ph-btn-secondary magnetic-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg>
          Watch Showreel
        </a>
      </div>

      <div class="ph-metrics" id="phMetrics">
        <div class="ph-metric-item">
          <svg class="ph-metric-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          500+ Projects Delivered
        </div>
        <div class="ph-metric-item">
          <svg class="ph-metric-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
          10M+ Views Generated
        </div>
        <div class="ph-metric-item">
          <svg class="ph-metric-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          48H Delivery
        </div>
      </div>
    </div>

    <!-- RIGHT SIDE: Video Showcase -->
    <div class="ph-right" id="phRight">
      <div class="ph-video-frame">
        <video class="ph-video" muted loop playsinline autoplay preload="auto">
          <source src="assets/posters/showreel-hero.mp4" type="video/mp4">
          <source src="https://cdn.coverr.co/videos/coverr-dark-abstract-background-2720/1080p.mp4" type="video/mp4">
        </video>
        <div class="ph-video-overlay"></div>
      </div>
    </div>
  </div>

</section>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    if (typeof gsap === 'undefined') return;

    // 1. Initial Load Animations
    const tl = gsap.timeline({ defaults: { ease: "power4.out" } });

    tl.to("#phBadge", { opacity: 1, y: 0, duration: 1 }, 0.2);

    // Staggered reveal of title lines from bottom
    tl.to(".ph-title-inner", { 
      opacity: 1, 
      y: 0, 
      duration: 1.2, 
      stagger: 0.15 
    }, 0.3);

    tl.to("#phSubtitle", { opacity: 1, y: 0, duration: 1 }, 0.7);
    tl.to("#phActions", { opacity: 1, y: 0, duration: 1 }, 0.9);
    tl.to("#phMetrics", { opacity: 1, y: 0, duration: 1 }, 1.1);

    // Reveal video frame
    tl.to("#phRight", { opacity: 1, scale: 1, duration: 1.5, ease: "back.out(1.2)" }, 0.5);

    // 2. Scroll Parallax Effect
    gsap.to(".ph-video-frame", {
      yPercent: 10,
      ease: "none",
      scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom top",
        scrub: true
      }
    });

    // 3. Magnetic Buttons Logic
    const magBtns = document.querySelectorAll('.magnetic-btn');
    magBtns.forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const h = rect.width / 2;
        const v = rect.height / 2;
        const x = e.clientX - rect.left - h;
        const y = e.clientY - rect.top - v;
        
        gsap.to(btn, {
          x: x * 0.3,
          y: y * 0.3,
          duration: 0.4,
          ease: "power2.out"
        });
      });
      
      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, {
          x: 0,
          y: 0,
          duration: 0.7,
          ease: "elastic.out(1, 0.3)"
        });
      });
    });
  });
</script>
"""

# Extract the script ending properly before "/* Premium Trust Section */"
# Wait, the end marker is inside a <style> block, so I should just split at the style block.
# Let's ensure the end_marker is exactly `<style>\n  /* Premium Trust Section */`
new_content = content[:start_idx] + new_hero + "\n<style>\n" + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hero layout replaced successfully!")
