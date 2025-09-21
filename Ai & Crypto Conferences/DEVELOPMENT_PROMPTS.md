# 🚀 Conference Summary Website – Development Prompts

## Cursor-Ready Development Instructions

Copy and paste these prompts directly into Cursor for immediate development setup.

---

## 🎯 Main Development Prompt

```markdown
# Conference Summary Website – Full Stack Development

Build a modern, minimalist conference discovery website with the following specifications:

## Tech Stack Requirements
- **Frontend**: Next.js 14+ (App Router) + TypeScript
- **Styling**: TailwindCSS + shadcn/ui components
- **Icons**: Lucide React
- **Animations**: Framer Motion
- **State Management**: Zustand
- **Data**: JSON/CSV from provided conference data

## Core Features to Implement

### 1. Homepage Layout
- Hero section with title "Upcoming AI & Crypto Conferences" and tagline
- Centered search bar with placeholder "Search conferences, speakers, topics..."
- Category tabs: AI, Crypto, Web3, Hybrid (with event counts)
- Quick filter buttons: "This Week", "Next Month", "Near Me"
- Timeline view showing events in chronological order

### 2. Event Cards
- Clean card design with rounded corners and subtle shadows
- Display: title, date/time, location, category badge, price range
- Hover effects with smooth animations
- Expandable details: description, speakers, agenda highlights
- Action buttons: "Get Tickets", "Add to Calendar", "Share Event"

### 3. Search & Filtering
- Full-text search across all event fields
- Multi-select filters for category, location, date range
- Filter pills showing active filters with clear options
- Real-time search suggestions and auto-complete

### 4. Responsive Design
- Mobile-first approach
- Perfect rendering on iPhone, iPad, MacBook
- Touch-friendly interactions
- Accessible design (WCAG 2.1 AA)

## Design System
- **Colors**: Black/white base with blue (#3B82F6) and purple (#8B5CF6) accents
- **Typography**: Inter font family
- **Spacing**: 4px base unit system
- **Components**: Use shadcn/ui for consistent styling

## Data Structure
Use the provided conference data structure from `sample-data/conferences.json`. Each event should include:
- id, title, description, startDate, endDate, location, category, price, speakers, links

## Performance Requirements
- < 2 seconds initial load time
- Optimized images with lazy loading
- Static generation where possible
- SEO-friendly with proper meta tags

Start by setting up the project structure and implementing the homepage with basic event cards. Focus on clean, minimalist design with smooth animations.
```

---

## 🔧 Setup & Configuration Prompt

```markdown
# Project Setup & Configuration

Set up a new Next.js project with the following configuration:

## Initial Setup
1. Create Next.js 14+ project with TypeScript and TailwindCSS
2. Install and configure shadcn/ui components
3. Set up the project structure:
   ```
   src/
   ├── app/                 # Next.js App Router
   ├── components/          # Reusable components
   ├── lib/                # Utilities and configurations
   ├── data/               # Conference data
   └── types/              # TypeScript interfaces
   ```

## Required Dependencies
```bash
npm install next@latest react@latest react-dom@latest typescript
npm install tailwindcss postcss autoprefixer
npm install @radix-ui/react-* lucide-react framer-motion zustand
npm install @types/node @types/react @types/react-dom
```

## Configuration Files Needed
- `tailwind.config.js` with custom color palette
- `components.json` for shadcn/ui setup
- `tsconfig.json` with strict TypeScript settings
- `.env.local` for environment variables

## Design System Setup
Configure TailwindCSS with:
- Custom colors (black, white, blue, purple accents)
- Inter font family
- Custom spacing scale
- Dark mode as default

Set up shadcn/ui with components for:
- Button, Card, Input, Select, Badge, Calendar
- Dialog, Dropdown, Tabs, Tooltip

Create a design system file documenting all components and their usage.
```

---

## 🎨 UI Components Prompt

