# **Strategisk integrering av Claude Code i samfunnsvitenskapelige forskningsprosesser: En teknisk og metodologisk rammeplan for profesjonell analyse**

Samfunnsvitenskapelig forskning befinner seg i en brytningstid der overgangen fra tradisjonelle, statiske analysemetoder til agentiske, AI-støttede arbeidsflyter krever en fundamental reevaluering av teknisk infrastruktur. Claude Code representerer i denne sammenhengen ikke bare et programmeringsverktøy, men et supervised agentisk miljø som kan navigere i komplekse datasett, utføre systematiske analyser og opprettholde en vitenskapelig integritet som overgår konvensjonelle chatbot-grensesnitt.1 For den profesjonelle forskeren er overgangen til Claude Code et skifte fra å bruke AI som et oppslagsverk til å bruke det som en metodologisk samarbeidspartner som kan operere autonomt innenfor gitte parametere.3

Denne rapporten redegjør for hvordan man best konfigurerer dette miljøet for å møte de strenge kravene til reproduserbarhet, datasikkerhet og analytisk presisjon som kjennetegner moderne samfunnsforskning. Ved å integrere IT-inspirerte strukturer som uforanderlige datamapper, arkitektoniske beslutningslogger og streng token-styring, kan forskningsprosjekter skaleres og valideres med en grad av gjennomsiktighet som tidligere var forbeholdt storskala programvareutvikling.5

## **Teknisk fundament og installasjonsmiljø for forskningsbruk**

Valget av operativt miljø er det første kritiske skrittet i å etablere en profesjonell forskningsstabel. Claude Code er designet for å kjøre på tvers av plattformer, men for samfunnsvitenskapelig analyse, som ofte involverer komplekse avhengigheter i språk som R eller Python, anbefales miljøer som støtter sandkassekjøring og robust pakkehåndtering.7

### **Plattformer og systemkrav**

For forskere som opererer på Windows, er valget mellom native installasjoner og Windows Subsystem for Linux (WSL 2\) av avgjørende betydning for sikkerhet og verktøytilgang. WSL 2 er den foretrukne løsningen i forskningsmiljøer fordi den støtter sandkassekjøring av kommandoer, noe som er essensielt når man kjører autonome agenter som har tillatelse til å utføre shell-kommandoer.7

| Komponent | Krav / Anbefaling | Forskningsmessig relevans |
| :---- | :---- | :---- |
| Operativsystem | macOS 13+, Ubuntu 20.04+, eller Windows (WSL 2\) | Stabilitet i kjøremiljøet og tilgang til Linux-verktøy. |
| Maskinvare | Minimum 4 GB RAM, x64 eller ARM64 prosessor | Håndtering av store datasett og flere agent-tråder. |
| Shell | Bash eller Zsh anbefales | Kompatibilitet med standardiserte forskningsskript. |
| Node.js | Versjon 18+ kreves | Grunnlaget for CLI og plugin-arkitektur. |

Installasjonsprosessen bør utføres uten bruk av sudo for å unngå rettighetsproblematikk som kan kompromittere sikkerheten i forskningsmiljøet.7 For macOS og Linux utføres installasjonen via en dedikert shell-kommando, mens Windows-brukere oppfordres til å benytte PowerShell eller WSL for å sikre korrekt sti-konfigurering. Det er verdt å merke seg at Claude Code støtter ulike utgivelseskanaler; for profesjonelle prosjekter anbefales kanalen "stable" for å unngå potensielle regresjoner i nye funksjoner som kan påvirke reproduserbarheten av pågående analyser.7

### **Verifisering av integritet**

I en profesjonell sammenheng er det kritisk å verifisere at binærfilene ikke er manipulert. Claude Code publiserer signaturnøkler som kan brukes til å validere installasjonen via GPG.7 Dette sikrer at forskningsdataene ikke blir behandlet av uautoriserte versjoner av verktøyet, noe som er et grunnleggende krav i institusjonelle IT-sikkerhetsvurderinger.

## **IT-inspirert mappestruktur for reproduserbar forskning**

En av de største utfordringene i samfunnsvitenskapelig analyse er "organisatorisk entropi", der data, skript og resultater blandes i en uoversiktlig struktur. For å maksimere Claude Codes evne til å forstå prosjektet, bør man implementere en logisk, standardisert mappestruktur inspirert av "Cookiecutter Data Science" (CCDS).8 En slik struktur fungerer som et kart for AI-agenten, slik at den automatisk vet hvor den skal lete etter rådata, hvor den skal lagre interimresultater, og hvor dokumentasjonen befinner seg.2

