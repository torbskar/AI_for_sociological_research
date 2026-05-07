import json, sys, io, re, os, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = "C:/Users/torbskar/OneDrive - Universitetet i Oslo/Dokumenter/Paper/2026/AI_for_sociological_research"

with open(f"{BASE}/literature/pdf_metadata_raw.json", encoding="utf-8") as f:
    data = json.load(f)

def format_authors(authors):
    if not authors:
        return "[No author]"
    if len(authors) == 1:
        return authors[0]
    elif len(authors) <= 10:
        return ", ".join(authors[:-1]) + ", and " + authors[-1]
    else:
        return ", ".join(authors[:7]) + ", et al."

def chicago_article(authors, year, title, journal, vol, issue, pages, doi, flag=""):
    parts = []
    parts.append(format_authors(authors) + ".")
    parts.append(f"{year}." if year else "[n.d.].")
    parts.append(f'"{title}."')
    j = f"*{journal}*" if journal else ""
    loc = ""
    if vol and issue:
        loc = f"{vol} ({issue})"
    elif vol:
        loc = str(vol)
    if pages:
        loc = loc + f": {pages}" if loc else pages
    if j and loc:
        parts.append(f"{j} {loc}.")
    elif j:
        parts.append(f"{j}.")
    elif loc:
        parts.append(loc + ".")
    if doi:
        d = doi if doi.startswith("http") else f"https://doi.org/{doi}"
        parts.append(d + ".")
    s = " ".join(parts)
    if flag:
        s += f" [*{flag}*]"
    return s

def chicago_book(authors, year, title, city, publisher, doi, flag=""):
    parts = []
    parts.append(format_authors(authors) + ".")
    parts.append(f"{year}.")
    parts.append(f"*{title}*.")
    if city and publisher:
        parts.append(f"{city}: {publisher}.")
    elif publisher:
        parts.append(f"{publisher}.")
    if doi:
        d = doi if doi.startswith("http") else f"https://doi.org/{doi}"
        parts.append(d + ".")
    s = " ".join(parts)
    if flag:
        s += f" [*{flag}*]"
    return s

def chicago_chapter(authors, year, title, editors, book_title, pages, city, publisher, doi, flag=""):
    parts = []
    parts.append(format_authors(authors) + ".")
    parts.append(f"{year}.")
    parts.append(f'"{title}."')
    if editors:
        if pages:
            parts.append(f"In *{book_title}*, edited by {editors}, {pages}.")
        else:
            parts.append(f"In *{book_title}*, edited by {editors}.")
    else:
        parts.append(f"In *{book_title}*.")
    if city and publisher:
        parts.append(f"{city}: {publisher}.")
    if doi:
        d = doi if doi.startswith("http") else f"https://doi.org/{doi}"
        parts.append(d + ".")
    s = " ".join(parts)
    if flag:
        s += f" [*{flag}*]"
    return s

def chicago_preprint(authors, year, title, server, doi, flag=""):
    parts = []
    parts.append(format_authors(authors) + ".")
    parts.append(f"{year}." if year else "[n.d.].")
    parts.append(f'"{title}."')
    parts.append(f"Preprint. {server}.")
    if doi:
        d = doi if doi.startswith("http") else f"https://doi.org/{doi}"
        parts.append(d + ".")
    s = " ".join(parts)
    if flag:
        s += f" [*{flag}*]"
    return s

refs = {}

refs["10.1007_s11186-025-09641-3.pdf"] = chicago_article(
    ["Ensar Acemi", "Balazs Aczel", "Nihan Albayrak", "Nicholas J. L. Brown", "et al."],
    2025, "Why I Declare a Conflict of Interest and You Should Not",
    "Theory and Society", "54", None, "1137-1172", "10.1007/s11186-025-09641-3"
)

refs["10.31222_osf.io_n5zkw.pdf"] = chicago_preprint(
    ["Nicki Lisa Cole", "Sven Ulpts", "Agata Bochynska", "Eva Kormann", "Matthew Good", "Barbara Leitner", "Tony Ross-Hellauer"],
    2024, "Reproducibility and Replicability of Qualitative Research: An Integrative Review of Concepts, Barriers and Enablers",
    "OSF Preprints", "10.31222/osf.io/n5zkw"
)

refs["Abbate_etal_2022_Investigating_Healthcare_40_Transition_Through_A_Knowledge.pdf"] = chicago_article(
    ["Stefano Abbate", "Piera Centobelli", "Roberto Cerchione", "Eugenio Oropallo", "Emanuela Riccio"],
    2022, "Investigating Healthcare 4.0 Transition Through a Knowledge Management Perspective",
    "IEEE Transactions on Engineering Management", None, None, None, "10.1109/TEM.2022.3200889"
)

refs["Adjovi_2025_A_Worldwide_Itinerary_Of_Research_Ethics_In.pdf"] = chicago_article(
    ["Ingrid Sonya Mawussi Adjovi"],
    2025, "A Worldwide Itinerary of Research Ethics in Science for a Better Social Responsibility and Justice: A Bibliometric Analysis and Review",
    "Frontiers in Research Metrics and Analytics", None, None, None, "10.3389/frma.2025.1504937"
)

refs["Administrator_2024_Current_Reporting_Practices_In_Human_Neuroscience_Research.pdf"] = chicago_preprint(
    ["Arianna M. Gard", "Deena Shariq", "Alison A. Albrecht", "Alaina Lurie", "Hyung Cho Kim", "Colter Mitchell", "Luke W. Hyde"],
    2024, "Current Reporting Practices in Human Neuroscience Research",
    "bioRxiv", "10.1101/2024.09.28.615619"
)

refs["Akker_2023_Preregistration_In_Practice.pdf"] = chicago_preprint(
    ["Olmo R. van den Akker", "Marcel A. L. M. van Assen", "Marjan Bakker", "Mahmoud Elsherif", "Tsz Keung Wong", "Jelte M. Wicherts"],
    2023, "Preregistration in Practice: A Comparison of Preregistered and Non-Preregistered Studies in Psychology",
    "MetaArXiv", "10.31222/osf.io/fhdbs"
)

