"""
Generates premium SVG assets for the wedding website.
"""
import os
import math


os.makedirs(r"d:\wedding\assets\images\gallery", exist_ok=True)
os.makedirs(r"d:\wedding\assets\music", exist_ok=True)

# 1. Royal Wax Seal
wax_seal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <radialGradient id="sealGold" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFF4D0"/>
      <stop offset="25%" stop-color="#E5C066"/>
      <stop offset="50%" stop-color="#C59B27"/>
      <stop offset="75%" stop-color="#9A7415"/>
      <stop offset="100%" stop-color="#6E500B"/>
    </radialGradient>
    <radialGradient id="sealRed" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#C93B4E"/>
      <stop offset="40%" stop-color="#9E1B32"/>
      <stop offset="75%" stop-color="#700E20"/>
      <stop offset="100%" stop-color="#420610"/>
    </radialGradient>
    <filter id="sealShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
    <filter id="emboss" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="1.5" result="blur"/>
      <feSpecularLighting in="blur" surfaceScale="2" specularConstant="1" specularExponent="20" lighting-color="#FFEBB0" result="spec">
        <fePointLight x="60" y="40" z="80"/>
      </feSpecularLighting>
      <feComposite in="spec" in2="SourceGraphic" operator="in"/>
    </filter>
  </defs>

  <!-- Wax Base with organic rim -->
  <path d="M100 12 C135 10 170 30 184 62 C198 94 186 136 166 164 C146 192 104 196 70 188 C36 180 8 152 14 116 C20 80 44 48 72 26 C82 18 90 12 100 12 Z" fill="url(#sealRed)" filter="url(#sealShadow)"/>

  <!-- Inner Gold Beaded Ring -->
  <circle cx="100" cy="100" r="72" fill="none" stroke="url(#sealGold)" stroke-width="2.5" stroke-dasharray="2,5" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="66" fill="#751222" stroke="url(#sealGold)" stroke-width="1.8"/>

  <!-- Monogram PK / PraKar -->
  <g fill="url(#sealGold)" filter="url(#emboss)" text-anchor="middle">
    <text x="100" y="85" font-family="'Cinzel Decorative', 'Playfair Display', Georgia, serif" font-size="28" font-weight="bold" letter-spacing="4">PK</text>
    <text x="100" y="112" font-family="'Montserrat', sans-serif" font-size="9" font-weight="600" letter-spacing="5">PRAKAR</text>
    <path d="M75 125 Q100 135 125 125 Q100 140 75 125 Z" fill="url(#sealGold)"/>
    <!-- Small traditional heart/tilak -->
    <path d="M100 50 C96 46 90 48 90 53 C90 58 100 64 100 64 C100 64 110 58 110 53 C110 48 104 46 100 50 Z" fill="url(#sealGold)"/>
  </g>
</svg>'''

# 2. Traditional Golden Mandala
mandala_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <defs>
    <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E5C066"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#AA771C"/>
    </linearGradient>
  </defs>
  <g fill="none" stroke="url(#goldGradient)" stroke-width="1.5" opacity="0.85">
    <circle cx="250" cy="250" r="230"/>
    <circle cx="250" cy="250" r="215" stroke-dasharray="4,6"/>
    <circle cx="250" cy="250" r="185"/>
    <circle cx="250" cy="250" r="150"/>
    <circle cx="250" cy="250" r="110"/>
    <circle cx="250" cy="250" r="70"/>
    <circle cx="250" cy="250" r="30" fill="url(#goldGradient)" fill-opacity="0.15"/>
    <!-- Petals 12-way symmetry -->
    <g transform="translate(250,250)">
      ''' + "".join([f'''<g transform="rotate({i*30})">
        <path d="M0 -30 Q-25 -90 0 -150 Q25 -90 0 -30 Z" fill="url(#goldGradient)" fill-opacity="0.08"/>
        <path d="M0 -150 Q-35 -185 0 -215 Q35 -185 0 -150 Z" fill="url(#goldGradient)" fill-opacity="0.12"/>
        <circle cx="0" cy="-185" r="4" fill="url(#goldGradient)"/>
        <path d="M-15 -110 Q0 -130 15 -110" stroke-width="1"/>
      </g>''' for i in range(12)]) + '''
    </g>
  </g>
</svg>'''