### **Den hierarkiske datamodellen**

Kjernen i en reproduserbar struktur er skillet mellom ulike datatilstander. Rådata må betraktes som uforanderlige (immutable), noe som betyr at de aldri redigeres manuelt eller overskrives av skript.11 All transformasjon må skje via kode som lagres separat, slik at man alltid kan gjenskape prosesserte data fra kilden.11

| Mappe | Innhold | Regel for Claude Code |
| :---- | :---- | :---- |
| data/raw/ | Originale spørreundersøkelser, registerdata, transkripter. | Skrivebeskyttet. Kun lesetilgang via Read. |
| data/interim/ | Mellomliggende filer (f.eks. etter vasking eller anonymisering). | Midlertidig lagring for sekvensielle prosesser. |
| data/processed/ | Endelige datasett klare for statistisk analyse. | Grunnlag for visualisering og rapportering. |
| data/external/ | Tredjepartsdata fra SSB, Eurostat eller andre kilder. | Referansemateriale for komparative studier. |
| src/ | Python/R-kode for vasking, modellering og analyse. | Primært arbeidsområde for kodegenerering. |
| notebooks/ | Jupyter-notatbøker for eksplorativ analyse. | Brukes til stegvis validering av hypoteser. |
| reports/ | Manuskripter, tabeller og figurer. | Sluttstasjon for analytiske output. |
| docs/adr/ | Beslutningslogger (Architecture Decision Records). | Loggføring av metodologiske veivalg. |

Ved å bruke numeriske prefikser for skript i src/-mappen (f.eks. 01\_clean\_data.py, 02\_run\_regression.py), kan man instruere Claude til å utføre analysen i en logisk rekkefølge.11 Dette gjør det mulig for andre forskere å reprodusere hele prosessen ved å kjøre skriptene sekvensielt, noe som er gullstandarden i åpen vitenskap.15

### **Navnekonvensjoner og maskinlesbarhet**

For at Claude Code skal operere mest mulig effektivt, må filnavn være konsistente og maskinlesbare. Bruk av mellomrom og spesialtegn i filnavn bør unngås til fordel for bindestreker eller understreker.14 Datoer bør følge ISO 8601-standarden (ÅÅÅÅ-MM-DD) for å sikre korrekt sortering, spesielt i prosjekter med longitudinelle data eller hyppige loggoppdateringer.11

## **Konfigurasjon og "Project Constitution" via CLAUDE.md**

I motsetning til generelle samtaleverktøy, leser Claude Code en spesifikk fil kalt CLAUDE.md ved starten av hver økt. Denne filen fungerer som prosjektets konstitusjon og definerer de tekniske og metodologiske reglene som agenten må følge.3 I en forskningssammenheng er dette stedet hvor man definerer kodestandarder for statistiske analyser, foretrukne biblioteker og prosedyrer for datahåndtering.16

### **Innhold i en profesjonell CLAUDE.md**

En godt utformet CLAUDE.md bør ikke inneholde informasjon som agenten selv kan utlede fra koden, men heller fokusere på de unike arkitektoniske og metodologiske beslutningene for prosjektet.3

For samfunnsvitenskapelige prosjekter bør følgende inkluderes:

* **Analyseparadigme**: Spesifiser om det brukes Bayesian eller frekventistisk statistikk, og hvilke terskler for signifikans som gjelder.  
* **Kodestil**: For R-brukere kan man kreve bruk av tidyverse-stilen fremfor base R for bedre lesbarhet. For Python-brukere kan man kreve type-hinting i alle analysefunksjoner.3  
* **Verifiseringsmetoder**: Definer hvordan Claude skal sjekke sine egne resultater, for eksempel ved å kjøre spesifikke enhetstester på vaskeskript eller validere summen av frekvenstabeller.3  
* **Repository Etikette**: Navngivningsregler for Git-grener og maler for commit-meldinger.3

Ved å bruke progressive disclosure-prinsipper kan CLAUDE.md peke til dypere dokumentasjon i docs/-mappen, for eksempel code\_conventions.md eller data\_anonymization\_protocol.md. Dette forhindrer at kontekstvinduet fylles med irrelevant informasjon i den innledende fasen av en økt.16

