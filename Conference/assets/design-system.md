# 🎨 Design System Guidelines

## Overview

The Conference Summary Website design system is built on principles of **minimalism**, **accessibility**, and **crypto-inspired aesthetics**. This document provides comprehensive guidelines for maintaining visual consistency across the platform.

## Design Philosophy

### Core Principles
- **Minimalism**: Clean, uncluttered interfaces that focus on content
- **Crypto-Inspired**: Subtle futuristic elements without being overwhelming
- **Accessibility**: Inclusive design that works for everyone
- **Performance**: Fast, responsive, and optimized for all devices

### Visual Identity
- **Tone**: Professional yet approachable
- **Style**: Modern, clean, and sophisticated
- **Personality**: Innovative, trustworthy, and forward-thinking

## Color Palette

### Primary Colors
```css
/* Base Colors */
--color-black: #000000;        /* Primary text, backgrounds */
--color-white: #FFFFFF;        /* Secondary text, cards */
--color-gray-50: #F9FAFB;      /* Light backgrounds */
--color-gray-100: #F3F4F6;     /* Subtle borders */
--color-gray-200: #E5E7EB;     /* Dividers */
--color-gray-300: #D1D5DB;     /* Disabled states */
--color-gray-400: #9CA3AF;     /* Placeholder text */
--color-gray-500: #6B7280;     /* Secondary text */
--color-gray-600: #4B5563;     /* Body text */
--color-gray-700: #374151;     /* Headings */
--color-gray-800: #1F2937;     /* Dark text */
--color-gray-900: #111827;     /* Darkest text */
```

### Accent Colors
```css
/* Crypto-Inspired Accents */
--color-blue-500: #3B82F6;     /* Primary accent */
--color-blue-600: #2563EB;     /* Hover states */
--color-blue-700: #1D4ED8;     /* Active states */
--color-purple-500: #8B5CF6;   /* Secondary accent */
--color-purple-600: #7C3AED;   /* Hover states */
--color-purple-700: #6D28D9;   /* Active states */
```

### Semantic Colors
```css
/* Status Colors */
--color-success: #10B981;      /* Success states */
--color-warning: #F59E0B;      /* Warning states */
--color-error: #EF4444;        /* Error states */
--color-info: #06B6D4;         /* Info states */
```

### Category Colors
```css
/* Event Category Colors */
--color-ai: #3B82F6;           /* AI events */
--color-crypto: #F59E0B;       /* Crypto events */
--color-web3: #8B5CF6;         /* Web3 events */
--color-hybrid: #10B981;       /* Hybrid events */
```

## Typography

### Font Family
```css
/* Primary Font */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

/* Monospace Font */
font-family: 'JetBrains Mono', 'Fira Code', 'Monaco', monospace;
```

### Font Weights
```css
--font-weight-normal: 400;     /* Body text */
--font-weight-medium: 500;     /* Emphasized text */
--font-weight-semibold: 600;   /* Subheadings */
--font-weight-bold: 700;       /* Headings */
```

### Font Sizes
```css
/* Desktop Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
--text-5xl: 3rem;      /* 48px */

/* Mobile Sizes (scaled down) */
--text-xs-mobile: 0.6875rem;   /* 11px */
--text-sm-mobile: 0.8125rem;   /* 13px */
--text-base-mobile: 0.9375rem; /* 15px */
--text-lg-mobile: 1.0625rem;   /* 17px */
--text-xl-mobile: 1.1875rem;   /* 19px */
```

### Line Heights
```css
--leading-tight: 1.25;         /* Headings */
--leading-normal: 1.5;         /* Body text */
--leading-relaxed: 1.625;      /* Long-form content */
```

## Spacing System

### Base Unit
The design system uses a **4px base unit** for consistent spacing:

```css
--space-1: 0.25rem;    /* 4px */
--space-2: 0.5rem;     /* 8px */
--space-3: 0.75rem;    /* 12px */
--space-4: 1rem;       /* 16px */
--space-5: 1.25rem;    /* 20px */
--space-6: 1.5rem;     /* 24px */
--space-8: 2rem;       /* 32px */
--space-10: 2.5rem;    /* 40px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
--space-20: 5rem;      /* 80px */
--space-24: 6rem;      /* 96px */
```

### Component Spacing
```css
/* Card Padding */
--card-padding: var(--space-6);        /* 24px */
--card-padding-mobile: var(--space-4); /* 16px */

/* Section Spacing */
--section-spacing: var(--space-16);    /* 64px */
--section-spacing-mobile: var(--space-12); /* 48px */

/* Element Spacing */
--element-spacing: var(--space-4);     /* 16px */
--element-spacing-mobile: var(--space-3); /* 12px */
```

