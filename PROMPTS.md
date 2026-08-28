# Prompts

These are the **one-shot** prompts used to generate the 50 websites in this repo.
Each page is a single model sample (Qwen 3.8 27B Q4_K_M, thinking on, one RTX 3090).
Prompts are in the git repo only — they are not shown on the GitHub Pages gallery.

Machine-readable copy: [`prompts.json`](prompts.json).

## System

~~~~
You are an expert web designer and frontend engineer.
Create a single polished standalone HTML webpage from the brief.

Return EXACTLY one fenced ```html code block and nothing else.

Rules:
- One self-contained HTML file. CSS and JavaScript inside the file. No build step.
- You may load fonts from a font CDN (such as Google Fonts) via <link>.
- All imagery must be created with CSS, SVG, gradients or canvas. Do NOT link
  to any external images or photo services.
- Realistic copy and content, never lorem ipsum.
- Modern CSS, deliberate typography, spacing and hierarchy.
- The first viewport must look complete at 1440x900.
~~~~

## User prompts

### AI product launch

`web_ai_product_launch` · [generated page](docs/demos/qwen38-q4km/web/ai-product-launch.html)

~~~~
Create a premium product launch page for a fictional AI model platform called ORBIT AI.

Requirements:
- dramatic hero with large headline
- glowing abstract AI visualization made with pure CSS, SVG or canvas
- compact navigation
- benchmark/stat cards
- capabilities section
- API/code preview block
- enterprise CTA

Avoid the generic purple-gradient AI landing page trope. Use strong typography, carefully controlled gradients, glass/translucent surfaces and a coherent system.
~~~~

### Airline lounge

`web_airline_lounge` · [generated page](docs/demos/qwen38-q4km/web/airline-lounge.html)

~~~~
Design a polished, distinctive standalone website for a fictional airline lounge called AIRLINE / LOUNGE. Include destination search, lounge availability, amenities, membership tiers, travel perks and booking CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Architecture portfolio

`web_architecture_studio` · [generated page](docs/demos/qwen38-q4km/web/architecture-studio.html)

~~~~
Create a visually striking architecture studio landing page for a fictional studio named FORM/NOIR.

Art direction:
- editorial architecture-magazine aesthetic
- oversized typography
- dramatic asymmetric grid
- large architectural imagery built from CSS gradients, duotone SVG shapes or abstract geometric compositions (no photos)
- minimal navigation
- project metadata and locations
- generous whitespace
- black, warm white and muted stone tones
- subtle hover motion

The first viewport should look like a premium architecture portfolio.
~~~~

### Auction house

`web_auction_house` · [generated page](docs/demos/qwen38-q4km/web/auction-house.html)

~~~~
Design a polished, distinctive standalone website for a fictional auction house called AUCTION / HOUSE. Include featured lot, bidding panel, auction timer, provenance, upcoming lots and bidder account action. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Automotive studio

`web_automotive` · [generated page](docs/demos/qwen38-q4km/web/automotive.html)

~~~~
Design a high-concept EV launch page for AER / 01. Include CSS/SVG vehicle hero, performance strip, charging experience, interior details, trim cards, reserve CTA and footer. Use near-black, silver and electric blue with controlled motion.
~~~~

### Independent bookstore

`web_bookstore` · [generated page](docs/demos/qwen38-q4km/web/bookstore.html)

~~~~
Create an online bookstore homepage for MARGIN NOTES. Include search/categories, typographic featured book cover, staff picks, new arrivals, author event, reading list and store footer. Make it literary, tactile and independent rather than a generic ecommerce grid.
~~~~

### Cinema streaming

`web_cinema_streaming` · [generated page](docs/demos/qwen38-q4km/web/cinema-streaming.html)

~~~~
Create a cinematic streaming homepage for FRAME/ONE. Include featured film hero with local poster art, watch CTA, metadata, continue-watching row, collections, film cards, director spotlight and subscription footer. Use rich dark tones and no external images.
~~~~

### Civic services

`web_civic_services` · [generated page](docs/demos/qwen38-q4km/web/civic-services.html)

~~~~
Create a modern city-services homepage for LUMEN CITY. Include municipal search, service finder, alerts, permits, waste, transit, payments, events and accessible contact footer. Prioritize wayfinding and clarity with civic blue and warm paper tones.
~~~~

### Climate dashboard

`web_climate_lab` · [generated page](docs/demos/qwen38-q4km/web/climate-lab.html)

~~~~
Design a polished, distinctive standalone website for a fictional climate dashboard called CLIMATE / DASHBOARD. Include emissions trend chart, region selector, impact metrics, scenario cards and data-source notes. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Community center

`web_community_center` · [generated page](docs/demos/qwen38-q4km/web/community-center.html)

~~~~
Design a polished, distinctive standalone website for a fictional community center called COMMUNITY / CENTER. Include today's activities, class calendar, volunteer CTA, room booking, announcements and location details. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Creative gallery

`web_creative_gallery` · [generated page](docs/demos/qwen38-q4km/web/creative-gallery.html)

~~~~
Create an experimental digital art gallery homepage for a fictional gallery called VOID/FORM.

Design goals:
- bold editorial composition
- huge typography
- dark background with one carefully chosen accent color
- artwork grid with unusual proportions — artworks are generative CSS/SVG/canvas compositions you design yourself
- artist names and metadata
- exhibition spotlight
- subtle cursor/hover interactions

This should feel like an award-winning creative-coding website, not a template.
~~~~

### CRM dashboard

`web_crm_dashboard` · [generated page](docs/demos/qwen38-q4km/web/crm-dashboard.html)

~~~~
Design a polished, distinctive standalone website for a fictional crm dashboard called CRM / DASHBOARD. Include pipeline board, contacts, activity feed, revenue summary, task list and global search. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Developer tool

`web_developer_tool` · [generated page](docs/demos/qwen38-q4km/web/developer-tool.html)

~~~~
Build the landing page for a fictional developer tool called FLUXTRACE, a fast distributed tracing platform.

Make it feel like a best-in-class developer product:
- crisp dark theme
- technical but highly polished typography
- hero statement
- terminal/code visual with realistic trace spans drawn in HTML/CSS
- performance metrics
- feature sections
- CTA

Use CSS/SVG for any diagrams. Restrained color, strong rhythm, real-looking copy.
~~~~

### Digital newsroom

`web_digital_newsroom` · [generated page](docs/demos/qwen38-q4km/web/digital-newsroom.html)

~~~~
Design a polished, distinctive standalone website for a fictional digital newsroom called DIGITAL / NEWSROOM. Include lead story, section navigation, live updates, article grid, editor picks, newsletter and subscription CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Online course

`web_education_course` · [generated page](docs/demos/qwen38-q4km/web/education-course.html)

~~~~
Design a signed-in learning dashboard for STUDIO CLASS. Include course progress, next lesson, lesson sidebar, instructor, notes, resources, discussion and assignment milestone. Use calm editorial classroom typography; make it an app screen, not marketing.
~~~~

### Email client

`web_email_client` · [generated page](docs/demos/qwen38-q4km/web/email-client.html)

~~~~
Design a polished, distinctive standalone website for a fictional email client called EMAIL / CLIENT. Include folders, inbox rows, reading pane, compose action, labels, search and calendar teaser. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Fashion editorial

`web_fashion_editorial` · [generated page](docs/demos/qwen38-q4km/web/fashion-editorial.html)

~~~~
Create an editorial fashion landing page for a fictional brand called ATELIER 09.

Design direction:
- luxury fashion magazine
- oversized serif paired with a modern sans-serif
- asymmetrical editorial layout
- minimal navigation
- collection teaser
- campaign statement
- product highlights
- refined footer

Create the visual drama with typography, whitespace, duotone CSS/SVG art and crop-like framing instead of photography. It should feel expensive and sparse.
~~~~

### Financial advisor

`web_financial_advisor` · [generated page](docs/demos/qwen38-q4km/web/financial-advisor.html)

~~~~
Design a premium personal-finance advisory homepage for CLEARWATER CAPITAL. Include trust-led hero, consultation CTA, services, market perspective cards, client journey, team and compliance footer. Use deep ink, parchment and one precise green accent; avoid generic fintech dashboards.
~~~~

### Fintech dashboard

`web_fintech_dashboard` · [generated page](docs/demos/qwen38-q4km/web/fintech-dashboard.html)

~~~~
Design a premium fintech analytics dashboard for a fictional product called Northstar Wealth.

It should feel like a real high-end SaaS product:
- top navigation with logo, workspace switcher and user avatar
- strong portfolio value hero area
- performance chart as the main visual (draw it with SVG or canvas)
- allocation breakdown
- recent transactions list
- small market indicators
- clear hierarchy between primary and secondary information

Use sophisticated typography, excellent spacing, subtle borders, soft shadows and refined micro-details. Avoid making it look like a generic Bootstrap dashboard.
~~~~

### Fleet logistics

`web_fleet_logistics` · [generated page](docs/demos/qwen38-q4km/web/fleet-logistics.html)

~~~~
Design a polished, distinctive standalone website for a fictional fleet logistics called FLEET / LOGISTICS. Include SVG vehicle map, live status, route cards, driver list, maintenance alerts and dispatch actions. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Furniture showroom

`web_furniture_showroom` · [generated page](docs/demos/qwen38-q4km/web/furniture-showroom.html)

~~~~
Design a polished, distinctive standalone website for a fictional furniture showroom called FURNITURE / SHOWROOM. Include gallery hero, room collections, material swatches, product details, design story and inquiry CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Indie game launcher

`web_game_launcher` · [generated page](docs/demos/qwen38-q4km/web/game-launcher.html)

~~~~
Design a polished, distinctive standalone website for a fictional indie game launcher called INDIE / GAME / LAUNCHER. Include featured game hero, game library, updates, friends panel, achievements and launch actions. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Grocery market

`web_grocery_market` · [generated page](docs/demos/qwen38-q4km/web/grocery-market.html)

~~~~
Create a refined grocery delivery homepage for GOODROOT. Include search, delivery location, cart, seasonal produce hero, categories, product cards with add controls, weekly basket and delivery promise. Use botanical colors, paper surfaces and CSS/SVG ingredient art.
~~~~

### Healthcare portal

`web_healthcare_portal` · [generated page](docs/demos/qwen38-q4km/web/healthcare-portal.html)

~~~~
Build a calm signed-in patient portal for NORTHSTAR HEALTH. Include next appointment, care team, medications, lab summaries, secure messages, billing shortcut and accessible navigation. Use reassuring copy, excellent contrast and a human clinical palette.
~~~~

### Hiking guide

`web_hiking_guide` · [generated page](docs/demos/qwen38-q4km/web/hiking-guide.html)

~~~~
Design a polished, distinctive standalone website for a fictional hiking guide called HIKING / GUIDE. Include route search, difficulty filters, featured trail, SVG elevation chart, conditions, packing list and save action. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Boutique hotel booking

`web_hotel_booking` · [generated page](docs/demos/qwen38-q4km/web/hotel-booking.html)

~~~~
Design a luxury booking homepage for fictional coastal hotel MIREN HOUSE. Include a CSS/SVG ocean hero, availability search, rooms, amenities, local experiences, book-now CTA and refined footer. Use stone, deep blue and coral; make it feel like an independent high-end hotel.
~~~~

### Incident response

`web_incident_response` · [generated page](docs/demos/qwen38-q4km/web/incident-response.html)

~~~~
Design a polished, distinctive standalone website for a fictional incident response called INCIDENT / RESPONSE. Include active incident banner, service health map, timeline, logs, owners, severity controls and postmortem link. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Insurance claims

`web_insurance_claims` · [generated page](docs/demos/qwen38-q4km/web/insurance-claims.html)

~~~~
Design a polished, distinctive standalone website for a fictional insurance claims called INSURANCE / CLAIMS. Include claim progress hero, document checklist, adjuster contact, incident timeline, coverage summary and upload action. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Inventory manager

`web_inventory_manager` · [generated page](docs/demos/qwen38-q4km/web/inventory-manager.html)

~~~~
Design a polished, distinctive standalone website for a fictional inventory manager called INVENTORY / MANAGER. Include warehouse selector, stock table, reorder alerts, item detail, movement chart and purchase action. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Job board

`web_job_board` · [generated page](docs/demos/qwen38-q4km/web/job-board.html)

~~~~
Build a polished job discovery homepage for WORKROOM. Include role/location search, recommended jobs with salary and tags, company spotlight, saved search, profile actions, career editorial and trust footer. Use a warm professional system with scan-friendly typography.
~~~~

### Language-learning app

`web_language_learning` · [generated page](docs/demos/qwen38-q4km/web/language-learning.html)

~~~~
Design a polished, distinctive standalone website for a fictional language-learning app called LANGUAGE-LEARNING / APP. Include daily streak, lesson progress, vocabulary cards, practice CTA, conversation goals and level map. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Legal consulting

`web_legal_consulting` · [generated page](docs/demos/qwen38-q4km/web/legal-consulting.html)

~~~~
Create a premium legal advisory site for VANTAGE LAW. Include consultation CTA, practice areas, featured insight, expertise metrics, partner profiles, offices and detailed footer. Use ink, parchment and copper with precise modern editorial typography.
~~~~

### Meal planner

`web_meal_planner` · [generated page](docs/demos/qwen38-q4km/web/meal-planner.html)

~~~~
Design a polished, distinctive standalone website for a fictional meal planner called MEAL / PLANNER. Include weekly calendar, recipe cards, grocery list, nutrition summary, servings control and quick-add interaction. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Museum exhibition

`web_museum_exhibition` · [generated page](docs/demos/qwen38-q4km/web/museum-exhibition.html)

~~~~
Design a polished, distinctive standalone website for a fictional museum exhibition called MUSEUM / EXHIBITION. Include exhibition hero, artist statement, artwork grid, visit details, current programs and ticket CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Music player

`web_music_player` · [generated page](docs/demos/qwen38-q4km/web/music-player.html)

~~~~
Build a polished desktop music player interface for a fictional app called SONORA.

Include:
- left navigation
- featured album hero
- recently played section
- curated playlists
- track list
- persistent bottom playback bar

Album artwork must be generated locally: gradient covers with SVG shapes or large typographic monograms (no external images).
Focus heavily on composition, typography, album-art treatment and visual depth.
~~~~

### Nonprofit campaign

`web_nonprofit_campaign` · [generated page](docs/demos/qwen38-q4km/web/nonprofit-campaign.html)

~~~~
Design a compelling environmental campaign for TIDE / TURN. Include hopeful hero, donation CTA, progress indicator, impact metrics, project stories, volunteer actions, field notes and partner footer. Use CSS/SVG shoreline imagery and humane editorial design.
~~~~

### Password manager

`web_password_manager` · [generated page](docs/demos/qwen38-q4km/web/password-manager.html)

~~~~
Design a polished, distinctive standalone website for a fictional password manager called PASSWORD / MANAGER. Include vault categories, search, password health summary, secure item cards, sharing and extension CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Pet care service

`web_pet_care` · [generated page](docs/demos/qwen38-q4km/web/pet-care.html)

~~~~
Build a premium pet-care booking page for PAWLINE. Include pet profile, upcoming booking, sitter search, care plans, reviews, trust signals, quick booking and neighborhood footer. Use terracotta, cream, moss and restrained CSS/SVG pet illustrations.
~~~~

### Podcast studio

`web_podcast_studio` · [generated page](docs/demos/qwen38-q4km/web/podcast-studio.html)

~~~~
Build a premium podcast network homepage for AFTERGLOW. Include featured episode player with SVG waveform, queue, show categories, host profiles, latest episodes, membership CTA and locally generated cover art. Use a dark broadcast palette with one warm accent.
~~~~

### Productivity app

`web_productivity_app` · [generated page](docs/demos/qwen38-q4km/web/productivity-app.html)

~~~~
Create a beautiful productivity application interface for a fictional product called DAYLINE.

A complete desktop app screen, not a marketing page:
- left sidebar
- date navigation
- today's focus hero
- task list
- calendar/timeline
- notes panel
- progress indicators
- quick-add interaction with hover/focus states

Calm, premium aesthetic. Typography, spacing, alignment and information density matter more than decorative effects.
~~~~

### Real estate search

`web_real_estate` · [generated page](docs/demos/qwen38-q4km/web/real-estate.html)

~~~~
Design FIELDHOUSE, a polished real-estate discovery interface. Include location search, filters, a CSS/SVG map panel, listing cards, featured property details, saved search and agent contact. Use warm-modern editorial typography and strong information density.
~~~~

### Research conference

`web_research_conference` · [generated page](docs/demos/qwen38-q4km/web/research-conference.html)

~~~~
Design a polished, distinctive standalone website for a fictional research conference called RESEARCH / CONFERENCE. Include conference hero, keynote speakers, call for papers, schedule, tracks, venue and registration CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Restaurant website

`web_restaurant` · [generated page](docs/demos/qwen38-q4km/web/restaurant.html)

~~~~
Create a premium restaurant website for a fictional restaurant called CASA ORO.

Style:
- contemporary Mediterranean fine dining
- warm cream, charcoal and olive palette
- elegant serif typography paired with a clean sans-serif
- menu highlights
- chef introduction
- reservation CTA
- location/hours
- refined footer

Evoke food and atmosphere through palette, ornament-free typography and simple SVG illustration rather than photographs. Award-winning feel, strong art direction.
~~~~

### Ski resort

`web_ski_resort` · [generated page](docs/demos/qwen38-q4km/web/ski-resort.html)

~~~~
Design a polished, distinctive standalone website for a fictional ski resort called SKI / RESORT. Include snow report, lift status, CSS/SVG trail map, lodging cards, lessons and pass CTA. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Sleep tracker

`web_sleep_tracker` · [generated page](docs/demos/qwen38-q4km/web/sleep-tracker.html)

~~~~
Design a polished, distinctive standalone website for a fictional sleep tracker called SLEEP / TRACKER. Include sleep score, nightly SVG graph, trends, bedtime routine, sound selector and coaching insight. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Sports club

`web_sports_club` · [generated page](docs/demos/qwen38-q4km/web/sports-club.html)

~~~~
Build a modern homepage for fictional women’s football team NORTHLINE FC. Include next match, results/table, player spotlights, tickets, membership, news and supporter store. Use navy, cream and signal red with CSS/SVG stadium motifs.
~~~~

### Travel editorial

`web_travel_editor` · [generated page](docs/demos/qwen38-q4km/web/travel-editor.html)

~~~~
Design an immersive travel editorial homepage for a fictional publication called THE NORTH EDIT.

The page should resemble a premium digital travel magazine:
- large destination hero built from layered CSS gradients and SVG landscape silhouettes (no photos)
- editorial headline and short story
- featured destinations
- horizontal story cards
- category navigation
- elegant footer

Typography and composition should be the main design strengths.
~~~~

### Weather atlas

`web_weather_atlas` · [generated page](docs/demos/qwen38-q4km/web/weather-atlas.html)

~~~~
Create an immersive weather dashboard called ISOBAR. Include current conditions, forecast, SVG hourly chart, abstract CSS/SVG city map, wind, air quality, daylight and saved locations. Use a dark atmospheric palette and precise instrument-like data visualization.
~~~~

### Wedding planner

`web_wedding_planner` · [generated page](docs/demos/qwen38-q4km/web/wedding-planner.html)

~~~~
Design a polished, distinctive standalone website for a fictional wedding planner called WEDDING / PLANNER. Include countdown, checklist, guest summary, vendor cards, budget progress and event timeline. Make the first viewport complete at 1440x900, use realistic copy, excellent hierarchy and responsive states. Create all imagery with CSS, SVG, gradients or canvas; do not use external images. Avoid generic templates and give the visual system a memorable palette and typography.
~~~~

### Wellness studio

`web_wellness_studio` · [generated page](docs/demos/qwen38-q4km/web/wellness-studio.html)

~~~~
Create a serene scheduling homepage for STILL / FORM. Include daily class schedule, booking CTA, philosophy hero, instructors, memberships, ritual feature, location and footer. Use warm mineral colors, serif headlines and soft CSS/SVG geometry.
~~~~
