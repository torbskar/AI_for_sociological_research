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

    # === EARLY EXCLUDE CRITERIA ===

    # Pure technical CS/ML papers (no research methodology angle)
    pure_cs_markers = [
        'deep learning', 'neural network', 'convolutional', 'recurrent neural',
        'transformer architecture', 'bert', 'gpt', 'reinforcement learning',
        'genetic algorithm', 'particle swarm', 'optimization algorithm',
        'classification model', 'regression model', 'clustering algorithm',
        'encoder decoder'
    ]

    # AI as subject of study (not tool) - very specific
    ai_as_subject_strict = [
        'ai detection', 'detecting ai generated', 'identifying ai generated',
        'authenticity detection', 'synthetic content detection'
    ]

    # Teaching/student/educational context (not researcher practice)
    education_markers = [
        'student learning', 'classroom', 'curriculum', 'pedagogy',
        'educational ai', 'learning platform', 'tutoring system', 'e-learning',
        'teaching students', 'student engagement'
    ]

    # Domain-specific applications with no methodological angle
    domain_app_only = [
        'medical diagnosis', 'disease diagnosis', 'disease classification',
        'patient diagnosis', 'clinical decision', 'clinical diagnosis',
        'fault detection', 'anomaly detection', 'machine monitoring',
        'cybersecurity intrusion', 'fraud detection', 'credit scoring',
        'stock prediction', 'predictive maintenance'
    ]

    # Tangential topics
    tangential = [
        'plagiarism detection', 'academic integrity', 'cheating detection',
        'bot detection', 'fake account detection', 'misinformation detection',
        'copyright', 'intellectual property'
    ]

    if any(marker in text for marker in pure_cs_markers):
        return 'EXCLUDE', 'Pure CS/ML technical paper'

    if any(marker in text for marker in ai_as_subject_strict):
        return 'EXCLUDE', 'AI as subject matter (detection)'

    if any(marker in text for marker in education_markers):
        if not any(w in text for w in ['research', 'scholarship', 'scholar', 'academic practice']):
            return 'EXCLUDE', 'Educational/teaching focus'

    if any(marker in text for marker in domain_app_only):
        if not any(w in text for w in ['research methodology', 'methodological', 'research design', 'systematic literature']):
            return 'EXCLUDE', 'Domain-specific application'

    if any(marker in text for marker in tangential):
        return 'EXCLUDE', 'Tangential topic'

    # === STRONG RETAIN CRITERIA ===

    # 1. Explicit research/scholarship + AI
    research_markers = [
        'research process', 'research workflow', 'research methodology',
        'research practice', 'conducting research', 'doing research',
        'ai-assisted research', 'ai-supported research', 'ai-enabled research',
        'research collaboration', 'academic research',
        'literature review', 'systematic review', 'meta-analysis', 'systematic literature review',
        'data analysis', 'qualitative analysis', 'coding', 'thematic analysis',
        'researcher practice', 'research team'
    ]

    # 2. Epistemology, philosophy, integrity
    epistemology_markers = [
        'epistemology', 'epistemological', 'philosophy of science', 'philosophy of',
        'scientific integrity', 'research integrity', 'research ethics',
        'reproducibility', 'replicability', 'reproducible', 'reliable',
        'transparency', 'open science', 'open scholarship', 'pre-registration',
        'rigor', 'validity', 'generalizability'
    ]

    # 3. Policy, governance, institutions
    policy_markers = [
        'journal policy', 'publication policy', 'publishing', 'journal guidelines',
        'peer review', 'institutional policy', 'research governance',
        'research regulation', 'institutional guidelines'
    ]

    # 4. Responsible/ethical AI in research
    responsible_ai = [
        'responsible ai', 'trustworthy ai', 'ethical ai', 'ai governance',
        'ai ethics', 'fairness', 'bias in ai', 'accountability'
    ]

    # 5. Specific research practice keywords
    research_practice = [
        'knowledge synthesis', 'knowledge extraction', 'research synthesis',
        'information synthesis', 'research mapping', 'bibliometric', 'scientometric',
        'research landscape', 'research trends'
    ]

    if any(m in text for m in research_markers):
        if 'ai' in text or 'artificial intelligence' in text:
            return 'RETAIN', 'AI as tool in research process'

    if any(m in text for m in epistemology_markers):
        if 'ai' in text or 'artificial intelligence' in text:
            return 'RETAIN', 'Epistemology/research integrity implications'

    if any(m in text for m in policy_markers):
        if 'ai' in text or 'artificial intelligence' in text:
            return 'RETAIN', 'Journal/institutional policy implications'

    if any(m in text for m in responsible_ai):
        if 'research' in text or 'academic' in text:
            return 'RETAIN', 'Responsible/ethical AI in research'

    if any(m in text for m in research_practice):
        if 'ai' in text or 'artificial intelligence' in text:
            return 'RETAIN', 'AI as tool in research practice'

    # === SPECIAL CASES ===

    # Sociology of technology/AI
    if 'sociology of' in text and ('ai' in text or 'artificial intelligence' in text or 'algorithm' in text or 'technology' in text):
        return 'RETAIN', 'Sociology of AI/technology'

    # Computational social science
    if 'computational social' in text or 'computational sociology' in text:
        return 'RETAIN', 'Computational social science'

    # Social science + AI
    if ('social science' in text or 'sociology' in text) and ('ai' in text or 'artificial intelligence' in text):
        return 'RETAIN', 'AI in social science research'

    # === UNCERTAIN ===

    # AI mentioned but framing unclear
    if 'ai' in text or 'artificial intelligence' in text:
        if len(abstract or '') < 150:
            return 'UNCERTAIN', 'AI present but abstract too sparse'
        return 'UNCERTAIN', 'AI mentioned, relevance to research practice unclear'

    return 'EXCLUDE', 'No AI or research methodology connection'


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

    # Show sample UNCERTAIN records
    print(f"\nSample UNCERTAIN records (first 10):")
    count = 0
    for record in screened:
        if record['Screening decision'] == 'UNCERTAIN' and count < 10:
            print(f"  {count+1}. {record['Title'][:75]}")
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