# 3. Ghibli-Style Romantic Couple Illustration
couple_ghibli_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000" width="800" height="1000">
  <defs>
    <!-- Soft Ghibli sky & magical lighting -->
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4A6572"/>
      <stop offset="30%" stop-color="#F9AA33"/>
      <stop offset="60%" stop-color="#FFD180"/>
      <stop offset="85%" stop-color="#FFF2DF"/>
      <stop offset="100%" stop-color="#F7EBE1"/>
    </linearGradient>
    <radialGradient id="sunGlow" cx="50%" cy="45%" r="45%">
      <stop offset="0%" stop-color="#FFFDE8" stop-opacity="1"/>
      <stop offset="40%" stop-color="#FFE599" stop-opacity="0.7"/>
      <stop offset="80%" stop-color="#FFAB40" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FFAB40" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="goldTrim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5D77F"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#996515"/>
    </linearGradient>
    <linearGradient id="sareeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C22036"/>
      <stop offset="40%" stop-color="#A51528"/>
      <stop offset="100%" stop-color="#6F0916"/>
    </linearGradient>
    <linearGradient id="sherwaniGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFDF8"/>
      <stop offset="60%" stop-color="#F2E6CE"/>
      <stop offset="100%" stop-color="#DDCBB1"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="bokehBlur" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="15"/>
    </filter>
  </defs>

  <!-- Sky Canvas -->
  <rect width="800" height="1000" fill="url(#skyGrad)"/>
  <!-- Sunset Glow -->
  <circle cx="400" cy="400" r="350" fill="url(#sunGlow)"/>

  <!-- Distant Ghibli Clouds & Rolling Hills -->
  <g opacity="0.6">
    <ellipse cx="200" cy="420" rx="180" ry="70" fill="#FFECCB" filter="url(#bokehBlur)"/>
    <ellipse cx="600" cy="400" rx="220" ry="80" fill="#FFE6B6" filter="url(#bokehBlur)"/>
    <path d="M0 650 Q200 580 400 620 T800 600 L800 1000 L0 1000 Z" fill="#E6C8A0" opacity="0.4"/>
    <path d="M0 720 Q250 670 500 700 T800 680 L800 1000 L0 1000 Z" fill="#D3AF83" opacity="0.5"/>
  </g>

  <!-- Traditional Mandap / Floral Toran Canopy at top -->
  <g opacity="0.85">
    <path d="M50 0 Q200 80 400 40 Q600 80 750 0 L750 -20 L50 -20 Z" fill="#751222"/>
    <path d="M50 15 Q200 95 400 55 Q600 95 750 15" stroke="url(#goldTrim)" stroke-width="4" fill="none"/>
    <!-- Marigold & Jasmine hanging garlands -->
    ''' + "".join([f'''<g transform="translate({100 + i*70}, 30)">
      <circle cx="0" cy="15" r="8" fill="#FF8F00"/>
      <circle cx="0" cy="32" r="7" fill="#FFC107"/>
      <circle cx="0" cy="48" r="6" fill="#FFFDE7"/>
      <circle cx="0" cy="62" r="5" fill="#FF8F00"/>
      <circle cx="0" cy="74" r="4" fill="#FFC107"/>
      <circle cx="0" cy="84" r="3" fill="#FFFDE7"/>
    </g>''' for i in range(10)]) + '''
  </g>

  <!-- Couple Silhouette & Artistic Ghibli Render -->
  <!-- Floating Petals in Air -->
  <g opacity="0.75">
    <path d="M120 280 C130 260 145 270 140 285 C135 300 115 295 120 280 Z" fill="#FF80AB"/>
    <path d="M220 380 C230 365 240 375 235 385 C230 395 215 390 220 380 Z" fill="#FF4081"/>
    <path d="M680 320 C690 305 700 315 695 325 C690 335 675 330 680 320 Z" fill="#FF80AB"/>
    <path d="M640 450 C650 435 660 445 655 455 C650 465 635 460 640 450 Z" fill="#FF4081"/>
    <circle cx="320" cy="310" r="3" fill="#FFFDE7" filter="url(#softGlow)"/>
    <circle cx="480" cy="330" r="4" fill="#FFFDE7" filter="url(#softGlow)"/>
    <circle cx="260" cy="460" r="3.5" fill="#FFFDE7" filter="url(#softGlow)"/>
    <circle cx="530" cy="480" r="2.5" fill="#FFFDE7" filter="url(#softGlow)"/>
  </g>

  <!-- Groom: Prasanth (Left) -->
  <g id="groom">
    <!-- Body / Sherwani -->
    <path d="M230 520 C250 450 310 440 370 470 C390 510 395 620 385 820 C360 830 230 830 215 820 C205 680 215 570 230 520 Z" fill="url(#sherwaniGrad)"/>
    <!-- Sherwani Royal Collar & Gold Trim -->
    <path d="M280 460 L320 540 L300 820" stroke="url(#goldTrim)" stroke-width="4" fill="none"/>
    <path d="M280 450 Q310 460 340 450" stroke="url(#goldTrim)" stroke-width="3" fill="none"/>
    <!-- Groom Stole / Dupatta (Maroon with Gold) -->
    <path d="M245 490 Q225 610 250 820 Q270 820 260 620 Q270 510 280 480 Z" fill="url(#sareeGrad)"/>
    <path d="M245 490 Q225 610 250 820" stroke="url(#goldTrim)" stroke-width="3" fill="none"/>
    <!-- Groom Head / Hair / Profile in Ghibli aesthetic -->
    <path d="M290 380 Q325 350 350 380 Q365 410 350 440 Q320 460 295 440 Q280 410 290 380 Z" fill="#FFE0B2"/>
    <!-- Hair -->
    <path d="M285 390 C280 350 310 335 345 345 C365 350 370 375 365 395 C355 380 345 375 330 380 C310 385 295 385 285 390 Z" fill="#2C2320"/>
    <!-- Gentle smiling expression -->
    <path d="M335 415 Q345 422 340 425" stroke="#795548" stroke-width="2" fill="none" stroke-linecap="round"/>
    <ellipse cx="338" cy="405" rx="3.5" ry="4" fill="#2C2320"/>
    <circle cx="339" cy="403" r="1" fill="#FFF"/>
  </g>

  <!-- Bride: Karthesha (Right, looking at Prasanth) -->
  <g id="bride">
    <!-- Royal Kanjeevaram Saree & Pallu -->
    <path d="M360 480 C410 450 480 460 520 520 C540 580 545 700 530 820 C490 830 385 830 370 820 C365 670 355 560 360 480 Z" fill="url(#sareeGrad)"/>
    <!-- Saree Zari Border & Motifs -->
    <path d="M390 510 Q460 580 430 820" stroke="url(#goldTrim)" stroke-width="6" fill="none"/>
    <path d="M430 500 Q500 580 480 820" stroke="url(#goldTrim)" stroke-width="3" fill="none"/>
    <!-- Saree Blouse & Gold Jewelry -->
    <path d="M400 465 Q450 470 470 495" fill="#C59B27"/>
    <!-- Traditional Bridal Necklace (Haar) -->
    <path d="M410 465 Q435 490 460 465" stroke="url(#goldTrim)" stroke-width="4" fill="none"/>
    <circle cx="435" cy="485" r="4" fill="#FFC107"/>
    <!-- Bride Head / Hair with Gajra / Profile -->
    <path d="M405 385 Q435 360 460 385 Q475 415 460 445 Q430 465 410 445 Q395 415 405 385 Z" fill="#FFE0B2"/>
    <!-- Long traditional braid & hair -->
    <path d="M420 375 C450 355 475 375 475 410 C485 450 495 500 490 560 C480 560 470 510 465 440 C450 425 435 415 420 375 Z" fill="#2C2320"/>
    <!-- Jasmine Flowers / Gajra in hair -->
    ''' + "".join([f'''<circle cx="{465 + (i%2)*8}" cy="{400 + i*14}" r="5" fill="#FFFDE7" stroke="#FFE082" stroke-width="1"/>''' for i in range(7)]) + '''
    <!-- Bride Profile / Gentle Smile -->
    <path d="M415 418 Q425 425 420 428" stroke="#A94442" stroke-width="2" fill="none" stroke-linecap="round"/>
    <ellipse cx="420" cy="408" rx="3.5" ry="4" fill="#2C2320"/>
    <circle cx="421" cy="406" r="1" fill="#FFF"/>
    <!-- Maang Tikka / Bindi -->
    <circle cx="423" cy="390" r="2.5" fill="#D32F2F"/>
    <circle cx="423" cy="390" r="1" fill="#FFD700"/>
  </g>

  <!-- Varmala / Rose & Jasmine Garlands for both -->
  <g id="garlands">
    <path d="M290 470 Q320 580 350 630 Q370 580 380 470" stroke="#E91E63" stroke-width="12" fill="none" stroke-dasharray="14,6" opacity="0.9"/>
    <path d="M290 470 Q320 580 350 630 Q370 580 380 470" stroke="#FFF9C4" stroke-width="8" fill="none" stroke-dasharray="8,12" opacity="0.95"/>
    <path d="M380 470 Q410 580 430 630 Q450 580 465 470" stroke="#E91E63" stroke-width="12" fill="none" stroke-dasharray="14,6" opacity="0.9"/>
    <path d="M380 470 Q410 580 430 630 Q450 580 465 470" stroke="#FFF9C4" stroke-width="8" fill="none" stroke-dasharray="8,12" opacity="0.95"/>
  </g>

  <!-- Joining Hands at Center -->
  <g transform="translate(345, 620)">
    <!-- Groom Hand -->
    <path d="M0 10 Q25 25 45 20 Q50 35 25 35 Q5 30 0 10 Z" fill="#FFE0B2"/>
    <!-- Bride Hand with Gold Bangles -->
    <path d="M60 20 Q40 25 25 20 Q20 5 45 5 Q60 10 60 20 Z" fill="#FFE0B2"/>
    <!-- Gold Bangles & Red Chooda on Bride's wrist -->
    <rect x="50" y="5" width="5" height="20" rx="2" fill="url(#goldTrim)"/>
    <rect x="56" y="6" width="4" height="18" rx="2" fill="#C22036"/>
    <rect x="61" y="6" width="4" height="18" rx="2" fill="url(#goldTrim)"/>
    <!-- Divine light spark between hands -->
    <circle cx="35" cy="20" r="10" fill="#FFF9C4" filter="url(#softGlow)"/>
    <circle cx="35" cy="20" r="3" fill="#FFFFFF"/>
  </g>

  <!-- Foreground Elegant Shadow & Floor Garland -->
  <path d="M100 820 C250 800 550 800 700 820 L800 1000 L0 1000 Z" fill="#6A1B29" opacity="0.85"/>
  <path d="M0 830 Q400 810 800 830 L800 1000 L0 1000 Z" fill="url(#goldTrim)" opacity="0.15"/>

  <!-- Elegant Inner Gold Foil Border -->
  <rect x="25" y="25" width="750" height="950" rx="20" fill="none" stroke="url(#goldTrim)" stroke-width="3"/>
  <rect x="35" y="35" width="730" height="930" rx="16" fill="none" stroke="url(#goldTrim)" stroke-width="1.2" stroke-dasharray="6,4"/>

  <!-- Corner Indian Paisley/Floral Motifs -->
  ''' + "".join([f'''<g transform="translate({x},{y}) rotate({rot})">
    <path d="M0 0 L40 0 C40 20 20 40 0 40 Z" fill="none" stroke="url(#goldTrim)" stroke-width="2"/>
    <circle cx="15" cy="15" r="4" fill="url(#goldTrim)"/>
  </g>''' for (x,y,rot) in [(40,40,0), (760,40,90), (760,960,180), (40,960,270)]]) + '''

  <!-- Overlay Text Badge at Bottom -->
  <g transform="translate(400, 910)" text-anchor="middle">
    <rect x="-170" y="-30" width="340" height="48" rx="24" fill="#580D1A" fill-opacity="0.9" stroke="url(#goldTrim)" stroke-width="1.5"/>
    <text y="-2" font-family="'Cinzel Decorative', Georgia, serif" font-size="19" font-weight="bold" fill="#FFE599" letter-spacing="3">PRASANTH &amp; KARTHESHA</text>
    <text y="14" font-family="'Montserrat', sans-serif" font-size="10" font-weight="600" fill="#E5C066" letter-spacing="4">#PRAKAR • FOREVER BEGINS</text>
  </g>
