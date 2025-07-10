import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def search_pubmed(query: str, retmax: int = 5) -> List[str]:
    url = f"{BASE_URL}/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except requests.RequestException as e:
        print(f"[ERROR] Failed to search PubMed: {e}")
        return []


def fetch_pubmed_details(paper_ids: List[str]) -> List[Dict[str, Optional[str]]]:
    if not paper_ids:
        return []

    url = f"{BASE_URL}/efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "xml"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        results: List[Dict[str, Optional[str]]] = []

        for article in root.findall(".//PubmedArticle"):
            paper: Dict[str, Optional[str]] = {
                "PubmedID": article.findtext(".//PMID"),
                "Title": article.findtext(".//ArticleTitle"),
                "Publication Date": article.findtext(".//PubDate/Year") or "Unknown",
                "Non-academic Author(s)": "",
                "Company Affiliation(s)": "",
                "Corresponding Author Email": "",
            }

            affiliations: List[str] = []
            authors: List[str] = []
            emails: List[str] = []

            for affiliation_info in article.findall(".//AffiliationInfo"):
                affil_text = affiliation_info.findtext("Affiliation") or ""
                if not is_academic(affil_text):
                    affiliations.append(affil_text)

            for author in article.findall(".//Author"):
                name_parts = [author.findtext("LastName", default=""), author.findtext("ForeName", default="")]
                author_name = " ".join(filter(None, name_parts)).strip()
                if author_name:
                    authors.append(author_name)

            for aff in affiliations:
                if "@" in aff:
                    emails.append(aff.split()[-1].strip(". ;:,").replace("mailto:", ""))

            paper["Non-academic Author(s)"] = "; ".join(authors) or "N/A"
            paper["Company Affiliation(s)"] = "; ".join(affiliations) or "N/A"
            paper["Corresponding Author Email"] = emails[0] if emails else "N/A"

            results.append(paper)

        return results

    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch PubMed details: {e}")
        return []
    except ET.ParseError as e:
        print(f"[ERROR] Failed to parse PubMed response: {e}")
        return []


def save_to_csv(papers: List[Dict[str, Optional[str]]], filename: str = "output.csv") -> None:
    import csv

    if not papers:
        print("[INFO] No data to save.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=papers[0].keys())
            writer.writeheader()
            writer.writerows(papers)

        print(f"[INFO] Results saved to {filename}")

    except Exception as e:
        print(f"[ERROR] Failed to save CSV: {e}")


def is_academic(affiliation: str) -> bool:
    academic_keywords = ["University", "College", "Institute", "School", "Hospital"]
    return any(keyword.lower() in affiliation.lower() for keyword in academic_keywords)
