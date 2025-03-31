# Political News Data Results

This project analyzes news coverage of Former Vice President Kamala Harris and President Donald Trump during the 2024 U.S. election season. It explores which outlets covered each candidate, how frequently, and what topics were most associated with each.

---

## Project Structure

```
political_campaign_2024/
│
├── political_news_data_2024/       # Scraped news data (CSV files)
├── python/
│   └── Political_News_Code.py      # Python script used for scraping and analysis
├── spaCy_objects/                  # spaCy NLP objects (tokens, processed docs)
├── Political_News_Data_Results.pdf # Final PDF report
├── Political_News_Data_Results.html # HTML version of report
├── newswords.spacy                 # spaCy language model
└── README.md                       # Project documentation (this file)
```

---

## Key Research Questions

- Did news outlets report on Kamala Harris and Donald Trump equally?
- What were the top sources for each candidate?
- How did coverage shift as Election Day approached?
- What topics were most associated with each candidate?

---

## Methodology

- News headlines were scraped from Google News RSS feeds.
- Data range: September 29 to November 6, 2024.
- Headlines were processed using spaCy to extract:
  - Named entities (e.g., "Kamala Harris")
  - Topics using part-of-speech tagging
  - Frequency of coverage over time

---

## Tools and Libraries

- Python (3.10)
- spaCy for natural language processing
- pandas for data manipulation
- matplotlib and seaborn for data visualization

---

## Outputs

- PDF Report: `Political_News_Data_Results.pdf`
- HTML Report: `Political_News_Data_Results.html`
- Cleaned dataset inside `political_news_data_2024/`

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/lawwrites/political_campaign_2024.git
   cd political_campaign_2024
   ```

---

## Contact

For questions or feedback, feel free to open an issue or connect with me on GitHub.

