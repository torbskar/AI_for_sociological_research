# Bokforslag: Systematisk bruk av KI i akademisk forskning — en praktisk innføring

**Av:** *Torbjørn Skardhamar*

**Arbeidstittel:** *Systematisk KI-assistert samfunnsvitenskap.*  
**Nivå:** Universitetsnivå, bachelor/master  
**Målgruppe:** Studenter og forskere i samfunnsvitenskap og humaniora uten programmeringsbakgrunn  
**Språk:** Norsk (med engelskspråklig terminologi i parentes der relevant)  
**Format:** Lærebok med øvingsoppgaver og maler; replikasjonspakke tilgjengelig på GitHub  
**Status:** Tidlig skisse — 2026-04-27

---

## Bokens idé og posisjon

Boken tar utgangspunkt i at KI-verktøy allerede brukes av studenter og forskere, men altfor ofte på en usystematisk måte: man spør, man får svar, og man bruker svaret uten å dokumentere hva man ba om eller hvorfor. Resultatet er at KI-assistert arbeid ikke kan vurderes, etterprøves eller forsvares faglig.

Boken argumenterer for *systematisk* KI-bruk: arbeid der instruksjoner er eksplisitte, der output verifiseres av mennesker, og der prosessen dokumenteres som en del av det faglige arbeidet. Dette er ikke primært et etisk argument — det er et metodologisk argument. Systematisk bruk gir bedre resultater, ikke bare mer transparente prosesser.

Boken er praktisk orientert. Hvert kapittel bygger opp et konkret element av arbeidsflyten, med skjermbilder, konfigurasjonsfiler, og øvingsoppgaver. Leseren skal kunne implementere det som beskrives direkte i sitt eget prosjekt.

Det spesifikke verktøyet som brukes gjennomgående er **Claude Code** (Anthropic) — et *agentisk* KI-verktøy som leser filer, husker kontekst på tvers av sesjoner, og opererer innenfor en stående prosjektkonfigurasjon. Der det er hensiktsmessig påpekes det hvordan de samme prinsippene kan implementeres med chat-baserte verktøy (ChatGPT, Gemini), men disse har høyere manuell kostnad.

---

## Kapitteloversikt

### Del I: Grunnlag

#### Kapittel 1: Hva er systematisk KI-bruk?

Introduserer skillet mellom systematisk og usystematisk KI-bruk. Usystematisk bruk: man spør, man godtar, man dokumenterer ikke. Systematisk bruk: eksplisitte kriterier, menneskelig verifisering i hvert ledd, dokumenterte artefakter.

Innfører begrepet *spørsmålsforfatterskap* (query authorship): den intellektuelle innsatsen ligger i å utforme spørsmålet, rubrikken og verifiseringsstrukturen — ikke bare i selve teksten som produseres med eller uten KI.

Forklarer kort hva KI-språkmodeller faktisk er og ikke er: de optimerer for plausibel tekst, ikke for sannhet. Systematisk bruk er det som konverterer en sannhetsindifferent generator til et sannhetsansvarlig arbeidsflyt.

Øvelse: Sammenlign to svar på samme spørsmål — ett fra et usystematisk prompt, ett fra et eksplisitt konfigurert prompt. Hva er forskjellen?

---

#### Kapittel 2: Installasjon og førsteoppsett

Steg-for-steg: installere Claude Code, opprette konto, kjøre første sesjon. Forklarer hva som skjer i bakgrunnen: hvorfor kontekst er begrenset, hva en sesjon er, og hva som skjer når konteksten fylles opp.

Presenterer token-økonomi som et praktisk konsept: hva er tokens, hva koster de, og hvilke konsekvenser har kontekstvindusindbegrensninger for hvordan man organiserer arbeidet? Ikke for teknisk — men nok til at studenten forstår *hvorfor* konfigurasjonsfiler og .claudeignore eksisterer.

Øvelse: Kjør en kort sesjon, se på token-tellingen, og tenk over hva som tar plass i konteksten.

---

### Del II: Konfigurasjon — det som gjør KI-bruk systematisk

Konfigurasjon er bokens viktigste del og skiller den fra alle "slik bruker du ChatGPT"-bøker. Dette er det som gjør KI-bruk reproduserbar, dokumenterbar og faglig forsvarlig.

#### Kapittel 3: Konteksthierarkiet — fire nivåer av instruksjoner