### **Hierarkiske innstillinger i settings.json**

Claude Code opererer med tre nivåer av konfigurasjon som gir forskeren finmasket kontroll over verktøyets oppførsel.18

1. **Globale innstillinger** (\~/.claude/settings.json): Gjelder for alle forskerens prosjekter, for eksempel API-nøkler og universelle sikkerhetspreferanser.  
2. **Prosjektinnstillinger** (.claude/settings.json): Lagres i prosjektmappen og sjekkes inn i Git, slik at hele forskerteamet deler de samme konfigurasjonene for verktøybruk og tillatelser.  
3. **Lokale overstyringer** (.claude/settings.local.json): Personlige preferanser som ikke deles med teamet, for eksempel stier til lokale datasett som ikke skal inkluderes i versjonskontroll.18

## **Spesialiserte ferdigheter (Skills) for samfunnsforskning**

En av de mest kraftfulle funksjonene i Claude Code er muligheten til å utvide dens kapabiliteter gjennom tilpassede ferdigheter, lagret som SKILL.md-filer.4 En ferdighet er i praksis en spesialisert lekebok som instruerer Claude i hvordan en bestemt klasse av oppgaver skal utføres.4 For samfunnsforskere betyr dette at man kan "trene" Claude i spesifikke metodiske tilnærminger, som tematisk koding eller bibliometrisk analyse.

### **Kvalitativ analyse og tematisk koding**

For kvalitative forskere kan man utvikle en ferdighet som fungerer som en PhD-nivå ekspert på fortolkende rammeverk.21 Denne ferdigheten kan inkludere instruksjoner for:

* **Åpen, aksial og selektiv koding**: Systematisk kategorisering av intervjutranskripter med referanser til kildetekst.21  
* **Refleksivitetsrevisjon**: Be Claude vurdere potensielle skjevheter i analysen basert på prosjektets målsettinger.21  
* **Datasaturasjon**: Evaluere om nye data tilfører nye koder eller om man har nådd et teoretisk metningspunkt.21

En ferdighet trigges enten automatisk når Claude detekterer en relevant oppgave (f.eks. "analyser disse intervjuene"), eller manuelt via en slash-kommando som /qualitative-coding.19 Dette sikrer en konsistent metodologisk utførelse på tvers av store mengder tekstmateriale, noe som er spesielt nyttig i prosjekter som involverer hundrevis av dokumenter.24

### **Kvantitativ metodikk og validering**

For kvantitative studier kan man opprette en ferdighet for "Computational Text Analysis" som veileder forskeren gjennom fem faser fra design til publikasjon.25 Denne ferdigheten kan støtte både R (for strukturelle emnemodeller) og Python (for transformator-baserte modeller som BERT), og inkluderer ferdigdefinerte valideringsstrategier for å sikre at modellene ikke bare produserer tall, men sosiologisk mening.25

| Ferdighet | Formål | Relevans for forskning |
| :---- | :---- | :---- |
| citation-verification | Sjekker.bib-filer mot CrossRef/OpenAlex. | Stopper hallusinerte referanser i manuskriptet.26 |
| data-anonymizer | Identifiserer og maskerer PII i råtekst. | Sikrer GDPR-etterlevelse før analyse.27 |
| statistical-audit | Gjennomgår R/Python-kode for metodiske feil. | Oppdager p-hacking eller feilaktig håndtering av manglende data.23 |
| literature-summarizer | Syntetiserer innsikt fra PDF-samlinger. | Effektiviserer litteraturgjennomgangen via Zotero.29 |

Disse ferdighetene lagres i .claude/skills/\[navn\]/SKILL.md og kan inneholde både instruksjoner og referansemateriale som Claude skal bruke som fasit.19

## **Plugins og integrasjon med det vitenskapelige økosystemet**

Claude Code fungerer som en hub som kan kobles til andre verktøy via Model Context Protocol (MCP). For samfunnsforskere er integrasjonen med referansehåndteringsverktøyet Zotero den kanskje viktigste utvidelsen.1

### **Zotero-integrasjon via MCP**

Gjennom spesialiserte MCP-servere som zotero-mcp eller zotero-fulltext, får Claude direkte tilgang til forskerens personlige bibliotek.31 Dette muliggjør en arbeidsflyt der forskeren kan stille spørsmål til sine egne kilder uten å måtte laste opp PDF-er manuelt til en web-tjeneste.31

