#!/usr/bin/env python3
"""
Filter records 678-903 from filter_candidates.json using semantic judgment.
Run this script with: python filter_part4.py
"""
import json
from pathlib import Path


def should_exclude(title, abstract):
    """
    Apply exclusion criteria based on semantic analysis of title and abstract.
    Returns (exclude: bool, reason: str or None)
    """
    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()
    combined = f"{title_lower} {abstract_lower}"

    # 1. NLP/text processing as primary focus
    nlp_terms = ["nlp", "text mining", "sentiment analysis", "named entity recognition",
                 "natural language processing", "tokenization", "text classification",
                 "computational linguistics", "discourse analysis"]
    if any(term in combined for term in nlp_terms):
        # Check if it's about methodology/validity/bias (those are retained)
        if not any(t in combined for t in ["research methodology", "epistemology", "validity", "bias"]):
            return True, "NLP/text processing primary focus"

    # 2. K-12 school context
    school_terms = ["k-12", "primary school", "secondary school", "elementary school",
                    "pupils", "schoolchildren"]
    if any(term in combined for term in school_terms):
        return True, "K-12 school context"

    # 3. Non-research applications
    non_research_terms = ["business productivity", "supply chain", "customer service",
                          "financial forecasting", "clinical diagnosis", "patient care",
                          "healthcare delivery", "sales optimization", "hr automation"]
    if any(term in combined for term in non_research_terms):
        if "research" not in combined:
            return True, f"Non-research application"

    # 4. Big data/digitisation without research methodology focus
    big_data_terms = ["big data analytics", "digital transformation", "industry 4.0", "smart city"]
    if any(term in combined for term in big_data_terms):
        if not any(t in combined for t in ["research", "methodology", "epistemology", "replication", "transparency"]):
            return True, "Big data/digitisation without research focus"

    # 5. Applied prediction/forecasting (not methodological inquiry)
    prediction_terms = ["predicting crime", "predict recidivism", "stock price predict",
                        "health outcome predict", "forecasting algorithm"]
    if any(term in combined for term in prediction_terms):
        if not any(t in combined for t in ["methodological", "methodology", "validity", "epistemology"]):
            return True, "Applied prediction/forecasting"

    # 6. Pedagogical effectiveness (student learning, not research methodology)
    if any(t in combined for t in ["student learning", "learning outcomes", "academic performance",
                                    "grades improve", "tutoring effectiveness"]):
        if not any(t in combined for t in ["research", "academic writing", "scholarly writing", "methodology"]):
            return True, "Pedagogical effectiveness (student learning)"

    return False, None


def main():
    """Process records 678-903 from filter_candidates.json"""
    input_file = Path("literature/filter_candidates.json")
    output_file = Path("literature/filter_decisions_part4.json")

    # Load all records
    print(f"Loading {input_file}...", flush=True)
    with open(input_file, "r", encoding="utf-8") as f:
        all_records = json.load(f)

    print(f"Total records in file: {len(all_records)}", flush=True)

    # Extract records 678-903 (0-indexed: 677-902 inclusive)
    target_records = all_records[677:903]
    print(f"Processing records 678-903: {len(target_records)} records", flush=True)

    # Process each record
    decisions = []
    retain_count = 0
    exclude_count = 0

    for i, record in enumerate(target_records, start=678):
        doi = record.get("doi", "")
        title = record.get("title", "")
        abstract = record.get("abstract", "")

        excluded, reason = should_exclude(title, abstract)

        if excluded:
            decision = "EXCLUDE"
            exclude_count += 1
        else:
            decision = "RETAIN"
            reason = "Relevant to AI in research, methodology, or journal policy"
            retain_count += 1

        decisions.append({
            "doi": doi,
            "decision": decision,
            "reason": reason if reason else ""
        })

        # Progress feedback
        if (i - 677) % 50 == 0:
            print(f"  Processed {i} ({i - 677} of 226 records)...", flush=True)

    # Write output
    print(f"Writing {output_file}...", flush=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(decisions, f, indent=2, ensure_ascii=False)

    # Summary
    print(f"\n{'='*60}")
    print(f"COMPLETED")
    print(f"{'='*60}")
    print(f"RETAIN:  {retain_count} records ({100*retain_count/226:.1f}%)")
    print(f"EXCLUDE: {exclude_count} records ({100*exclude_count/226:.1f}%)")
    print(f"Total:   {len(decisions)} records")
    print(f"Output:  {output_file}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