En av de viktigste innsiktene i systematisk KI-bruk er at instruksjoner kan og bør organiseres i nivåer: fra det som gjelder for alle prosjekter alltid, til det som bare gjelder for én bestemt mappe i ett bestemt prosjekt akkurat nå. Dette hierarkiet tjener to formål samtidig: det gir KI-en mer fokusert og relevant kontekst for den konkrete oppgaven, og det sparer tokens — KI-en lastes ikke med informasjon som er irrelevant for det den akkurat skal gjøre.

Kapittelet introduserer de fire nivåene og forklarer hva som hører hjemme på hvert:

---

**Nivå 1: Global CLAUDE.md (`~/.claude/CLAUDE.md`)**

Den globale CLAUDE.md ligger ikke i prosjektmappen, men i brukerens hjemmemappe. Den lastes automatisk ved *hver* sesjon i *alle* prosjekter. Her hører det hjemme som er stabilt og personlig: hvem du er som forsker, hvilket teknisk miljø du bruker, hvilken tone og kritikalitetsnivå du forventer av KI-en, og eventuelle stående protokoller som alltid gjelder.

Eksempel på innhold (forenklet fra forfatters egen globale konfigurasjon):

```markdown
# Role & Persona
- User: Professor i sosiologi (UiO), kvantitativ spesialist.
- Tone: Direkte, akademisk likemann, kritisk samtalepartner. Ingen
  bekreftende fraser ("Godt spørsmål").
- Criticality: Spill djevelens advokat. Flagg logiske og metodologiske
  svakheter tidlig. Prioriter svake punkter over ros.
- Language: Norsk hvis promptet på norsk; ellers engelsk.

# Technical Core
- Environment: R (tidyverse, data.table, arrow), Quarto, RStudio.
- Data: Store administrative registre (Parquet/Feather via arrow) eller
  spørreskjema (haven/labelled).
- Rule: Ikke foreslå suboptimale tilnærminger for å matche mine vaner;
  flagg bedre alternativer.
```

Token-konsekvens: Den globale CLAUDE.md bør holdes kort. Den lastes inn i *alle* sesjoner; alt som står her koster tokens i hvert eneste prosjekt.

---

**Nivå 2: .claudedocs/ — kryssprosjekt faglige standarder**

`.claudedocs/` er en mappe i prosjektrot (eller i hjemmekatalogen) som inneholder mer detaljerte stående instruksjoner som er for lange eller spesialiserte til å stå i den globale CLAUDE.md. Typisk innhold: epistemologiske standarder, disiplinfaglige krav til argumentasjon, metodologiske tommelfingerregler.

I motsetning til den globale CLAUDE.md lastes ikke `.claudedocs/`-filer automatisk. De er tilgjengelige og kan leses ved sesjonsstart via en protokoll i den globale CLAUDE.md:

```markdown
## Session setup — .claudedocs/ loading

At the start of every session, before any other work:
1. Use the Glob tool to find all files in `.claudedocs/**/*.md`.
2. Use the Read tool to load each file found.
3. If no `.claudedocs/` directory exists, skip silently.
```

Eksempel på innholdet i `.claudedocs/epistemology.md`:

```markdown
# Epistemologiske standarder for fagfellevurdering

Kritikk skal primært vurdere argumenter mot Popperianske og Mayoanske
standarder:
- Falsifiserbarhet: Er påstanden prinsipielt testbar?
- Severity testing: Er testen streng nok til at et positivt resultat
  er informativt?
- Konfirmasjons-bias: Er konklusjonen sterkere enn evidensen tillater?
```

Fordelen med `.claudedocs/` over den globale CLAUDE.md er granularitet: du kan ha separate filer for epistemologi, statistisk praksis, sitatstil, og annet — og laste bare det som er relevant for en gitt sesjon. Det er også enklere å redigere og versjonere enkeltfiler enn ett stort globalt dokument. Vel så viktig er det at du kan ønske å endre på disse konfigurasjonene mellom prosjekter og over tid, og samtidig bevare konfigurasjoner på avsluttede prosjekter. 

Token-konsekvens: Fordi innlasting er eksplisitt (via Glob + Read), kan du velge å ikke laste `.claudedocs/` i enkle sesjoner der det ikke trengs. Innholdet koster kun tokens når det er relevant.

---

**Nivå 3: Prosjekt-CLAUDE.md (prosjektrot)**

Prosjekt-CLAUDE.md ligger i roten av det aktuelle prosjektet og lastes automatisk for dette prosjektet. Her hører det hjemme som er spesifikt for dette prosjektet: forskningsspørsmålet, argumentets kjerne, nøkkelskiller og begreper, omfangsbegrensninger, filstruktur, og hvilke instrukser som gjelder for dette arbeidet.

