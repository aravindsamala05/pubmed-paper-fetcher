# 🧪 PubMed Paper Fetcher

A command-line tool to search for research papers on PubMed, extract key metadata (title, authors, journal, date, affiliations), and save the results to a CSV file.

---

## 🚀 Features

- 🔍 Search PubMed using any keyword (e.g., "cancer", "covid vaccine")
- 📄 Fetch paper details like title, authors, journal, date, and affiliation
- 🗃️ Save results to a CSV file (default or custom filename)
- 🐍 Built with Python using Poetry for dependency management
- 🛠️ Optional debug mode for detailed terminal output

---

## 📁 Project Structure

```
pubmed-paper-fetcher/
├── papers/
│   └── fetch.py              # Core logic to fetch and parse PubMed data
├── scripts/
│   └── cli.py                # CLI entry point
├── pyproject.toml            # Poetry configuration file
├── README.md                 # Project documentation
└── pubmed_results.csv        # Example output file (generated after run)
```

---

## ⚙️ Installation

> Requires Python 3.8+ and [Poetry](https://python-poetry.org/docs/#installation).

### 📌 1. Clone the Repository

```bash
git clone https://github.com/aravindsamala05/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### 📌 2. Install Dependencies Using Poetry

```bash
poe