</svg>'''

# 4. Divine Lord Rama and Goddess Sita Painting / Illustration
divine_rama_sita_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 950" width="800" height="950">
  <defs>
    <radialGradient id="divineAura" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#FFFDF0"/>
      <stop offset="25%" stop-color="#FFE082"/>
      <stop offset="55%" stop-color="#FFB300" stop-opacity="0.6"/>
      <stop offset="85%" stop-color="#FF6F00" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#4A0E17" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="divineBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3B0910"/>
      <stop offset="40%" stop-color="#5E0F1E"/>
      <stop offset="70%" stop-color="#4A0B17"/>
      <stop offset="100%" stop-color="#24040B"/>
    </linearGradient>
    <linearGradient id="goldArch" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="35%" stop-color="#F1C40F"/>
      <stop offset="65%" stop-color="#D4AC0D"/>
      <stop offset="100%" stop-color="#9A7B0C"/>
    </linearGradient>
    <linearGradient id="ramaSkin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#81D4FA"/>
      <stop offset="50%" stop-color="#29B6F6"/>
      <stop offset="100%" stop-color="#0288D1"/>
    </linearGradient>
    <linearGradient id="sitaSkin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF8E1"/>
      <stop offset="50%" stop-color="#FFE082"/>
      <stop offset="100%" stop-color="#FFCA28"/>
    </linearGradient>
    <linearGradient id="pitambara" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF176"/>
      <stop offset="50%" stop-color="#FBC02D"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </linearGradient>
    <linearGradient id="sitaSaree" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#D81B60"/>
      <stop offset="60%" stop-color="#C2185B"/>
      <stop offset="100%" stop-color="#880E4F"/>
    </linearGradient>
    <filter id="haloGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="16" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="950" fill="url(#divineBg)"/>

  <!-- Prabhavali / Sacred Temple Arch -->
  <g stroke="url(#goldArch)" fill="none" opacity="0.9">
    <!-- Outer Arch Pillar -->
    <path d="M120 850 L120 400 C120 220 250 120 400 120 C550 120 680 220 680 400 L680 850" stroke-width="14"/>
    <path d="M140 850 L140 410 C140 240 260 145 400 145 C540 145 660 240 660 410 L660 850" stroke-width="4" stroke-dasharray="8,6"/>
    <!-- Kirtimukha (Crown of Arch) -->
    <g transform="translate(400, 110)">
      <circle cx="0" cy="0" r="30" fill="url(#goldArch)"/>
      <path d="M-40 20 Q0 -25 40 20 Q0 35 -40 20 Z" fill="url(#goldArch)"/>
      <circle cx="0" cy="-5" r="8" fill="#D32F2F"/>
    </g>
    <!-- Flames/Kalasas along Arch -->
    ''' + "".join([f'''<path d="M{400 + 260*math.cos(i*3.14159/10)} {380 - 250*math.sin(i*3.14159/10)} Q{400 + 285*math.cos(i*3.14159/10)} {380 - 275*math.sin(i*3.14159/10)} {400 + 270*math.cos(i*3.14159/10)} {380 - 260*math.sin(i*3.14159/10)}" stroke="url(#goldArch)" stroke-width="4"/>''' for i in range(1, 10)]) + '''
  </g>

  <!-- Large Divine Aura -->
  <circle cx="400" cy="380" r="300" fill="url(#divineAura)"/>
  <!-- Circular Golden Halo behind Divine Couple -->
  <circle cx="330" cy="310" r="95" fill="#FFE57F" fill-opacity="0.3" stroke="url(#goldArch)" stroke-width="3" filter="url(#haloGlow)"/>
  <circle cx="470" cy="330" r="90" fill="#FFE57F" fill-opacity="0.3" stroke="url(#goldArch)" stroke-width="3" filter="url(#haloGlow)"/>

  <!-- LORD RAMA (Left) -->
  <g id="lordRama">
    <!-- Body / Blue Shyamal Varna -->
    <path d="M250 420 C270 380 320 375 350 395 C380 435 390 520 380 720 L270 720 C250 630 240 500 250 420 Z" fill="url(#ramaSkin)"/>
    <!-- Pitambara (Sacred Yellow Silk Dhoti & Angavastram) -->
    <path d="M260 560 Q340 590 380 560 L390 750 Q310 770 250 750 Z" fill="url(#pitambara)"/>
    <path d="M250 430 Q280 540 270 720" stroke="url(#goldArch)" stroke-width="8" fill="none"/>
    <!-- Yajnopavita (Sacred Thread) -->
    <path d="M280 410 Q320 480 340 550" stroke="#FFF" stroke-width="3" fill="none"/>
    <path d="M280 410 Q320 480 340 550" stroke="url(#goldArch)" stroke-width="1.5" stroke-dasharray="4,4" fill="none"/>
    <!-- Golden Ornaments / Haras -->
    <path d="M290 420 Q330 460 360 420" stroke="url(#goldArch)" stroke-width="6" fill="none"/>
    <path d="M280 440 Q330 500 370 440" stroke="url(#goldArch)" stroke-width="5" fill="none"/>
    <!-- Head & Face -->
    <path d="M300 280 Q335 250 355 285 Q370 325 350 360 Q320 375 295 355 Q285 320 300 280 Z" fill="url(#ramaSkin)"/>
    <!-- Tilak (Urdhva Pundra with Chandan & Kumkum) -->
    <path d="M328 300 L328 322 M334 300 L334 322" stroke="#FFFFFF" stroke-width="2"/>
    <path d="M331 303 L331 326" stroke="#D32F2F" stroke-width="2.5"/>
    <circle cx="331" cy="328" r="1.5" fill="#FFEB3B"/>
    <!-- Calm, gracious divine eyes -->
    <path d="M312 330 Q322 338 328 332" stroke="#0D47A1" stroke-width="2" fill="none"/>
    <path d="M335 332 Q342 338 350 330" stroke="#0D47A1" stroke-width="2" fill="none"/>
    <!-- Divine smile -->
    <path d="M325 352 Q332 358 340 352" stroke="#C2185B" stroke-width="2" fill="none"/>
    <!-- Magnificent Kirita Makuta (Golden Crown) -->
    <path d="M290 275 L332 170 L370 275 Q330 260 290 275 Z" fill="url(#goldArch)" stroke="#B7950B" stroke-width="2"/>
    <path d="M310 270 L332 190 L350 270" fill="#FFF9C4" opacity="0.6"/>
    <circle cx="332" cy="220" r="6" fill="#D32F2F"/>
    <circle cx="332" cy="170" r="5" fill="#00E676"/>
    <!-- Kodanda Bow (Sacred Bow of Rama) on Shoulder -->
    <path d="M230 190 Q210 450 240 730" stroke="url(#goldArch)" stroke-width="8" fill="none"/>
    <path d="M235 200 L235 720" stroke="#FFE082" stroke-width="2" stroke-dasharray="2,3"/>
  </g>

  <!-- GODDESS SITA (Right) -->
  <g id="goddessSita">
    <!-- Radiant Golden Body & Bridal Saree -->
    <path d="M410 430 C440 390 490 395 520 440 C540 480 545 600 535 730 L430 730 C415 650 405 520 410 430 Z" fill="url(#sitaSaree)"/>
    <!-- Golden Saree Zari Pallu -->
    <path d="M440 450 Q520 540 480 730" stroke="url(#goldArch)" stroke-width="12" fill="none"/>
    <path d="M420 540 Q490 590 530 550" stroke="url(#goldArch)" stroke-width="6" fill="none"/>
    <!-- Ornaments / Gold Necklaces & Kasu Mala -->
    <path d="M435 435 Q465 480 495 435" stroke="url(#goldArch)" stroke-width="6" fill="none"/>
    <path d="M425 455 Q465 520 505 455" stroke="url(#goldArch)" stroke-width="4" fill="none"/>
    <!-- Head & Face -->
    <path d="M440 300 Q475 270 495 305 Q510 345 490 380 Q460 395 435 375 Q425 340 440 300 Z" fill="url(#sitaSkin)"/>
    <!-- Hair with Jasmine flowers -->
    <path d="M450 295 C485 275 510 295 515 330 C520 370 515 410 500 450 C490 430 480 400 485 360 C470 340 455 330 450 295 Z" fill="#212121"/>
    ''' + "".join([f'''<circle cx="{495 + (i%2)*6}" cy="{330 + i*16}" r="5" fill="#FFFDE7" stroke="#FFE082" stroke-width="1"/>''' for i in range(6)]) + '''
    <!-- Kumkum Tilak & Bindi -->
    <circle cx="465" cy="335" r="3" fill="#D32F2F"/>
    <circle cx="465" cy="335" r="1.2" fill="#FFEB3B"/>
    <!-- Gracious Eyes & Gentle Smile -->
    <path d="M448 348 Q456 355 462 350" stroke="#3E2723" stroke-width="2" fill="none"/>
    <path d="M470 350 Q478 355 486 348" stroke="#3E2723" stroke-width="2" fill="none"/>
    <path d="M458 370 Q465 376 472 370" stroke="#C2185B" stroke-width="2" fill="none"/>
    <!-- Golden Crown (Makuta) for Sita Mata -->
    <path d="M435 295 L468 200 L500 295 Q470 280 435 295 Z" fill="url(#goldArch)" stroke="#B7950B" stroke-width="2"/>
    <circle cx="468" cy="245" r="5" fill="#D32F2F"/>
    <circle cx="468" cy="200" r="4" fill="#E91E63"/>
    <!-- Holding Sacred Lotus Flower in Hand -->
    <g transform="translate(420, 520)">
      <path d="M0 0 Q-15 -30 -5 -45 Q15 -30 0 0 Z" fill="#F06292"/>
      <path d="M-8 -15 Q-30 -35 -20 -50 Q-5 -40 -8 -15 Z" fill="#EC407A"/>
      <path d="M8 -15 Q30 -35 20 -50 Q5 -40 8 -15 Z" fill="#EC407A"/>
      <circle cx="0" cy="-30" r="5" fill="#FFEB3B"/>
      <path d="M0 0 L5 40" stroke="#4CAF50" stroke-width="4"/>
    </g>
  </g>

  <!-- Abhaya Mudra (Rama's Blessing Hand) & Sita's Gentle Hand -->
  <g transform="translate(370, 480)">
    <!-- Rama Right Hand in Divine Blessing (Abhaya Hasta) -->
    <path d="M-15 0 C-10 -25 10 -25 15 0 C15 20 -5 30 -15 0 Z" fill="url(#ramaSkin)"/>
    <circle cx="0" cy="5" r="6" fill="#D32F2F" opacity="0.6"/>
  </g>

  <!-- Big Lotus Throne / Padmasana at Bottom -->
  <g transform="translate(400, 770)">
    <!-- Lotus Petals -->
    ''' + "".join([f'''<path d="M0 0 Q{i*40} 45 {i*60} 70 Q{i*30} 85 0 90 Q{-i*30} 85 {-i*60} 70 Q{-i*40} 45 0 0 Z" fill="#E91E63" fill-opacity="{0.2 + (5-abs(i))*0.15}"/>''' for i in range(-5, 6)]) + '''
    <ellipse cx="0" cy="80" rx="320" ry="25" fill="url(#goldArch)"/>
  </g>

  <!-- Decorative Outer Golden Frame -->
  <rect x="25" y="25" width="750" height="900" rx="16" fill="none" stroke="url(#goldArch)" stroke-width="3"/>
  <rect x="35" y="35" width="730" height="880" rx="12" fill="none" stroke="url(#goldArch)" stroke-width="1.2" stroke-dasharray="6,4"/>

  <!-- Holy Inscription at Top -->
  <g transform="translate(400, 70)" text-anchor="middle">
    <text font-family="'Cinzel Decorative', Georgia, serif" font-size="18" font-weight="bold" fill="#FFE599" letter-spacing="4">॥ శ్రీ సీతారామచంద్ర పరబ్రహ్మణే నమః ॥</text>
  </g>

  <!-- Elegant Divine Blessings Text at Bottom -->
  <g transform="translate(400, 895)" text-anchor="middle">
    <text font-family="'Cinzel Decorative', Georgia, serif" font-size="16" font-weight="bold" fill="#FFE599" letter-spacing="4">DIVINE BLESSINGS OF SRI SITA RAMA</text>
  </g>
</svg>'''