Dette er det primære dokumentet de fleste brukere tenker på når de hører "CLAUDE.md". Det fungerer analogt med en pre-registrering: det fester rammeverket og kriteriene *før* det analytiske arbeidet begynner.

Eksempel på seksjon fra en prosjekt-CLAUDE.md:

```markdown
## Prosjekt: Segregasjonsanalyse — Oslo 2000–2020

Forskningsspørsmål: Hvordan har segregasjonsmønstre i Oslo endret
seg fra 2000 til 2020, og hvilke mekanismer driver endringen?

Nøkkelbegreper:
- Segregasjonsindeks: D (dissimilaritetsindeks) og H (Theil-indeks)
- Geografisk enhet: grunnkrets (ikke bydel)
- Populasjon: bosatte per 1. januar hvert år

Omfang: Registerdata fra SSB. Kun deskriptiv og dekomponerende
analyse — ingen kausal identifikasjon i dette prosjektet.
```

---

**Nivå 4: Undermapper med egne CLAUDE.md-filer**

Undermapper i prosjektet kan ha sine egne CLAUDE.md-filer. Disse lastes i tillegg til prosjektrot-CLAUDE.md, men *kun* når KI-en arbeider i den aktuelle undermappen eller med filer der. De er ikke synlige i andre deler av prosjektet.

Dette tjener begge formålene samtidig:

*Fokusert kontekst:* En CLAUDE.md i `logs/` inneholder spesifikke instruksjoner for loggformat, hva som skal dokumenteres, og hva som ikke skal logges. En CLAUDE.md i `draft/` inneholder versjoneringskonvensjoner og stilinstrukser for manuskriptarbeid. En CLAUDE.md i `scripts/` inneholder kodestandarder. KI-en som arbeider med et loggdokument trenger ikke scriptinstruksene; KI-en som skriver kode trenger ikke loggformatet.

*Token-økonomi:* Instruksjoner som bare er relevante i én del av prosjektet koster tokens i alle deler av prosjektet hvis de alle samles i rotnivå-CLAUDE.md. Med undermappefiler lastes kun relevant kontekst.

Kapittelet viser et fullstendig eksempel på et prosjekt med fire undermappefiler og forklarer hva som hører hjemme hvor.

Eksempel på innholdet i `draft/CLAUDE.md`:

```markdown
# CLAUDE.md — draft/

## Versjoneringskonvensjon

- `vN-draft.md` — produsert av KI
- `vN-draft - manualEdit.md` — lagret av forfatter etter direkte
  redigering

Før strukturelle endringer: sjekk nyeste fil i draft/.
Hvis nyeste fil er manualEdit: opprett ny vN+1-draft.md og arbeid
fra den. Ikke rediger manualEdit-filen.
```

---

**Oppsummering: hva hører hjemme hvor**

| Innhold                        | Globalt | .claudedocs/ | Prosjektrot | Undermappe   |
| ------------------------------ | ------- | ------------ | ----------- | ------------ |
| Rolle og persona               | ✓       |              |             |              |
| Teknisk miljø (R, Python)      | ✓       |              |             |              |
| Epistemologiske standarder     |         | ✓            |             |              |
| Disiplinfaglige krav           |         | ✓            |             |              |
| Forskningsspørsmål og argument |         |              | ✓           |              |
| Nøkkelbegreper og omfang       |         |              | ✓           |              |
| Filstruktur og protokoller     |         |              | ✓           |              |
| Loggformat og -instrukser      |         |              |             | ✓ (logs/)    |
| Versjoneringskonvensjon        |         |              |             | ✓ (draft/)   |
| Kodestandarder                 |         |              |             | ✓ (scripts/) |

Øvelse: Kartlegg ditt eget prosjekt. Skriv en global CLAUDE.md (maks 30 linjer), en prosjekt-CLAUDE.md, og minst én undermappefil. Kjør en sesjon og observer hvilke instruksjoner som faktisk brukes.

---

#### Kapittel 4: Kontekststyring og token-økonomi (.claudeignore)

.claudeignore er filen som forteller Claude Code hvilke mapper og filer som skal *utelates* fra KI-ens kontekst. Formålet er effektivitet: en stor kodebase, en mappe med hundrevis av PDF-er, eller tunge datafiler kan raskt fylle kontekstvinduet og gjøre sesjonen tregere og dyrere. .claudeignore holder irrelevant innhold unna KI-ens oppmerksomhet slik at konteksten brukes på det som faktisk har betydning for oppgaven som gjøres akkurat nå.

Dette er token-økonomi i praksis: kontekstvinduet er en begrenset ressurs, og det som ikke lastes inn koster ingenting. .claudeignore er det verktøyet som gir forskeren kontroll over hva som tar opp plassen.