## Border Radius

```css
--radius-sm: 0.25rem;   /* 4px - Small elements */
--radius-md: 0.5rem;    /* 8px - Cards, buttons */
--radius-lg: 0.75rem;   /* 12px - Large cards */
--radius-xl: 1rem;      /* 16px - Hero sections */
--radius-full: 9999px;  /* Fully rounded */
```

## Shadows

```css
/* Elevation System */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);

/* Hover Shadows */
--shadow-hover: 0 8px 25px -5px rgba(0, 0, 0, 0.15), 0 4px 10px -2px rgba(0, 0, 0, 0.1);
```

## Component Guidelines

### Buttons

#### Primary Button
```css
.btn-primary {
  background: var(--color-blue-500);
  color: var(--color-white);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: var(--color-blue-600);
  transform: translateY(-1px);
  box-shadow: var(--shadow-hover);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: var(--color-blue-500);
  border: 1px solid var(--color-blue-500);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
}
```

### Cards

#### Event Card
```css
.event-card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--card-padding);
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
  border: 1px solid var(--color-gray-100);
}

.event-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-blue-200);
}
```

### Form Elements

#### Input Fields
```css
.input {
  background: var(--color-white);
  border: 1px solid var(--color-gray-300);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-base);
  transition: border-color 0.2s ease;
}

.input:focus {
  outline: none;
  border-color: var(--color-blue-500);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
```

## Animation Guidelines

### Transition Timing
```css
--transition-fast: 0.15s ease;
--transition-normal: 0.2s ease;
--transition-slow: 0.3s ease;
```

### Hover Effects
- **Subtle lift**: `transform: translateY(-1px to -2px)`
- **Shadow enhancement**: Increase shadow intensity
- **Color transitions**: Smooth color changes
- **Scale effects**: Minimal scale (1.02x) for interactive elements

### Loading States
- **Skeleton screens**: Animated placeholders
- **Spinner**: Subtle rotation animation
- **Progress bars**: Smooth width transitions
- **Fade in**: Content appears with opacity transition

## Responsive Design

### Breakpoints
```css
/* Mobile First Approach */
--breakpoint-sm: 640px;   /* Small devices */
--breakpoint-md: 768px;   /* Medium devices */
--breakpoint-lg: 1024px;  /* Large devices */
--breakpoint-xl: 1280px;  /* Extra large devices */
--breakpoint-2xl: 1536px; /* 2X large devices */
```

### Grid System
```css
/* 12-Column Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}

/* Responsive Columns */
.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }
.col-6 { grid-column: span 6; }
.col-12 { grid-column: span 12; }

/* Mobile Responsive */
@media (max-width: 768px) {
  .col-md-6 { grid-column: span 6; }
  .col-md-12 { grid-column: span 12; }
}
```

## Accessibility Guidelines

### Color Contrast
- **Normal text**: Minimum 4.5:1 contrast ratio
- **Large text**: Minimum 3:1 contrast ratio
- **Interactive elements**: Minimum 3:1 contrast ratio

### Focus States
```css
.focus-visible {
  outline: 2px solid var(--color-blue-500);
  outline-offset: 2px;
}
```

### Touch Targets
- **Minimum size**: 44px × 44px
- **Recommended spacing**: 8px between touch targets
- **Visual feedback**: Clear pressed states

## Dark Mode Support

### Dark Mode Colors
```css
/* Dark Mode Variables */
[data-theme="dark"] {
  --color-background: var(--color-gray-900);
  --color-surface: var(--color-gray-800);
  --color-text: var(--color-gray-100);
  --color-text-secondary: var(--color-gray-400);
  --color-border: var(--color-gray-700);
}
```

### Implementation
- Use CSS custom properties for theme switching
- Provide toggle in user preferences
- Respect system preference by default
- Smooth transitions between themes

## Performance Considerations

### Image Optimization
- Use WebP format with fallbacks
- Implement lazy loading
- Provide multiple sizes for responsive images
- Use placeholder images during loading

### Animation Performance
- Use `transform` and `opacity` for animations
- Avoid animating layout properties
- Use `will-change` sparingly
- Implement `prefers-reduced-motion` support

---

*This design system ensures consistency, accessibility, and performance across the Conference Summary Website. All components should follow these guidelines for a cohesive user experience.*