# 5. Rama Hand (Left hand entering from left)
hand_rama_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="400" height="240">
  <defs>
    <linearGradient id="ramaHandSkin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B3E5FC"/>
      <stop offset="50%" stop-color="#4FC3F7"/>
      <stop offset="100%" stop-color="#0288D1"/>
    </linearGradient>
    <linearGradient id="goldKada" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="45%" stop-color="#F1C40F"/>
      <stop offset="80%" stop-color="#D4AC0D"/>
      <stop offset="100%" stop-color="#9A7B0C"/>
    </linearGradient>
    <radialGradient id="sacredBlueGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#E1F5FE" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#81D4FA" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#0288D1" stop-opacity="0"/>
    </radialGradient>
    <filter id="handGlow">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Celestial Glow behind Hand -->
  <ellipse cx="240" cy="120" rx="140" ry="80" fill="url(#sacredBlueGlow)" filter="url(#handGlow)"/>

  <!-- Lord Rama Arm and Hand (Extending gently toward right) -->
  <g id="ramaHandGroup">
    <!-- Forearm -->
    <path d="M0 80 Q100 85 180 95 Q240 100 280 115 Q260 160 170 155 Q90 150 0 145 Z" fill="url(#ramaHandSkin)"/>

    <!-- Royal Golden Bracelets / Kangan on Rama's Wrist -->
    <g transform="translate(140, 75)">
      <rect x="0" y="5" width="22" height="80" rx="6" fill="url(#goldKada)" stroke="#B7950B" stroke-width="1.5"/>
      <circle cx="11" cy="20" r="4" fill="#D32F2F"/>
      <circle cx="11" cy="45" r="4" fill="#00E676"/>
      <circle cx="11" cy="70" r="4" fill="#D32F2F"/>
      <!-- Sacred Rudraksha beads string -->
      ''' + "".join([f'''<circle cx="28" cy="{15 + i*13}" r="5" fill="#6D4C41" stroke="#3E2723" stroke-width="1"/>''' for i in range(5)]) + '''
    </g>

    <!-- Palm & Fingers reaching out open for Hastamelap / Panigrahana -->
    <!-- Thumb (Top) -->
    <path d="M220 98 Q260 85 295 90 Q310 95 305 105 Q285 115 250 115 Z" fill="url(#ramaHandSkin)"/>
    <!-- Index Finger -->
    <path d="M260 108 Q315 105 355 110 Q370 115 365 125 Q335 130 280 125 Z" fill="url(#ramaHandSkin)"/>
    <!-- Middle Finger (Longest) -->
    <path d="M265 118 Q325 115 375 120 Q390 126 385 135 Q340 142 280 135 Z" fill="url(#ramaHandSkin)"/>
    <!-- Ring Finger with Golden Ring -->
    <path d="M255 128 Q315 128 360 132 Q372 138 368 146 Q330 150 275 142 Z" fill="url(#ramaHandSkin)"/>
    <rect x="305" y="128" width="8" height="15" rx="3" fill="url(#goldKada)"/>
    <!-- Little Finger -->
    <path d="M245 138 Q290 142 335 145 Q345 150 340 157 Q305 160 255 150 Z" fill="url(#ramaHandSkin)"/>

    <!-- Sacred Red Alta / Lotus symbol on Palm -->
    <circle cx="270" cy="125" r="14" fill="#D32F2F" fill-opacity="0.35"/>
    <circle cx="270" cy="125" r="5" fill="#D32F2F" fill-opacity="0.8"/>
  </g>