Kapittelet dekker:

- Syntaks og eksempler: glob-mønstre, mappeutelukkelser, unntaksregler
- Hva som typisk bør ekskluderes: bulk-PDF-er, midlertidige filer, tunge datasett, kompilerte artefakter, git-metadata
- Forskjellen på .claudeignore og .gitignore — hva som er usynlig for KI vs. hva som er utenfor versjonskontroll; de to filene overlapper ikke nødvendigvis
- Dynamisk bruk: .claudeignore kan justeres i løpet av et prosjekt når arbeidsoppgaven skifter

Datasikkerhet behandles separat i kapittel 8, som en del av oppsettet for empiriske prosjekter med personopplysninger.

Øvelse: Sett opp .claudeignore for et prosjekt med mange PDF-er og et stort datasett. Sammenlign token-tellingen med og uten filen aktiv.

---

#### Kapittel 5: Skills — konfigurerte arbeidsflyter

En skill er en konfigurasjonsfil som koder en arbeidsflyt som et sett med eksplisitte, repeterbare instruksjoner. Skills aktiveres med en triggerfraser og er dokumenterbare artefakter: en annen forsker kan lese skill-filen og vurdere om instruksjonene var faglig forsvarlige.

Kapittelet dekker:

- Hva en skill er, og hvordan den skiller seg fra et vanlig prompt
- YAML-frontmatter: navn, beskrivelse, triggerfrase
- Skill-kropp: steg, beslutningsregler, menneskelige sjekkpunkter
- Tre eksempel-skills presenteres i sin helhet:
  1. **Fagfellevurdering-skill**: konfigurert kritisk gjennomgang av et manuskript; inkluderer eksplisitte instrukser om å være kritisk (motvirker KIs tilbøyelighet til å bekrefte)
  2. **Stil-skill**: enkoder rytme, hedging-hierarki og retorisk holdning for akademisk skriving
  3. **Oppsett-skill**: setter opp et nytt forskningsprosjekt med riktig mappestruktur, CLAUDE.md og logging

Øvelse: Skriv en enkel fagfellevurdering-skill for din egen disiplin. Kjør den på et avsnitt fra din egen tekst.

---

#### Kapittel 6: Versjonskontroll og sesjonslogging

Systematisk KI-bruk produserer artefakter som må dokumenteres og bevares. Kapittelet introduserer to komplementære systemer:

**Versjonskontroll (git):** Git-commit-historikken tidsstempler alle endringer i prosjektfiler, inkludert konfigurasjonsfiler og loggfiler. Dette gir et uavhengig tidsstempel som er vesentlig vanskeligere å forfalske enn et manuelt skrevet dato. Kapittelet dekker grunnleggende git-bruk for ikke-programmerere: init, add, commit, log. Ikke mer.

**Sesjonslogging (tre-filsystemet):** Hvert sesjon produserer tre loggfiler: en beslutningslogg, en forfatter-input-fil (hva du bidro med), og en KI-bidragsfil (hva KI-en bidro med). Formålet er å dokumentere den intellektuelle arbeidsdelingen — hvem som initierte hva, og hvem som tok beslutningene.

Kapittelet dekker:

- Logformat og eksempelfiler
- Sesjonstartprotokoll: hva gjøres ved starten av hver sesjon
- Praktisk: hvordan skrive loggfiler uten at det tar for lang tid
- Forholdet mellom loggfiler og åpen vitenskap: loggfilene er forskningsprosjektets laboratoriebok

Øvelse: Gjennomfør en arbeidsøkt og skriv alle tre loggfilene etterpå. Hvor lang tid tok det?

---

### Del III: Arbeidsflytens deler

#### Kapittel 7: Kildehåndtering og syntese med NotebookLM

Kapittelet handler ikke om å søke etter litteratur, men om hva man gjør med litteraturen man har funnet: filtrering, sortering og syntese.

**NotebookLM som grunnfestet KI-verktøy.** I motsetning til en generell chatbot er NotebookLM begrenset til kildene man laster opp. Svar er forankret i og sitert fra disse kildene. Hallusinerte referanser er strukturelt umulige — NotebookLM kan ikke sitere noe det ikke har tilgang til.

Kapittelet dekker:

- Hva NotebookLM er og hva det ikke er
- Oppsett av et notebook: hvilke dokumenter lastes opp, og hvorfor utvalget er et spørsmålsforfatterskap-beslutning
- Stående instruksjoner: krav til sitering, kildedekning og kildesjekk
- Q0-protokollen: kildedekkingssjekk som første spørsmål i hvert notebook
- Syntesespørsmål: utformingen av spørsmålet bestemmer kvaliteten på svaret
- Eksport og verifisering: hvordan man kryssjekker svar mot kildene