Funksjonaliteten inkluderer:

* **Semantisk søk**: Finne artikler basert på mening og konseptuelle sammenhenger ved bruk av lokale embedding-modeller som all-MiniLM-L6-v2.31  
* **Fulltekst-interaksjon**: Claude kan lese indekserte PDF-er, hente ut spesifikke passasjer og verifisere påstander mot primærkilder.30  
* **Metadata-håndtering**: Oppdatere tags, legge til notater og eksportere korrekte BibTeX-filer direkte fra terminalen.34

For forskere som foretrekker en grafisk tilnærming, finnes det også plugins som llm-for-zotero som integrerer AI-sidebarer direkte i Zotero-leseren, men for dyp analyse og automatisert rapportering er CLI-integrasjonen via MCP overlegen på grunn av muligheten for script-basert batch-prosessering.33

### **Andre relevante utvidelser**

Utover referansehåndtering kan Claude Code kobles til verktøy for web-søk (f.eks. Google Search via MCP) for å finne grå litteratur eller de nyeste statistikkene som ennå ikke er publisert i akademiske databaser.4 Det finnes også spesialiserte plugins for visualisering, som lar Claude generere komplekse arkitekturdiagrammer eller flytskjemaer som dokumenterer forskningsprosessen.26

## **Sikkerhet for personopplysninger (GDPR) i AI-støttet forskning**

Behandling av personopplysninger i skybaserte AI-systemer krever en proaktiv tilnærming til sikkerhet. For samfunnsforskere som opererer under GDPR, er det ikke tilstrekkelig å stole på leverandørens personvernerklæring; man må implementere tekniske barrierer som hindrer utilsiktet lekkasje av sensitive data.36

### **Den lokale redaksjonsbarrieren**

En av de mest effektive metodene for å sikre personopplysninger er å bruke "Hooks" i Claude Code for å etablere en lokal redaksjonsbarriere.38 En PreToolUse-hook kan konfigureres til å kjøre et lokalt skript (f.eks. i Python) som skanner all tekst for sensitive mønstre før den sendes til skyen.38

| Metode | Mekanisme | Fordel for GDPR |
| :---- | :---- | :---- |
| **Maskering (Redaction)** | Erstatter navn og e-poster med tagger som \<PERSON\_1\>. | Dataminimering; modellen ser kun anonymisert kontekst.27 |
| **Blokkering (Blocking)** | Stopper kommandoer som forsøker å lese filer i data/raw. | Hindrer rådata fra å forlate den lokale maskinen.39 |
| **Syntetisk erstatning** | Erstatter ekte identifikatorer med troverdige, men falske data. | Bevarer datastrukturen for debugging uten risiko.41 |

Verktøy som ScrubDuck eller lokale PII-filtere kan integreres som hooks for å automatisk oppdage og fjerne over 150 typer personopplysninger på tvers av flere land.28 Dette sikrer at forskeren overholder prinsippet om "innebygd personvern" (Privacy by Design).36

### **Samtykke, sletting og datasuverenitet**

GDPR krever at enkeltpersoner har rett til innsyn og sletting.36 I et AI-støttet forskningsprosjekt betyr dette at man må ha kontroll over hvor deltakerdataene befinner seg. Ved å bruke lokale Zotero-databaser og unngå lagring av sensitive data i Claude Codes historikk (f.eks. ved hyppig bruk av /clear), reduserer man risikoen for at personopplysninger blir liggende i systemlogger.3 Det er også viktig å merke seg at Claude Code støtter "Zero Data Retention" (ZDR) for visse funksjoner, noe som betyr at dataene slettes fra leverandørens servere umiddelbart etter at responsen er generert.45

## **Logging av beslutninger og vitenskapelig audit-trail**

I profesjonell forskning er beslutningsprosessen like viktig som sluttresultatet. For å sikre vitenskapelig etterrettelighet må hver endring i analysemodeller eller databehandlingsrutiner dokumenteres grundig. Dette løses best ved å kombinere Git for versjonskontroll av kode med Architecture Decision Records (ADR) for metodiske veivalg.5

### **Git-arbeidsflyt for forskere**

Claude Code er en "supervised agent", noe som betyr at den kan foreslå commits og skrive detaljerte commit-meldinger som forklarer logikken bak en endring.1 For forskningsprosjekter anbefales en arbeidsflyt der:

