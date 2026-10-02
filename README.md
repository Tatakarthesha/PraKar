# 💍 Prasanth & Karthesha Wedding Invitation (#PraKar)

A luxurious, modern, mobile-first Indian wedding invitation website crafted for **Prasanth & Karthesha**.

Designed with rich Indian wedding aesthetics — ivory/cream paper textures, royal antique gold accents, sacred motifs, smooth animations, and cultural warmth.

---

## ✨ Features & User Experience Flow

1. **Welcome / Envelope Opening**
   - Elegant physical wedding invitation envelope aesthetic.
   - Royal wax seal with `#PraKar` monogram.
   - Ghibli-style romantic couple artwork.
   - Exact Telugu phrase: **“అంటే... ప్రశు కార్తీకి పెళ్లంట!”**
   - **“Open Invitation”** gold-foil action button.
   - Upon clicking, the envelope unfolds, background wedding music starts automatically, and seamlessly launches the divine opening sequence.

2. **Divine Rama & Sita Opening Animation**
   - Sacred, peaceful dawn ambiance with celestial lighting.
   - Divine hands inspired by Lord Rama and Goddess Sita gently glide from opposite sides and join in sacred *Hastamelap* / *Panigrahana*.
   - A golden divine halo glow bursts at the point of touch.
   - Reveals the sacred Kalyana Rama & Sita blessing artwork, followed by:
     ```
     Prasanth
        &
     Karthesha
     ```
   - Automatically and gracefully glides into the main wedding website without requiring another click.

3. **Background Wedding Music & Floating Player**
   - Starts automatically when visitor taps “Open Invitation” (adhering to browser autoplay standards).
   - Elegant floating gold-glassmorphism pill with live animated equalizer wave bars.
   - Tap to Play / Pause anytime.
   - Built-in dual audio engine:
     - Directly plays your custom audio file in `assets/music/wedding_song.mp3` or `assets/music/wedding_melody.wav`.
     - Built-in soothing Indian classical Shehnai & Tanpura Web Audio synthesizer fallback so audio plays reliably even before an MP3 is uploaded!

4. **Our Families**
   - Main focus on **Bride’s Parents** (*Tata Hanumantha Rao & Tata Lakshmi Kumari*) and **Groom’s Parents** (*Inavolu Purnachandra Rao & Inavolu Indrani*) with grand gold-framed cards.
   - Elegant cards for immediate family:
     - Bride’s Sister & Husband: *Kandukuri Sai Kiran & Kandukuri Kiranmai*
     - Groom’s Brother & Wife: *Inavolu Dinesh & Inavolu Sujana*
     - Groom’s Sister & Husband: *Mitta Phanindra & Mitta Sowgandhika*

5. **Our Special Days**
   - **Wedding**: December 4, 2026 • 8:58 PM Muhurtham • Vinukonda, Andhra Pradesh.
   - **Reception**: December 6, 2026 • 7:00 PM • Narasaraopeta, Andhra Pradesh.

6. **Venue & Details + Google Maps + Add to Calendar**
   - **Wedding Venue**: Vinukonda, Andhra Pradesh (Placeholder with “View Wedding Venue” informational modal).
   - **Reception Venue**: Narasaraopeta, Andhra Pradesh with direct link to Google Maps:
     `https://maps.app.goo.gl/mqv5M2b1FCXx2fSG8?g_st=ac`
   - **Add to Calendar**:
     - “Add Wedding to Calendar” (generates & downloads standard `.ics` file).
     - “Add Reception to Calendar” (generates & downloads standard `.ics` file).
     - Works across Apple Calendar, Google Calendar, Outlook, and mobile devices.

7. **Our Beautiful Moments (Photo Gallery Carousel)**
   - Continuous horizontal auto-sliding carousel.
   - Full touch/swipe support on mobile and mouse drag on desktop.
   - Smooth infinite loop and interactive pagination dots.
   - 6 categorized photo placeholders:
     - Pre-wedding photos
     - Engagement photos
     - Couple photos
     - Before-marriage memories
     - Journey/memories together
     - Other beautiful moments

