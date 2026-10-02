/**
 * Prasanth & Karthesha Wedding Invitation Website (#PraKar)
 * Main Interactive Script
 * ========================================================
 */

(function () {
  'use strict';

  // Configuration reference
  const CONFIG = window.WEDDING_CONFIG || {};

  // DOM Elements Cache
  const welcomeScreen = document.getElementById('welcome-screen');
  const btnOpenInvitation = document.getElementById('btn-open-invitation');
  const divineOverlay = document.getElementById('divine-opening-overlay');
  const divineStage = document.getElementById('divine-anim-stage');
  const mainWebsite = document.getElementById('main-website');
  const musicFloatingBtn = document.getElementById('music-floating-btn');
  const bgAudio = document.getElementById('bg-wedding-audio');

  // Carousel Elements
  const carouselContainer = document.getElementById('carousel-container');
  const btnCarouselPrev = document.getElementById('carousel-btn-prev');
  const btnCarouselNext = document.getElementById('carousel-btn-next');
  const carouselPagination = document.getElementById('carousel-pagination');

  // Countdown Elements
  const countDays = document.getElementById('count-days');
  const countHours = document.getElementById('count-hours');
  const countMinutes = document.getElementById('count-minutes');
  const countSeconds = document.getElementById('count-seconds');
  const countGrid = document.getElementById('countdown-grid');
  const countFinishedMsg = document.getElementById('countdown-finished-msg');

  // WhatsApp Share Button
  const btnWhatsappShare = document.getElementById('btn-whatsapp-share');

  // Modal Elements
  const venueModal = document.getElementById('venue-details-modal');
  const btnCloseModal = document.getElementById('btn-close-modal');
  const btnViewWeddingVenue = document.getElementById('btn-view-wedding-venue');

  // Calendar Buttons
  const btnAddWeddingCal = document.getElementById('btn-add-wedding-cal');
  const btnAddReceptionCal = document.getElementById('btn-add-reception-cal');

  /* ==========================================================================
     1. BACKGROUND AUDIO & WEB AUDIO SYNTHESIZER FALLBACK
     ========================================================================== */
  let isAudioPlaying = false;
  let userEnabledMusic = false;
  let audioContext = null;
  let synthInterval = null;

  function isPageHidden() {
    return document.hidden || document.visibilityState === 'hidden';
  }

  function pauseMusicForBackground() {
    if (!userEnabledMusic) return;
    if (bgAudio && !bgAudio.paused) {
      bgAudio.pause();
    }
    if (audioContext && audioContext.state === 'running') {
      audioContext.suspend();
    }
  }

  function resumeMusicFromBackground() {
    if (!userEnabledMusic || isPageHidden()) return;
    if (audioContext) {
      if (audioContext.state === 'suspended') {
        audioContext.resume();
      }
      return;
    }
    if (bgAudio && bgAudio.paused) {
      const playPromise = bgAudio.play();
      if (playPromise !== undefined) {
        playPromise.catch(function () {});
      }
    }
  }

  function handlePageVisibilityChange() {
    if (isPageHidden()) {
      pauseMusicForBackground();
    } else {
      resumeMusicFromBackground();
    }
  }

  // Initialize and play audio
  function startWeddingMusic() {
    userEnabledMusic = true;
    if (isAudioPlaying) return;

    // First attempt HTML5 audio element
    if (bgAudio) {
      bgAudio.volume = 0.65;
      const playPromise = bgAudio.play();
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            isAudioPlaying = true;
            updateMusicButtonState(true);
            if (isPageHidden()) {
              pauseMusicForBackground();
            }
          })
          .catch((err) => {
            console.log('Audio file playback fallback to Web Audio synthesizer:', err);
            // Fallback to Web Audio Ambient Shehnai / Tanpura
            startWebAudioIndianDrone();
            isAudioPlaying = true;
            updateMusicButtonState(true);
          });
      }
    } else {
      startWebAudioIndianDrone();
      isAudioPlaying = true;
      updateMusicButtonState(true);
    }
  }

  // Soothing Indian classical Tanpura drone using Web Audio API
  function startWebAudioIndianDrone() {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      audioContext = new AudioCtx();

      // Master Gain
      const masterGain = audioContext.createGain();
      masterGain.gain.setValueAtTime(0.18, audioContext.currentTime);
      masterGain.connect(audioContext.destination);

      // Tanpura fundamental frequencies (Sa - Pa - Sa' in D / 146.83 Hz)
      const freqs = [146.83, 220.0, 293.66, 367.08];
      const oscillators = [];

      freqs.forEach((freq, idx) => {
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();
        osc.type = idx % 2 === 0 ? 'sine' : 'triangle';
        osc.frequency.setValueAtTime(freq, audioContext.currentTime);

        // Gentle tremolo modulation
        gain.gain.setValueAtTime(0.08, audioContext.currentTime);
        osc.connect(gain);
        gain.connect(masterGain);
        osc.start();
        oscillators.push({ osc, gain });
      });

      // Play soft occasional flute notes in Raag Yaman / Kalyani scale
      const swaras = [293.66, 329.63, 369.99, 415.3, 440.0, 493.88, 554.37, 587.33]; // D, E, F#, G#, A, B, C#, D'
      synthInterval = setInterval(() => {
        if (!isAudioPlaying || !audioContext) return;
        const note = swaras[Math.floor(Math.random() * swaras.length)];
        playFluteNote(audioContext, masterGain, note);
      }, 2400);

      window._droneOscillators = oscillators;
    } catch (e) {
      console.warn('Web Audio synthesis error:', e);
    }
  }

  function playFluteNote(ctx, dest, freq) {
    try {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, ctx.currentTime);

      const now = ctx.currentTime;
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.06, now + 0.4);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.2);

      osc.connect(gain);
      gain.connect(dest);
      osc.start(now);
      osc.stop(now + 2.3);
    } catch (e) {}
  }

  function stopWeddingMusic() {
    userEnabledMusic = false;
    if (bgAudio) {
      bgAudio.pause();
    }
    if (audioContext && audioContext.state === 'running') {
      audioContext.suspend();
    }
    isAudioPlaying = false;
    updateMusicButtonState(false);
  }

  function toggleWeddingMusic() {
    if (isAudioPlaying) {
      stopWeddingMusic();
    } else {
      userEnabledMusic = true;
      if (audioContext && audioContext.state === 'suspended') {
        audioContext.resume();
        isAudioPlaying = true;
        updateMusicButtonState(true);
      } else {
        startWeddingMusic();
      }
    }
  }

  function updateMusicButtonState(playing) {
    if (!musicFloatingBtn) return;
    const label = musicFloatingBtn.querySelector('.music-label');
    if (playing) {
      musicFloatingBtn.classList.add('playing');
      if (label) label.textContent = 'Pause Music';
    } else {
      musicFloatingBtn.classList.remove('playing');
      if (label) label.textContent = 'Play Music';
    }
  }

  if (musicFloatingBtn) {
    musicFloatingBtn.addEventListener('click', toggleWeddingMusic);
  }

  document.addEventListener('visibilitychange', handlePageVisibilityChange);
  window.addEventListener('pagehide', pauseMusicForBackground);
  window.addEventListener('pageshow', resumeMusicFromBackground);
  window.addEventListener('blur', pauseMusicForBackground);
  window.addEventListener('focus', resumeMusicFromBackground);

  /* ==========================================================================
     2. ENVELOPE OPENING & DIVINE OPENING SEQUENCE (8-Step Sacred Flow)
     ========================================================================== */
  const btnSkipDivine = document.getElementById('btn-skip-divine');
  let divineAnimationTimers = [];

  function clearDivineAnimation() {
    divineAnimationTimers.forEach(id => clearTimeout(id));
    divineAnimationTimers = [];
  }

  function skipDivineAnimation() {
    clearDivineAnimation();
    if (!divineOverlay) return;
    divineOverlay.classList.add('state-fade-out');
    if (mainWebsite) {
      mainWebsite.classList.add('visible');
    }
    setTimeout(() => {
      divineOverlay.style.display = 'none';
      if (welcomeScreen) welcomeScreen.style.display = 'none';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }, 600);
  }

  if (btnSkipDivine) {
    btnSkipDivine.addEventListener('click', skipDivineAnimation);
  }

  if (btnOpenInvitation) {
    btnOpenInvitation.addEventListener('click', function () {
      // 1. Play background music immediately on guest interaction
      startWeddingMusic();

      // 2. Animate envelope open
      welcomeScreen.classList.add('opened');

      // 3. Trigger Divine Rama & Sita Opening Animation
      setTimeout(() => {
        triggerDivineAnimation();
      }, 500);
    });
  }

  function triggerDivineAnimation() {
    if (!divineOverlay) return;
    clearDivineAnimation();

    // Reset any previous state classes
    divineOverlay.classList.remove(
      'state-fade-out', 'step-hands-enter', 'step-hands-join',
      'step-hands-meet', 'step-reveal-image', 'step-reveal-names'
    );
    divineOverlay.style.display = 'flex';

    // STEP 1 — DARK/DIVINE INTRO (t = 0)
    // Seamless entrance into deep sacred burgundy & gold ambiance
    divineOverlay.classList.add('active');

    // STEP 2 & STEP 3 — LORD RAMA & GODDESS SITA REAL HANDS APPEAR (t = 600ms)
    // Lord Rama's hand extends naturally from the left
    // Goddess Sita's hand extends gracefully from the right
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('step-hands-enter');
    }, 600));

    // STEP 4 — REALISTIC HAND JOINING (t = 2400ms)
    // Both real hand images slowly move toward each other
    // Sita's fingers gently rest right into Rama's cupped open palm
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('step-hands-join');
    }, 2400));

    // STEP 5 — HANDS JOIN & SACRED CONTACT GLOW (t = 4800ms)
    // The hands meet at the exact point of union:
    // Position is held in sacred peace; divine warm golden halo softly blossoms
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('step-hands-meet');
    }, 4800));

    // STEP 6 — TRANSITION TO REAL COMBINED RAMA & SITA IMAGE (t = 7000ms)
    // Joined hands gently dissolve upward as the full sacred portrait is revealed
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('step-reveal-image');
    }, 7000));

    // STEP 7 — SHOW COUPLE NAMES (t = 8200ms)
    // Elegant wedding typography: "Prasanth & Karthesha"
    // "With the Divine Blessings of Sri Sita Rama"
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('step-reveal-names');
    }, 8200));

    // STEP 8 — TRANSITION TO HOMEPAGE (t = 11400ms)
    // Smooth cinematic crossfade into the main wedding homepage without extra clicks
    divineAnimationTimers.push(setTimeout(() => {
      divineOverlay.classList.add('state-fade-out');
      if (mainWebsite) {
        mainWebsite.classList.add('visible');
      }

      // Hide overlay after smooth fade finishes
      divineAnimationTimers.push(setTimeout(() => {
        divineOverlay.style.display = 'none';
        if (welcomeScreen) welcomeScreen.style.display = 'none';
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }, 1400));
    }, 11400));
  }

  /* ==========================================================================
     3. HORIZONTAL PHOTO CAROUSEL (Auto-slide + Swipe/Drag + Loop)
     ========================================================================== */
  let isDragging = false;
  let startX = 0;
  let scrollLeftStart = 0;
  let autoSlideTimer = null;
  let currentSlideIndex = 0;

  function initCarousel() {
    if (!carouselContainer) return;

    const slides = carouselContainer.querySelectorAll('.carousel-slide');
    if (!slides.length) return;

    // Create pagination dots
    if (carouselPagination) {
      carouselPagination.innerHTML = '';
      slides.forEach((_, idx) => {
        const dot = document.createElement('button');
        dot.className = `carousel-dot ${idx === 0 ? 'active' : ''}`;
        dot.setAttribute('aria-label', `Go to slide ${idx + 1}`);
        dot.addEventListener('click', () => {
          goToSlide(idx);
          resetAutoSlide();
        });
        carouselPagination.appendChild(dot);
      });
    }

    // Next / Prev buttons
    if (btnCarouselPrev) {
      btnCarouselPrev.addEventListener('click', () => {
        scrollSlide(-1);
        resetAutoSlide();
      });
    }

    if (btnCarouselNext) {
      btnCarouselNext.addEventListener('click', () => {
        scrollSlide(1);
        resetAutoSlide();
      });
    }

    // Touch & Swipe Gesture Support
    carouselContainer.addEventListener('touchstart', (e) => {
      isDragging = true;
      startX = e.touches[0].pageX - carouselContainer.offsetLeft;
      scrollLeftStart = carouselContainer.scrollLeft;
      clearInterval(autoSlideTimer);
    }, { passive: true });

    carouselContainer.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      const x = e.touches[0].pageX - carouselContainer.offsetLeft;
      const walk = (x - startX) * 1.2;
      carouselContainer.scrollLeft = scrollLeftStart - walk;
    }, { passive: true });

    carouselContainer.addEventListener('touchend', () => {
      isDragging = false;
      snapToClosestSlide();
      startAutoSlide();
    });

    // Mouse Drag Support
    carouselContainer.addEventListener('mousedown', (e) => {
      isDragging = true;
      carouselContainer.classList.add('grabbing');
      startX = e.pageX - carouselContainer.offsetLeft;
      scrollLeftStart = carouselContainer.scrollLeft;
      clearInterval(autoSlideTimer);
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - carouselContainer.offsetLeft;
      const walk = (x - startX) * 1.5;
      carouselContainer.scrollLeft = scrollLeftStart - walk;
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        carouselContainer.classList.remove('grabbing');
        snapToClosestSlide();
        startAutoSlide();
      }
    });

    // Listen to scroll to update pagination dots
    carouselContainer.addEventListener('scroll', debounce(() => {
      updatePaginationFromScroll();
    }, 50), { passive: true });

    // Pause on hover
    carouselContainer.addEventListener('mouseenter', () => clearInterval(autoSlideTimer));
    carouselContainer.addEventListener('mouseleave', () => startAutoSlide());

    // Start auto slide
    startAutoSlide();
  }

  function scrollSlide(direction) {
    if (!carouselContainer) return;
    const slides = carouselContainer.querySelectorAll('.carousel-slide');
    if (!slides.length) return;

    const slideWidth = slides[0].offsetWidth + 24; // width + gap
    const maxScroll = carouselContainer.scrollWidth - carouselContainer.clientWidth;

    if (direction > 0) {
      if (carouselContainer.scrollLeft >= maxScroll - 10) {
        // Loop back to start smoothly
        carouselContainer.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        carouselContainer.scrollBy({ left: slideWidth, behavior: 'smooth' });
      }
    } else {
      if (carouselContainer.scrollLeft <= 10) {
        // Loop to end
        carouselContainer.scrollTo({ left: maxScroll, behavior: 'smooth' });
      } else {
        carouselContainer.scrollBy({ left: -slideWidth, behavior: 'smooth' });
      }
    }
  }

  function goToSlide(index) {
    if (!carouselContainer) return;
    const slides = carouselContainer.querySelectorAll('.carousel-slide');
    if (!slides[index]) return;
    const targetScroll = slides[index].offsetLeft - carouselContainer.offsetLeft - 8;
    carouselContainer.scrollTo({ left: targetScroll, behavior: 'smooth' });
  }

  function snapToClosestSlide() {
    if (!carouselContainer) return;
    const slides = carouselContainer.querySelectorAll('.carousel-slide');
    if (!slides.length) return;

    const currentScroll = carouselContainer.scrollLeft;
    let closestIndex = 0;
    let minDiff = Infinity;

    slides.forEach((slide, idx) => {
      const diff = Math.abs(slide.offsetLeft - carouselContainer.offsetLeft - currentScroll);
      if (diff < minDiff) {
        minDiff = diff;
        closestIndex = idx;
      }
    });

    goToSlide(closestIndex);
  }

  function updatePaginationFromScroll() {
    if (!carouselContainer || !carouselPagination) return;
    const slides = carouselContainer.querySelectorAll('.carousel-slide');
    const dots = carouselPagination.querySelectorAll('.carousel-dot');
    if (!slides.length || !dots.length) return;

    const currentScroll = carouselContainer.scrollLeft;
    let closestIndex = 0;
    let minDiff = Infinity;

    slides.forEach((slide, idx) => {
      const diff = Math.abs(slide.offsetLeft - carouselContainer.offsetLeft - currentScroll);
      if (diff < minDiff) {
        minDiff = diff;
        closestIndex = idx;
      }
    });

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === closestIndex);
    });
  }

  function startAutoSlide() {
    clearInterval(autoSlideTimer);
    autoSlideTimer = setInterval(() => {
      scrollSlide(1);
    }, 4200);
  }

  function resetAutoSlide() {
    clearInterval(autoSlideTimer);
    startAutoSlide();
  }

  /* ==========================================================================
     4. WEDDING COUNTDOWN TIMER
     Target: December 4, 2026 at 8:58 PM (IST)
     ========================================================================== */
  function initCountdown() {
    // Target time: 2026-12-04 20:58:00 IST (+05:30)
    const targetDate = new Date("2026-12-04T20:58:00+05:30").getTime();

    function updateTimer() {
      const now = new Date().getTime();
      const distance = targetDate - now;

      if (distance <= 0) {
        if (countGrid) countGrid.style.display = 'none';
        if (countFinishedMsg) {
          countFinishedMsg.style.display = 'block';
          countFinishedMsg.innerHTML = "Today, our forever begins! ❤️";
        }
        return;
      }

      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((distance % (1000 * 60)) / 1000);

      if (countDays) countDays.textContent = String(days).padStart(2, '0');
      if (countHours) countHours.textContent = String(hours).padStart(2, '0');
      if (countMinutes) countMinutes.textContent = String(minutes).padStart(2, '0');
      if (countSeconds) countSeconds.textContent = String(seconds).padStart(2, '0');
    }

    updateTimer();
    setInterval(updateTimer, 1000);
  }

  /* ==========================================================================
     5. ADD TO CALENDAR FUNCTIONALITY (.ICS Download + Google Calendar Fallback)
     ========================================================================== */
  function generateIcsFile(event) {
    const pad = (n) => String(n).padStart(2, '0');
    const formatIcsDate = (date) => {
      return (
        date.getUTCFullYear() +
        pad(date.getUTCMonth() + 1) +
        pad(date.getUTCDate()) +
        'T' +
        pad(date.getUTCHours()) +
        pad(date.getUTCMinutes()) +
        pad(date.getUTCSeconds()) +
        'Z'
      );
    };

    const startDate = new Date(event.startIso);
    const endDate = new Date(event.endIso);
    const now = new Date();

    const icsContent = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//PraKar Wedding//Wedding Invitation//EN',
      'CALSCALE:GREGORIAN',
      'METHOD:PUBLISH',
      'BEGIN:VEVENT',
      `UID:${Date.now()}@prakarwedding.com`,
      `DTSTAMP:${formatIcsDate(now)}`,
      `DTSTART:${formatIcsDate(startDate)}`,
      `DTEND:${formatIcsDate(endDate)}`,
      `SUMMARY:${event.title}`,
      `DESCRIPTION:${event.description.replace(/\n/g, '\\n')}`,
      `LOCATION:${event.location}`,
      'STATUS:CONFIRMED',
      'BEGIN:VALARM',
      'TRIGGER:-P1D',
      'ACTION:DISPLAY',
      `DESCRIPTION:Reminder: ${event.title}`,
      'END:VALARM',
      'END:VEVENT',
      'END:VCALENDAR'
    ].join('\r\n');

    const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.setAttribute('download', `${event.filename}.ics`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  if (btnAddWeddingCal) {
    btnAddWeddingCal.addEventListener('click', () => {
      generateIcsFile({
        title: "Prasanth & Karthesha Wedding",
        startIso: "2026-12-04T20:58:00+05:30",
        endIso: "2026-12-04T23:58:00+05:30",
        location: "Vinukonda, Andhra Pradesh",
        description: "Prasanth & Karthesha Wedding Muhurtham at 8:58 PM. Venue: Wedding Venue – Details Coming Soon. #PraKar",
        filename: "Prasanth-Karthesha-Wedding"
      });
    });
  }

  if (btnAddReceptionCal) {
    btnAddReceptionCal.addEventListener('click', () => {
      generateIcsFile({
        title: "Prasanth & Karthesha Reception",
        startIso: "2026-12-06T19:00:00+05:30",
        endIso: "2026-12-06T23:00:00+05:30",
        location: "Narasaraopeta, Andhra Pradesh",
        description: "Prasanth & Karthesha Reception celebration at 7:00 PM in Narasaraopeta, Andhra Pradesh. Google Maps: https://maps.app.goo.gl/mqv5M2b1FCXx2fSG8?g_st=ac #PraKar",
        filename: "Prasanth-Karthesha-Reception"
      });
    });
  }

  /* ==========================================================================
     6. WHATSAPP SHARING
     ========================================================================== */
  if (btnWhatsappShare) {
    btnWhatsappShare.addEventListener('click', () => {
      const currentUrl = window.location.href;
      const shareMessage = 
`💍 Prasanth & Karthesha
#PraKar ❤️

We are getting married!
We would love for you to be part of our special day.

December 4, 2026

💌 View our wedding invitation:
${currentUrl}`;

      const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareMessage)}`;
      window.open(whatsappUrl, '_blank');
    });
  }

  /* ==========================================================================
     7. WEDDING VENUE COMING SOON MODAL
     ========================================================================== */
  if (btnViewWeddingVenue && venueModal) {
    btnViewWeddingVenue.addEventListener('click', (e) => {
      e.preventDefault();
      venueModal.classList.add('active');
    });
  }

  if (btnCloseModal && venueModal) {
    btnCloseModal.addEventListener('click', () => {
      venueModal.classList.remove('active');
    });

    venueModal.addEventListener('click', (e) => {
      if (e.target === venueModal) {
        venueModal.classList.remove('active');
      }
    });
  }

  /* ==========================================================================
     8. OPTIMIZED PARTICLES CANVAS (Golden Sparkles & Soft Petals)
     ========================================================================== */
  function initParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const maxParticles = window.innerWidth < 768 ? 22 : 45;

    for (let i = 0; i < maxParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2.8 + 1,
        color: Math.random() > 0.4 ? 'rgba(212, 175, 55, ' : 'rgba(233, 30, 99, ',
        alpha: Math.random() * 0.6 + 0.2,
        speedX: (Math.random() - 0.5) * 0.6,
        speedY: Math.random() * 0.7 + 0.3,
        rotation: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 1.5,
        isPetal: Math.random() > 0.5
      });
    }

    function animate() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach((p) => {
        p.x += p.speedX;
        p.y += p.speedY;
        p.rotation += p.rotSpeed;

        if (p.y > height) {
          p.y = -10;
          p.x = Math.random() * width;
        }
        if (p.x > width) p.x = 0;
        if (p.x < 0) p.x = width;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);

        if (p.isPetal) {
          // Delicate jasmine / rose petal shape
          ctx.beginPath();
          ctx.ellipse(0, 0, p.radius * 2.2, p.radius * 1.3, 0, 0, Math.PI * 2);
          ctx.fillStyle = `${p.color}${p.alpha})`;
          ctx.fill();
        } else {
          // Golden sparkle
          ctx.beginPath();
          ctx.arc(0, 0, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255, 235, 150, ${p.alpha})`;
          ctx.shadowBlur = 6;
          ctx.shadowColor = '#D4AF37';
          ctx.fill();
        }
        ctx.restore();
      });

      requestAnimationFrame(animate);
    }

    animate();
  }

  /* ==========================================================================
     9. SCROLL REVEAL (IntersectionObserver)
     ========================================================================== */
  function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal-fade-up');
    if (!revealElements.length || !('IntersectionObserver' in window)) return;

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          obs.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach((el) => observer.observe(el));
  }

  // Utility Debounce
  function debounce(func, wait) {
    let timeout;
    return function (...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  // Document Ready Initialization
  document.addEventListener('DOMContentLoaded', () => {
    initCountdown();
    initCarousel();
    initParticles();
    initScrollReveal();
  });

})();
