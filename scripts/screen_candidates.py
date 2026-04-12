"""
Enhanced semantic screening of filter_candidates.json.
Writes filter_decisions.json with RETAIN/EXCLUDE decisions.
"""
import json, sys
from collections import Counter

CANDIDATES_PATH = "literature/automated_literature_searches/filter_tidying/filter_candidates.json"
DECISIONS_PATH  = "literature/automated_literature_searches/filter_tidying/filter_decisions.json"

with open(CANDIDATES_PATH, encoding='utf-8') as f:
    records = json.load(f)

def screen(rec):
    title = (rec.get('title') or '').lower()
    abstract = (rec.get('abstract') or '').lower()
    text = title + ' ' + abstract

    # Override signals: paper is about research practice
    research_signals = any(w in text for w in [
        'research method', 'research practice', 'research workflow', 'research process',
        'researcher', 'academic writing', 'scholarly writing', 'scientific writing',
        'literature review', 'systematic review', 'research integrity',
        'peer review', 'publication', 'journal policy', 'open science',
        'reproducib', 'replicab', 'transparency', 'pre-registr',
        'social science', 'sociology', 'sociolog', 'criminolog',
        'qualitative research', 'quantitative research', 'mixed method',
        'research design', 'epistem', 'methodology', 'tacit knowledge',
        'scientific knowledge', 'knowledge production',
        'higher education research', 'academic research',
    ])

    # C1: NLP/text processing as PRIMARY focus (building NLP systems)
    c1_strong = [
        'named entity recognition', 'part-of-speech', 'dependency parsing',
        'machine translation', 'speech recognition', 'optical character recognition',
        'word2vec', 'bert-based', 'transformer-based model',
        'text summarization', 'question answering system', 'dialogue system',
        'information retrieval system', 'knowledge graph extraction',
    ]
    c1_weak = [
        'natural language processing', 'nlp ', ' nlp,', 'text mining',
        'sentiment analysis', 'named entity', 'text classification',
        'information extraction', 'word embedding', 'topic model',
        'text analytics', 'computational linguistics',
    ]
    if any(t in text for t in c1_strong):
        if not research_signals:
            hit = next(t for t in c1_strong if t in text)
            return 'EXCLUDE', f'NLP system building: {hit}'
    if any(t in text for t in c1_weak):
        if not research_signals and not any(w in text for w in ['research tool', 'research assistant', 'academic', 'scholar']):
            hit = next(t for t in c1_weak if t in text)
            return 'EXCLUDE', f'NLP/text processing focus: {hit}'

    # C2: K-12 school context
    c2_terms = [
        'primary school', 'secondary school', ' k-12', 'k12 ', 'k-12 ',
        'schoolchildren', 'school pupils', 'high school student',
        'middle school student', 'elementary school', 'school district',
        'school teacher', 'k-12 education',
    ]
    if any(t in text for t in c2_terms):
        if not any(w in text for w in [
            'higher education', 'university student', 'college student',
            'graduate student', 'academic research', 'research practice',
        ]):
            hit = next(t for t in c2_terms if t in text)
            return 'EXCLUDE', f'K-12/school context: {hit}'

    # C3: Non-research operational AI
    c3_strong = [
        'supply chain management', 'supply chain optimization', 'supply chain resilience',
        'inventory management', 'demand forecasting', 'logistics optimization',
        'customer service automation', 'customer churn', 'customer satisfaction prediction',
        'clinical decision support system', 'computer-aided diagnosis', 'medical image analysis',
        'radiology ai', 'pathology detection', 'drug discovery pipeline',
        'financial fraud detection', 'credit scoring', 'algorithmic trading',
        'talent acquisition ai', 'employee performance prediction', 'workforce planning',
        'smart manufacturing', 'predictive maintenance', 'quality control automation',
        'crop yield prediction', 'precision agriculture', 'autonomous vehicle',
        'traffic management system', 'energy consumption prediction', 'building automation',
    ]
    c3_hit = next((t for t in c3_strong if t in text), None)
    if c3_hit and not research_signals:
        return 'EXCLUDE', f'Non-research operational AI: {c3_hit}'

    # C4: Big data / Industry 4.0 / digitalisation (not research-focused)
    c4_terms = [
        'big data analytics', 'industry 4.0', 'smart city',
        'digital transformation strategy', 'digitalization strategy',
        'internet of things', 'iot-enabled', 'cyber-physical system',
        'cloud computing adoption', 'digital twin technology',
    ]
    c4_hit = next((t for t in c4_terms if t in text), None)
    if c4_hit and not research_signals:
        return 'EXCLUDE', f'Big data/Industry 4.0 frame: {c4_hit}'

    # C5: Prediction as primary purpose
    c5_terms = [
        'recidivism prediction', 'recidivism risk assessment', 'crime prediction',
        'predictive policing', 'stock market prediction', 'stock price prediction',
        'cryptocurrency price prediction', 'disease outbreak prediction', 'mortality prediction',
        'hospital readmission prediction', 'sepsis prediction', 'suicide risk prediction',
        'poverty prediction', 'election outcome prediction', 'student dropout prediction',
    ]
    c5_hit = next((t for t in c5_terms if t in text), None)
    if c5_hit and not research_signals:
        return 'EXCLUDE', f'Prediction/forecasting as primary purpose: {c5_hit}'

    # C6: Pedagogical effectiveness (student learning outcomes, NOT research/writing)
    c6_terms = [
        'student learning outcome', 'student academic achievement',
        'automated essay scoring', 'automated grading system',
        'intelligent tutoring system', 'adaptive learning platform',
        'personalized learning system', 'student engagement platform',
        'gamification in education', 'flipped classroom effectiveness',
        'blended learning effectiveness', 'e-learning effectiveness',
    ]
    c6_hit = next((t for t in c6_terms if t in text), None)
    if c6_hit:
        if not any(w in text for w in [
            'research', 'scholarly writing', 'academic writing',
            'dissertation', 'thesis', 'literature review', 'research skill',
        ]):
            return 'EXCLUDE', f'Pedagogical effectiveness (student outcomes): {c6_hit}'

    # Additional clearly out-of-scope domains
    oos_terms = [
        'military target', 'weapon system', 'surveillance infrastructure',
        'smart home automation', 'wearable health monitoring device',
        'autonomous robot navigation', 'drone delivery', 'self-driving car',
        'satellite image classification for', 'flood prediction system',
    ]
    oos_hit = next((t for t in oos_terms if t in text), None)
    if oos_hit and not research_signals:
        return 'EXCLUDE', f'Out-of-scope domain: {oos_hit}'

    return 'RETAIN', 'Within scope: AI in research, methodology, policy, epistemology, or related'


results = []
for rec in records:
    decision, reason = screen(rec)
    results.append({'doi': rec.get('doi', ''), 'decision': decision, 'reason': reason})

with open(DECISIONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

retained = sum(1 for r in results if r['decision'] == 'RETAIN')
excluded = sum(1 for r in results if r['decision'] == 'EXCLUDE')
print(f'Total: {len(results)}  |  Retained: {retained} ({retained/len(results)*100:.1f}%)  |  Excluded: {excluded} ({excluded/len(results)*100:.1f}%)')
print()
print('Exclusion breakdown:')
reasons = Counter(r['reason'].split(':')[0] for r in results if r['decision'] == 'EXCLUDE')
for cat, n in reasons.most_common():
    print(f'  {n:3d}  {cat}')