refs["AlHoorie_2021_Open_Science_In_Applied_Linguistics_An_Introduction.pdf"] = chicago_chapter(
    ["Ali H. Al-Hoorie", "Phil Hiver"],
    2021, "Open Science in Applied Linguistics: An Introduction to Metascience",
    "Luke Plonsky", "Open Science in Applied Linguistics", None, None, "John Benjamins", None,
    flag="year/pages need verification"
)

refs["Alberts_2023_Large_Language_Models_Llm_And_Chatgpt_What.pdf"] = chicago_article(
    ["Ian L. Alberts", "Lorenzo Mercolli", "Thomas Pyka", "George Prenosil", "Kuangyu Shi", "Axel Rominger", "Ali Afshar-Oromieh"],
    2023, "Large Language Models (LLM) and ChatGPT: What Will the Impact on Nuclear Medicine Be?",
    "European Journal of Nuclear Medicine and Molecular Imaging", None, None, None, "10.1007/s00259-023-06172-w"
)

refs["Applicable_2023_Meta_psychology_2023_Vol_7_Mp20223271.pdf"] = chicago_article(
    None, 2023, "Unfortunately, Journals in Industrial, Work, and Organizational Psychology Still Fail to Support Open Science Practices",
    "Meta-Psychology", "7", None, None, "10.15626/MP.2022.3271",
    flag="authors not identified from PDF"
)

refs["Article_2022_Meta_psychology_2022_Vol_6_Mp20202601.pdf"] = chicago_article(
    None, 2022, "Better Understanding the Population Size and Stigmatization of Psychologists Using Questionable Research Practices",
    "Meta-Psychology", "6", None, None, "10.15626/MP.2020.2601",
    flag="authors not identified from PDF"
)

refs["Author_2025_Accepted_4_July_2025_Published_Online_18.pdf"] = chicago_article(
    ["Daniele Mezzadri"],
    2025, "The Paradox of Ethical AI-Assisted Research",
    "Journal of Academic Ethics", "23", None, "2653-2667", "10.1007/s10805-025-09671-7"
)

refs["Available_2023_Doi_Httpsdoiorg1037074jalt20236120.pdf"] = chicago_article(
    ["Md Doulotuzzaman Xames"],
    2023, "ChatGPT for Research and Publication: Opportunities and Challenges",
    "Journal of Applied Learning and Teaching", "6", "1", None, "10.37074/jalt.2023.6.1.20",
    flag="page numbers not extracted"
)

refs["Barman_2025_Reinforcement_Learning_From_Human_Feedback_In_Llms.pdf"] = chicago_article(
    ["Kristian Gonzalez Barman", "Simon Lohse", "Henk W. de Regt"],
    2025, "Reinforcement Learning from Human Feedback in LLMs: Whose Culture, Whose Values, Whose Perspectives?",
    "Philosophy and Technology", "38", None, "35", "10.1007/s13347-025-00861-0"
)

refs["Bochynska_2023_Reproducible_Research_Practices_And_Transparency_Across_Ling.pdf"] = chicago_article(
    ["Agata Bochynska", "Liam Keeble", "Caitlin Halfacre", "Joseph V. Casillas", "Irys-Amelie Champagne", "Kaidi Chen", "Melanie Rothlisberger", "Erin M. Buchanan", "Timo B. Roettger"],
    2023, "Reproducible Research Practices and Transparency across Linguistics",
    "Glossa Psycholinguistics", None, None, None, None,
    flag="journal/volume/pages need verification"
)

refs["Botvinik_etal_2022_Analysis_Reproducibility_In_Mental_Health_Research_Challenge.pdf"] = chicago_article(
    ["Rotem Botvinik-Nezer", "Tor D. Wager"],
    2022, "Analysis Reproducibility in Mental Health Research: Challenges and Solutions",
    "Neuropsychopharmacology", None, None, None, None,
    flag="journal/volume/pages need verification"
)

refs["Care_etal_2023_Medicine_Health_Care_And_Philosophy_2023_2612.pdf"] = chicago_article(
    None, 2023, "Questions About ChatGPT",
    "Medicine, Health Care and Philosophy", "26", None, "1-2", "10.1007/s11019-023-10136-0",
    flag="authors not identified; title provisional"
)

refs["Cassinadri_2024_Chatgpt_And_The_Technology_education_Tension_Applying_Contex.pdf"] = chicago_article(
    ["Guido Cassinadri"],
    2024, "ChatGPT and the Technology-Education Tension: Applying Contextual Virtue Epistemology to a Cognitive Artifact",
    "Philosophy and Technology", "37", None, "14", "10.1007/s13347-024-00701-7"
)

refs["Chakravorti_etal_2025_Social_Scientists_On_The_Role_Of_Ai.pdf"] = chicago_article(
    ["Tatiana Chakravorti", "Xinyu Wang", "Pranav Narayanan Venkit", "Sai Koneru", "Kevin Munger", "Sarah Rajtmajer"],
    2025, "Social Scientists on the Role of AI in Research",
    "Proceedings of the AAAI/ACM Conference on AI Ethics and Society", "8", "1", None, "10.1609/aies.v8i1.36568"
)

refs["Challenge_2026_Journal_Of_Business_And_Psychology_2022_37459467.pdf"] = chicago_article(
    ["Christopher M. Castille", "Liana M. Kreamer", "Betsy H. Albritton", "George C. Banks", "Steven G. Rogelberg"],
    2022, "The Open Science Challenge: Adopt One Practice that Enacts Widely Shared Values",
    "Journal of Business and Psychology", "37", None, "459-467", "10.1007/s10869-022-09806-2"
)

