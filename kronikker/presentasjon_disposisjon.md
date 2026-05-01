# Presentasjonsdisposisjon: Query Authorship

## «A Framework for Systematic AI Use in Social Science»

**Format:** ~19 slides / inntil 45 min  
**Publikum:** Kvantitativt orienterte kolleger, kritisk innstilte, praktisk behov  
**Struktur:** Problem → Begrep → Praksis → Epistemologi → Politikk

---

## Slide 1 — Tittel

**Query Authorship: A Framework for Systematic AI Use in Social Science**

Torbjørn Skardhamar, UiO  
[Preprint: SocArXiv / dato]

---

## Slide 2 — Utgangspunkt: AI er allerede i bruk

- Spørsmålet er ikke *om* — det er *hvordan*
- Institusjonelt svar: krav om deklarering og forbud
- Men dette identifiserer feil dimensjon
- Tesen: skillet mellom systematisk og usystematisk bruk er det epistemisk relevante akset — ikke bruk vs. ikke-bruk

*Introduksjon av foredragets struktur*

---

## Slide 3 — Problemet: hva usystematisk KI-bruk gjør

**Ikke tilfeldig støy — retningsfeil:**

- Hindawi/Wiley: 8 000+ retraksjoner (2022–23) — AI-verktøy industrialiserte papermills
- Hallusinerte siteringer forurenser det evidensielle grunnlaget
- Ludwig, Mullainathan & Rambachan (2024): valg av modell og prompt-formulering → substantielt forskjellige parameterestimat

**PARKing** (Kosch & Feger 2025): iterativ prompt-justering til ønsket resultat
— analogt med p-hacking, men usynlig fordi prosessen er udokumentert

---

## Slide 4 — Hvorfor KI svikter systematisk (ikke tilfeldig)

- **Sycophancy** (Cheng et al. 2026): bekrefter snarere enn utfordrer — reduserer uavhengig vurdering
- **Generaliseringsbias** (Peters & Chin-Yee 2025): oversetter konklusjoner utover det data støtter
- **Frankfurt-poenget** (Hicks et al. 2024): LLMs optimaliserer for plausibel fortsettelse, ikke for sannhet

> «The liar tracks the truth in order to subvert it; the bullshitter is indifferent to whether what they say is true.»

Usystematisk bruk betyr å akseptere output fra en prosess som ikke i seg selv sporer sannheten.

---

## Slide 5 — Erklæringspolitikk: hvorfor det ikke er nok

- 24 sjekkliste-instrumenter, 10–66 items — ingen konsensus om hva «full disclosure» betyr
- Erklæring er et *post hoc*-instrument: forutsetter at prosessen var god, spør bare om du rapporterte den
- Pervers insentivstruktur: driver KI-bruk under radaren, hjelper ikke ærlige aktører
- Ariely-ironien: det empiriske grunnlaget for at erklæringer endrer atferd — er selv fabrikkert (retraktert 2021)

**Binær politikk behandler systematisk og usystematisk bruk identisk.**  
Det er det sentrale problemet.

---

## Slide 6 — Nøkkeldistinksjonen: systematisk vs. usystematisk

**Systematisk KI-bruk har tre definerende trekk:**

1. **Eksplisitte kriterier** — instruksjoner spesifiserer hva og på hvilket grunnlag  
2. **Menneskelig verifisering** — kontrollpunkt ved hvert trinn der output evalueres mot kriteriene  
3. **Dokumenterte outputs** — prompt-konfigurasjoner, rubrikker, loggfiler bevares som artefakter

Usystematisk bruk er *utenfor* dette spekteret, ikke i den laveste enden:  
fraværet av kriterier og dokumentasjon er kategorisk forskjellig, ikke en svak versjon av systematisk bruk.

---

## Slide 7 — Query authorship: det sentrale begrepet

**Den intellektuelle bidrag ligger i instruksjonene — ikke i teksten KI produserer.**

| Query                    | Hva den koder                                      |
| ------------------------ | -------------------------------------------------- |
| Søkestrengen             | En teori om hva relevant litteratur er             |
| Inkluskjonsrubrikken     | Scopeforpliktelser for artikkelen                  |
| Analysespecifikasjonen   | Teori om måling og kausal struktur                 |
| Reviewer-konfigurasjonen | Evalueringsstandarden forfatteren vil stå inne for |

Abbott (2004): det kreative arbeidet i samfunnsvitenskap er «the heuristic move» — innrammingen, ikke eksekusjonen.  
Krippendorff: koding er designet for at koderen skal være utbyttbar; den analytiske konstruksjonen er forfatterens bidrag.  
**LLM query authorship er neste steg i denne linjen.**

---

## Slide 8 — Hva gjør forfatteren? (ICMJE-kriteriene)

**AI kan ikke være forfatter** — kriterium 3 (sluttgodkjenning) og 4 (ansvarlighet) utelukker det kategorisk.

