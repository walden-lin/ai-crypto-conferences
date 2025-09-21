#!/usr/bin/env python3
"""
CSV Parser for AI Events and Hackathons
Handles the actual CSV structure from Cerebral Valley
"""

import csv
import json
import re
from datetime import datetime, date
from typing import List, Dict, Any

def parse_date_string(date_str: str, month_context: str = "") -> tuple:
    """Parse date strings like 'November 17-19' or '24 October'"""
    if not date_str or date_str.strip() == "":
        return None, None
    
    date_str = date_str.strip()
    
    # Handle "24 October" format (hackathons)
    if re.match(r'^\d+\s+\w+$', date_str):
        try:
            parsed_date = datetime.strptime(date_str, "%d %B")
            # Use 2025 as default year
            parsed_date = parsed_date.replace(year=2025)
            return parsed_date.date(), parsed_date.date()
        except:
            pass
    
    # Handle "November 17-19" format (events)
    if '-' in date_str:
        try:
            # Extract month and day range
            parts = date_str.split()
            if len(parts) >= 2:
                month = parts[0]
                day_range = parts[1]
                
                if '-' in day_range:
                    start_day, end_day = day_range.split('-')
                    start_date = datetime.strptime(f"{month} {start_day} 2025", "%B %d %Y").date()
                    end_date = datetime.strptime(f"{month} {end_day} 2025", "%B %d %Y").date()
                    return start_date, end_date
        except:
            pass
    
    # Handle single date like "November 17"
    try:
        parsed_date = datetime.strptime(f"{date_str} 2025", "%B %d %Y").date()
        return parsed_date, parsed_date
    except:
        pass
    
    return None, None

def clean_location(location: str) -> str:
    """Clean location string"""
    if not location:
        return "Unknown"
    
    # Remove quotes and extra whitespace
    location = location.strip().strip('"').strip("'")
    
    # Extract city, state/country
    if ',' in location:
        parts = location.split(',')
        city = parts[0].strip()
        return city
    else:
        return location.strip()

def parse_events_csv(filename: str) -> List[Dict[str, Any]]:
    """Parse the events CSV file"""
    events = []
    current_month = ""
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        # Find the header line (contains "Month,Event,Date")
        header_line = None
        for i, line in enumerate(lines):
            if 'Month' in line and 'Event' in line and 'Date' in line:
                header_line = i
                break
        
        if header_line is None:
            print(f"Could not find header in {filename}")
            return events
        
        # Parse data starting from line after header
        for line_num, line in enumerate(lines[header_line + 1:], start=header_line + 2):
            if not line.strip():
                continue
                
            # Split by comma, but handle quoted fields
            reader = csv.reader([line])
            row = next(reader)
            
            if len(row) < 6:
                continue
            
            month, event, date_str, time, location, link = row[:6]
            
            # Skip empty events
            if not event or event.strip() == "":
                continue
            
            # Update current month if provided
            if month and month.strip():
                current_month = month.strip()
            
            # Parse dates
            start_date, end_date = parse_date_string(date_str, current_month)
            
            if start_date is None:
                continue
            
            # Clean location
            location_clean = clean_location(location)
            
            event_data = {
                "id": f"event_{len(events) + 1}",
                "title": event.strip(),
                "description": "",
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat(),
                "location": location_clean,
                "category": "Conference",
                "link": link.strip() if link else "",
                "time": time.strip() if time else "",
                "source": "events_csv"
            }
            
            events.append(event_data)
    
    return events

def parse_hackathons_csv(filename: str) -> List[Dict[str, Any]]:
    """Parse the hackathons CSV file"""
    events = []
    current_month = ""
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        # Find the header line (contains "Month,Event,Start Date")
        header_line = None
        for i, line in enumerate(lines):
            if 'Month' in line and 'Event' in line and 'Start Date' in line:
                header_line = i
                break
        
        if header_line is None:
            print(f"Could not find header in {filename}")
            return events
        
        # Parse data starting from line after header
        for line_num, line in enumerate(lines[header_line + 1:], start=header_line + 2):
            if not line.strip():
                continue
                
            # Split by comma, but handle quoted fields
            reader = csv.reader([line])
            row = next(reader)
            
            if len(row) < 6:
                continue
            
            month, event, start_date_str, end_date_str, location, link = row[:6]
            
            # Skip empty events
            if not event or event.strip() == "":
                continue
            
            # Update current month if provided
            if month and month.strip():
                current_month = month.strip()
            
            # Parse start date
            start_date, _ = parse_date_string(start_date_str, current_month)
            end_date, _ = parse_date_string(end_date_str, current_month)
            
            if start_date is None:
                continue
            
            if end_date is None:
                end_date = start_date
            
            # Clean location
            location_clean = clean_location(location)
            
            event_data = {
                "id": f"hackathon_{len(events) + 1}",
                "title": event.strip(),
                "description": "",
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat(),
                "location": location_clean,
                "category": "Hackathon",
                "link": link.strip() if link else "",
                "time": "",
                "source": "hackathons_csv"
            }
            
            events.append(event_data)
    
    return events

def main():
    """Main function to parse both CSV files and create merged JSON"""
    
    print("🔄 Parsing CSV files...")
    
    # Parse events
    events_file = "data/Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv"
    hackathons_file = "data/Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv"
    
    events = parse_events_csv(events_file)
    hackathons = parse_hackathons_csv(hackathons_file)
    
    print(f"✅ Parsed {len(events)} events")
    print(f"✅ Parsed {len(hackathons)} hackathons")
    
    # Combine all events
    all_events = events + hackathons
    
    # Remove duplicates based on title and start date
    seen = set()
    unique_events = []
    for event in all_events:
        key = (event['title'], event['startDate'])
        if key not in seen:
            seen.add(key)
            unique_events.append(event)
    
    print(f"✅ Total unique events: {len(unique_events)}")
    
    # Save to JSON
    output_file = "data/events.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_events, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved to {output_file}")
    
    # Print sample events
    print("\n📋 Sample events:")
    for i, event in enumerate(unique_events[:5]):
        print(f"{i+1}. {event['title']} - {event['startDate']} - {event['location']}")

if __name__ == "__main__":
    main()