```markdown
# UI Components Development

Create the following reusable components with shadcn/ui and TailwindCSS:

## 1. EventCard Component
```typescript
interface EventCardProps {
  event: ConferenceEvent;
  variant?: 'default' | 'compact' | 'featured';
  onFavorite?: (eventId: string) => void;
  onShare?: (eventId: string) => void;
}
```

Features:
- Responsive card layout with hover animations
- Category badge with color coding
- Date/time display with timezone
- Location with map pin icon
- Price indicator (Free, $, $$, $$$)
- Action buttons with proper spacing
- Expandable details section

## 2. SearchBar Component
```typescript
interface SearchBarProps {
  placeholder?: string;
  onSearch: (query: string) => void;
  suggestions?: string[];
  isLoading?: boolean;
}
```

Features:
- Real-time search with debouncing
- Auto-suggestions dropdown
- Search history (local storage)
- Clear button and loading states
- Keyboard navigation support

## 3. FilterPanel Component
```typescript
interface FilterPanelProps {
  categories: string[];
  locations: string[];
  dateRange: { start: Date; end: Date };
  onFiltersChange: (filters: EventFilters) => void;
}
```

Features:
- Multi-select category filters
- Location dropdown with search
- Date range picker
- Filter pills showing active filters
- Clear all filters option
- Filter result counts

## 4. TimelineView Component
```typescript
interface TimelineViewProps {
  events: ConferenceEvent[];
  loading?: boolean;
  onEventClick: (event: ConferenceEvent) => void;
}
```

Features:
- Chronological event ordering
- Infinite scroll loading
- Skeleton loading states
- Empty state with helpful message
- Responsive grid layout

## 5. Navigation Component
```typescript
interface NavigationProps {
  activeCategory?: string;
  onCategoryChange: (category: string) => void;
  quickFilters: QuickFilter[];
}
```

Features:
- Sticky header with smooth scrolling
- Category tabs with event counts
- Quick filter buttons
- Mobile hamburger menu
- Search integration

Style all components with:
- Consistent spacing using 4px base unit
- Smooth hover and focus animations
- Proper focus states for accessibility
- Dark mode styling as default
- Mobile-first responsive design
```

---

## 📱 Responsive Design Prompt

```markdown
# Responsive Design Implementation

Implement responsive design for all screen sizes:

## Breakpoints
- Mobile: 320px - 768px
- Tablet: 768px - 1024px  
- Desktop: 1024px+

## Mobile Optimizations
- Touch-friendly tap targets (44px minimum)
- Swipe gestures for category navigation
- Collapsible filter panel
- Bottom sheet for event details
- Optimized typography scaling

## Tablet Optimizations
- Two-column event grid
- Sidebar filter panel
- Enhanced hover states
- Larger touch targets

## Desktop Enhancements
- Three-column event grid
- Persistent filter sidebar
- Keyboard shortcuts
- Advanced hover animations
- Multi-select with Ctrl/Cmd

## Component Responsive Behavior

### EventCard
- Mobile: Full width, stacked layout
- Tablet: Two columns, compact info
- Desktop: Three columns, expanded details

### SearchBar
- Mobile: Full width, prominent
- Tablet: Centered, medium width
- Desktop: Centered, max width 600px

### FilterPanel
- Mobile: Bottom sheet overlay
- Tablet: Collapsible sidebar
- Desktop: Persistent sidebar

### Navigation
- Mobile: Hamburger menu
- Tablet: Horizontal tabs
- Desktop: Full navigation with quick filters

## Testing Requirements
- Test on actual devices (iPhone, iPad, MacBook)
- Use browser dev tools for all breakpoints
- Verify touch interactions work properly
- Check accessibility with screen readers
- Validate performance on slower connections
```

---

## 🔍 Search & Filtering Prompt