**Det mer interessante spørsmålet:** hva impliserer ICMJE-kriteriene for *forskeren* i KI-assistert arbeid?

- **Kriterium 1** (konsepsjon og design): query authorship — søkestreng, rubrikk, analysespesifikasjon
- **Kriterium 2** (kritisk revisjon): author-input-filer — hva ble rettet, avvist, omdirigert
- **Kriterium 4** (ansvarlighet): du kan bare stå ansvarlig for arbeid du kan rekonstruere og forklare

Systematisk bruk produserer evidens for at kriteriene er oppfylt.  
Usystematisk bruk produserer ingen slik evidens.

---

## Slide 9 — Workflow: oversikt

**Fem stadier, samme struktur på hvert:**

> Eksplisitte kriterier → KI eksekverer → Menneskelig verifisering → Dokumentert artefakt

| Stadium                    | Transparency-artefakt                                 |
| -------------------------- | ----------------------------------------------------- |
| Litteratursøk og screening | Søkestrenger, inklusjonskriteria, screening-log       |
| Empiriske data og analyse  | Analysekode, kodebook, data-management-protokoll      |
| Utkast                     | Skill-fil, prompt-templates, session-logger           |
| Review                     | Reviewer-konfigurasjoner, persona-prompts, syntesefil |
| Dokumentasjon              | Replication package                                   |

Mappestruktur: `literature/`, `scripts/`, `draft/`, `logs/`, `supplementary/`

---

## Slide 10 — Litteratursøk i praksis

**Tre ruter som fanger hva de andre mister:**

1. Automatiserte keyword-søk (Scopus/WebOfScience) — dokumenterte boolean-strenger
2. Semantiske søk (OpenAlex, Elicit) — finner papers uavhengig av terminologi
3. Manuell målrettet henting

**Screening:** eksplisitt inklusjonsrubrikk *før* søket kjøres — ikke konstruert post hoc  
Eksempel på rubrikk: «Ta med hvis abstrakt handler om AI-bruk i empirisk forskningspraksis; ekskluder hvis AI bare er *objekt* for forskningen; ta med ved tvil»

**Syntese:** NotebookLM (eller tilsvarende) — innebygde siteringer fra kildedokumentene  
Forskeren kan verifisere direkte mot originalkilden

---

## Slide 11 — Empiriske data: separasjonsprinsippet

*(Relevant for kvantitativt orienterte)*

**Prinsipp: KI opererer på analysekoden — aldri på dataene**

- `data/raw/` er immutabel og ekskludert fra KI-kontekst (`.claudeignore`)
- **PII-hook**: automatisk screening før enhver fil-lese-operasjon — stopper rådata fra å nå API
- Tre soner: `raw/` (alltid ekskludert) → `interim/` (pseudonymisert) → `processed/` (fullt anonymisert)

Immutabilitetsnormen = dataekvivalenten til pre-registrering:  
forhindrer etterfølgende manipulasjon av utgangsbetingelsene.

Under GDPR: dette er ikke bare epistemisk god praksis — det er den rettslig korrekte tilnærmingen ved personopplysninger.

---

## Slide 12 — Review: tre komponenter

**1. Kollega-review** — den primære eksterne kontrollen; KI-review er et supplement

**2. Strukturert KI-reviewer i *frisk* session**  

- Ikke i samme sesjon som skriving — unngår kontekst-bias  
- Adversarial konfigurasjon: eksplisitt instruert til å kritisere, reise innvendinger, spille djevelens advokat  
- Dette er en *strukturell* motforanstaltning mot sycophancy — i konfigurasjonen, ikke i enkeltprompter

**3. Cross-model persona review**  

- Samme reviewer-prompts kjørt på tvers av minst to modeller fra ulike utviklere  
- For dette paperet: 6 personas (teoretisk sosiolog, filosof, økonom, computasjonell statsvitenskap, regulatorisk komité, utvikler)  
- Pluss én *fiendtlig* persona (den «giftige kollegaen») — overraskende fruktbart  
- Innvending uavhengig reist av ≥2 modeller: substansiell; av kun én: til individuell vurdering

---

## Slide 13 — Dokumentasjon: to nivåer

**Nivå 1 — Arbeidslogger** (lab-notisbokanalogi)

- Daglige session-logger: beslutninger tatt, revidert, forkastet
- *Author-input-filer*: hva forfatteren brakte til sesjonen — ideer, omretninger, korrekturer

**Nivå 2 — Supplementary materials / replication package**

- Skill-filer, prompt-templates, søkeskript, screening-logger, persona-prompts

Loggene dokumenterer *prosess-integritet*; supplementet dokumenterer *replikerbarhet*.  
Analogt med pre-registrering vs. metodekapittel — ingen av dem erstatter den andre.

