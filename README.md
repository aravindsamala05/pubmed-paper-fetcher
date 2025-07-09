# PubMed Paper Fetcher

\# PubMed Paper Fetcher



This project fetches scientific papers from the PubMed database, extracts non-academic authors working in pharmaceutical/biotech companies, and saves the results to a CSV file.



---



\## 🔧 Features



\- Search PubMed using a keyword.

\- Extract paper details: title, authors, affiliations, and emails.

\- Identify authors from non-academic affiliations (pharma/biotech companies).

\- Save results to a CSV file.

\- Easy to use Command Line Interface (CLI).



---



\## 🚀 Installation



1\. Clone the project:

&nbsp;  ```bash

&nbsp;  git clone <your-repository-url>

&nbsp;  cd pubmed-paper-fetcher

&nbsp;  ```



2\. Install dependencies using Poetry:

&nbsp;  ```bash

&nbsp;  python -m poetry install

&nbsp;  ```



---



\## ▶️ Usage



Basic example:

```bash

python -m poetry run get-papers-list "cancer"

```



Specify output file:

```bash

python -m poetry run get-papers-list "covid-19" -f covid\_results.csv

```



Enable debug mode:

```bash

python -m poetry run get-papers-list "malaria" -f malaria\_results.csv --debug

```



---



\## ⚙️ CLI Options



| Option / Argument | Purpose                                |

|--------------------|----------------------------------------|

| `<query>`          | Search term for PubMed (required)     |

| `-f, --file`       | CSV file to save results (optional)   |

| `-d, --debug`      | Show debug info during execution      |

| `-h, --help`       | Show help message                     |



---



\## 📂 Example Output (CSV)



| PubmedID | Title                   | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |

|----------|--------------------------|------------------|------------------------|------------------------|---------------------------|

| 38765421 | Cancer drug discovery     | 2024             | Alice Brown            | PharmaCorp Inc.        | alice@pharma.com          |

| 38765201 | Clinical trial results    | 2023             | N/A                    | N/A                    | N/A                       |



---



\## 🤖 LLM Usage (ChatGPT)



During development, ChatGPT was used for:

\- API documentation lookup.

\- Designing the CSV format.

\- Debugging Python errors.

\- Improving code readability.

\- Explaining Poetry usage and CLI best practices.



---



\## 🔬 PubMed API Used



\- \*\*esearch:\*\* to get PubMed IDs for a search query.

\- \*\*efetch:\*\* to get full paper details using PubMed IDs.



---



\## ✅ Done By



Aravind Samala