```markdown
# Advanced Search & Filtering Implementation

Implement comprehensive search and filtering functionality:

## Search Implementation
```typescript
interface SearchConfig {
  fields: string[];           // Fields to search in
  weights: Record<string, number>; // Field importance
  fuzzy: boolean;            // Enable fuzzy matching
  minLength: number;         // Minimum query length
  debounceMs: number;        // Debounce delay
}
```

Features:
- Full-text search across title, description, speakers, topics
- Weighted search (title more important than description)
- Fuzzy matching for typos
- Search suggestions based on popular queries
- Search history with local storage
- Clear search functionality

## Filter System
```typescript
interface EventFilters {
  categories: string[];
  locations: string[];
  dateRange: { start: Date; end: Date };
  priceRange: { min: number; max: number };
  eventTypes: string[];
  speakers: string[];
}
```

Features:
- Multi-select category filtering
- Location filtering with autocomplete
- Date range picker with presets
- Price range slider
- Event type filtering (Conference, Meetup, etc.)
- Speaker filtering
- Filter combination logic (AND/OR)

## Performance Optimizations
- Debounced search (300ms delay)
- Virtualized results for large datasets
- Memoized filter calculations
- Lazy loading of filter options
- URL state management for shareable filters

## User Experience
- Real-time filter updates
- Filter result counts
- Clear all filters option
- Filter persistence in URL
- Keyboard navigation support
- Loading states for all operations

## Advanced Features
- Saved filter presets
- Filter recommendations
- Search analytics (popular queries)
- A/B testing for search algorithms
```

---

## 🚀 Performance & SEO Prompt

```markdown
# Performance & SEO Optimization

Optimize the website for speed and search engine visibility:

## Performance Optimization
- Static generation for all pages
- Image optimization with Next.js Image component
- Lazy loading for below-the-fold content
- Code splitting and dynamic imports
- Service worker for offline functionality
- CDN optimization for global delivery

## SEO Implementation
```typescript
// Dynamic meta tags for each event
export async function generateMetadata({ params }: { params: { id: string } }) {
  const event = await getEvent(params.id);
  return {
    title: `${event.title} - AI & Crypto Conference`,
    description: event.description,
    openGraph: {
      title: event.title,
      description: event.description,
      images: [event.image],
    },
  };
}
```

Features:
- Dynamic meta tags for each event page
- Structured data (JSON-LD) for events
- XML sitemap generation
- robots.txt configuration
- Open Graph and Twitter Card meta tags
- Canonical URLs for all pages

## Analytics Setup
- Privacy-focused analytics (Plausible or Fathom)
- Core Web Vitals monitoring
- User interaction tracking
- Search query analytics
- Performance monitoring

## Accessibility
- WCAG 2.1 AA compliance
- Screen reader optimization
- Keyboard navigation
- High contrast mode support
- Focus management
- ARIA labels and descriptions

## Testing
- Lighthouse audits (aim for 95+ score)
- Core Web Vitals testing
- Cross-browser compatibility
- Mobile performance testing
- Accessibility testing with axe-core
```

---

## 📊 Data Management Prompt

```markdown
# Data Management & API Integration

Set up robust data management for conference information:

## Data Structure
```typescript
interface ConferenceEvent {
  id: string;
  title: string;
  description: string;
  startDate: Date;
  endDate: Date;
  location: {
    city: string;
    country: string;
    venue?: string;
    coordinates?: { lat: number; lng: number };
  };
  category: 'AI' | 'Crypto' | 'Web3' | 'Hybrid';
  price: {
    type: 'Free' | 'Paid' | 'Premium';
    amount?: number;
    currency?: string;
  };
  speakers: Speaker[];
  links: {
    website?: string;
    tickets?: string;
    livestream?: string;
  };
  tags: string[];
  image?: string;
}
```

## Data Loading Strategy
- Static data loading for initial build
- Incremental Static Regeneration (ISR) for updates
- Client-side data fetching for real-time updates
- Error boundaries for failed data loads
- Loading states and skeleton screens

## Data Validation
- TypeScript interfaces for type safety
- Runtime validation with Zod
- Data sanitization and cleaning
- Duplicate detection and removal
- Date/time validation and normalization

## API Integration (Future)
- RESTful API endpoints for CRUD operations
- GraphQL for complex queries
- Webhook integration for real-time updates
- Rate limiting and caching
- Authentication and authorization

## Data Updates
- Manual data refresh mechanism
- Automated data sync (if API available)
- Version control for data changes
- Backup and recovery procedures
- Data migration scripts
```