refs["Chapter_etal_2023_Proceedings_Of_The_17th_Conference_Of_The.pdf"] = chicago_chapter(
    ["Anders Sogaard", "Daniel Hershcovich", "Miryam de Lhoneux"],
    2023, "A Two-Sided Discussion of Preregistration of NLP Research",
    None, "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics",
    "83-93", None, "Association for Computational Linguistics", "10.18653/v1/2023.eacl-main.6"
)

refs["Datta_etal_2024_Toward_Open_Science.pdf"] = chicago_preprint(
    ["Lachlan Deer", "Susanne Adler", "Hannes Datta", "Natalie Mizik", "Marko Sarstedt"],
    2024, "Toward Open Science in Marketing Research",
    "OSF Preprints", "10.31219/osf.io/f7a8c"
)

refs["Dehouche_2021_Plagiarism_In_The_Age_Of_Massive_Generative.pdf"] = chicago_article(
    ["Nassim Dehouche"],
    2021, "Plagiarism in the Age of Massive Generative Pre-Trained Language Models",
    "Ethics in Science and Environmental Politics", "21", None, "17-23", "10.3354/esep00195"
)

refs["Deressa_etal_2023_More_Than_Half_Of_Statistically_Significant_Research.pdf"] = chicago_article(
    ["Teshome K. Deressa", "David I. Stern", "Jaco Vangronsveld", "Jan Minx", "Sebastien Lizin", "Robert Malina", "Stephan B. Bruns"],
    2023, "More Than Half of Statistically Significant Research Findings in the Environmental Sciences are Actually Not",
    "Environmental Science and Technology", None, None, None, None,
    flag="journal/volume/pages need verification"
)

refs["Economicus_etal_2023_.pdf"] = chicago_article(
    ["Irina Gennadievna Dezhina"],
    2023, "Advantages and Problems of Open Science Practices",
    "Terra Economicus", "21", "3", "70-87", "10.18522/2073-6606-2023-21-3-70-87",
    flag="article in Russian; title translated"
)

refs["Editors_XXXX_Full_Guide_A_Guide_For_Social_Science.pdf"] = chicago_preprint(
    ["Priya Silverstein", "Colin Elman", "Amanda Montoya", "et al."],
    2023, "A Guide for Social Science Journal Editors on Easing into Open Science (Full Guide)",
    "OSF Preprints", "10.31219/osf.io/hstcx"
)

refs["Ethics_2023_The_Ethics_Of_Disclosing_The_Use_Of.pdf"] = chicago_article(
    None, 2023, "The Ethics of Disclosing the Use of Artificial Intelligence Tools in Academic Writing",
    "Research Ethics", "19", "4", "449-465", "10.1177/17470161231180449",
    flag="authors not identified from PDF"
)

refs["Fixter_2025_Opportunities_Challenges_And_Tensions_Open_Science.pdf"] = chicago_article(
    ["Madeleine Pownall", "Charlotte V. Talbot", "Laura Kilby", "Pete Branney"],
    2023, "Opportunities, Challenges, and Tensions: Open Science through a Lens of Qualitative Social Psychology",
    "Qualitative Psychology", None, None, None, None,
    flag="volume/pages need verification"
)

refs["Formosa_2024_Can_Chatgpt_Be_An_Author_Generative_Ai.pdf"] = chicago_article(
    ["Paul Formosa", "Sarah Bankins", "Rita Matulionyte", "Omid Ghasemi"],
    2024, "Can ChatGPT be an Author? Generative AI Creative Writing Assistance and Perceptions of Authorship, Creatorship, Responsibility, and Disclosure",
    "AI and Society", "40", None, "3405-3417", "10.1007/s00146-024-02081-0"
)

refs["Forsberg_2023_Edited_By_Eva_Forsberg_Lars_Geschwind.pdf"] = chicago_book(
    ["Eva Forsberg", "Lars Geschwind", "Sara Levander", "Wieland Wermke"],
    2023, "Peer Review in an Era of Evaluation: Understanding the Practice of Gatekeeping in Academia",
    None, "Springer", None
)

refs["Gallifant_2025_The_Tripod_llm_Reporting_Guideline_For_Studies_Using.pdf"] = chicago_article(
    ["Jack Gallifant", "Majid Afshar", "Saleem Ameen", "Yindalon Aphinyanaphongs", "Shan Chen", "et al."],
    2025, "The TRIPOD-LLM Reporting Guideline for Studies Using Large Language Models",
    "Nature Medicine", "31", None, "60-69", "10.1038/s41591-024-03425-5"
)

refs["Ganjavi_etal_2024_Publishers_And_Journals_Instructions_To_Authors_On.pdf"] = chicago_article(
    ["Conner Ganjavi", "Michael B. Eppler", "Asli Pekcan", "Brett Biedermann", "Andre Abreu", "Gary S. Collins", "Inderbir S. Gill", "Giovanni E. Cacciamani"],
    2024, "Publishers' and Journals' Instructions to Authors on Use of Generative Artificial Intelligence in Academic and Scientific Publishing: Bibliometric Analysis",
    "BMJ", "384", None, "e077192", "10.1136/bmj-2023-077192"
)

refs["Grant_2022_Transparent_Open_And_Reproducible_Prevention_Science.pdf"] = chicago_article(
    ["Sean Grant", "Kathleen E. Wendt", "Bonnie J. Leadbeater", "Lauren H. Supplee", "Evan Mayo-Wilson", "Frances Gardner", "Catherine P. Bradshaw"],
    2022, "Transparent, Open, and Reproducible Prevention Science",
    "Prevention Science", None, None, None, "10.1007/s11121-022-01336-w",
    flag="volume/pages need verification"
)

refs["Grossmann_etal_2023_AI_Transformation_Social_Science_Research.pdf"] = chicago_article(
    ["Igor Grossmann", "Matthew Feinberg", "Dawn C. Parker", "Nicholas A. Christakis", "Philip E. Tetlock", "William A. Cunningham"],
    2023, "AI and the Transformation of Social Science Research",
    "Science", "380", "6650", "1108-1109", "10.1126/science.adi1778",
    flag="DOI/pages need verification -- inferred from known citation"
)

