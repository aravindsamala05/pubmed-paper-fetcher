# papers/cli.py

import argparse
from papers.fetch import search_pubmed, fetch_pubmed_details, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and save company authors to CSV.")

    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, default="pubmed_results.csv", help="Output CSV file name.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output.")

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Searching PubMed for query: {args.query}")

    paper_ids = search_pubmed(args.query)

    if args.debug:
        print(f"[DEBUG] Found PubMed IDs: {paper_ids}")

    if not paper_ids:
        print("No papers found for the query.")
        return

    papers = fetch_pubmed_details(paper_ids)

    if args.debug:
        print("[DEBUG] Paper details fetched.")

    save_to_csv(papers, filename=args.file)

if __name__ == "__main__":
    main()
