# 🧪 PubMed Paper Fetcher

A command-line tool to search for research papers on PubMed, extract key metadata (title, authors, journal, date, affiliations), and save the results to a CSV file. It filters papers to include only those with at least one **non-academic** author affiliated with a **pharmaceutical or biotech** company.

---

## 🚀 Features

- 🔍 Search PubMed using any query
- 📄 Filter papers with **non-academic authors**
- 🧠 Identify **pharma/biotech affiliations**
- 📤 Save structured results to a CSV file
- 🐍 CLI built with Python and Poetry
- 📦 Published to [Test PyPI](https://test.pypi.org/project/pubmed-paper-fetcher-aravind/)

---

## 📦 Install from Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps pubmed-paper-fetcher-aravind
```

---

## ▶️ Run the CLI

```bash
get-papers-list "covid vaccine" -f demo_output.csv --debug
```

---

## 📁 Project Structure

```
pubmed-paper-fetcher/
├── papers/
│   └── fetch.py              # Core logic
├── scripts/
│   └── cli.py                # CLI entry point
├── pyproject.toml            # Poetry configuration
├── README.md                 # Documentation
└── pubmed_results.csv        # Output sample
```

---

## ⚙️ Installation (From Source)

```bash
git clone https://github.com/aravindsamala05/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
poetry shell
```

Run:

```bash
python scripts/cli.py "covid vaccine" -f demo_output.csv --debug
```

---

## 🧠 Author Affiliation Heuristics

The tool includes a heuristic to identify **non-academic authors** based on affiliation keywords.

### 🏫 Academic Keywords (excluded):
- "University", "Institute", "School", "Hospital", "College", "Lab"

### 🏢 Non-Academic Keywords (included):
- "Inc", "Ltd", "LLC", "GmbH", "Pharma", "Biotech", "Corporation", "Company"

If a paper contains **at least one** author with a non-academic affiliation, it is included in the output CSV.

---

## 📤 Sample Output (`demo_output.csv`)

| PubmedID  | Title                                      | Publication Date | Non-Academic Author(s) | Company Affiliation(s)        | Corresponding Author Email      |
|-----------|--------------------------------------------|------------------|--------------------------|--------------------------------|----------------------------------|
| 38629493  | The impact of COVID-19 vaccine hesitancy   | 2024-03-10       | Dr. Jane Smith           | Pfizer Inc.                    | jane.smith@pfizer.com            |
| 38621745  | Efficacy of mRNA vaccines in India         | 2023-12-18       | Rajesh K. Sharma         | Serum Institute of India Ltd.  | r.sharma@seruminstitute.com      |

---

## 📥 Command-Line Flags

| Flag           | Description                                |
|----------------|--------------------------------------------|
| `"query"`      | PubMed query string                        |
| `-f, --file`   | Custom CSV output filename                 |
| `-d, --debug`  | Enable verbose output                      |
| `-h, --help`   | Show help message                          |

---

## 🐛 Troubleshooting

```text
ModuleNotFoundError: No module named 'papers'
```

✅ Solution:

```bash
set PYTHONPATH=.
python scripts/cli.py "query"
```

Or simply use:

```bash
poetry run python scripts/cli.py "query"
```

---

## 🤖 External Tools and Resources Used

- **ChatGPT (OpenAI)** – Used for guidance, code review, and logic suggestions
- **PubMed API Docs** – For query formatting and parsing results
- **Python Docs** – For libraries like `argparse`, `csv`, `xml.etree`

All logic and implementation were built, reviewed, and tested locally by the author.

---

## 👨‍💻 Author

**Aravind Samala**  
GitHub: [@aravindsamala05](https://github.com/aravindsamala05)  
Email: aravind.samala16@gmail.com

---

## 📝 License

This project is licensed under the MIT License.