refs["HP_2025_Microsoft_Word_19019_tamplate.pdf"] = chicago_article(
    ["Tiegue Vieira Rodrigues"],
    2025, "Distant Writing and the Epistemology of Authorship: On Creativity, Delegation, and Plagiarism in the Age of AI",
    "International Journal of Social Sciences and Humanities Invention", "12", "5", "8598-8613", "10.18535/ijsshi/v12i05.04"
)

refs["Hamaniuk_etal_2025_Genai_As_Scholarly_Ally_Patterns_Pedagogy_And.pdf"] = chicago_article(
    ["Vita A. Hamaniuk", "Serhiy O. Semerikov", "Yaroslav V. Shramko"],
    2025, "GenAI as Scholarly Ally: Patterns, Pedagogy, and Policies in Graduate Writing Research",
    "Educational Technology Quarterly", "2025", "3", "234-252", "10.55056/etq.965"
)

refs["Health_XXXX_Achieving_Health_Equity_Through_Conversational_Ai_A.pdf"] = chicago_article(
    None, None, "Achieving Health Equity through Conversational AI",
    "PLOS Digital Health", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Health_XXXX_Bias_In_Medical_Ai_Implications_For_Clinical.pdf"] = chicago_article(
    None, None, "Bias in Medical AI: Implications for Clinical Decision-Making",
    "PLOS Digital Health", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Health_XXXX_When_Eliza_Meets_Therapists_A_Turing_Test.pdf"] = chicago_article(
    None, None, "When Eliza Meets Therapists: A Turing Test",
    "PLOS Mental Health", None, None, None, "10.1371/journal.pmen.0000145",
    flag="authors/year not identified from PDF"
)

refs["Holzinger_2020_Measuring_The_Quality_Of_Explanations_The_System.pdf"] = chicago_article(
    ["Andreas Holzinger", "Andre Carrington", "Heimo Muller"],
    2020, "Measuring the Quality of Explanations: The System Causability Scale (SCS)",
    "KI -- Kunstliche Intelligenz", "34", None, "193-198", "10.1007/s13218-020-00636-z"
)

refs["Hopewell_2025_Consort_2025_Statement_Updated_Guideline_For_Reporting.pdf"] = chicago_article(
    None, 2025, "CONSORT 2025 Statement: Updated Guideline for Reporting Randomized Trials",
    "Nature Medicine", "31", None, "1776-1783", "10.1038/s41591-025-03635-5",
    flag="authors listed as writing group; not individually extractable from first 2 pages"
)

refs["Hosseini_2023_Fighting_Reviewer_Fatigue_Or_Amplifying_Bias_Considerations.pdf"] = chicago_article(
    ["Mohammad Hosseini", "Serge P.J.M. Horbach"],
    2023, "Fighting Reviewer Fatigue or Amplifying Bias? Considerations and Recommendations for Use of ChatGPT and Other Large Language Models in Scholarly Peer Review",
    "Research Integrity and Peer Review", "8", None, "4", "10.1186/s41073-023-00133-5"
)

refs["In_XXXX_The_Role_Of_Large_Language_Models_In.pdf"] = chicago_article(
    None, None, "The Role of Large Language Models in Medical Imaging",
    "Quantitative Imaging in Medicine and Surgery", None, None, None, "10.21037/qims-23-892",
    flag="authors/year not identified from PDF"
)

refs["Innovation_etal_2026_Untitled.pdf"] = chicago_article(
    ["Marc Selgas-Cors"],
    2025, "Sociotechnical Transformation: A Systematic Review on the Impact of Artificial Intelligence on Society and Organizations",
    "FinTech and Sustainable Innovation", None, None, None, "10.47852/bonviewFSI52026076"
)

refs["Isch_2025_Reflections_On_Adversarial_Collaboration_From_The_Adversarie.pdf"] = chicago_article(
    ["Calvin Isch", "Philip E. Tetlock", "Cory J. Clark"],
    2025, "Reflections on Adversarial Collaboration from the Adversaries: Was It Worth It?",
    "Theory and Society", "54", None, "929-946", "10.1007/s11186-025-09634-2"
)

refs["Issue_XXXX_Ending_Publication_Bias_A_Values_based_Approach_To.pdf"] = chicago_article(
    None, None, "Ending Publication Bias: A Values-Based Approach",
    "PLOS Biology", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Jensen_2025_377_Belardinelli.pdf"] = chicago_article(
    None, 2025, "Preregistration in Public Administration Research",
    "Journal of Behavioral Public Administration", "8", "1", "377", "10.30636/jbpa.81.377",
    flag="first author name not identified from PDF"
)

refs["Journal_2026_Httpsdoiorg101007s41471_025_00218_5.pdf"] = chicago_article(
    ["Meikel Soliman", "Marko Sarstedt", "Susanne J. Adler", "Doreen Siegfried", "Oliver Genschow", "Monika Imschloss"],
    2025, "A Tale of Open Science: Emergence of a New Normal",
    "Schmalenbach Journal of Business Research", "77", None, "763-792", "10.1007/s41471-025-00218-5"
)

refs["Lawson_2025_Running_Head_Citing_Decisions_In_Psychology.pdf"] = chicago_preprint(
    ["Katherine M. Lawson", "Brett A. Murphy", "Jovani Azpeitia", "Ella J. Lombard", "Terrence J. Pope"],
    2025, "Citing Decisions in Psychology: A Roadblock to Cumulative and Inclusive Science",
    "PsyArXiv", "10.31234/osf.io/6kvqg"
)

refs["Leonelli_2023_The_Philosophy_Of_Open_Science.pdf"] = chicago_book(
    ["Sabina Leonelli"],
    2023, "The Philosophy of Open Science",
    "Cambridge", "Cambridge University Press", "10.1017/9781009416368"
)