Øvelse: Last opp fem artikler om et tema du kjenner. Kjør Q0-protokollen. Skriv ett syntesespørsmål. Vurder svaret mot kildene.

---

#### Kapittel 8: Tre måter å bruke KI til R-koding

KI kan brukes til koding på tre prinsipielt forskjellige måter. De skiller seg fra hverandre i tilgang til filer og data, i krav til brukerens kompetanse, og i grad av systematisering. Kapittelet presenterer alle tre og tar eksplisitt stilling til hva de egner seg til — og ikke.

---

**Tilnærming 1: Chat-vinduet**

Den enkleste tilnærmingen er å lime kode inn i et chat-vindu og stille spørsmål. Tre typiske bruksområder:

a) *Finne feil i eksisterende kode.* Man limer inn et script som ikke fungerer og ber KI-en identifisere problemet. Dette er lavterskel og fungerer godt for isolerte feil.

b) *Få forklart hva kode gjør.* Nyttig i undervisningssammenheng eller når man arver andres kode. KI-en kan oversette teknisk kode til prosaforklaring, linje for linje.

c) *Få hjelp med spesifikke operasjoner.* «Hvordan slår jeg sammen to datasett på variabel X?» eller «Hvordan lager jeg en Kaplan-Meier-kurve i R?» Kvaliteten på svaret avhenger i stor grad av kvaliteten på spørsmålet — og det krever at man vet nok om hva man driver med til å spesifisere ordentlig. Konfigurasjonsprinsipper gjelder her også: jo tydeligere man oppgir datastruktur, variabeltyper og formål, jo bedre svar.

Ulemper: ingen tilgang til egne filer, ingen kontekst mellom spørsmål, ingen dokumentasjon av hva som ble gjort.

En praktisk fordel: fordi chat-vinduet ikke har tilgang til filer, er dette den tryggeste tilnærmingen når man jobber med sensitive data. Man kan lime inn en anonymisert feilmelding eller et kodesnutt uten å sende data til API-et. Det er imidlertid mulig å laste opp spesifikke filer, og man må derfor ha god innsikt i hva som regnes som persondata hvis man gjør det. 

---

**Tilnærming 2: Innebygd KI i IDE**

Flere utviklingsmiljøer har nå innebygd KI-assistanse: GitHub Copilot i RStudio, Cursor (en KI-orientert kodeeditor), og tilsvarende. Disse verktøyene ser koden du skriver i sanntid og foreslår neste linje, fyller ut funksjoner, og kan svare på spørsmål i sidevinduet.

Dette er effektivt når man skriver kode selv, men trenger støtte for å jobbe raskere — for eksempel for å unngå å slå opp syntaks man kan halvt huske, eller for å få forslag til mer idiomatisk kode.

For god effekt krever dette at koden er godt kommentert og har tydelige formål. Kommentarer fungerer her analogt med konfigurasjonsfiler: de gir KI-en kontekst om hva koden er ment å gjøre, slik at forslagene treffer. En blokk som begynner med `# Konstruer Dissimilaritetsindeks D for hvert år, aggregert på grunnkretsnivå` gir vesentlig bedre forslag enn ingen kommentar.

Viktig: innebygde IDE-verktøy har tilgang til åpne filer og kan ha tilgang til andre mapper avhengig av konfigurasjon. Det er avgjørende å ha kontroll på hvilke mapper, datasett og API-nøkler som er synlige i arbeidsøkten — det samme prinsippet som .claudeignore ivaretar for agentisk KI, men håndhevet manuelt her.

---

**Tilnærming 3: Agentisk KI**

Agentisk KI — som Claude Code — opererer i prosjektmappene dine, leser filer, skriver script, og kan kjøre dem. Det er denne tilnærmingen som er aktuell for denne boken. Kapitlene 3–6 og kapittel 9 dokumenterer hvordan den settes opp og brukes systematisk.

Den avgjørende forskjellen fra de to foregående tilnærmingene er at agentisk KI kan drive et fullstendig kodingsprosjekt fremover mellom sesjoner — ikke bare besvare enkeltspørsmål. Den husker prosjektkonteksten (via CLAUDE.md), kan gjøre sekvensielle endringer på tvers av filer, og produserer loggbare artefakter. Det er dette som gjør systematisk KI-bruk mulig i empirisk analyse.

---

**Vurdering: hva egner seg til hva**

