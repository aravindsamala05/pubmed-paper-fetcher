# 📚 PubMed Paper Fetcher

A simple Python CLI tool to fetch PubMed paper details and extract non-academic author affiliations.

---

## 🚀 Features

- 🔍 Search PubMed papers by query.
- 📄 Output paper details including:
   - PubMed ID
   - Title
   - Publication Date
   - Non-academic Authors
   - Company Affiliations
   - Corresponding Author Email
- ✅ Save results to a CSV file or display in the terminal.
- ⚙️ Easy-to-use CLI.
- 📦 Packaged with Poetry, published to Test PyPI.

---

## 📦 Installation

### ✅ Install from Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-paper-fetcher-aravind
```

✔️ The package is available on **Test PyPI**, a testing Python package repository.

---

## 🔧 CLI Usage

### ▶️ Basic Example (Print to Console)

```bash
get-papers-list "cancer"
```

### ▶️ Save Output to CSV

```bash
get-papers-list "cancer" -f results.csv
```

### ▶️ Show Debug Information

```bash
get-papers-list "cancer" -f results.csv --debug
```

---

## 📑 CLI Arguments

| Argument / Option          | Description                                   | Required |
|----------------------------|-----------------------------------------------|----------|
| `query`                    | Search term for PubMed                        | ✅ Yes   |
| `-f`, `--file`             | Output CSV file name                          | Optional |
| `-d`, `--debug`            | Show debug info (IDs, data)                   | Optional |
| `-h`, `--help`             | Show CLI help message                         | Auto     |

---

## 🔗 Example CSV Output

| PubmedID | Title                 | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|------------------------|------------------|------------------------|------------------------|---------------------------|
| 40635126 | Cancer Genomics         | 2025             | John Doe               | BioPharma Inc.         | john.doe@biopharma.com    |

---

## 🛡️ LLM Assistance

This project was developed with the assistance of Large Language Models (LLMs) for:
- API exploration
- Code refactoring
- Documentation writing

---

## 🔨 Development & Build (Optional)

To build and upload the project:
```bash
python -m poetry build
twine upload --repository testpypi dist/*
```

---

## ✅ License

MIT License