</svg>'''

# 6. Sita Hand (Right hand entering from right)
hand_sita_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="400" height="240">
  <defs>
    <linearGradient id="sitaHandSkin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF8E1"/>
      <stop offset="50%" stop-color="#FFE082"/>
      <stop offset="100%" stop-color="#FFCA28"/>
    </linearGradient>
    <linearGradient id="sitaGoldKada" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="50%" stop-color="#F1C40F"/>
      <stop offset="100%" stop-color="#B7950B"/>
    </linearGradient>
    <linearGradient id="bridalRed" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EF5350"/>
      <stop offset="50%" stop-color="#D32F2F"/>
      <stop offset="100%" stop-color="#880E4F"/>
    </linearGradient>
    <radialGradient id="sacredGoldGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#FFE082" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#FF8F00" stop-opacity="0"/>
    </radialGradient>
    <filter id="handGlow2">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Golden Aura behind Sita's Hand -->
  <ellipse cx="160" cy="120" rx="140" ry="80" fill="url(#sacredGoldGlow)" filter="url(#handGlow2)"/>

  <!-- Goddess Sita Arm and Hand (Extending gently toward left) -->
  <g id="sitaHandGroup">
    <!-- Forearm -->
    <path d="M400 85 Q300 90 220 100 Q160 105 120 120 Q140 165 230 160 Q310 155 400 150 Z" fill="url(#sitaHandSkin)"/>

    <!-- Bridal Bangles (Chooda & Gold Kadas) on Sita's Wrist -->
    <g transform="translate(210, 80)">
      <!-- Gold Kadas & Red Bridal Glass Bangles -->
      <rect x="0" y="5" width="8" height="80" rx="4" fill="url(#sitaGoldKada)" stroke="#B7950B" stroke-width="1"/>
      <rect x="10" y="7" width="5" height="76" rx="2" fill="url(#bridalRed)"/>
      <rect x="17" y="7" width="5" height="76" rx="2" fill="url(#bridalRed)"/>
      <rect x="24" y="6" width="6" height="78" rx="3" fill="url(#sitaGoldKada)"/>
      <rect x="32" y="7" width="5" height="76" rx="2" fill="url(#bridalRed)"/>
      <rect x="39" y="7" width="5" height="76" rx="2" fill="url(#bridalRed)"/>
      <rect x="46" y="5" width="8" height="80" rx="4" fill="url(#sitaGoldKada)" stroke="#B7950B" stroke-width="1"/>
    </g>

    <!-- Palm & Delicate Fingers reaching to join Rama's hand -->
    <!-- Thumb (Top) -->
    <path d="M180 102 Q140 90 105 95 Q90 100 95 110 Q115 120 150 120 Z" fill="url(#sitaHandSkin)"/>
    <!-- Index Finger -->
    <path d="M140 112 Q85 110 45 115 Q30 120 35 130 Q65 135 120 130 Z" fill="url(#sitaHandSkin)"/>
    <!-- Middle Finger -->
    <path d="M135 122 Q75 120 25 125 Q10 131 15 140 Q60 147 120 140 Z" fill="url(#sitaHandSkin)"/>
    <!-- Ring Finger with Golden Ring -->
    <path d="M145 132 Q85 132 40 136 Q28 142 32 150 Q70 154 125 146 Z" fill="url(#sitaHandSkin)"/>
    <rect x="85" y="132" width="8" height="15" rx="3" fill="url(#sitaGoldKada)"/>
    <!-- Little Finger -->
    <path d="M155 142 Q110 146 65 149 Q55 154 60 161 Q95 164 145 154 Z" fill="url(#sitaHandSkin)"/>

    <!-- Traditional Henna / Mehendi patterns on Sita's palm & fingers -->
    <g fill="none" stroke="#791A23" stroke-width="1.8" opacity="0.85">
      <!-- Mandala on palm -->
      <circle cx="130" cy="130" r="12"/>
      <circle cx="130" cy="130" r="6" fill="#791A23"/>
      <!-- Henna cap on finger tips -->
      <path d="M48 115 Q30 120 35 130 Q45 132 50 125 Z" fill="#791A23"/>
      <path d="M28 125 Q10 131 15 140 Q25 142 30 135 Z" fill="#791A23"/>
      <path d="M43 136 Q28 142 32 150 Q42 152 45 145 Z" fill="#791A23"/>
      <!-- Delicately painted vines on back of hand -->
      <path d="M140 125 Q170 135 195 125" stroke-dasharray="2,3"/>
    </g>
  </g>
</svg>'''

