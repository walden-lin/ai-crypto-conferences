# 📊 Conference Data Schema Documentation

## Overview

This document defines the data structure for conference events used in the Conference Summary Website. The schema is designed to be flexible, extensible, and optimized for search and filtering.

## Core Data Structure

### ConferenceEvent Interface

```typescript
interface ConferenceEvent {
  id: string;                    // Unique identifier
  title: string;                 // Event title
  description: string;           // Full event description
  startDate: string;            // ISO 8601 date string
  endDate: string;              // ISO 8601 date string
  location: Location;           // Location object
  category: Category;           // Event category
  price: Price;                 // Pricing information
  speakers: Speaker[];          // Array of speakers
  links: Links;                 // External links
  tags: string[];               // Searchable tags
  image?: string;               // Optional event image URL
}
```

### Location Interface

```typescript
interface Location {
  city: string;                 // City name
  country: string;              // Country name
  venue?: string;               // Optional venue name
  coordinates?: {               // Optional GPS coordinates
    lat: number;
    lng: number;
  };
}
```

### Category Type

```typescript
type Category = 'AI' | 'Crypto' | 'Web3' | 'Hybrid';
```

### Price Interface

```typescript
interface Price {
  type: 'Free' | 'Paid' | 'Premium';
  amount?: number;              // Price amount (if not free)
  currency?: string;            // Currency code (USD, EUR, etc.)
}
```

### Speaker Interface

```typescript
interface Speaker {
  name: string;                 // Speaker name
  title: string;                // Speaker title/position
  image?: string;               // Optional speaker photo URL
  bio?: string;                 // Optional speaker biography
  social?: {                    // Optional social media links
    twitter?: string;
    linkedin?: string;
    website?: string;
  };
}
```

### Links Interface

```typescript
interface Links {
  website?: string;             // Main event website
  tickets?: string;             // Ticket purchase link
  livestream?: string;          // Live streaming link
  agenda?: string;              // Event agenda/schedule
  contact?: string;             // Contact information
}
```

## Data Validation Rules

### Required Fields
- `id`: Must be unique, alphanumeric with hyphens
- `title`: Minimum 5 characters, maximum 100 characters
- `description`: Minimum 50 characters, maximum 1000 characters
- `startDate`: Valid ISO 8601 date string
- `endDate`: Valid ISO 8601 date string, must be after startDate
- `location.city`: Non-empty string
- `location.country`: Non-empty string
- `category`: Must be one of the defined categories
- `price.type`: Must be one of the defined price types

### Optional Fields
- `location.venue`: String, maximum 100 characters
- `location.coordinates`: Valid latitude (-90 to 90) and longitude (-180 to 180)
- `price.amount`: Positive number if type is not 'Free'
- `price.currency`: Valid ISO 4217 currency code
- `speakers`: Array of valid speaker objects
- `links`: Object with valid URLs
- `tags`: Array of strings, maximum 10 tags per event
- `image`: Valid URL to image file

### Data Quality Guidelines

1. **Dates**: All dates should be in UTC timezone
2. **Images**: Use high-quality images (minimum 800x400px)
3. **URLs**: All links should be valid and accessible
4. **Tags**: Use lowercase, hyphenated tags (e.g., "machine-learning")
5. **Descriptions**: Write engaging, informative descriptions
6. **Speakers**: Include professional headshots when available

## Search and Filtering

### Searchable Fields
- `title` (weight: 3)
- `description` (weight: 2)
- `speakers[].name` (weight: 2)
- `tags[]` (weight: 1)
- `location.city` (weight: 1)
- `location.country` (weight: 1)

### Filterable Fields
- `category`: Exact match
- `location.city`: Exact match
- `location.country`: Exact match
- `price.type`: Exact match
- `startDate`: Date range
- `tags[]`: Contains any of the specified tags

## Data Import Process

### From Spreadsheet
1. Export spreadsheet as CSV
2. Map columns to schema fields
3. Validate data against schema
4. Convert to JSON format
5. Import into application

### Data Transformation
```typescript
// Example transformation function
function transformSpreadsheetRow(row: any): ConferenceEvent {
  return {
    id: generateId(row.title),
    title: row.title,
    description: row.description,
    startDate: parseDate(row.startDate),
    endDate: parseDate(row.endDate),
    location: {
      city: row.city,
      country: row.country,
      venue: row.venue,
      coordinates: row.coordinates ? parseCoordinates(row.coordinates) : undefined
    },
    category: mapCategory(row.category),
    price: {
      type: mapPriceType(row.priceType),
      amount: row.priceAmount ? parseFloat(row.priceAmount) : undefined,
      currency: row.currency
    },
    speakers: parseSpeakers(row.speakers),
    links: {
      website: row.website,
      tickets: row.tickets,
      livestream: row.livestream
    },
    tags: parseTags(row.tags),
    image: row.image
  };
}
```

## Sample Data

See `conferences.json` for complete examples of properly formatted conference data.

## Future Extensions

### Additional Fields (Phase 2)
- `capacity`: Maximum number of attendees
- `registrationDeadline`: Last date to register
- `language`: Primary language of the event
- `difficulty`: Beginner, Intermediate, Advanced
- `format`: In-person, Virtual, Hybrid
- `sponsors`: Array of sponsor information
- `agenda`: Detailed event schedule
- `reviews`: User reviews and ratings

### API Integration
- Real-time data updates
- Webhook notifications for changes
- Bulk data import/export
- Data validation endpoints
- Search analytics

---

*This schema is designed to be flexible and extensible. When adding new fields, ensure backward compatibility and update the validation rules accordingly.*