---

## 🎯 Testing & Quality Assurance Prompt

```markdown
# Testing & Quality Assurance

Implement comprehensive testing strategy:

## Unit Testing
```typescript
// Example test for EventCard component
import { render, screen, fireEvent } from '@testing-library/react';
import { EventCard } from '@/components/EventCard';

describe('EventCard', () => {
  it('renders event information correctly', () => {
    const mockEvent = {
      id: '1',
      title: 'AI Conference 2024',
      startDate: new Date('2024-06-01'),
      location: { city: 'San Francisco', country: 'USA' },
      category: 'AI'
    };
    
    render(<EventCard event={mockEvent} />);
    
    expect(screen.getByText('AI Conference 2024')).toBeInTheDocument();
    expect(screen.getByText('San Francisco, USA')).toBeInTheDocument();
  });
});
```

## Integration Testing
- Component integration tests
- API integration tests
- Search and filter functionality
- User flow testing
- Cross-browser testing

## End-to-End Testing
- Playwright for E2E testing
- Critical user journeys
- Mobile device testing
- Performance testing
- Accessibility testing

## Quality Assurance Checklist
- [ ] All components render correctly
- [ ] Search functionality works as expected
- [ ] Filters apply and clear properly
- [ ] Responsive design on all devices
- [ ] Accessibility standards met
- [ ] Performance benchmarks achieved
- [ ] SEO optimization complete
- [ ] Cross-browser compatibility verified

## Continuous Integration
- Automated testing on pull requests
- Performance regression testing
- Accessibility testing in CI/CD
- Code quality checks (ESLint, Prettier)
- Security vulnerability scanning
```

---

## 🚀 Deployment & Production Prompt

```markdown
# Deployment & Production Setup

Deploy the conference website to production:

## Vercel Deployment (Recommended)
1. Connect GitHub repository to Vercel
2. Configure build settings:
   - Build Command: `npm run build`
   - Output Directory: `.next`
   - Install Command: `npm install`
3. Set environment variables
4. Configure custom domain
5. Enable automatic deployments

## Environment Configuration
```bash
# .env.local
NEXT_PUBLIC_SITE_URL=https://your-domain.com
NEXT_PUBLIC_ANALYTICS_ID=your-analytics-id
DATABASE_URL=your-database-url (if applicable)
```

## Production Optimizations
- Enable Vercel Analytics
- Configure CDN caching
- Set up monitoring and alerts
- Implement error tracking (Sentry)
- Configure backup procedures

## Domain & SSL
- Purchase custom domain
- Configure DNS settings
- Enable SSL certificate
- Set up redirects (www to non-www)
- Configure subdomains if needed

## Monitoring & Maintenance
- Uptime monitoring
- Performance monitoring
- Error tracking and alerting
- Regular security updates
- Data backup procedures
- Content update workflows

## Launch Checklist
- [ ] All features tested in production
- [ ] Analytics and tracking configured
- [ ] SEO meta tags verified
- [ ] Performance benchmarks met
- [ ] Security headers configured
- [ ] Backup procedures in place
- [ ] Monitoring alerts set up
- [ ] Documentation updated
```

---

## 📝 Additional Development Notes

### Code Quality Standards
- Use TypeScript for all components
- Follow React best practices
- Implement proper error handling
- Use semantic HTML elements
- Follow accessibility guidelines
- Write clean, documented code

### Git Workflow
- Feature branches for new development
- Pull request reviews required
- Automated testing on all PRs
- Semantic commit messages
- Regular code reviews

### Documentation
- Component documentation with Storybook
- API documentation (if applicable)
- Deployment runbooks
- User guides and FAQs
- Developer onboarding guide

---

*Copy any of these prompts into Cursor to start development immediately. Each prompt is self-contained and provides specific, actionable instructions for building the conference summary website.*
