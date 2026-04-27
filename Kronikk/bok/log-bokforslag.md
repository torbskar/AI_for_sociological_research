# Logg: bokforslag — systematisk KI-assistert samfunnsvitenskap

**Dato:** 2026-04-27  
**Fil:** `Kronikk/bok/bokforslag-outline.md`  
**Status:** Tidlig skisse, ikke sendt til forlag

---

## Utgangspunkt og idé

Utgangspunktet for bokforslaget er artikkelen *Query Authorship: A Framework for Systematic AI Use in Social Science* (arbeidstittel, under utarbeiding for Sociological Science). Artikkelen argumenterer for skillet mellom systematisk og usystematisk KI-bruk i forskning, introduserer begrepet spørsmålsforfatterskap, og demonstrerer en konkret arbeidsflyt gjennom sin egen produksjonsprosess.

Bokideen er forfatterens: den systematiske arbeidsflyten som ble utviklet for artikkelen er i seg selv et pedagogisk rammeverk som egner seg som grunnlag for en universitetslærebok. Der artikkelen argumenterer prinsipielt, skal boken være praktisk — steg for steg, med eksempler og øvingsoppgaver, rettet mot studenter og forskere uten programmeringsbakgrunn.

Arbeidstittel: *Systematisk KI-assistert samfunnsvitenskap.*

---

## Forfatterinput — ideer og beslutninger som er forfatters

Følgende elementer ble introdusert av forfatteren og er ikke resultater av KI-elaborering:

**Bokideen som sådan.** Forfatteren identifiserte at arbeidsflyten fra artikkelen har et pedagogisk potensial som strekker seg utover én fagartikkel, og at det mangler en norsk, praktisk orientert lærebok på dette feltet for samfunnsvitenskap.

**Avgrensning av innhold.** Forfatteren besluttet at litteratursøk ikke skal være en del av boken, men at NotebookLM for filtrering og syntese skal inkluderes. Empirisk dataanalyse og datasikkerhet skal ha et eget kapittel. Denne avgrensningen reflekterer forfatterens vurdering av hva som er pedagogisk gangbart for målgruppen kontra hva som er for spesialisert.

**Behandling av .claudeignore.** Forfatteren spesifiserte at .claudeignore skal fremstilles primært som et kontekst- og token-økonomi-verktøy, ikke som et sikkerhetsverktøy. Datasikkerhet skal behandles separat og mer grundig i kapitlet om empirisk analyse.

**Syntetiske og shufflede data.** Forfatteren introduserte de to konkrete metodene — `synthpop`-basert syntese og shuffling av kolonneverdier — som praktiske løsninger for å jobbe med sensitiv data lokalt. Arbeidsflyten (lokal utvikling → ferdig script → overføring til TSD/SAFE) er forfatterens erfaring fra egen forskningspraksis.

**Tre tilnærminger til KI-koding i R.** Forfatteren strukturerte dette kapittelet og formulerte de tre tilnærmingene (chat-vindu, innebygd IDE-KI, agentisk KI) med tilhørende vurderinger. Vurderingen — at chat er praktisk men ikke systematisk, at IDE-innebygd er for spesielt interesserte, og at agentisk KI er den foretrukne men krevende tilnærmingen — er forfatterens faglige standpunkt.

**Konfigurasjonsfiler trenger ekstra dekning.** Forfatteren presiserte at konfigurasjonskapitlene måtte utvides, og introduserte sin egen globale CLAUDE.md som eksempel på hva global konfigurasjon kan inneholde.

**Fjerne forlagsavsnittet.** Forfatteren besluttet å fjerne listen over mulige forlag for å holde utkastet nøytralt i forkant av kontakt med forlagsredaktør.

**Norsk som skriftspråk.** Forfatteren besluttet dette underveis i sesjonen.

---

## Beslutninger om struktur og innhold

### Kapittelstruktur (per 2026-04-27)

Boken er organisert i fire deler og 13 kapitler:

- **Del I: Grunnlag** (Kap 1–2): systematisk/usystematisk-skillet; installasjon og token-økonomi
- **Del II: Konfigurasjon** (Kap 3–6): konteksthierarkiet (global CLAUDE.md / .claudedocs/ / prosjekt / undermapper); .claudeignore som kontekststyring; skills; versjonskontroll og sesjonslogging
- **Del III: Arbeidsflytens deler** (Kap 7–11): NotebookLM; tre tilnærminger til R-koding; empirisk analyse og datasikkerhet; skriving og revisjon; fagfellevurdering
- **Del IV: Åpen vitenskap og faglig ansvarlighet** (Kap 12–13): replikasjonspakken; forfatterskap og faglig ansvar

### Nøkkelbeslutninger om enkeltkapitler

**Kapittel 3 (konteksthierarkiet):** Utvides til å dekke fire nivåer — global CLAUDE.md, .claudedocs/, prosjekt-CLAUDE.md, og undermappefiler — med token-økonomi og fokusert kontekst som felles begrunnelse. Forfatterens egen globale konfigurasjon brukes som eksempel.

**Kapittel 4 (.claudeignore):** Begrenses til kontekststyring og token-økonomi. Databeskyttelsesaspektet flyttes til Kapittel 9 med en eksplisitt peker.

**Kapittel 8 (R-koding):** Nytt kapittel. Tre tilnærminger presentert med forfatterens eksplisitte rangering; chat-vinduet anerkjennes som legitimt for sensitive data og avgrensede oppgaver.

**Kapittel 9 (empirisk analyse og datasikkerhet):** To-delt. Del A dekker KI som kodeassistent. Del B dekker datasikkerhet med syntetiske/shufflede data som primær praktisk løsning, tre-sone-modellen, settings.json, og PreToolUse-hooks.

---

## Hva som gjenstår

- Gjennomgang av hele utkastet for konsistens og tone
- Forfatterens vurdering av om alle 13 kapitler er riktig omfang og rekkefølge
- Eventuell utvidelse med eksempelkonfigurasjonsfiler som appendiks
- Kontakt med forlagsredaktør

---

*Logg skrevet 2026-04-27. Ikke ekstern distribusjon.*