# 7. Gallery SVGs
gallery_themes = [
    ("gallery-1-prewedding.svg", "Pre-Wedding Moments", "Golden Sunset & Promises", "#F57C00", "#FFD54F"),
    ("gallery-2-engagement.svg", "Engagement Celebration", "Family Blessings & Rings", "#C2185B", "#F48FB1"),
    ("gallery-3-couple.svg", "Together Forever", "Smiles, Laughter & Joy", "#512DA8", "#B39DDB"),
    ("gallery-4-memories.svg", "Before-Marriage Memories", "Cherished Conversations", "#00796B", "#80CBC4"),
    ("gallery-5-journey.svg", "Our Journey Together", "Growing Closer Every Day", "#E64A19", "#FFAB91"),
    ("gallery-6-blessings.svg", "Love & Endless Blessings", "Surrounded by Pure Love", "#6A1B29", "#FFE082"),
]

for filename, title, subtitle, col1, col2 in gallery_themes:
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 750" width="600" height="750">
  <defs>
    <linearGradient id="bgGrad_{filename[:3]}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{col1}"/>
      <stop offset="60%" stop-color="{col1}EE"/>
      <stop offset="100%" stop-color="#1A0A10"/>
    </linearGradient>
    <linearGradient id="goldBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF4D0"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#9A7415"/>
    </linearGradient>
  </defs>

  <rect width="600" height="750" rx="20" fill="url(#bgGrad_{filename[:3]})"/>

  <!-- Decorative Mandala Pattern Watermark -->
  <g fill="none" stroke="{col2}" stroke-width="1.2" opacity="0.2" transform="translate(300, 320)">
    <circle r="180"/>
    <circle r="140" stroke-dasharray="4,6"/>
    <circle r="100"/>
    <circle r="60"/>
    ''' + "".join([f'''<path d="M0 0 L{150*math.cos(i*3.14159/6)} {150*math.sin(i*3.14159/6)}"/>''' for i in range(12)]) + f'''
  </g>

  <!-- Photo Placeholder Center Icon -->
  <g transform="translate(300, 310)">
    <circle r="90" fill="{col2}" fill-opacity="0.15" stroke="url(#goldBorder)" stroke-width="2"/>
    <!-- Couple Silhouette / Heart Camera -->
    <path d="M-35 -15 C-55 -40 -15 -60 0 -35 C15 -60 55 -40 35 -15 C15 15 0 35 0 35 C0 35 -15 15 -35 -15 Z" fill="{col2}" fill-opacity="0.8"/>
    <!-- Sparkles -->
    <circle cx="-45" cy="-45" r="4" fill="#FFF"/>
    <circle cx="45" cy="-45" r="3" fill="#FFF"/>
    <circle cx="0" cy="50" r="3" fill="#FFF"/>
  </g>

  <!-- Bottom Details & Typography -->
  <rect x="30" y="560" width="540" height="150" rx="16" fill="#000000" fill-opacity="0.45" stroke="url(#goldBorder)" stroke-width="1"/>
  <text x="300" y="615" font-family="'Cinzel Decorative', Georgia, serif" font-size="24" font-weight="bold" fill="#FFE599" text-anchor="middle" letter-spacing="2">{title}</text>
  <text x="300" y="650" font-family="'Montserrat', sans-serif" font-size="14" fill="#F5F5F5" text-anchor="middle" letter-spacing="1">{subtitle}</text>
  <text x="300" y="680" font-family="'Montserrat', sans-serif" font-size="11" font-weight="600" fill="url(#goldBorder)" text-anchor="middle" letter-spacing="3">#PRAKAR • REPLACE WITH YOUR PHOTO</text>

  <!-- Card Border -->
  <rect x="15" y="15" width="570" height="720" rx="16" fill="none" stroke="url(#goldBorder)" stroke-width="2"/>
  <rect x="23" y="23" width="554" height="704" rx="12" fill="none" stroke="url(#goldBorder)" stroke-width="1" stroke-dasharray="6,4"/>