refs["Leonelli_2023_Opacity_And_Reproducibility_In_Data_Processing.pdf"] = chicago_chapter(
    ["Sabina Leonelli"],
    2023, "Opacity and Reproducibility in Data Processing: Reflections on the Dependence of AI on the Data Ecosystem",
    None, "Unknown edited volume", None, None, "De Gruyter", "10.1515/9783839467664-017",
    flag="editor and book title not identified from PDF"
)

refs["Library_2024_Obvious_Artificial_Intelligencegenerated_Anomalies_In_Publis.pdf"] = chicago_article(
    ["Bashar Haruna Gulumbe"],
    2024, "Obvious Artificial Intelligence-Generated Anomalies in Published Journal Articles: A Call for Enhanced Editorial Diligence",
    "Learned Publishing", None, None, None, "10.1002/leap.1626",
    flag="volume/pages need verification"
)

refs["Louderback_2021_Gambling_Researchers_Use_And_Views_Of_Open.pdf"] = chicago_preprint(
    ["Debi A. LaPlante", "Eric R. Louderback"],
    2021, "Gambling Researchers' Use and Views of Open Science Principles and Practices: A Brief Report",
    "OSF Preprints", "10.31219/osf.io/zpyta"
)

refs["Mendes_2023_Rae_revista_De_Administracao_De_Empresas_Fgv_Eaesp.pdf"] = chicago_article(
    ["Wesley Mendes-Da-Silva"],
    2023, "What Lecturers and Researchers in Business Management Need to Know about Open Science",
    "RAE -- Revista de Administracao de Empresas", "63", "1", None, "10.1590/S0034-759020230408x",
    flag="pages/article number not extracted"
)

refs["Nakagawa_2025_Poor_Hypotheses_And_Research_Waste_In_Biology.pdf"] = chicago_article(
    ["Shinichi Nakagawa", "David W. Armitage", "Tom Froese", "Yefeng Yang", "Malgorzata Lagisz"],
    2025, "Poor Hypotheses and Research Waste in Biology: Learning from a Theory Crisis in Psychology",
    "BMC Biology", "23", None, "33", "10.1186/s12915-025-02134-w"
)

refs["Nakagawa_2024_Untitled.pdf"] = chicago_preprint(
    ["Shinichi Nakagawa", "David W. Armitage", "Tom Froese", "Yefeng Yang", "Malgorzata Lagisz"],
    2024, "Poor Hypotheses and Research Waste in Biology: Learning from a Theory Crisis in Psychology",
    "EcoEvoRxiv", "10.32942/x2s03w",
    flag="preprint version; see published version Nakagawa 2025"
)

refs["Navigation_XXXX_Political_Orientation_And_Moral_Judgment_Of_Sexual.pdf"] = chicago_article(
    None, None, "Political Orientation and Moral Judgment of Sexual Behaviour",
    "Journal of Social and Political Psychology", None, None, None, "10.5964/jspp.9823",
    flag="metadata not extractable from PDF"
)

refs["Navigation_XXXX_Research_Into_Evidence_based_Psychological_Interventions_Nee.pdf"] = chicago_article(
    None, None, "Research into Evidence-Based Psychological Interventions Needs More Rigor",
    "European Journal of Psychology Open", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Ng_etal_2024_Investigating_The_Nature_Of_Open_Science_Practices.pdf"] = chicago_article(
    ["Jeremy Y. Ng", "Brenda Lin", "Tisha Parikh", "Holger Cramer", "David Moher"],
    2024, "Investigating the Nature of Open Science Practices across Complementary, Alternative, and Integrative Medicine Journals: An Audit",
    "PLOS ONE", None, None, None, None,
    flag="volume/pages need verification"
)

refs["Penders_2022_Process_And_Bureaucracy_Scientific_Reform_As_Civilisation.pdf"] = chicago_preprint(
    ["Bart Penders"],
    2022, "Process and Bureaucracy: Scientific Reform as Civilisation",
    "OSF Preprints", "10.31222/osf.io/685hx"
)

refs["Perkins_2025_Academic_Publisher_Guidelines_On_Ai_Usage_A.pdf"] = chicago_article(
    ["Mike Perkins", "Jasper Roe"],
    2024, "Academic Publisher Guidelines on AI Usage: A ChatGPT-Supported Thematic Analysis",
    "F1000Research", "12", None, "1398", "10.12688/f1000research.142411.2"
)

refs["Peterson_2025_Addressing_Student_Use_Of_Generative_Ai_In.pdf"] = chicago_article(
    ["Steven Peterson"],
    2025, "Addressing Student Use of Generative AI in Schools and Universities through Academic Integrity",
    "Frontiers in Education", None, None, None, "10.3389/feduc.2025.1610836",
    flag="volume/article number not extracted"
)

refs["Pownall_etal_2021_Embedding_Open_And_Reproducible_Science_Into_Teaching.pdf"] = chicago_article(
    ["Madeleine Pownall", "Flavio Azevedo", "Alaa Aldoh", "Mahmoud Elsherif", "Martin Vasilev", "Charlotte R. Pennington", "Olly Robertson", "et al."],
    2021, "Embedding Open and Reproducible Science into Teaching: A Bank of Lesson Plans and Resources",
    "Scholarship of Teaching and Learning in Psychology", None, None, None, None,
    flag="volume/pages need verification"
)

refs["Practices_etal_2023_Reproducible_Research_Practices_And_Barriers_To_Reproducible.pdf"] = chicago_preprint(
    ["Peter Kedron", "Joseph Holler", "Sarah Bardin"],
    2023, "Reproducible Research Practices and Barriers to Reproducible Research in Geography: Insights from a Survey",
    "OSF Preprints", "10.31219/osf.io/nyrq9"
)

refs["Quarterly_2025_Management_Review_Quarterly.pdf"] = chicago_article(
    None, 2025, "AI-Assisted Systematic Literature Reviews: A Hybrid Framework",
    "Management Review Quarterly", None, None, None, "10.1007/s11301-025-00522-8",
    flag="authors not identified from PDF"
)

