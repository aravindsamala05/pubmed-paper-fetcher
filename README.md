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

## 📦 Published on Test PyPI

This package is published for testing on **Test PyPI**.

🔗 View on Test PyPI:  
[https://test.pypi.org/project/pubmed-paper-fetcher-aravind/](https://test.pypi.org/project/pubmed-paper-fetcher-aravind/)

### 📥 To Install:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps pubmed-paper-fetcher-aravind
```

### ▶️ To Run:

```bash
get-papers-list "covid vaccine" --debug
```

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

## ⚙️ Installation (From Source)

> Requires Python 3.8+ and [Poetry](https://python-poetry.org/docs/#installation)

### 📌 1. Clone the Repository

```bash
git clone https://github.com/aravindsamala05/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### 📌 2. Install Dependencies

```bash
poetry install
```

### 📌 3. Activate Virtual Environment

```bash
poetry shell
```

---

## 👤 How Users Can Run This Project and Get Output

### 🧾 1. Run the Tool

#### Basic:

```bash
python scripts/cli.py "cancer"
```

#### With Custom File:

```bash
python scripts/cli.py "covid vaccine" -f covid.csv
```

#### With Debug Output:

```bash
python scripts/cli.py "heart disease" -f heart.csv --debug
```

---

## 🧪 Usage via CLI Script

If installed from Test PyPI:

```bash
get-papers-list "diabetes treatment" -f output.csv --debug
```

---

## 📤 Output Format

The output is saved as a CSV file containing:

| PubmedID | Title | Publication Date | Non-Academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|------------------|-------------------------|-------------------------|-----------------------------|

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'papers'`

Fix it by using:

```bash
set PYTHONPATH=.
python scripts/cli.py "query"
```

Or install and run from PyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps pubmed-paper-fetcher-aravind
get-papers-list "query"
```

---

## 🔮 Future Improvements

- Export to JSON/Excel
- Detect institutions more intelligently
- Web-based frontend
- Email summary reports

---

## 👨‍💻 Author

**Aravind Samala**  
GitHub: [@aravindsamala05](https://github.com/aravindsamala05)

---

## 📝 License

This project is licensed under the MIT License.
