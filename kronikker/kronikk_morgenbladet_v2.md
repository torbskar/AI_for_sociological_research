# En KI-tsunami av vitenskapelige artikler: men hva er etterrettelig?

*Torbjørn Skardhamar, professor i sosiologi, Universitetet i Oslo*

---

Debatten om kunstig intelligens i forskning har så langt dreid seg om ett spørsmål: hvor
mye hjelper det egentlig? Tore Wig er begeistret. Surowiec og Kirkeby er mer forbeholdne.
Begge posisjoner er forståelige, og erfaringsforskjellene de beskriver er reelle. Men
debatten mangler et viktigere spørsmål — og det er ikke spørsmålet hvor gode modellene har blitt.

Wig skriver at KI-agenter kan produsere vitenskapelige artikler gode nok til å bli
publisert i seriøse tidsskrift på under en time. La oss anta at det er riktig. Da er det
neste spørsmålet ikke om artiklene er gode, men hva det innebærer at de kan produseres så
raskt og så billig. For det medfører et problem vi kjenner godt fra metodelitteraturen —
bare dramatisk forsterket.

**P-hacking på paper-nivå**

P-hacking er praksisen der man kjører mange analyser og bare rapporterer de som gir
signifikante resultater. Faren er at dette fører til overflod av resultater som ser overbevisende ut, men som egentlig er støy. Det er et anerkjent problem i empirisk forskning, og mye av open science-bevegelsen de siste femten årene har handlet om å begrense det. Løsningen er pre-registrering: at man forplikter seg til hypotese, design og analyseplan *før* man ser dataene.

Når KI kan produsere et publiserbart paper på en time, får vi det samme problemet på et
nytt nivå. En forsker kan nå generere hundre paper i løpet av en arbeidsuke, se hvilke
resultater som er mest interessante eller overbevisende, og sende inn de beste. Det er
p-hacking løftet fra enkeltanalyser til hele forskningsartikler. Alle de kjente
replikasjonsproblemene er der — bare skalert opp dramatisk og gjort nesten kostnadsfrie.

Det er ikke et argument mot KI i forskning. Det er et argument mot naiv KI-bruk i
forskning, og mot tidsskrifter som ikke har justert kravene sine i takt med det som nå
er teknologisk mulig.

**Hva etterprøvbarhet faktisk krever**

For empirisk forskning med kode er KI-bruk i prinsippet etterprøvbar. Et R-script eller
et Python-script kan i prinsippet kjøres på nytt av andre. Det er det minst
kontroversielle tilfellet, og det er et reelt fremskritt at KI gjør slik kode lettere å
skrive. Selv om KI om noen år skulle mestre kausal identifikasjon og metodologiske vurderinger, forsvinner ikke behovet for sporbarhet — det forsterkes.

Det krever for det første en dokumentert historikk — en *paper trail* — som viser hvilke
valg som ble tatt underveis, og i hvilken rekkefølge. Verktøy som GitHub gir dette
naturlig for kode: hver endring er tidsstemplet og sporbar. En logging-prosedyre for
hele forskningsprosessen, inkludert KI-interaksjoner, fyller den samme funksjonen. Det
er ikke byråkrati, men dokumentasjon av at konklusjonene ikke er cherry-picked fra et
stort antall forsøk.

Det krever for det andre pre-registrering. Det er det eneste instrumentet som faktisk
blokkerer seleksjon etter resultat, fordi det krever en offentlig, tidsstemplet
forpliktelse til hypotese og design *før* man ser resultatene. Når produksjonskostnaden
for et paper nærmer seg null, er pre-registrering ikke lenger bare god praksis. Det er
en nødvendig betingelse for at publiserte resultater skal bety noe.

Jeg argumenterer altså for to ting. Det ene er løpende dokumentasjon av
forskningsprosessen — en etterprøvbar sporbarhet i hvert trinn. Det andre er
pre-registrering som standardkrav, ikke som frivillig tilleggspoeng. Disse to tiltakene
er ikke nye ideer. De eksisterer allerede i open science-infrastrukturen. Det som er nytt,
er at KI gjør dem *nødvendige* på en måte de ikke var før. Men etterprøvbarhet krever mer enn at koden teknisk sett kan reproduseres. Dette argumentet er uavhengig av hvor god KI blir. 

**Tidsskriftene har for lave forventninger**

Wigs begeistrede beskrivelse av KI-produserte artikler som holder publiseringsstandard,
bør leses som en advarsel til tidsskriftene, ikke som en anbefaling til forskerne. Hvis
et paper kan skrives på en time og fortsatt passere fagfellevurdering, er
fagfellevurderingen utilstrekkelig — ikke fordi vurdererne gjør en dårlig jobb, men
fordi selve publiseringsmodellen ikke er rigget for en verden der produksjonskostnaden er
eliminert.

Det er ikke vanskelig å se hva som følger. Antallet innsendte manuskripter øker allerede
dramatisk — 50 til 100 prosent ifølge tall som sirkulerer i feltet. Det vil fortsette.
Tidsskrifter som ikke stiller krav om pre-registrerte protokoller og dokumentert arbeidsflyt vil bli oversvømt av resultater man ikke kan vurdere om er genuine funn eller er cherry-picked fra hundre forsøk.

Surowiec og Kirkeby avslutter sitt innlegg med en advarsel om Gell-Mann-amnesi: vi er
flinke til å se feil i KI-output innenfor eget fagfelt, men stoler for lett på output i
felt vi ikke kjenner. Det er et godt poeng. Men det understreker nettopp behovet for
systematisk dokumentasjon: en sporbar prosess er ikke avhengig av at leseren kjenner
fagfeltet godt nok til å oppdage feil. Den gjør feilene og svakheter synlige og lokaliserbare.

**Hva bør gjøres**

Vitenskapelig dømmekraft — som Wig identifiserer som det menneskelige bidraget som
gjenstår — innebærer ikke bare å vurdere om et output ser bra ut. Det innebærer å kunne
stå inne for *prosessen* som produserte det, og å ha strukturert den prosessen slik at
andre kan etterprøve den. Den egenskapen kan ikke delegeres til en KI-agent.

I en artikkel tilgjengelig på SocArXiv foreslår jeg et rammeverk for systematisk
og dokumentert KI-bruk i samfunnsvitenskapelig forskning. Det er ikke et argument mot KI
i forskning — jeg bruker det selv, og det er produktivt. Det er et forslag til hvordan
bruken kan struktureres slik at den blir etterprøvbar. Hvordan slike rammeverk bør se ut
i praksis, hvilken kompetanse de krever, og hvordan tidsskrifter bør respondere — det er
debatter vi trenger. Pre-registrerte protokoller og løpende dokumentasjon av
analyseprosessen gir en nødvendig start.

Alternativet er en forskningslitteratur der vi ikke lenger kan skille genuine funn fra
de beste resultatene i et stort antall forsøk vi aldri får vite om.

---

*Ca. 5600 tegn med mellomrom*
