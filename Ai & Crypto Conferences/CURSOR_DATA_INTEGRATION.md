# 🛠 Cursor Data Integration Instructions

## Overview

You now have **3 data sources** successfully merged into a unified dataset:

1. **`Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv`** - 4,842 conference events
2. **`Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv`** - 332 hackathon events  
3. **`techweek.json`** - 5 Tech Week events

**Total: 5,179 events** merged and normalized into `merged-events.json`

---

## 🎯 Cursor Development Prompt

Copy and paste this prompt into Cursor to start development:

```markdown
# Conference Summary Website - Data Integration & Development

## Data Sources Available
I have 3 data sources already merged into a unified format:

1. **Conference Events**: 4,842 events from Cerebral Valley AI Events CSV
2. **Hackathon Events**: 332 events from Cerebral Valley AI Hackathons CSV  
3. **Tech Week Events**: 5 events from Tech Week calendar

**Total: 5,179 events** in `/data/merged-events.json`

## Your Task
Build a modern conference discovery website using this data with:

### 1. Data Loading
- Load events from `/data/merged-events.json`
- Implement proper TypeScript interfaces for the data structure
- Add data validation and error handling

### 2. Core Features
- **Homepage**: Hero section with search bar and category tabs
- **Timeline View**: Chronological display of all events
- **Event Cards**: Clean cards showing title, date, location, category
- **Search & Filter**: Full-text search + category/date/location filters
- **Responsive Design**: Mobile-first, works on all devices

### 3. Tech Stack
- **Frontend**: Next.js 14+ with TypeScript
- **Styling**: TailwindCSS + shadcn/ui components
- **Icons**: Lucide React
- **Animations**: Framer Motion

### 4. Data Structure
Each event has:
```typescript
interface ConferenceEvent {
  id: string;
  title: string;
  description: string;
  startDate: string;
  endDate: string;
  location: {
    city: string;
    country: string;
    venue: string;
  };
  category: 'AI' | 'Crypto' | 'Web3' | 'Hybrid' | 'Conference' | 'Hackathon' | 'Tech';
  price: {
    type: 'Free' | 'Paid' | 'Premium';
    amount: number;
    currency: string;
  };
  speakers: Speaker[];
  links: {
    website: string;
    tickets: string;
    livestream: string;
  };
  tags: string[];
  image: string;
  source: string;
  time: string;
  month: string;
}
```

### 5. Key Requirements
- **Performance**: < 2s load time, optimized for 5K+ events
- **Search**: Fast full-text search across all event fields
- **Filters**: Category, date range, location, price type
- **Accessibility**: WCAG 2.1 AA compliant
- **SEO**: Dynamic meta tags, sitemap generation

### 6. Design System
- **Colors**: Black/white base with blue (#3B82F6) and purple (#8B5CF6) accents
- **Typography**: Inter font family
- **Spacing**: 4px base unit system
- **Components**: Use shadcn/ui for consistency

Start by:
1. Setting up the Next.js project with TypeScript and TailwindCSS
2. Creating the data loading utilities
3. Building the homepage with event timeline
4. Implementing search and filtering

Focus on clean, minimalist design with smooth animations and excellent user experience.
```

---

## 📁 Project Structure for Cursor

```
conference-website/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── layout.tsx         # Root layout
│   │   ├── page.tsx           # Homepage
│   │   └── events/
│   │       └── [id]/
│   │           └── page.tsx   # Individual event pages
│   ├── components/            # Reusable components
│   │   ├── EventCard.tsx     # Event card component
│   │   ├── SearchBar.tsx     # Search functionality
│   │   ├── FilterPanel.tsx   # Filter controls
│   │   ├── TimelineView.tsx  # Event timeline
│   │   └── Navigation.tsx    # Site navigation
│   ├── lib/                  # Utilities
│   │   ├── data.ts          # Data loading functions
│   │   ├── utils.ts         # Helper functions
│   │   └── types.ts         # TypeScript interfaces
│   └── data/                # Data files
│       └── merged-events.json # Your merged event data
├── public/                   # Static assets
├── tailwind.config.js       # Tailwind configuration
├── next.config.js           # Next.js configuration
└── package.json             # Dependencies
```

---

## 🚀 Quick Start Commands

```bash
# 1. Create Next.js project
npx create-next-app@latest conference-website --typescript --tailwind --eslint --app

# 2. Install additional dependencies
cd conference-website
npm install @radix-ui/react-* lucide-react framer-motion zustand

# 3. Install shadcn/ui
npx shadcn-ui@latest init
npx shadcn-ui@latest add button card input select badge calendar

# 4. Copy your data
cp /path/to/merged-events.json src/data/

# 5. Start development
npm run dev
```

---

## 📊 Data Statistics

Your merged dataset contains:

- **Total Events**: 5,179
- **Conference Events**: 4,842 (93.5%)
- **Hackathon Events**: 332 (6.4%)
- **Tech Week Events**: 5 (0.1%)

**Categories Distribution**:
- Conference: 4,842 events
- Hackathon: 332 events  
- Tech: 5 events

**Geographic Distribution**:
- San Francisco: ~2,000+ events
- New York: ~500+ events
- London: ~300+ events
- Other cities: ~2,000+ events

---

## 🔧 Data Processing Notes

The merge utility has already:
- ✅ Normalized all data formats
- ✅ Removed duplicates
- ✅ Sorted chronologically
- ✅ Added proper IDs and metadata
- ✅ Categorized events appropriately
- ✅ Generated searchable tags

**Data Quality**: The merged data includes some parsing artifacts (quotes in city names, date formatting issues) that you may want to clean up during development.

---

## 🎨 Design Implementation

Use the design system from `/assets/design-system.md`:

- **Dark mode default** with crypto-inspired aesthetics
- **Mobile-first responsive** design
- **Smooth animations** and hover effects
- **Accessible** color contrast and keyboard navigation
- **Performance optimized** with lazy loading and virtualization

---

## 📈 Success Metrics

Aim for:
- **Load Time**: < 2 seconds
- **Search Performance**: < 100ms for queries
- **Mobile Experience**: 95+ Lighthouse score
- **Accessibility**: WCAG 2.1 AA compliance
- **User Engagement**: 3+ minutes average session

---

*Copy the development prompt above into Cursor to start building your conference summary website with the merged data!*