| Tilnærming   | Styrke                                                                 | Begrensning                                                                                    | Passer for                           |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------ |
| Chat-vindu   | Lav terskel, ingen fileksponering, men kan laste opp spesifikke filer. | Ikke systematisk, ingen kontekst. Men kan spesifisere for hver sesjon, eller lage assistenter. | Feilsøking, forklaringer, uten data  |
| IDE-innebygd | Rask kodeassistanse i sanntid                                          | Krever god egenkompetanse                                                                      | Erfarne kodere som vil jobbe raskere |
| Agentisk     | Systematisk, dokumenterbar, full kontekst                              | Krever oppsett og kompetanse                                                                   | Foretrukket tilnærming i denne boken |

Chat-vindu-tilnærmingen er praktisk og fullt legitim til avgrensede oppgaver — særlig når man håndterer sensitive data og ønsker å holde filer unna API-et. Den er imidlertid ikke systematisk i den grad dette kapittelet ellers krever, og bør ikke være primærverktøyet for et fullt forskningsprosjekt.

Innebygd IDE-KI er for spesielt interesserte med god programmeringskompetanse. Den er ikke omtalt videre i denne boken.

Agentisk KI er den foretrukne tilnærmingen — og den som krever mest kompetanse å bruke riktig. Det er det boken handler om å bygge.

Øvelse: Prøv alle tre tilnærmingene på samme problem: «Lag en funksjon som beregner Gini-koeffisienten for en numerisk vektor i R.» Sammenlign svarene. Hva får du gratis i tilnærming 1 som du må spesifisere eksplisitt i tilnærming 3?

---

#### Kapittel 9: Empirisk dataanalyse — KI som kodeassistent og datasikkerhet

KI-en leser og skriver kode — den leser ikke data. Dette er kapittelet kjernepåstand og det prinsippet som gjør empirisk KI-bruk metodologisk forsvarlig.

**Del A: KI som kodeassistent**

Kapittelet dekker:

- Mappestruktur for empiriske prosjekter: `data/raw/`, `data/interim/`, `data/processed/`
- Uforanderlighetsregelen for rådata: `data/raw/` skal aldri endres etter mottak — kodes som eksplisitt regel i CLAUDE.md
- Nummererte script-filer: `01_import.R`, `02_clean.R`, `03_analyse.R` — eksplisitt rekkefølge som dokumentasjon
- Hva KI-en faktisk gjør: skriver, gjennomgår og dokumenterer analysekoden — inspiserer ikke dataene
- Spørsmålsforfatterskap i empirisk register: forskeren spesifiserer hvilke variabler som konstrueres, hvilken analysestrategi som brukes, og hvordan grensetilfeller håndteres; KI-en implementerer
- Lesbarhetskrav: kode skal være forståelig for en forsker uten dyp programmeringskompetanse

---

**Del B: Datasikkerhet og personvern**

For prosjekter med personopplysninger er KI-verktøy en potensiell risiko: hvis KI-en leser en fil med fødselsnummer og sender den til et sky-API, er data overført til en ekstern aktør. Denne delen behandler konfigurasjonsvalgene som forhindrer dette strukturelt.

*Syntetiske og shufflede data — den praktiske løsningen:*
Den enkleste og mest robuste tilnærmingen er å unngå problemet i utgangspunktet: utvikle og test all kode på data som ikke er sensitive, og kopier deretter det ferdige scriptet til den sikre serveren der de ekte dataene befinner seg. KI-en assisterer med kodeutviklingen lokalt; KI-en berører aldri de reelle dataene.

To metoder gir ulike avveininger:

1. **Syntetiske data** genererer et nytt datasett med samme statistiske egenskaper som originalen — samme variabler, fordelinger og omtrentlig korrelasjonsstruktur — men uten kobling til enkeltpersoner. R-pakken `synthpop` er standardverktøyet for samfunnsvitenskapelig registerdata; alternativer er `fabricatr` og `simstudy`. Syntetiske data er nyttige der kode bør gi substansielt realistiske mellomresultater under utvikling, for eksempel ved modellering eller imputering.

2. **Shuffling** er enklere og raskere: verdiene i hver kolonne blandes tilfeldig uavhengig av hverandre. Datastrukturen, variabelnavnene og datatypene bevares, men alle reelle sammenhenger brytes — ingen rad representerer lenger en virkelig person. Shuffling er tilstrekkelig for å teste at kode kjører feilfritt og at variabelkonstruksjoner fungerer teknisk, men ikke for å teste at analyseresultatene er substansielt meningsfulle.

3. **Kombinasjon:** Shuffle dataene for rask struktursjekk; generer syntetiske data for mer realistisk test av analyselogikken.