**Author-input-filer** er direkte instantiering av ICMJE kriterium 2:  
sesjon for sesjon — hva forfatteren rettet, hva forfatteren avviste.

---

## Slide 14 — Pre-registreringsanalogen

**Felles funksjon:** eksternalisering — krever at beslutninger artikuleres *før* utfall er kjent

| Pre-registrering               | Systematisk KI-bruk                    |
| ------------------------------ | -------------------------------------- |
| Eksplisitt design-forpliktelse | Eksplisitte kriterier i prompt/rubrikk |
| Tidsstempel som binder         | Logg av iterativ prosess               |
| Offentlig                      | Privat (men kan pre-registreres)       |

**PARKing er akkurat den svikten pre-spesifikasjon forhindrer.**

*Relevant disanalogi:* systematisk KI-bruk er ikke offentlig. Men:  
externaliseringsbonusen følger av selve spesifikasjonshandlingen, uavhengig av om den er offentlig.  
Og det er ikke noe i veien for å pre-registrere et systematisk KI-workflow.

---

## Slide 15 — Systematisk bruk som åpen vitenskap

- Transparency-artefaktene har de formelle egenskapene åpen-vitenskap-infrastruktur allerede krever
- De er delbare, versjonerbare og uavhengig evaluerbare
- **Ingen ny infrastruktur trengs** — tidsskrifter som allerede krever replication packages har det de trenger

Freese & Peterson (2017): sosiologiens mangelfulle engasjement med åpen vitenskap  
Systematisk KI-bruk produserer nøyaktig den type beslutningsdokumentasjon de etterlyser — som biprodukt av workflow, ikke som ekstra byrde.

---

## Slide 16 — Hva systematisk bruk *ikke* garanterer

*(Viktig for kritisk publikum)*

**Tre nivåer:**

1. **Hva dokumentasjon *sertifiserer*:** kriteriene ble spesifisert *før* verktøyet kjørte — ikke konstruert post hoc
2. **Hva dokumentasjon *muliggjør*, men ikke sertifiserer:** uavhengig evaluering av om KIs eksekusjon av kriteriene var korrekt
3. **Hva *ingen* dokumentasjonsregime fullt ut løser:** ikke-deterministiske outputs og modell-versjonsendringer

Systematisk bruk garanterer ikke høy kvalitet eller eliminerer feil.  
Poenget er at det gjør feil *synlige og korrigerbare* — noe usystematisk bruk ikke gjør.

---

## Slide 17 — Politikkimplikasjon: feil og riktig spørsmål

| Feil spørsmål                           | Riktig spørsmål                               |
| --------------------------------------- | --------------------------------------------- |
| «Brukte du KI?»                         | «Kan du vise oss den systematiske prosessen?» |
| Binær disclosure                        | Dokumentasjonsbasert rammeverk                |
| Behandler systematisk/usystematisk likt | Gjør distinksjonen evaluerbar                 |

**Operasjonelt:** utvid eksisterende replication package-normer til KI-workflows.

- Regresjonsanalyse: kode og data  
- Systematisk KI-workflow: skill-filer, prompt-templates, søkeskript, screening-logger

Ingen ny prinsipp. Ingen ny infrastruktur.

---

## Slide 18 — Dette paperet som proof of concept

- Replication package tilgjengelig: https://github.com/torbskar/structured-use-of-AI
- Appendix A: kuraterte utdrag — søkestrenger, screening-rubrikk, reviewer-konfigurasjoner, author-input-logger
- En leser kan *undersøke* den systematiske prosessen, ikke bare lese beskrivelsen av den

**Åpne spørsmål:**  

- Forbedrer systematisk bruk gjennomsnittlig outputkvalitet i sosiologi? (Zeng et al. 2025: ja i data science — ukjent i sosiologi)  
- Rammeverket er for tekst-tung og empirisk samfunnsvitenskap; generaliserbarhet til andre felt er et åpent spørsmål

---

## Slide 19 — Oppsummering og diskusjon

**Tre kjernepåstander:**

1. **Distinksjon:** Systematisk/usystematisk — ikke bruk/ikke-bruk — er det epistemisk relevante akset
2. **Query authorship:** Det intellektuelle bidraget i KI-assistert forskning ligger i instruksjonene, rubrikken, konfigurasjonen — ikke i teksten KI produserer
3. **Policy:** Dokumentasjonsbasert rammeverk er mer epistemisk ærlig og mer konsistent med eksisterende åpen-vitenskap-infrastruktur enn binær politikk

**Mulige diskusjonspunkter:**

- Hva ville «god nok» systematikk se ut som i daglig praksis?
- Hvem validerer reviewer-konfigurasjoner og skill-filer?
- Hva skjer med accountability når modell-versjoner endres?

---

*Disposisjon for presentasjon av: «Query Authorship: A Framework for Systematic AI Use in Social Science» (Skardhamar, SocArXiv 2026)*