1. **Forskningstråder separeres**: Bruk av grener (branches) for ulike eksperimenter eller analyser.1  
2. **Beskrivende commits**: I stedet for "fixed bug", instrueres Claude til å skrive meldinger som "Oppdatert regresjonsmodell for å inkludere kontroll for sosioøkonomisk status".1  
3. **Pull Requests som fagfellevurdering**: Ved samarbeid i team kan Claude åpne pull requests der andre forskere kan gå gjennom koden og argumentasjonen før den merges inn i hovedprosjektet.1

Dette skaper en uforanderlig historie over prosjektet, der man kan gå tilbake til nøyaktig den versjonen av koden som produserte resultatene i en bestemt publikasjon.15

### **Implementering av ADR i forskningskontekst**

En ADR er et kort dokument som beskriver en viktig beslutning, konteksten den ble tatt i, og dens konsekvenser.5 I samfunnsforskning kan dette handle om valg av vekting i en spørreundersøkelse, ekskludering av outliers, eller endring av kodingstemaer midt i et prosjekt.6

En typisk ADR bør følge en "omvendt pyramide"-stil, der den viktigste beslutningen kommer først, etterfulgt av argumentasjon og tekniske detaljer.5

| Status i ADR | Betydning | Handling |
| :---- | :---- | :---- |
| **Proposed** | Under diskusjon i forskerteamet. | Muliggjør refleksjon før implementering. |
| **Accepted** | Beslutningen er aktiv og styrende for analysen. | Dokumenterer det gjeldende metodiske valget. |
| **Superseded** | Beslutningen er erstattet av en ny (f.eks. nyere statistisk metode). | Bevarer historikken uten å skape forvirring.5 |
| **Rejected** | En foreslått retning ble forkastet. | Hindrer at teamet kaster bort tid på å diskutere det samme valget på nytt.6 |

Ved å lagre ADR-er som Markdown-filer i docs/adr/ sørger man for at de er lett tilgjengelige, maskinlesbare og versjonskontrollerte sammen med resten av prosjektet.5

## **Kostnadskontroll og effektiv token-styring**

Bruk av avanserte AI-modeller medfører løpende kostnader. For forskningsprosjekter med begrensede midler er det avgjørende å ha en strategi for token-økonomi som balanserer analytisk kvalitet mot økonomisk bærekraft.49

### **Styring av budsjett via CLI**

Claude Code tilbyr spesifikke flagg som gir forskeren direkte kontroll over pengebruken. Ved å kjøre Claude i "print mode" (-p) med budsjettgrenser, kan man automatisere store analyseoppgaver uten risiko for uforutsette utgifter.49

* **\--max-budget-usd**: Setter en hard grense for hvor mye Claude kan bruke på API-kall i en gitt økt.49  
* **\--max-turns**: Begrenser hvor mange runder agenten kan bruke på å løse en oppgave, noe som hindrer den i å gå inn i endeløse løkker ved komplekse feil.49  
* **\--effort**: Lar forskeren velge mellom "low", "medium" og "high" innsats. For rutinemessig formatering kan man bruke lav innsats, mens man sparer høy innsats til de mest kritiske analytiske fasene.49

### **Kontekststyring og cashing**

Hver gang Claude leser et prosjekt, brukes tokens. For å redusere dette forbruket bør man aktivt bruke /clear for å tømme kontekstvinduet når man starter på en ny, urelatert oppgave.3 Claude støtter også prompt-cashing, noe som betyr at hvis man sender de samme store dokumentene (f.eks. et helt bokmanuskript eller et omfattende datasett) gjentatte ganger, reduseres kostnadene for de påfølgende kallene betraktelig.45

For forskere som jobber med PDF-filer, er cashing spesielt effektivt når det kombineres med Claude sitt innebygde siteringssystem, som tillater nøyaktige referanser til sidetall uten at sitert tekst teller mot output-tokens.45

## **Syntese: En robust rammeplan for digital forskningspraksis**

Etableringen av et profesjonelt forskningsmiljø med Claude Code krever en bevisst integrasjon av tekniske verktøy og vitenskapelige prinsipper. Ved å følge denne rammeplanen sikrer man at AI-en fungerer som en forlengelse av forskerens intellekt, snarere enn en uforutsigbar erstatning.