8. **Our Journey**
   - Exactly formatted romantic narrative:
     > “It all began with a simple “yes” and a beautiful family bond. One year of conversations, understanding, laughter, emotions, and countless memories brought us closer than ever. What started with our families became a love that grew naturally between us—and today, we are ready to begin our forever together. ❤️”

9. **Counting Down to Forever**
   - Live real-time countdown targeting **December 4, 2026 at 8:58 PM**.
   - Displays Days, Hours, Minutes, and Seconds.
   - Changes gracefully to *“Today, our forever begins! ❤️”* upon arrival.

10. **WhatsApp Share**
    - Section: **“Share Our Wedding”**
    - Button: **“Share Our Wedding 💚”**
    - Pre-filled message with wedding details and automatic website link.
    - Full Open Graph metadata (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) for rich preview cards when sharing.

11. **Emotional Closing Footer**
    - Closing statement:
      > “We can't wait to celebrate this beautiful journey with you♥️”
    - Sign-off:
      > **with love, PraKar**

12. **Design Specifications Verified**
    - ❌ No navbar (continuous luxury invitation experience)
    - ❌ No QR code
    - ❌ No wishes/guestbook section
    - ✅ Mobile-first, fully responsive across phones, tablets, and desktops
    - ✅ Floating particles canvas with golden sparkles and falling jasmine petals

---

## 📁 Project Structure

```text
wedding/
│
├── index.html                   # Main semantic HTML structure & metadata
├── README.md                    # Documentation & customization guide
│
├── css/
│   └── style.css                # Premium styling, animations, responsive breakpoints
│
├── js/
│   ├── config.js                # Central configuration (Dates, Venues, URLs, Names)
│   └── script.js                # Interactive logic (Audio, Envelope, Hands, Carousel, Countdown)
│
└── assets/
    ├── images/
    │   ├── couple-ghibli.svg    # Ghibli-inspired couple illustration (Welcome screen)
    │   ├── divine-rama-sita.svg # Lord Rama & Goddess Sita Kalyana artwork
    │   ├── hand-rama.svg        # Lord Rama blessing hand
    │   ├── hand-sita.svg        # Goddess Sita blessing hand
    │   ├── envelope-seal.svg    # Royal PraKar wax seal
    │   ├── mandala.svg          # Golden traditional mandala
    │   ├── kalash.svg           # Auspicious Mangala Kalash motif
    │   ├── diya.svg             # Auspicious oil lamp motif
    │   └── gallery/             # 6 gallery photo placeholders
    │       ├── gallery-1-prewedding.svg
    │       ├── gallery-2-engagement.svg
    │       ├── gallery-3-couple.svg
    │       ├── gallery-4-memories.svg
    │       ├── gallery-5-journey.svg
    │       └── gallery-6-blessings.svg
    └── music/
        ├── wedding_melody.wav   # Generated audio sample
        └── wedding_song.mp3     # Place your custom wedding song MP3 here
```

---

## 🎨 How to Customize Placeholders Later

### 1. Updating the Wedding Venue & Google Maps Link (Vinukonda)
When your wedding venue is finalized, open `js/config.js` and `index.html`:
- In `js/config.js`:
  ```javascript
  wedding: {
    // ...
    venueName: "Your Kalyana Mandapam Name",
    googleMapsUrl: "https://maps.app.goo.gl/YourActualWeddingLocationLink",
    isVenueFinalized: true
  }
  ```
- In `index.html`: Update the button link inside `#venue-and-details`.

### 2. Replacing Couple & Gallery Photos
- **Couple Image**: Save your couple photo as `assets/images/couple-ghibli.svg` or `couple.jpg` (update path in `js/config.js` or `index.html`).
- **Gallery Photos**: Replace the SVG placeholders in `assets/images/gallery/` with your own `.jpg` or `.png` files.

### 3. Adding Your Preferred Wedding Song
- Place your audio file as `assets/music/wedding_song.mp3`.
- The audio player will automatically detect and play your file.

---

## 🚀 How to Preview Locally

You can preview the website in any modern web browser:
1. Double click `index.html` to open it directly in Chrome, Edge, Safari, or Firefox.
2. Or run a local HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.
