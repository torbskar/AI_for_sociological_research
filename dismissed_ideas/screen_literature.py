#!/usr/bin/env python3
import csv
import re
from pathlib import Path

def screen_record(title, abstract, keywords, source):
    """
    Refined screening based on the rubric:
    - RETAIN: AI as tool in research process, methodological implications
    - EXCLUDE: AI as subject, purely technical, teaching/student, tangential
    - UNCERTAIN: ambiguous or borderline
    """

    text = f"{title} {abstract} {keywords} {source}".lower()

    # === EXCLUDE CRITERIA (check these FIRST to avoid false positives) ===

    # 1. Pure technical CS/ML papers (no research methodology angle)
    pure_cs_markers = [
        'deep learning', 'neural network', 'convolutional', 'recurrent neural',
        'transformer architecture', 'bert', 'gpt', 'reinforcement learning',
        'genetic algorithm', 'particle swarm', 'optimization algorithm',
        'classification model', 'regression model', 'clustering algorithm'
    ]

    # 2. AI as subject of study (not tool)
    ai_as_subject = [
        'ai detection', 'detecting ai', 'identifying ai', 'gpt detection',
        'ai-generated content', 'authenticity detection', 'synthetic content',
        'ai literacy', 'understanding ai', 'ai awareness', 'ai perception'
    ]

    # 3. Teaching/student/educational context (not researcher practice)
    education_markers = [
        'student learning', 'classroom', 'curriculum', 'pedagogy',
        'educational ai', 'learning platform', 'tutoring system', 'e-learning'
    ]

    # 4. Domain-specific applications (not methodological)
    domain_app = [
        'medical diagnosis', 'disease detection', 'healthcare', 'clinical',
        'fault detection', 'anomaly detection', 'cybersecurity', 'intrusion',
        'image recognition', 'object detection', 'face recognition', 'biometric',
        'predictive maintenance', 'fraud detection', 'credit scoring'
    ]

    # 5. Tangential topics
    tangential = [
        'plagiarism detection', 'academic integrity', 'cheating detection',
        'bot detection', 'fake account', 'misinformation detection',
        'copyright', 'intellectual property'
    ]

    # Check for exclude categories
    if any(marker in text for marker in pure_cs_markers):
        return 'EXCLUDE', 'Pure CS/ML technical paper'

    if any(marker in text for marker in ai_as_subject):
        return 'EXCLUDE', 'AI as subject matter (detection/authenticity)'

    if any(marker in text for marker in education_markers):
        # Exception: if also about research methodology
        if not any(w in text for w in ['research', 'scholarship', 'academic work', 'scholarly']):
            return 'EXCLUDE', 'Educational/teaching focus'

    if any(marker in text for marker in domain_app):
        # Exception: if framed as methodological contribution to research
        if not any(w in text for w in ['research methodology', 'method', 'workflow', 'systematic']):
            return 'EXCLUDE', 'Domain-specific application'

    if any(marker in text for marker in tangential):
        return 'EXCLUDE', 'Tangential topic (integrity/detection)'

    # === RETAIN CRITERIA ===

    # 1. Explicit research methodology angle
    research_methodology = [
        'research process', 'research workflow', 'research methodology',
        'research practice', 'conducting research', 'doing research',
        'ai-assisted research', 'ai-supported research',
        'literature review', 'systematic review', 'meta-analysis',
        'data analysis', 'qualitative analysis', 'coding',
        'researcher', 'research team'
    ]

    # 2. Epistemology, philosophy, policy
    epistemology_policy = [
        'epistemology', 'epistemological', 'philosophy of science',
        'scientific integrity', 'research integrity', 'research ethics',
        'reproducibility', 'replicability', 'reproducible',
        'transparency', 'open science', 'pre-registration',
        'journal policy', 'publication', 'peer review',
        'institutional policy', 'research governance', 'research regulation'
    ]

    # 3. Explicit about structured/systematic AI use
    structured_use = [
        'structured', 'systematic', 'structured ai use', 'systematic ai',
        'protocol', 'framework', 'guidelines', 'best practice',
        'responsible ai', 'trustworthy ai', 'ethical ai'
    ]

    if any(m in text for m in research_methodology):
        if 'ai' in text:
            return 'RETAIN', 'AI as tool in research process'

    if any(m in text for m in epistemology_policy):
        if 'ai' in text:
            return 'RETAIN', 'Epistemological or policy implications'

    if any(m in text for m in structured_use):
        if 'ai' in text:
            return 'RETAIN', 'Structured/systematic AI use'

    # === UNCERTAIN ===

    # AI mentioned but framing unclear
    if 'ai' in text or 'artificial intelligence' in text:
        if len(abstract or '') < 150:
            return 'UNCERTAIN', 'AI present but abstract too sparse'
        return 'UNCERTAIN', 'AI mentioned, framing unclear'

    return 'EXCLUDE', 'No clear research methodology + AI connection'


def main():
    csv_path = Path("literature/scopus_export_Apr 4-2026_18c5e5be-9b6a-4485-b333-09e7e156a29a.csv")
    records = []

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    print(f"Read {len(records)} records")

    # Screen all records
    screened = []
    stats = {'RETAIN': 0, 'EXCLUDE': 0, 'UNCERTAIN': 0}

    for record in records:
        decision, reason = screen_record(
            record.get('Title', ''),
            record.get('Abstract', ''),
            record.get('Author Keywords', ''),
            record.get('Source title', '')
        )
        record['Screening decision'] = decision
        record['Reason'] = reason
        screened.append(record)
        stats[decision] += 1

    print(f"\nScreening results:")
    print(f"  RETAIN: {stats['RETAIN']}")
    print(f"  EXCLUDE: {stats['EXCLUDE']}")
    print(f"  UNCERTAIN: {stats['UNCERTAIN']}")

    # Show sample RETAIN records
    print(f"\nSample RETAIN records:")
    count = 0
    for record in screened:
        if record['Screening decision'] == 'RETAIN' and count < 5:
            print(f"  - {record['Title'][:70]}")
            count += 1

    # Show sample UNCERTAIN records
    print(f"\nSample UNCERTAIN records:")
    count = 0
    for record in screened:
        if record['Screening decision'] == 'UNCERTAIN' and count < 5:
            print(f"  - {record['Title'][:70]}")
            count += 1

    # Write output
    output_path = Path("literature/scopus_screening_results.csv")
    fieldnames = list(records[0].keys()) + ['Screening decision', 'Reason']

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(screened)

    print(f"\nScreened results written to: {output_path}")


if __name__ == '__main__':
    main()