refs["Researchers_2021_Frma_2020_586992_120.pdf"] = chicago_article(
    ["Daniel Toribio-Florez", "Lukas Anneser", "Felipe Nathan de Oliveira-Lopes", "Martijn Pallandt", "Isabell Tunn", "Hendrik Windel"],
    2021, "Where Do Early Career Researchers Stand on Open Science Practices? A Survey Within the Max Planck Society",
    "Frontiers in Research Metrics and Analytics", "2020", None, None, "10.3389/frma.2020.586992",
    flag="volume/pages need verification"
)

refs["Review_2021_Downloaded_From_Wwwannualreviewsorg_Guest_Guest_Ip_178742470.pdf"] = chicago_article(
    ["Brian A. Nosek", "Tom E. Hardwicke", "Hannah Moshontz", "Aurelien Allard", "Katherine S. Corker", "Anna Dreber", "Fiona Fidler", "et al."],
    2022, "Replicability, Robustness, and Reproducibility in Psychological Science",
    "Annual Review of Psychology", "73", None, "719-748", None,
    flag="DOI needs verification"
)

refs["Romero_2020_Scientific_Self_correction_The_Bayesian_Way.pdf"] = chicago_article(
    ["Felipe Romero", "Jan Sprenger"],
    2021, "Scientific Self-Correction: The Bayesian Way",
    "Synthese", "198", "Suppl 23", "S5803-S5823", "10.1007/s11229-020-02697-x"
)

refs["RossHellauer_2021_Dynamics_Of_Cumulative_Advantage_And.pdf"] = chicago_preprint(
    ["Tony Ross-Hellauer", "Stefan Reichmann", "Nicki Lisa Cole", "Angela Fessl", "Thomas Klebel", "Nancy Pontika"],
    2021, "Dynamics of Cumulative Advantage and Threats to Equity in Open Science: A Scoping Review",
    "SocArXiv", "10.31235/osf.io/d5fz7"
)

refs["Rudin_2023_Copyright_2023_By_International_Federation_Of_Social.pdf"] = chicago_article(
    ["Stephen M. Marson"],
    2023, "Editorial: My Experience with Artificial Intelligence",
    "International Journal of Social Work Values and Ethics", "20", "2", None, "10.55521/10-020-200"
)

refs["Sallam_2023_The_Utility_Of_Chatgpt_As_An_Example.pdf"] = chicago_preprint(
    ["Malik Sallam"],
    2023, "The Utility of ChatGPT as an Example of Large Language Models in Healthcare Education, Research and Practice",
    "SSRN", None,
    flag="preprint version; see published Sallam 2023 Healthcare"
)

refs["Sallam_XXXX_Chatgpt_Utility_In_Healthcare_Education_Research_And.pdf"] = chicago_article(
    ["Malik Sallam"],
    2023, "ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns",
    "Healthcare", "11", "6", "887", "10.3390/healthcare11060887"
)

refs["Schmalz_2025_Lets_Talk_About_Languageand_Its_Role_For.pdf"] = chicago_article(
    ["Xenia Schmalz", "Johannes Breuer", "Mario Haim", "Andrea Hildebrandt", "Philipp Knopfle", "Anna Yi Leung", "Timo Roettger"],
    2025, "Let's Talk about Language -- and Its Role for Replicability",
    "Humanities and Social Sciences Communications", None, None, None, "10.1057/s41599-025-04381-2",
    flag="volume/article number need verification"
)

refs["Sci_2023_Untitled.pdf"] = chicago_article(
    ["Zongjin Lin"],
    2023, "Why and How to Embrace AI Such as ChatGPT in Your Academic Life",
    "Royal Society Open Science", "10", None, "230658", "10.1098/rsos.230658"
)

refs["Science_2023_Reproducibility_In_Management_Science.pdf"] = chicago_preprint(
    ["Milos Fisar", "Ben Greiner", "Christoph Huber", "Elena Katok", "Ali I. Ozkes", "and the Management Science Reproducibility Collaboration"],
    2023, "Reproducibility in Management Science",
    "OSF Preprints", "10.31219/osf.io/mydzv"
)

refs["Sebastian_etal_2025_Em_jice250006_284290.pdf"] = chicago_article(
    ["Rigin Sebastian", "Noufal Naheem Kottekkadan", "Toney K. Thomas", "Mohammed Niyas KK"],
    2025, "Generative AI Tools (ChatGPT) in Social Science Research",
    "Journal of International Consumer Experience", None, None, "284-290", None,
    flag="journal/DOI need verification"
)

refs["Semmelrock_2025_Reproducibility_In_Machinelearningbased_Research_Overview_Ba.pdf"] = chicago_article(
    ["Harald Semmelrock", "Tony Ross-Hellauer", "Simone Kopeinik", "Dieter Theiler", "Armin Haberl", "Stefan Thalmann", "Dominik Kowald"],
    2025, "Reproducibility in Machine-Learning-Based Research: Overview, Barriers, and Drivers",
    "AI Magazine", None, None, None, "10.1002/aaai.70002",
    flag="volume/pages need verification"
)

refs["Series_2022_Towards_Bayesian_Model_based_Demography.pdf"] = chicago_book(
    ["Jakub Bijak"],
    2022, "Towards Bayesian Model-Based Demography: Agency, Complexity and Uncertainty in Migration Studies",
    "Cham", "Springer", None
)

refs["Silverstein_2024_A_Guide_For_Social_Science_Journal_Editors.pdf"] = chicago_article(
    ["Priya Silverstein", "et al."],
    2024, "A Guide for Social Science Journal Editors on Easing into Open Science",
    "Research Integrity and Peer Review", "9", None, "2", "10.1186/s41073-023-00141-5"
)

refs["Society_XXXX_Are_Concerns_Related_To_Artificial_Intelligence_Development.pdf"] = chicago_article(
    None, 2023, "Are Concerns Related to Artificial Intelligence Development and Use Really Necessary? A Philosophical Discussion",
    "Digital Society", "2", None, "40", "10.1007/s44206-023-00070-2",
    flag="author not identified from PDF"
)