</svg>'''
    with open(os.path.join(r"d:\wedding\assets\images\gallery", filename), "w", encoding="utf-8") as f:
        f.write(svg_content)

# 8. Kalash / Auspicious Pot Motif
kalash_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 240" width="200" height="240">
  <defs>
    <linearGradient id="kalashGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="50%" stop-color="#E5C066"/>
      <stop offset="100%" stop-color="#AA771C"/>
    </linearGradient>
    <linearGradient id="mangoLeaf" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#81C784"/>
      <stop offset="100%" stop-color="#2E7D32"/>
    </linearGradient>
  </defs>
  <!-- Mango Leaves -->
  <path d="M100 80 Q70 30 50 20 Q70 60 90 85 Z" fill="url(#mangoLeaf)"/>
  <path d="M100 80 Q130 30 150 20 Q130 60 110 85 Z" fill="url(#mangoLeaf)"/>
  <path d="M100 80 Q60 50 30 50 Q60 80 85 90 Z" fill="url(#mangoLeaf)"/>
  <path d="M100 80 Q140 50 170 50 Q140 80 115 90 Z" fill="url(#mangoLeaf)"/>
  <path d="M100 80 Q100 15 100 5 Q100 40 100 80 Z" stroke="url(#mangoLeaf)" stroke-width="10"/>

  <!-- Coconut (Nariyal) -->
  <ellipse cx="100" cy="65" rx="28" ry="32" fill="#795548"/>
  <path d="M100 35 L100 15" stroke="#4E342E" stroke-width="4"/>

  <!-- Brass / Gold Pot (Lota) -->
  <path d="M80 90 L120 90 L135 110 C155 135 155 180 135 200 L65 200 C45 180 45 135 65 110 Z" fill="url(#kalashGold)" stroke="#9A7415" stroke-width="2"/>
  <!-- Base Stand -->
  <path d="M70 200 L130 200 L140 215 L60 215 Z" fill="url(#kalashGold)"/>

  <!-- Swastika / Auspicious Mark on Pot -->
  <g fill="none" stroke="#D32F2F" stroke-width="3" stroke-linecap="round">
    <line x1="85" y1="150" x2="115" y2="150"/>
    <line x1="100" y1="135" x2="100" y2="165"/>
    <line x1="115" y1="150" x2="115" y2="140"/>
    <line x1="85" y1="150" x2="85" y2="160"/>
    <line x1="100" y1="135" x2="110" y2="135"/>
    <line x1="100" y1="165" x2="90" y2="165"/>
    <!-- 4 Dots -->
    <circle cx="92" cy="142" r="1.5" fill="#D32F2F"/>
    <circle cx="108" cy="142" r="1.5" fill="#D32F2F"/>
    <circle cx="92" cy="158" r="1.5" fill="#D32F2F"/>
    <circle cx="108" cy="158" r="1.5" fill="#D32F2F"/>
  </g>
</svg>'''