Arbeidsflyten er da: lag syntetiske/shufflede data lokalt → utvikle og test kode med full KI-assistanse → verifiser at scriptet kjører korrekt → kopier scriptet til sikker server (TSD, SAFE, eller tilsvarende) → kjør mot ekte data der uten KI-assistanse. Kapittelet viser et fullstendig eksempel med `synthpop` for et typisk registerprosjekt med inntekts- og utdanningsvariabler.

*Tre-sone-modellen og parallelle mapper:*
For oppsett der man arbeider tettere på ekte data supplerer en romlig separasjon i mappestrukturen den praktiske tilnærmingen over. `data/raw/` inneholder data med identifikatorer og er aldri lesbar for KI-en. `data/interim/` inneholder pseudonymiserte eller anonymiserte data og kan brukes til KI-assistert kodeutvikling. `data/processed/` inneholder analyserklare data uten identifikatorer. Soneinndelingen håndheves teknisk gjennom .claudeignore og hooks — ikke bare som konvensjon.

*settings.json — tillatelsesprofiler:*
Claude Code kan konfigureres via `settings.json` til å kreve eksplisitt godkjenning for bestemte operasjoner — for eksempel fillesing i angitte mapper. Der .claudeignore holder mapper utenfor KI-ens oppmerksomhet, stopper settings.json KI-en fra å *utføre* handlinger selv om den vet at filene finnes. Kapittelet viser en settings.json som setter `data/raw/` i "require approval"-modus og blokkerer nettverksforespørsler i analysemiljøet.

*PreToolUse-hook:*
En hook er et skript som kjøres automatisk *før* Claude Code utfører en verktøyoperasjon. En PreToolUse-hook på fillesing scanner målfilen for personidentifiserbare mønstre (fødselsnummer, D-nummer, e-postadresser) og blokkerer operasjonen hvis mønstre detekteres — før noen data sendes til API-et. Kapittelet viser et fullstendig eksempel i Python med Microsoft Presidio for norske identifikatorer, og forklarer hva hooks er, hvordan de konfigureres, og hvilke hendelser som kan utløse dem.

*GDPR-implikasjoner:*
Å sende personopplysninger til et sky-API uten databehandleravtale er som hovedregel et brudd på GDPR. Den syntetiske/shufflede arbeidsmetoden er den enkleste løsningen — den forhindrer at personidentifiserbare data overhodet befinner seg i det lokale prosjektet der KI-en opererer. For mer komplekse oppsett gir kombinasjonen av .claudeignore, settings.json og PreToolUse-hook tre uavhengige sikringslag.

Kapittelet dekker:

- Syntetiske data med `synthpop`: fullstendig eksempel og arbeidsflyt
- Shuffling: enkel implementasjon i R; når det er tilstrekkelig
- Kombinert strategi og overføring av ferdig script til sikker server (TSD/SAFE)
- Tre-sone-modellen og mappestruktur
- settings.json: tillatelsesprofiler og operasjonsstyring
- PreToolUse-hooks: konfigurasjon og eksempelkode
- GDPR-orientering: når kreves databehandleravtale, og hva forhindrer behovet

Øvelse: Generer et syntetisk datasett fra et offentlig eksempeldatasett med `synthpop`. Sjekk at variabelstruktur og fordelinger bevares. Skriv et analysemanuskript med KI-assistanse mot de syntetiske dataene. Verifiser at scriptet kjører uendret mot originaldataene.

---

#### Kapittel 10: Skriving og revisjon

Kapittelet behandler skriving som et kognitivt verktøy — ikke bare en praktisk oppgave. Poenget er at systematisk KI-bruk i skrivefasen ikke fratar forskeren den kognitive innsatsen som skriving gir, men det krever at forskeren er bevisst på dette.

Kapittelet dekker:

- Stil-skills: hva de koder og hvorfor det er faglig arbeid å skrive dem
- Utkast som innspill til menneskelig revisjon — ikke ferdige produkter
- Hermeneutisk sirkel: utkast → gjennomlesning → revisjon → ny forståelse → nytt utkast
- Faren for å bli passiv: KI kan skrive uten at forfatteren tenker; dette er et reelt problem og krever bevisst motstand
- Versjonskontroll av utkast: navnekonvensjon (`v1-draft.md`, `v1-draft - manualEdit.md`)

Øvelse: Skriv et avsnitt manuelt. Gi det til KI-en med en stil-skill. Sammenlign. Revider KI-ens versjon. Hva endret du, og hvorfor?

---

#### Kapittel 11: Fagfellevurdering med konfigurerte KI-personas