refs["Sociologist_2023_The_American_Sociologist_2023_54193210.pdf"] = chicago_article(
    None, 2023, "Preregistration and Registered Reports in Sociology",
    "The American Sociologist", "54", None, "193-210", "10.1007/s12108-023-09563-6",
    flag="authors not identified from PDF"
)

refs["Started_XXXX_An_Exploratory_Survey_About_Using_Chatgpt_In.pdf"] = chicago_article(
    None, None, "An Exploratory Survey about Using ChatGPT in Education, Healthcare, and Research",
    "PLOS ONE", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Started_XXXX_Creating_A_Diagnostic_Assessment_Model_For_Autism.pdf"] = chicago_article(
    None, 2024, "Creating a Diagnostic Assessment Model for Autism Using Generative AI",
    "PLOS ONE", None, None, None, "10.1371/journal.pone.0311209",
    flag="authors not identified from PDF"
)

refs["Started_XXXX_Higher_Education_Students_Perceptions_Of_Chatgpt_A.pdf"] = chicago_article(
    None, None, "Higher Education Students' Perceptions of ChatGPT",
    "PLOS ONE", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Started_XXXX_Prevalence_Of_Questionable_Research_Practices_Research_Misco.pdf"] = chicago_article(
    None, None, "Prevalence of Questionable Research Practices, Research Misconduct, and Their Potential Explanatory Factors",
    "PLOS ONE", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Started_XXXX_The_Use_And_Acceptability_Of_Preprints_In.pdf"] = chicago_article(
    None, None, "The Use and Acceptability of Preprints in Different Scientific Communities",
    "PLOS ONE", None, None, None, None,
    flag="metadata not extractable from PDF"
)

refs["Sweeten_2020_Standard_Errors_In_Quantitative_Criminology_Taking_Stock.pdf"] = chicago_article(
    ["Gary Sweeten"],
    2020, "Standard Errors in Quantitative Criminology: Taking Stock and Looking Forward",
    "Journal of Quantitative Criminology", "36", None, "263-272", "10.1007/s10940-020-09463-9"
)

refs["Team_2024_Ethical_Implications_And_Principles_Of_Using_Artificial.pdf"] = chicago_article(
    None, 2024, "Ethical Implications and Principles of Using Artificial Intelligence",
    "International Journal of Interactive Multimedia and Artificial Intelligence", "8", "5", None, "10.9781/ijimai.2024.02.010",
    flag="authors not identified from PDF"
)

refs["Theory_2024_Managing_The_Terror_Of_Publication_Bias_A.pdf"] = chicago_preprint(
    ["Lihan Chen", "Rachele Benjamin", "Yingchi Guo", "Addison Lai", "Steven J. Heine"],
    2023, "Managing the Terror of Publication Bias: A Comprehensive P-Curve Analysis of the Terror Management Theory Literature",
    "Research Square", "10.21203/rs.3.rs-1254756/v1"
)

refs["Thurzo_2025_Revisiting_The_Role_Of_Review_Articles_In.pdf"] = chicago_article(
    ["Andrej Thurzo", "Ivan Varga"],
    2025, "Revisiting the Role of Review Articles in the Age of AI-Agents: Integrating AI-Reasoning and AI-Synthesis Reshaping the Future of Scientific Publishing",
    "Bratislava Medical Journal", "126", None, "381-393", "10.1007/s44411-025-00106-8"
)

refs["Trials_etal_2023_Preregistration_And_Credibility_Of_Clinical_Trials.pdf"] = chicago_preprint(
    ["Christian Decker", "Marco Ottaviani"],
    2023, "Preregistration and Credibility of Clinical Trials",
    "medRxiv", "10.1101/2023.05.22.23290326"
)

refs["Turing_2023_Mathematician_Alan_Turing.pdf"] = chicago_article(
    None, 2023, "What Was the Turing Test Actually About?",
    "Nature", None, None, None, "10.1038/d41586-023-04056-5",
    flag="author not identified from PDF"
)

refs["USER_2024_Edelweiss_Applied_Science_And_Technology.pdf"] = chicago_article(
    ["Malik Sallam", "Kholoud Al-Mahzoum", "Omar Marzoaq", "Mohammad Alfadhel"],
    2024, "Evident Gap between Generative Artificial Intelligence as an Academic Editor Compared to Human Editors in Scientific Publishing",
    "Edelweiss Applied Science and Technology", "8", "6", "960-979", "10.55214/25768484.v8i6.2189"
)

refs["Unknown_2020_Background_The_Coronavirus_Disease_2019_Covid_19_Pandemic.pdf"] = chicago_article(
    None, 2020, "Survey on Researchers' Attitudes toward Preprints during COVID-19",
    "Journal of Korean Medical Science", None, None, None, None,
    flag="authors/DOI/volume not identified from PDF"
)

refs["Unknown_2021_Meta_psychology_2021_Vol_5_Mp20202625.pdf"] = chicago_article(
    None, 2021, "Tutorial on Meta-Psychology Open Science Practices",
    "Meta-Psychology", "5", None, None, "10.15626/MP.2020.2625",
    flag="authors not identified from PDF"
)

refs["Unknown_2024_Microsoft_Word_Jkm_preprint_paulavazquez.pdf"] = chicago_preprint(
    None, 2024, "The Role of Product Innovation and Customer Centricity in Transforming Tacit and Explicit Knowledge into Profitability",
    "Preprint", None,
    flag="authors/DOI not identified from PDF"
)

refs["Unknown_2024_Undertaking_Peer_Review_For_Academic_Journals_The.pdf"] = chicago_article(
    None, 2024, "Undertaking Peer Review for Academic Journals: The Implications for Critical Care Nursing",
    "Critical Care Nurse", None, None, None, None,
    flag="authors/DOI/volume not identified from PDF"
)

