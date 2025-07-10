import argparse
from typing import Optional
from papers.fetch import search_pubmed, fetch_pubmed_details, save_to_csv

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and extract non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename (optional)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Running search for query: '{args.query}'")

    paper_ids = search_pubmed(args.query)

    if args.debug:
        print(f"[DEBUG] Found PubMed IDs: {paper_ids}")

    if not paper_ids:
        print("[INFO] No papers found for this query.")
        return

    paper_data = fetch_pubmed_details(paper_ids)

    if args.debug:
        print(f"[DEBUG] Extracted paper data: {paper_data}")

    if args.file:
        save_to_csv(paper_data, args.file)
    else:
        print("\n[OUTPUT]\n")
        for paper in paper_data:
            for key, value in paper.items():
                print(f"{key}: {value}")
            print("-" * 50)

if __name__ == "__main__":
    main()
