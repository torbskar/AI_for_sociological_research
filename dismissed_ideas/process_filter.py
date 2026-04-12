#!/usr/bin/env python3
import json

file_path = r"C:\Users\torbskar\OneDrive - Universitetet i Oslo\Dokumenter\Paper\2026\AI_for_sociological_research\literature\filter_candidates.json"

with open(file_path, 'r', encoding='utf-8') as f:
    all_records = json.load(f)

records_to_process = all_records[904:1133]

def should_exclude(title, abstract):
    """Return (exclude, reason) tuple"""

    text = (title + " " + abstract).lower()

    # 1. NLP/text processing as primary focus
    nlp_terms = ['nlp', 'natural language processing', 'text mining', 'sentiment analysis', 'named entity recognition', 'topic modeling']
    if any(term in text for term in nlp_terms):
        if 'qualitative coding' in text and 'pipeline' not in text:
            pass
        else:
            return True, "NLP/text processing as primary focus"

    # 2. School or K-12 context
    k12_terms = ['k-12', 'primary school', 'secondary school', 'schoolchildren', 'pupils', 'grade school']
    higher_ed_terms = ['university', 'higher education', 'academic research', 'college', 'researcher']

    if any(term in text for term in k12_terms):
        if not any(term in text for term in higher_ed_terms):
            return True, "K-12/school context"

    # 3. AI affecting non-research outcomes
    non_research_terms = ['business productivity', 'hr management', 'supply chain', 'customer service', 'financial forecasting', 'clinical diagnosis', 'healthcare delivery']
    if any(term in text for term in non_research_terms):
        return True, "AI applied to non-research outcome"

    # 4. Big data/digitisation frame
    big_data_terms = ['big data analytics', 'digital transformation', 'industry 4.0', 'smart city']
    if any(term in text for term in big_data_terms):
        return True, "Big data/digitisation frame"

    # 5. Prediction/forecasting as primary purpose
    prediction_terms = ['predicting crime', 'stock price prediction', 'recidivism prediction', 'health outcome prediction']
    if any(term in text for term in prediction_terms):
        return True, "Prediction/forecasting as primary applied method"

    # 6. Pedagogical effectiveness
    if 'student learning' in text or 'tutoring' in text or 'grades' in text:
        if not any(t in text for t in ['research', 'academic writing', 'scholarly']):
            return True, "Pedagogical effectiveness for student learning"

    return False, None

results = []

for record in records_to_process:
    doi = record.get('doi', 'UNKNOWN')
    title = record.get('title', '')
    abstract = record.get('abstract', '')

    exclude, reason = should_exclude(title, abstract)

    if exclude:
        decision = "EXCLUDE"
        final_reason = reason
    else:
        decision = "RETAIN"
        final_reason = "Within scope: AI as research tool, methodology, epistemology, or policy"

    results.append({
        "doi": doi,
        "decision": decision,
        "reason": final_reason
    })

retain_count = sum(1 for r in results if r['decision'] == 'RETAIN')
exclude_count = sum(1 for r in results if r['decision'] == 'EXCLUDE')

print(f"RETAIN: {retain_count}")
print(f"EXCLUDE: {exclude_count}")
print(f"TOTAL: {len(results)}")

output_path = r"C:\Users\torbskar\OneDrive - Universitetet i Oslo\Dokumenter\Paper\2026\AI_for_sociological_research\literature\filter_decisions_part5.json"

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nResults written to: {output_path}")
