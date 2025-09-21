# AI & Crypto Events Timeline

A modern, responsive website showcasing AI conferences, hackathons, and crypto events. Built with vanilla HTML, CSS, and JavaScript.

## 🌟 Features

- **4,887+ Events**: Comprehensive database of AI and crypto events
- **Smart Filtering**: Filter by category, location, and time period
- **Time-Based Navigation**: This Week, This Month, Upcoming, Past Events
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Dark theme with neon accents and glass effects
- **Real-time Search**: Find events by title or keywords

## 📊 Data Sources

- **4,794 Conference Events** from Cerebral Valley 2025 Events
- **329 Hackathons** from Cerebral Valley 2025 Hackathons
- **Automated Parsing**: Smart CSV parsing with date normalization
- **Deduplication**: Removes duplicate events automatically

## 🚀 Live Demo

Visit the live website: [https://walden-lin.github.io/ai-crypto-events](https://walden-lin.github.io/ai-crypto-events)

## 🛠️ Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/walden-lin/ai-crypto-events.git
   cd ai-crypto-events
   ```

2. **Start local server**:
   ```bash
   python3 -m http.server 3000
   ```

3. **Open in browser**:
   ```
   http://localhost:3000
   ```

## 📁 Project Structure

```
├── index.html              # Main website
├── test.html               # Data loading test page
├── parse_csv.py            # CSV parsing script
├── data/
│   ├── events.json         # Parsed and normalized events
│   ├── Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv
│   └── Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv
└── README.md
```

## 🔄 Data Updates

To update the events data:

1. **Update CSV files** in the `data/` directory
2. **Run the parser**:
   ```bash
   python3 parse_csv.py
   ```
3. **Commit changes**:
   ```bash
   git add data/events.json
   git commit -m "Update events data"
   git push
   ```

## 🎨 Design Features

- **Dark Theme**: Modern dark background with neon accents
- **Gradient Text**: Animated gradient text effects
- **Glass Morphism**: Backdrop blur effects on cards
- **Hover Animations**: Smooth transitions and hover effects
- **Responsive Grid**: Adaptive layout for all screen sizes

## 📱 Mobile Optimized

- Touch-friendly interface
- Responsive grid layout
- Optimized typography for mobile
- Fast loading on mobile networks

## 🌐 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.

---

**Built with ❤️ for the AI and crypto community**