Kjernen i denne praksisen er reproduserbarhet gjennom struktur. Ved å låne prinsipper fra IT-verdenen, som uforanderlige rådata og streng versjonskontroll, skapes et miljø der hver eneste analytiske slutning kan spores tilbake til sitt utgangspunkt. Bruken av spesialiserte ferdigheter (skills) og MCP-utvidelser som Zotero transformerer Claude fra en generell koder til en dyp domeneekspert som kan operere med en presisjon som tidligere krevde store team av forskningsassistenter.

Samtidig må sikkerhet og etikk stå i sentrum. Gjennom implementering av lokale hooks for PII-redaksjon og bevisst bruk av ADR-er for beslutningslogging, møter man både de juridiske kravene i GDPR og de akademiske kravene til transparens og integritet. Den økonomiske styringen gjennom token-kontroll sikrer at disse avanserte metodene forblir tilgjengelige for forskningsmiljøer med varierte budsjettrammer.

Fremtidens samfunnsforskning vil i økende grad bli utført i terminalen, der koding og analyse smelter sammen. Ved å bygge prosjektet på dette fundamentet, legger man grunnlaget for en forskningspraksis som er raskere, mer omfattende og mer etterrettelig enn noen gang før.

#### **Referanser**

1. Claude Code overview \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview)  
2. The Complete Claude Code CLI Guide \- Live & Auto-Updated Every 2 Days \- GitHub, brukt april 14, 2026, [https://github.com/Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide)  
3. Best Practices for Claude Code \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)  
4. 10 Must-Have Skills for Claude (and Any Coding Agent) in 2026 | by unicodeveloper | Mar, 2026, brukt april 14, 2026, [https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051)  
5. Architecture Decision Record \- Martin Fowler, brukt april 14, 2026, [https://martinfowler.com/bliki/ArchitectureDecisionRecord.html](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)  
6. ADR process \- AWS Prescriptive Guidance, brukt april 14, 2026, [https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)  
7. Advanced setup \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup)  
8. How to Spin Up a Project Structure with Cookiecutter | Towards Data Science, brukt april 14, 2026, [https://towardsdatascience.com/how-to-spin-up-a-project-structure-with-cookiecutter/](https://towardsdatascience.com/how-to-spin-up-a-project-structure-with-cookiecutter/)  
9. What Is Cookiecutter Data Science?, brukt april 14, 2026, [https://www.institutedata.com/us/blog/what-is-cookiecutter-data-science/](https://www.institutedata.com/us/blog/what-is-cookiecutter-data-science/)  
10. Using the template \- Cookiecutter Data Science, brukt april 14, 2026, [https://cookiecutter-data-science.drivendata.org/using-the-template/](https://cookiecutter-data-science.drivendata.org/using-the-template/)  
11. How to Organize Research Data: Folder Structure & Naming Conventions \- Plotivy, brukt april 14, 2026, [https://plotivy.app/blog/research-data-organization-guide](https://plotivy.app/blog/research-data-organization-guide)  
12. 2.2 Structuring a project | A Guide to Reproducible Research \- Bookdown, brukt april 14, 2026, [https://bookdown.org/arnold\_c/repro-research/2-2-structuring-a-project.html](https://bookdown.org/arnold_c/repro-research/2-2-structuring-a-project.html)  
13. Structuring Your Data Science Project: A Guide to the Cookiecutter Template | by Utsav Raj, brukt april 14, 2026, [https://medium.com/@utsavraj.ptn04/structuring-your-data-science-project-a-guide-to-the-cookiecutter-template-c55a0eeac10e](https://medium.com/@utsavraj.ptn04/structuring-your-data-science-project-a-guide-to-the-cookiecutter-template-c55a0eeac10e)  
14. How To Organize Your Project: Best Practices for Open Reproducible Science, brukt april 14, 2026, [https://earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/get-started-open-reproducible-science/best-practices-for-organizing-open-reproducible-science/](https://earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/get-started-open-reproducible-science/best-practices-for-organizing-open-reproducible-science/)  
15. Organizing your projects — Reproducible research documentation, brukt april 14, 2026, [https://coderefinery.github.io/reproducible-research/organizing-projects/](https://coderefinery.github.io/reproducible-research/organizing-projects/)  
16. Writing a good CLAUDE.md | HumanLayer Blog, brukt april 14, 2026, [https://www.humanlayer.dev/blog/writing-a-good-claude-md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)  
17. My Claude Code Setup \- Pedro H. C. Sant'Anna, brukt april 14, 2026, [https://psantanna.com/claude-code-my-workflow/workflow-guide.html](https://psantanna.com/claude-code-my-workflow/workflow-guide.html)  
18. Claude Code settings \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings)  
19. Claude Skills Explained: Use Custom Skills on Claude Code, brukt april 14, 2026, [https://www.analyticsvidhya.com/blog/2026/03/claude-skills-custom-skills-on-claude-code/](https://www.analyticsvidhya.com/blog/2026/03/claude-skills-custom-skills-on-claude-code/)  
20. How to Use Claude Code Skills Like the 1% (it’s easy actually), brukt april 14, 2026, [https://www.youtube.com/watch?v=6-D3fg3JUL4](https://www.youtube.com/watch?v=6-D3fg3JUL4)  
21. Qualitative Research \- Claude Code Skill for Data Analysis \- MCP Market, brukt april 14, 2026, [https://mcpmarket.com/tools/skills/qualitative-research-specialist](https://mcpmarket.com/tools/skills/qualitative-research-specialist)  
22. Using Claude Code for Qualitative Data (Thematic Coding) | by Fatin Asnan \- Medium, brukt april 14, 2026, [https://medium.com/@fatinnazirahasnan/using-claude-code-for-qualitative-data-thematic-coding-0f73f6b2bc37](https://medium.com/@fatinnazirahasnan/using-claude-code-for-qualitative-data-thematic-coding-0f73f6b2bc37)  
23. GitHub \- DrCatHicks/learning-opportunities: A Claude Code skill for deliberate skill development during AI-assisted coding, brukt april 14, 2026, [https://github.com/DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)  
24. Discovering Connections: How Claude Code Analyzed 100 Books \- DEV Community, brukt april 14, 2026, [https://dev.to/dd8888/discovering-connections-how-claude-code-analyzed-100-books-41li](https://dev.to/dd8888/discovering-connections-how-claude-code-analyzed-100-books-41li)  
25. Text Analyst Claude Code Skill | Computational Sociology \- MCP Market, brukt april 14, 2026, [https://mcpmarket.com/tools/skills/computational-text-analyst-1](https://mcpmarket.com/tools/skills/computational-text-analyst-1)  
26. I built a Claude Code skill that catches hallucinated citations ... \- Reddit, brukt april 14, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1s1axkk/i\_built\_a\_claude\_code\_skill\_that\_catches/](https://www.reddit.com/r/ClaudeAI/comments/1s1axkk/i_built_a_claude_code_skill_that_catches/)  
27. What measures ensure LLM compliance with data privacy laws like GDPR? \- Milvus, brukt april 14, 2026, [https://milvus.io/ai-quick-reference/what-measures-ensure-llm-compliance-with-data-privacy-laws-like-gdpr](https://milvus.io/ai-quick-reference/what-measures-ensure-llm-compliance-with-data-privacy-laws-like-gdpr)  
28. I built a CLI tool to strip PII/Secrets from Server Logs and Configs before debugging with AI, brukt april 14, 2026, [https://www.reddit.com/r/devops/comments/1q6oe42/i\_built\_a\_cli\_tool\_to\_strip\_piisecrets\_from/](https://www.reddit.com/r/devops/comments/1q6oe42/i_built_a_cli_tool_to_strip_piisecrets_from/)  
29. Automating Academic Research with AI: A Deep Dive into LLM-Powered Zotero Analysis, brukt april 14, 2026, [https://medium.com/@arto.thurlin/automating-academic-research-with-ai-a-deep-dive-into-llm-powered-zotero-analysis-da50944f9f30](https://medium.com/@arto.thurlin/automating-academic-research-with-ai-a-deep-dive-into-llm-powered-zotero-analysis-da50944f9f30)  
30. Zotero Research Agent | Claude Code Skill for Academic Writing \- MCP Market, brukt april 14, 2026, [https://mcpmarket.com/tools/skills/zotero-research-agent](https://mcpmarket.com/tools/skills/zotero-research-agent)  
31. Zotero MCP: Chat with your Research Library—Local or Web—in Claude, ChatGPT, and more. \- GitHub, brukt april 14, 2026, [https://github.com/54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)  
32. zotero-fulltext | MCP Servers \- LobeHub, brukt april 14, 2026, [https://lobehub.com/mcp/statzhero-zotero-fulltext](https://lobehub.com/mcp/statzhero-zotero-fulltext)  
33. yilewang/llm-for-zotero: A research agent system deeply rooted in your own Zotero library. \- GitHub, brukt april 14, 2026, [https://github.com/yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero)  
34. zotero-cli | Skills Marketplace \- LobeHub, brukt april 14, 2026, [https://lobehub.com/skills/openclaw-skills-zotero-cli](https://lobehub.com/skills/openclaw-skills-zotero-cli)  
35. MCP for Zotero — connect your library to Claude, ChatGPT, and other AI assistants, brukt april 14, 2026, [https://forums.zotero.org/discussion/130133/mcp-for-zotero-connect-your-library-to-claude-chatgpt-and-other-ai-assistants](https://forums.zotero.org/discussion/130133/mcp-for-zotero-connect-your-library-to-claude-chatgpt-and-other-ai-assistants)  
36. What Is GDPR Compliance? \- Palo Alto Networks, brukt april 14, 2026, [https://www.paloaltonetworks.com/cyberpedia/gdpr-compliance](https://www.paloaltonetworks.com/cyberpedia/gdpr-compliance)  
37. GDPR Compliance Best Practices for Handling Personal Data | by SOCLYio \- Medium, brukt april 14, 2026, [https://medium.com/@soclyio12\_74302/gdpr-compliance-best-practices-for-handling-personal-data-6ea0bf856798](https://medium.com/@soclyio12_74302/gdpr-compliance-best-practices-for-handling-personal-data-6ea0bf856798)  
38. Automate workflows with hooks \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)  
39. Claude Code Hooks: Automate Your AI Coding Workflow \- Kyle Redelinghuys, brukt april 14, 2026, [https://www.ksred.com/claude-code-hooks-a-complete-guide-to-automating-your-ai-coding-workflow/](https://www.ksred.com/claude-code-hooks-a-complete-guide-to-automating-your-ai-coding-workflow/)  
40. Redaction hooks for Claude Code \- GitHub Gist, brukt april 14, 2026, [https://gist.github.com/ruvnet/332336ad5e0516daa810d98f8f0ddca9](https://gist.github.com/ruvnet/332336ad5e0516daa810d98f8f0ddca9)  
41. Redact PII Before Sending Data to LLMs: A Developer's Guide \- DEV Community, brukt april 14, 2026, [https://dev.to/raviteja\_nekkalapu\_/redact-pii-before-sending-data-to-llms-a-developers-guide-1j04](https://dev.to/raviteja_nekkalapu_/redact-pii-before-sending-data-to-llms-a-developers-guide-1j04)  
42. How to Prevent PII Leaks in AI Systems: Automated Data Redaction for LLM Prompts, brukt april 14, 2026, [https://www.gravitee.io/blog/how-to-prevent-pii-leaks-in-ai-systems-automated-data-redaction-for-llm-prompt](https://www.gravitee.io/blog/how-to-prevent-pii-leaks-in-ai-systems-automated-data-redaction-for-llm-prompt)  
43. 5 Best Automated Redaction Software for GDPR and FOIA Workflows — SecureRedact, brukt april 14, 2026, [https://www.secureredact.ai/articles/best-automated-redaction-software-for-gdpr-and-foia](https://www.secureredact.ai/articles/best-automated-redaction-software-for-gdpr-and-foia)  
44. A guide to GDPR data privacy requirements \- GDPR.eu, brukt april 14, 2026, [https://gdpr.eu/data-privacy/](https://gdpr.eu/data-privacy/)  
45. Citations \- Claude API Docs, brukt april 14, 2026, [https://platform.claude.com/docs/en/build-with-claude/citations](https://platform.claude.com/docs/en/build-with-claude/citations)  
46. Maintain an architecture decision record (ADR) \- Microsoft Azure Well-Architected Framework, brukt april 14, 2026, [https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)  
47. Architecture decision record (ADR) examples for software planning, IT leadership, and template documentation \- GitHub, brukt april 14, 2026, [https://github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record)  
48. Architecture decision records overview \- Google Cloud Documentation, brukt april 14, 2026, [https://docs.cloud.google.com/architecture/architecture-decision-records](https://docs.cloud.google.com/architecture/architecture-decision-records)  
49. CLI reference \- Claude Code Docs, brukt april 14, 2026, [https://code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference)