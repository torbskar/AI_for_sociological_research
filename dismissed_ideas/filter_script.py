#!/usr/bin/env python3
import json
import re
import sys

# Read the JSON file
with open('literature/filter_candidates.json', 'r', encoding='utf-8') as f:
    all_records = json.load(f)

# Process first 226 records (indices 0-225)
records = all_records[0:226]

def should_exclude(title, abstract):
    """Apply exclusion criteria"""
    text = f"{title} {abstract}".lower()

    # 1. NLP/text processing focus
    if re.search(r'\bnlp\b|natural language processing|text mining|text classification|sentiment analysis|named entity|inductive coding', text):
        return True, "NLP/text processing or sentiment analysis focus"

    # 2. School/K-12 context (but not higher ed)
    if re.search(r'\bk-12\b|primary school|secondary school|elementary school|pupils|schoolchildren', text):
        if not re.search(r'higher education|academic research|research practice|scholarly|university', text):
            return True, "K-12/school context (not higher education)"

    # 3. AI affecting non-research outcomes
    if re.search(r'business productivity|business process|supply chain|inventory|warehouse|human resources|hr\b|recruitment|hiring|customer service|customer experience|clinical diagnosis|healthcare delivery|stock price|financial forecasting', text):
        return True, "Business/HR/healthcare/finance non-research context"

    # 4. Big data/digitisation frame unrelated to research
    if re.search(r'big data analytics|digital transformation|industry 4\.0|smart city', text):
        if not re.search(r'methodological|epistemological|research method|research practice', text):
            return True, "Big data/digitisation frame, not research methodology"

    # 5. Prediction/forecasting as applied method (not methodological inquiry)
    if re.search(r'predicting crime|recidivism prediction|forecasting crime', text):
        return True, "Crime/recidivism prediction as applied method"

    # 6. Pedagogical effectiveness (unless about research/scholarly writing)
    if re.search(r'student learning|student grades|exam score|tutoring\b', text):
        if not re.search(r'research|scholarly|academic writing|thesis|dissertation', text):
            return True, "Pedagogical effectiveness (student learning/tutoring)"

    # 7. Automated qualitative coding as technical NLP pipeline
    if re.search(r'automated coding|algorithmic coding|computational analysis of text|qualitative coding pipeline', text):
        return True, "Automated qualitative coding as technical pipeline"

    return False, ""

results = []
for record in records:
    doi = record.get('doi', '')
    title = record.get('title', '')
    abstract = record.get('abstract', '')

    exclude, reason = should_exclude(title, abstract)

    if exclude:
        decision = "EXCLUDE"
    else:
        decision = "RETAIN"
        # Provide reasoning for retain
        text = f"{title} {abstract}".lower()
        if re.search(r'ai.*research|research tool|literature review|systematic review', text):
            reason = "AI as research tool"
        elif re.search(r'methodological|epistemological|research method|research design', text):
            reason = "Methodological inquiry"
        elif re.search(r'ethical|responsible ai|transparency|accountability|bias', text):
            reason = "Ethical/transparency dimensions"
        elif re.search(r'open science|replication|reproducibility|research integrity|pre-registration', text):
            reason = "Open science/replication"
        elif re.search(r'journal policy|publication ethics|editorial|peer review', text):
            reason = "Journal policy/publication ethics"
        elif re.search(r'higher education|academic writing|scholarly practice|research workflow', text):
            reason = "Higher education/academic research"
        else:
            reason = "Uncertain; retain for human review"

    results.append({
        "doi": doi,
        "decision": decision,
        "reason": reason
    })

# Write results
with open('literature/filter_decisions_part1.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

retain = sum(1 for r in results if r['decision'] == 'RETAIN')
exclude = sum(1 for r in results if r['decision'] == 'EXCLUDE')

print(f"Processed: {len(results)} records")
print(f"RETAIN: {retain}")
print(f"EXCLUDE: {exclude}")
print(f"Output written to: literature/filter_decisions_part1.json")