# 9. Auspicious Brass Diya / Oil Lamp
diya_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <defs>
    <linearGradient id="diyaGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="50%" stop-color="#F1C40F"/>
      <stop offset="100%" stop-color="#B7950B"/>
    </linearGradient>
    <radialGradient id="flameGrad" cx="50%" cy="60%" r="50%">
      <stop offset="0%" stop-color="#FFFDE7"/>
      <stop offset="30%" stop-color="#FFEE58"/>
      <stop offset="70%" stop-color="#FF7043"/>
      <stop offset="100%" stop-color="#D84315"/>
    </radialGradient>
    <filter id="flameGlow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Lamp Base & Bowl -->
  <path d="M40 135 L120 135 L110 145 L50 145 Z" fill="url(#diyaGold)"/>
  <path d="M70 120 L90 120 L90 135 L70 135 Z" fill="url(#diyaGold)"/>
  <path d="M20 95 Q80 135 140 95 Q145 90 135 90 Q80 110 25 90 Z" fill="url(#diyaGold)" stroke="#9A7B0C" stroke-width="1.5"/>

  <!-- Flame with Glow -->
  <ellipse cx="80" cy="65" rx="30" ry="40" fill="#FFE082" fill-opacity="0.25" filter="url(#flameGlow)"/>
  <path d="M80 40 Q65 65 72 82 Q80 92 88 82 Q95 65 80 40 Z" fill="url(#flameGrad)" filter="url(#flameGlow)"/>
  <circle cx="80" cy="75" r="4" fill="#FFFFFF"/>
</svg>'''

# Save individual SVG files
files_to_write = [
    (r"d:\wedding\assets\images\envelope-seal.svg", wax_seal_svg),
    (r"d:\wedding\assets\images\mandala.svg", mandala_svg),
    (r"d:\wedding\assets\images\couple-ghibli.svg", couple_ghibli_svg),
    (r"d:\wedding\assets\images\divine-rama-sita.svg", divine_rama_sita_svg),
    (r"d:\wedding\assets\images\hand-rama.svg", hand_rama_svg),
    (r"d:\wedding\assets\images\hand-sita.svg", hand_sita_svg),
    (r"d:\wedding\assets\images\kalash.svg", kalash_svg),
    (r"d:\wedding\assets\images\diya.svg", diya_svg),
]

for path, content in files_to_write:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())

print("All SVGs created successfully!")