Den beste tilbakemeldingen på et manuskript er fra medstudenter, kollegaer, venner eller andre mennesker. Men du kan også få hjelp av KI. Mennesker bruker lengre tid, og er ikke alltid tilgjengelig. Bruk derfor KI til å gjøre en del grunnarbeid, og gi manuskriptet til andre først når du faktisk trenger det. En viktig del av tilbakemelding er å fange opp feil, mangler og forbedringspotensiale. Du trenger derfor konfigurere KI-tilbakemelding til å være kritisk. 

Systematisk fagfellevurdering med KI har tre komponenter som kapittelet behandler i rekkefølge:

1. **Fersk-sesjon-kravet:** Gjennomgang i en sesjon med fullt prosjektkontekst gir bias mot konsistens med tidligere utkast. En ny sesjon uten prosjektkontekst gir en mer uavhengig vurdering — nærmere posisjonen til en ekstern fagfelle.

2. **Adversarial konfigurasjon:** Skill-filen instruerer eksplisitt KI-en til å være kritisk, reise innvendinger og spille djevelens advokat. Uten denne instruksen vil KI-en typisk gi for mye positiv tilbakemelding (sycophancy). Konfigurasjonen er en strukturell motforanstaltning, ikke et enkelt prompt.

3. **Kryssmodell-gjennomgang:** Samme reviewer-prompts kjøres i ferske sesjoner i minst to modeller fra ulike utviklere (f.eks. Claude og Gemini). Innvendinger som reises uavhengig av to eller flere modeller har vesentlig høyere troverdighet enn innvendinger fra én modell alene. Divergens mellom modeller signaliserer reell tvetydighet.

Kapittelet inkluderer eksempel-personas og synteseprosedyre: handle på innvendinger reist av to eller flere modeller; flagg for individuell vurdering ved én modell; ignorer sycofantisk positiv tilbakemelding.

Øvelse: Kjør to reviewer-personas på et eget avsnitt — én i Claude, én i Gemini. Sammenlign svarene. Hva er likt, hva er ulikt?

---

### Del IV: Åpen vitenskap og faglig ansvarlighet

#### Kapittel 12: Replikasjonspakken — hva den er og hva den inneholder

Kobler systematisk KI-bruk til åpen vitenskapspraksis. Transparensartefaktene (skill-filer, prompt-maler, søkestrenger, screeningslogger, forfatter-input-filer) har de formelle egenskapene åpen vitenskap-infrastruktur allerede krever for andre forskningsoutputs: de kan deles, versjoneres og evalueres uavhengig.

For en studie som bruker regresjonsanalyse inneholder replikasjonspakken kode og data. For en studie som bruker systematisk KI-arbeidsflyt inneholder den skill-filer, prompt-maler, søkeskript og screeningslogger. Samme logikk; ulike artefakter.

Kapittelet dekker hva som bør inngå i pakken, hvordan den organiseres i GitHub, og hva som bør dokumenteres i et supplement til artikkelen.

---

#### Kapittel 13: Forfatterskap og faglig ansvar

Behandler ICMJE-kriteriene (Vancouver-kriteriene) som et positivt rammeverk for å vurdere menneskeforskeres bidrag i KI-assistert arbeid — ikke bare som et instrument for å utelukke KI som forfatter, noe alle er enige om.

Spørsmålsforfatterskap som en direkte operasjonalisering av kriterium 1 (vesentlige bidrag til konsepsjon eller design). Forfatter-input-filer som en operasjonalisering av kriterium 2 (kritisk revisjon av viktig intellektuelt innhold). Loggfilene som grunnlag for kriterium 4 (ansvarlig for alle aspekter av arbeidet).

Kapittelet behandler ikke KI-forfatterskap (det er avgjort) men hva kriteriene krever av menneskeforskeren i en KI-assistert arbeidsflyt.

---

## Didaktiske prinsipper

- Hvert kapittel åpner med et konkret scenario: "Du har samlet 200 artikler og skal finne de 30 mest relevante. Hva gjør du?"
- Konfigurasjonsfiler og skill-filer presenteres i sin helhet, ikke i utdrag
- Øvingsoppgaver er knyttet til studentens eget prosjekt, ikke konstruerte eksempler
- Maler for alle konfigurasjonsfiler tilgjengelig i replikasjonspakken på GitHub
- Ingen forutsetning om programmeringskunnskap; R og Python introduseres der de trengs, med forklaring. Det henvises ellers til standard samfunnsvitenskaplige metodeemner. 

---

---

*Skisse utarbeidet 2026-04-27.*