refs["Woods_2024_Incentivising_Research_Data_Sharing_A_Scoping_Review.pdf"] = chicago_article(
    ["Helen Buckley Woods", "Stephen Pinfield"],
    2022, "Incentivising Research Data Sharing: A Scoping Review",
    "Wellcome Open Research", "6", None, "355", "10.12688/wellcomeopenres.17286.2"
)

refs["Workflow_etal_XXXX_Ecaw_manuscriptalspac_230428.pdf"] = chicago_preprint(
    ["Robert T. Thibault", "Marton Kovacs", "Tom E. Hardwicke", "Alexandra Sarafoglou", "John P. A. Ioannidis", "Marcus R. Munafoo"],
    2023, "Reducing Bias in Secondary Data Analysis via an Explore and Confirm Analysis Workflow (ECAW): A Proposal and Survey of Observational Researchers",
    "OSF Preprints", "10.31222/osf.io/md2xz"
)

refs["Writing_etal_2026_Jle_Vol_11_No_4_2025.pdf"] = chicago_article(
    ["Lilia Raitskaya", "Elena Tikhonova"],
    2025, "The 2025 Landscape of Generative AI in Scholarly Writing and Publishing: A Scoping Review of Uses and Ethical Approaches",
    "Journal of Language and Education", "11", "4", None, "10.17323/jle.2025.29876",
    flag="pages need verification"
)

refs["Xu_etal_2026_Scaling_Reproducibility_AI_Assisted_Workflow.pdf"] = chicago_preprint(
    ["Yiqing Xu", "Leo Yang Yang"],
    2026, "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Replication and Reanalysis",
    "Preprint (working paper)", None
)

refs["al_2023_Using_Chatgpt_In_Academic_Writing_Is_Not.pdf"] = chicago_article(
    ["Adeeb M. Jarrah", "Yousef Wardat"],
    2023, "Using ChatGPT in Academic Writing Is (Not) a Form of Plagiarism: What Does the Literature Say?",
    "Online Journal of Communication and Media Technologies", "13", "4", "e202346", None,
    flag="DOI not extracted from PDF"
)

refs["al_2024_Vis_Repligogy.pdf"] = chicago_preprint(
    ["Uzma Haque Syeda", "Laura South", "Justin Raynor", "Liudas Panavas", "David Saffo", "Thomas Morriss", "Cody Dunne", "Michelle A. Borkin"],
    2024, "Vis Repligogy: Towards a Culture of Facilitating Replication Studies in Visualization Pedagogy and Research",
    "OSF Preprints", "10.31219/osf.io/h2qfn"
)

refs["daVeiga_2025_Ethical_Guidelines_Generative_AI_Scholarly_Publishing.pdf"] = chicago_article(
    ["Adele da Veiga"],
    2025, "Ethical Guidelines for Generative AI in Scholarly Publishing",
    "Science Editing", None, None, None, None,
    flag="volume/DOI not fully identified from PDF"
)

refs["growi_2020_Microsoft_Word_Msl_2020_65.pdf"] = chicago_article(
    ["Abdullah F. AlMulhim"],
    2020, "The Effect of Tacit Knowledge and Organizational Learning on Financial Performance in Service Industry",
    "Management Science Letters", "10", None, "2211-2220", "10.5267/j.msl.2020.3.015"
)

refs["intilib_2025_Joit2024_38.pdf"] = chicago_article(
    None, 2024, "AI in Research: Applications and Challenges",
    "Journal of Innovation and Technology", "2024", "38", None, "10.61453/joit.v2024no38",
    flag="authors not identified from PDF"
)

refs["zeynep_2022_E_mail_Lalebasaririeuedutr.pdf"] = chicago_article(
    ["Lale Basarir"],
    2022, "Modelling AI in Architectural Education",
    "Gazi University Journal of Science", "35", "4", "1260-1278", "10.35378/gujs.967981"
)

refs["abc_2024_International_Journal_Of_Research_In_Medical_Sciences.pdf"] = chicago_article(
    ["Anil Sharma", "Praveen Rao", "Mohammad Zubair Ahmed", "Krishnakant Chaturvedi"],
    2025, "Artificial Intelligence in Scientific Writing: Opportunities and Ethical Considerations",
    "International Journal of Research in Medical Sciences", "13", "1", "532-542", "10.18203/2320-6012.ijrms20244167"
)

# Check coverage
all_files = set()
upload_dirs_list = [
    f"{BASE}/literature/notebooklm/upload_theme_a",
    f"{BASE}/literature/notebooklm/upload_theme_b",
    f"{BASE}/literature/notebooklm/upload_theme_c",
]
for d in upload_dirs_list:
    for f in os.listdir(d):
        if f.endswith(".pdf"):
            all_files.add(f)

missing = [f for f in all_files if f not in refs]
print(f"Total unique PDFs: {len(all_files)}")
print(f"Coverage: {len(refs)}")
print(f"Missing: {len(missing)}")
for f in missing:
    print(f"  {f}")

# Sort refs alphabetically by the formatted string (which starts with author surname)
def sort_key(text):
    # Remove markdown formatting for sort
    clean = text.replace("*", "").replace('"', "")
    # Handle [No author] case
    if clean.startswith("[No author]"):
        return "zzz" + clean
    return clean.lower()

sorted_refs = sorted(refs.values(), key=sort_key)

# Write output
output_path = f"{BASE}/literature/chicago_references.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Chicago 17th Edition Reference List\n\n")
    f.write("Generated from upload_theme_a, upload_theme_b, and upload_theme_c folders.\n")
    f.write("Date: 2026-05-07.\n\n")
    f.write("Notes:\n")
    f.write("- Entries marked [*flag*] have incomplete metadata that requires manual verification.\n")
    f.write("- Authors/metadata extracted from PDF first two pages and OpenAlex CSV where available.\n")
    f.write("- Preprints are formatted with 'Preprint. [server].' notation.\n")
    f.write("- Journal names in italics (markdown *name*).\n\n")
    f.write("---\n\n")
    for ref in sorted_refs:
        f.write(ref + "\n\n")

print(f"\nWrote {len(sorted_refs)} references to {output_path}")
