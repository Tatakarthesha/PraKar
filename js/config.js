/**
 * Wedding Invitation Configuration & Easy Placeholders
 * ====================================================
 * You can easily edit any details, links, or image paths in this file.
 */

const WEDDING_CONFIG = {
  // Couple Details
  groom: {
    name: "Prasanth",
    fullName: "Inavolu Prasanth",
    parents: "Inavolu Purnachandra Rao & Inavolu Indrani"
  },
  bride: {
    name: "Karthesha",
    fullName: "Tata Karthesha",
    parents: "Tata Hanumantha Rao & Tata Lakshmi Kumari"
  },
  hashtag: "#PraKar",

  // Dates & Times (Format: YYYY-MM-DDTHH:mm:ss)
  wedding: {
    title: "Prasanth & Karthesha Wedding",
    date: "December 4, 2026",
    time: "8:58 PM",
    muhurtham: "8:58 PM",
    targetDateTime: "2026-12-04T20:58:00+05:30", // IST (Indian Standard Time)
    location: "Vinukonda, Andhra Pradesh",
    venueName: "Tashvi Grands & Convention Hall",
    isVenueFinalized: false,
    googleMapsUrl: "", // Add Google Maps URL when finalized
    description: "Muhurtham celebration for the wedding of Karthesha & Prasanth."
  },

  reception: {
    title: "Prasanth & Karthesha Reception",
    date: "December 6, 2026",
    time: "7:00 PM",
    targetDateTime: "2026-12-06T19:00:00+05:30",
    location: "Narasaraopeta, Andhra Pradesh",
    venueName: "Mega Convention Hall",
    isVenueFinalized: true,
    googleMapsUrl: "https://maps.app.goo.gl/mqv5M2b1FCXx2fSG8?g_st=ac",
    description: "Reception celebration welcoming the newlyweds Prasanth & Karthesha."
  },

  // Media & Images (Replace these paths with your own photos anytime)
  assets: {
    // 1. Welcome / Envelope Couple Image (Ghibli / anime romantic style)
    coupleImage: "assets/images/couple.jpg",
    coupleImageAlt: "Prasanth & Karthesha - PraKar Wedding",

    // 2. Divine Opening Image
    divineImage: "assets/images/divine-rama-sita.svg",
    divineImageAlt: "Lord Rama and Goddess Sita Kalyana Blessing",

    // 3. Background Music (Put your preferred wedding MP3 in assets/music/)
    musicFile: "assets/music/wedding_song.mp3",

    // 4. Open Graph Share Preview Image
    ogPreviewImage: "assets/images/whatsapp-preview.jpg",

    // 5. Gallery Images (Horizontal photo carousel)
    gallery: [
      {
        url: "assets/images/gallery/gallery-1-prewedding.svg",
        title: "Pre-Wedding Moments",
        caption: "Golden hour promises and warm smiles"
      },
      {
        url: "assets/images/gallery/gallery-2-engagement.svg",
        title: "Engagement Celebration",
        caption: "A joyful beginning with our loving families"
      },
      {
        url: "assets/images/gallery/gallery-3-couple.svg",
        title: "Together Forever",
        caption: "Finding home in each other's laughter"
      },
      {
        url: "assets/images/gallery/gallery-4-memories.svg",
        title: "Before-Marriage Memories",
        caption: "Cherished conversations that brought us close"
      },
      {
        url: "assets/images/gallery/gallery-5-journey.svg",
        title: "Our Journey Together",
        caption: "Every little step leading to our special day"
      },
      {
        url: "assets/images/gallery/gallery-6-blessings.svg",
        title: "Love & Blessings",
        caption: "Surrounded by smiles, joy, and forever love"
      }
    ]
  },

  // Family Members
  families: {
    parents: {
      bride: {
        title: "Bride's Parents",
        father: "Tata Hanumantha Rao",
        mother: "Tata Lakshmi Kumari"
      },
      groom: {
        title: "Groom's Parents",
        father: "Inavolu Purnachandra Rao",
        mother: "Inavolu Indrani"
      }
    },
    relatives: [
      {
        relation: "Bride's Sister & Husband",
        names: ["Kandukuri Sai Kiran", "Kandukuri Kiranmai"]
      },
      {
        relation: "Groom's Brother & Wife",
        names: ["Inavolu Dinesh", "Inavolu Sujana"]
      },
      {
        relation: "Groom's Sister & Husband",
        names: ["Mitta Phanindra", "Mitta Sowgandhika"]
      }
    ]
  },

  // Journey Narrative (DO NOT CHANGE)
  journeyText: "It all began with a simple “yes” and a beautiful family bond. One year of conversations, understanding, laughter, emotions, and countless memories brought us closer than ever. What started with our families became a love that grew naturally between us—and today, we are ready to begin our forever together. ❤️",

  // Telugu Opening Text (DO NOT CHANGE)
  teluguOpeningText: "అంటే... ప్రశు కార్తీకి పెళ్లంట!",

  // Footer Closing (DO NOT CHANGE)
  footerMessage: "We can't wait to celebrate this beautiful journey with you♥️",
  footerSignoff: "with love, PraKar"
};

// Export to window object
if (typeof window !== "undefined") {
  window.WEDDING_CONFIG = WEDDING_CONFIG;
}
