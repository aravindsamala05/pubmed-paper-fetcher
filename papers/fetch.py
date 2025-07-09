# papers/fetch.py

import requests
import xml.etree.ElementTree as ET
import csv

# List of academic keywords to filter out academic institutions
ACADEMIC_KEYWORDS = ["University", "Institute", "College", "Hospital", "School", "Department", "Faculty", "Laboratory"]

def search_pubmed(query: str):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5  # Limit results
    }
    response = requests.get(url, params=params)
    data = response.json()
    ids = data.get("esearchresult", {}).get("idlist", [])
    return ids

def fetch_pubmed_details(pubmed_ids):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)

    root = ET.fromstring(response.content)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID", default="Unknown")
        title = article.findtext(".//ArticleTitle", default="No Title")
        pub_date = article.findtext(".//PubDate/Year", default="Unknown")

        non_academic_authors = []
        company_affiliations = []
        corresponding_email = ""

        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName", "")
            fore_name = author.findtext("ForeName", "")
            full_name = f"{fore_name} {last_name}".strip()

            affiliation = author.findtext(".//Affiliation", default="")
            email = ""

            # Find email if available in the affiliation text
            if "@" in affiliation:
                email = affiliation.split()[-1] if "@" in affiliation.split()[-1] else ""

            # If email found and not set yet, use it as corresponding author email
            if email and not corresponding_email:
                corresponding_email = email.strip("()[]<>.")

            # Check if this is a non-academic affiliation
            if affiliation and not any(keyword in affiliation for keyword in ACADEMIC_KEYWORDS):
                if full_name:
                    non_academic_authors.append(full_name)
                company_affiliations.append(affiliation)

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) if non_academic_authors else "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "N/A",
            "Corresponding Author Email": corresponding_email or "N/A"
        })

    return papers

def save_to_csv(papers, filename="pubmed_results.csv"):
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]

    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)

    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    query = "cancer"
    paper_ids = search_pubmed(query)
    print("Found paper IDs:", paper_ids)

    if paper_ids:
        papers = fetch_pubmed_details(paper_ids)

        # Print the data to check
        for paper in papers:
            print("\n--- Paper ---")
            for key, value in paper.items():
                print(f"{key}: {value}")

        # Save to CSV
        save_to_csv(papers)
