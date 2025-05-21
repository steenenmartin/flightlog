from django.core.management.base import BaseCommand
from ...models import Norm, Exercise

class Command(BaseCommand):
    help = 'Create or update Norms and Exercises'

    def handle(self, *args, **kwargs):
        norms_data = [
            {
                "id": 1,
                "title": "G1: Fortrolighed med UL-flyet",
                "longdescription": """<strong>Formål med øvelsen: (Kun briefing)</strong><br>Formålet med øvelsen er at introducere eleven til opbygning af et UL-fly.<br>Eleven skal orienteres om indretning af cockpit, betjeningsgreb og instrumenter, og eleven skal prøve at sidde i flyet.<br>Eleven skal desuden orienteres om, at der forud for flyvning indgår eftersyn, kontrol og cockpitcheck, og at disse sker efter checklister i flyet eller i flyets håndbog.""",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {"title": "UL-flyets opbygning", "longdescription": "Gennemgang af krop, vinger og haleplan samt vingebefæstigelse og rorforbindelser"},
                    {"title": "Cockpit, instrumenter og udstyr ", "longdescription": "Placering i cockpit med udsyn mv., gennemgang af instrumenter i flyet. Desuden gennemgås andet nødvendigt udstyr – f.eks. ildslukker og dennes placering og sikring, hvis en sådan er installeret"},
                    {"title": "Rorbetjening: styrepind, pedaler, flaps, trim og hjulbremser", "longdescription": "Lad eleven prøve alle ting og konstatere, hvordan de enkelte input forplanter sig til rorbevægelser mv."},
                    {"title": "Motorinstallation og tilhørende udstyr – herunder brændstof", "longdescription": "Demonstrer hvordan motoren betjenes samt briefing om brændstof og smøreolie."},
                    {"title": "Checklister, afprøvning og kontrol", "longdescription": "Checklisten for dagligt tilsyn gennemgås jfr. flyets håndbog, og den skriftlige checkliste for cockpitcheck gennemgås med eleven. Udover dette gennemgås andre checks – f.eks. radiocheck på flyets radio osv."},
                ]
            },
            {
                "id": 2,
                "title": "G2: Nødprocedurer",
                "longdescription": "<strong>Formål med øvelsen (Kun briefing):</strong><br>Formålet med øvelsen er at introducere eleven til mulige nødprocedurer i luften og på jorden.<br>Der bør også briefes om andre sikkerhedsprocedurer, som måtte opstå ifm. flyvningen",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {"title": "Brand mens flyet er på jorden eller i luften", "longdescription": "Procedure jfr. flyets håndbog gennemgås.<br>Hvis ingen anden forskrift så: Luk for benzinen, lad motoren køre med høje omdrejninger til benzin i karburator er brugt op. Sluk evt. med ildslukker, hvis det fortsat brænder."},
                    {"title": "Brand i kabinen og i det elektriske system", "longdescription": "Procedure jfr. flyets håndbog gennemgås.<br>Hvis ingen anden forskrift så: Land hurtigst muligt og sluk med ildslukker, hvis det fortsat brænder. Ved el-brand: Sluk for strømmen, og brug ildslukker, hvis denne forefindes.<br>Afgiv nødmelding hvis aktuelt"},
                    {"title": "Reaktioner på systemfejl og fejlbetjening", "longdescription": "Eleven skal briefes om, at langt de fleste fejlsituationer i et UL-fly er ufarlige og kan genoprettes med sædvanlige metoder.<br>Gennemgå ufarlige situationer i forhold til farlige situationer:<br><strong>Ufarlige:</strong> Batteriet har ikke mere strøm, der er en mislyd ved et af rorene, for høj udstødningstemperatur osv.<br><strong>Farlige:</strong> Blokerede ror, manglende rorforbindelse, faldende olietryk, stigende olietemperatur, mangel på brændstof osv."},
                    {"title": "Øvelse i procedure for evakuering af flyet – herunder brug af redningssystem", "longdescription": "Lad eleven prøve – på jorden – at spænde sig fri af selerne, åbne dørene og forlade flyet hurtigst muligt.<br>Gennemgå forløbet, hvis det bliver nødvendigt at udløse flyets redningssystem"},
                ]
            },
            {
                "id": 3,
                "title": "G3: Forberedelse før og efter flyvning",
                "longdescription": "<strong>Formål med øvelsen (Kun briefing):</strong><br>Formålet med øvelsen er at introducere eleven til det set-up, der er for overhovedet at kunne flyve skoleflyvning på en flyvedag. Briefingen skal indeholde noget om den briefing, som eleven skal have forud for skoleflyvningen, men også under skolingen. Eleven skal også briefes om sin opgave med at få fly ud af hangaren, samt om de praktiske ting, der påvirker en god træningsflyvning.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {"title": "Briefing før skoleflyvning ",
                     "longdescription": "Eleven være forberedt på at blive briefet med udgangspunkt i elevloggen og dermed ud fra seneste lektion."},
                    {"title": "Nødvendige dokumenter ombord og på pladsen",
                     "longdescription": "Flyets dokumenter gennemgås, og der skelnes mellem dokumenter, som SKAL være med ombord og dokumenter, som skal være til stede på pladsen"},
                    {"title": "Udstyr som skal bruges til påtænkt flyvning",
                     "longdescription": "F.eks. GPS, brug af transponder og radio, Kort og frekvensliste"},
                    {"title": "Udvendige og indvendige eftersyn på flyet",
                     "longdescription": "Dagligt tilsyn og cockpitcheck gennemgås. Procedure for tankning."},
                    {"title": "Sikring af vægt og balance",
                     "longdescription": "Gennemgang af min. og max. vægt i sæderne og – hvis eleven er for let – hvordan den manglende vægt opvejes med ballast"},
                    {"title": "Justering af seler, sæde og pedaler",
                     "longdescription": "Eleven hjælpes til at skabe den rigtige position i cockpittet, så eleven selv fremover kan håndtere dette"},
                    {"title": "Check før start og efter landing",
                     "longdescription": "Gennemgå de kontrolforanstaltninger, som skal gennemføres inden flyvningen kan gå i gang:<br><br>1. Kontrol før start og opvarmning<br> 2. Kontrol af motorens ydelse<br>3. Procedure for at slukke motor og elektrisk udstyr"},
                    {"title": "Parkering og sikring efter landing",
                     "longdescription": "Parkering og sikring af flyet efter landing gennemgås. Herunder at sætte flyet i hangar og/eller tøjre fly udenfor. Afslutning af administrative procedurer med elevlog og flyets logbog."},
                ]
            },
            {
                "id": 4,
                "title": "G4: Tilvænningsflyvning",
                "longdescription": "Skyhøjden større end 1500 fod AGL og sigtbarheden 8 km eller mere<br><br><strong>Formål med øvelsen:</strong><br>Formålet med øvelsen er at lade eleven opleve en flyvning med tilhørende start og landing samt introducere eleven til det landskab, som ligger i nærheden af flyvepladsen.<br><br>På denne øvelse skal eleven også introduceres til betydningen af at holde godt udkig. Det skal ske inden påbegyndelse af drej, men også helt generelt under VFR-flyvning og især i nærheden af flyvepladsen før landingsrunde.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {"title": "Kendskab til området omkring flyvepladsen",
                     "longdescription": "Eleven skal opleve landskabet omkring flyvepladsen med markante punkter, som kan lede eleven tilbage til flyvepladsen til landing"},
                    {"title": "Check før taxi, opstart og håndtering af motor",
                     "longdescription": "Indgår i UL-flyets checkliste"},
                    {"title": "Procedure for parkeringsområdet og hensyn der skal tages",
                     "longdescription": "Indgår i UL-flyets checkliste"},
                    {"title": "Vindens indflydelse og rorbevægelser til korrektion samt pladsens/banens overflade",
                     "longdescription": "Indgår normalt i UL-flyets checkliste"},
                    {"title": "Sikre frie rorbevægelser og kontrol af instrumenter",
                     "longdescription": "Indgår i UL-flyets checkliste"},
                    {"title": "Procedurer med evt. flyvekontrol hvis aktuelt",
                     "longdescription": "Dækker også procedurer på ikke-kontrollerede flyvepladser – herunder svæveflyve- og UL-pladser"},
                ]
            },
            {
                "id": 5,
                "title": "G5: Rorvirkning og funktion af systemer",
                "longdescription": "Skyhøjden større end 1500 fod AGL og sigtbarheden 8 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal på denne øvelse lære, hvordan rorene virker enkeltvis, og eleven skal dermed opleve, at brug af krænge- eller sideror enkeltvis giver en ikke-optimal flyvning.<br><br>Eleven skal lære at bruge de visuelle referencer – både under ligeudflyvning og i forbindelse med at holde vingerne vandrette.<br><br>Eleven skal have demonstreret og selv prøve, at der er en direkte sammenhæng mellem flyets næsestilling og flyvehastigheden. Eleven skal desuden prøve virkningen af krængerorenes sekundære virkning.<br><br>Udover normal flyvning skal eleven opleve, hvilken betydning flaps og evt. optrækkeligt understel har på flyvetilstanden.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Procedure for udkig",
                        "longdescription": "Ingen kursændring foretages uden sikring af frit luftrum. Kig ud!"
                    },
                    {
                        "title": "Brug af visuelle referencer",
                        "longdescription": "Eleven skal lære at aflæse flyets stilling ift. horisonten og vandret flyvning ift. vingetippernes afstand til horisonten i hver side."
                    },
                    {
                        "title": "Effekter under ligeudflyvning og under krængning",
                        "longdescription": "Virkningen af højderoret og krængerorene demonstreres for og prøves af eleven. Indledende krængning demonstreres."
                    },
                    {
                        "title": "Afledte virkninger af brugen af sideror, højderor og krængeror",
                        "longdescription": "Betydning for: Flyvehastighed, slipstrøm, brugen af motor, trimning, flaps, andre rorflader hvis aktuelt – f.eks. luftbremser."
                    },
                    {
                        "title": "Brugen af karburatorforvarmer",
                        "longdescription": "Principper for brug af karburatorforvarmer gennemgås og introduceres som en nødvendig del af standardprocedurer ved bl.a. descend, landingsrunder og flyvning med lave motoromdrejninger."
                    },
                    {
                        "title": "Brugen af cockpitvarme og ventilation",
                        "longdescription": "Brugen af cockpitvarme og ventilation gennemgås. Introduktion til hvad disse systemer kan betyde i nødsituationer."
                    }
                ]
            },
            {
                "id": 6,
                "title": "G6: Taxiøvelser",
                "longdescription": "<strong>Formål med øvelsen:</strong><br>Eleven skal på denne øvelse lære samt træne i at bevæge sig med UL-flyet på jorden. Eleven skal endvidere lære brugen af klareringer eller informationer fra flyveledelse etc.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Check før taxi",
                        "longdescription": "Eleven skal lære at tage hensyn til anden trafik før påbegyndelse af taxi samt tage hensyn til lokale regler på flyvepladsen for at bevæge sig der."
                    },
                    {
                        "title": "Indledning af taxi og kontrol af taxihastighed samt opmærksomhed på at kunne stoppe igen",
                        "longdescription": "Eleven skal kunne taxi med flyet på en sådan måde, at flyet kan stoppes igen, hvis er er risiko for at kollidere med anden trafik, og hvis piloten får besked på at stoppe."
                    },
                    {
                        "title": "Håndtering af motoren",
                        "longdescription": "Motoren skal kunne håndteres, så flyet kan bevæge sig efter instruktioner mv."
                    },
                    {
                        "title": "Kontrol af muligheden for at styre UL-flyet på jorden",
                        "longdescription": "Eleven skal kunne styre på en sådan måde, at flyet kan styres i den rigtige retning og dreje i en ønsket retning."
                    },
                    {
                        "title": "Drej med UL-flyet indenfor et begrænset område",
                        "longdescription": "Eleven skal kunne taxi flyet på en sådan måde, at der tages hensyn til andre luftfartøjer, som er parkeret på flyvepladsen. Eleven skal have opmærksomhed på procedurerne og forhold, som man skal være opmærksom på."
                    },
                    {
                        "title": "Brug af rorene i forhold til vindens påvirkning",
                        "longdescription": "Eleven skal lære at taxi med styrepinden imod vindsiden og i øvrigt være forberedt på påvirkning af sidevind, når flyet skal startes."
                    },
                    {
                        "title": "Flyvepladsens overflade i forhold til taxi med et UL-fly",
                        "longdescription": "Eleven skal lære, at en ujævn overflade på den flyveplads, som UL-flyet vil flyve fra, vil få indflydelse på, hvordan UL-flyet taxier på den pågældende flyveplads."
                    },
                    {
                        "title": "Frie rorbevægelser",
                        "longdescription": "Forud for en start skal piloten sikre sig, at alle ror er frit bevægelige."
                    },
                    {
                        "title": "Check af instrumenter",
                        "longdescription": "Forud for starten skal piloten sikre sig, at flyets instrumenter fortsat er indenfor de tilladte tolerancer (”Grønt område”)."
                    },
                    {
                        "title": "Klarering fra eventuel flyvekontrol",
                        "longdescription": "Hvis flyvningen foregår fra en kontrolleret flyveplads, skal eleven sikre sig at have fornøden klarering til den kommende flyvning."
                    }
                ]
            },
            {
                "id": 7,
                "title": "G7: Nødsituationer mens flyet er på jorden",
                "longdescription": "<strong>Formål med øvelsen:</strong><br>Eleven skal lære den rigtige reaktion, hvis flyet ikke længere kan styres under taxi, eller hvis flyets bremser svigter.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Test af styring og bremser inden påbegyndelse af taxi",
                        "longdescription": "Eleven skal lære at prøve bremsevirkningen inden egentlig taxi, og eleven skal samtidig efterprøve, at retningen kan styres vha. bremser eller koblet næsehjul/halehjul."
                    },
                    {
                        "title": "Bremsesvigt under taxi",
                        "longdescription": "Eleven skal lære proceduren ved bremsesvigt jfr. flyets håndbog – typisk vil det være at stoppe motoren og styre flyet fri af forhindringer."
                    },
                    {
                        "title": "Styringssvigt under taxi",
                        "longdescription": "Eleven skal lære proceduren for styringssvigt jfr. flyets håndbog – typisk vil det være at stoppe motoren og bremse flyet vha. flyets hjulbremser."
                    }
                ]
            },
            {
                "id": 8,
                "title": "G8: Flyvning ligeud i samme højde",
                "longdescription": "Skyhøjden større end 1000 fod AGL og sigtbarheden 8 km eller mere<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at flyve UL-flyet i samme højde, med vandrette vinger og på den valgte kurs. Eleven skal endvidere kunne holde samme højde, når flyets hastighed ændres, og hastigheden skal kunne holdes indenfor det tilladte område ved ændring af flyets konfiguration – f.eks. ved udfældning af flaps.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Flyvning ved normal rejsehastighed",
                        "longdescription": "Eleven skal opnå og fastholde flyvning i samme højde under ligeudflyvning."
                    },
                    {
                        "title": "Flyvning ved kritisk lav hastighed",
                        "longdescription": "Eleven skal kunne fastholde ligeudflyvning i samme højde ved kritisk lav hastighed, som ligger over stallingsgrænsen."
                    },
                    {
                        "title": "Demonstration af flyets egenstabilitet",
                        "longdescription": "Demonstration af flyets egen stabilitet omkring de tre akser: Højakse, tværakse og længdeakse."
                    },
                    {
                        "title": "Fastholdelse af næsestilling, vandrette vinger og kurs – herunder trimning af flyet",
                        "longdescription": "Træne flyets næsestilling under ligeudflyvning ift. horisonten samt fastholde vandrette vinger og den valgte kurs. Brugen af trim trænes."
                    },
                    {
                        "title": "Flyvning ved forskellige hastigheder vedr. brug af motoren",
                        "longdescription": "Holde højde ved forskellige hastigheder og med samtidig brug af trimmet. Højden styres med gashåndtaget og hastigheden med styrepinden."
                    },
                    {
                        "title": "Flyvning under ændring af hastigheder og flyets konfiguration",
                        "longdescription": "Afstemme flyets hastighed, så det holdes indenfor rammerne iht. flyets håndbog."
                    },
                    {
                        "title": "Brug af instrumenter i forbindelse med præcisionsflyvning",
                        "longdescription": "Eleven skal f.eks. lære opmærksomhed omkring fartmålerens områder samt variometerets evt. bevægelser ved hastighedsændringer."
                    }
                ]
            },
            {
                "id": 9,
                "title": "G9: Stigning",
                "longdescription": "Skyhøjden større end 1500 fod AGL og sigtbarheden 8 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære sammenhængen mellem stigning i et UL-fly og brugen af flyets motor, dets højderor og dets flaps.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Indgang i og fastholdelse af stigning ved normal og max. stigning samt at flade ud, når højden er nået",
                        "longdescription": "Eleven skal lære at stige ved bedste stigehastighed (”Blue line”) samt ved bedste stigevinkel. Eleven skal desuden lære at flade ud i den korrekte højde."
                    },
                    {
                        "title": "Udfladning i forskellige højder",
                        "longdescription": "Eleven skal kunne stige og flade ud i højder, som eleven forud har fået anvist."
                    },
                    {
                        "title": "Stigning en-route",
                        "longdescription": "Eleven skal lære at stige under rejseflyvning til en højde, som forud er angivet af enten instruktøren eller en flyvekontrol."
                    },
                    {
                        "title": "Stigning med flaps ude",
                        "longdescription": "Eleven skal lære stigning med flaps, hvor hastigheden hele tiden holdes indenfor tilladt hastighedsområde på fartmåleren (hvid bue)."
                    },
                    {
                        "title": "Overgang til normal stigning",
                        "longdescription": "Eleven skal lære overgang fra stigning med flaps til stigning uden flaps."
                    },
                    {
                        "title": "Stigning med max. stigevinkel",
                        "longdescription": "Eleven skal kunne skelne mellem stigning med bedste stigehastighed og hastigheden for bedste stigevinkel. Sidstnævnte kan være nødvendig med forhindringer ved baneenden."
                    },
                    {
                        "title": "Brug af instrumenter under stigningen",
                        "longdescription": "Eleven skal lære betydningen af brugen af både fartmåler, variometer, omdrejninger samt olie- og motortemperatur."
                    }
                ]
            },
            {
                "id": 10,
                "title": "G10: Nedstigning (Descend)",
                "longdescription": "Skyhøjden større end 1500 fod AGL og sigtbarheden 8 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at nedstige fra én højde til en anden og skal lære at gøre det både med motorydelse og med motoren i reducerede omdrejninger – evt. i tomgang.<br><br>Hvis flytypen er egnet og godkendt til det, skal eleven endvidere bruge sideglidning til forøgelse af synkehastigheden.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Indgang i og fastholdelse af nedstigningsrate samt udfladning i den ønskede højde efter nedstigning",
                        "longdescription": "Eleven skal lære baggrunden for at måtte nedstige til en lavere højde samt beslutningen om at gøre det."
                    },
                    {
                        "title": "Udfladning i forudbestemte højder",
                        "longdescription": "Eleven skal lære at flade ud i den højde, som instruktøren har angivet."
                    },
                    {
                        "title": "Glideflyvning, nedstigning med motor og nedstigning under cruise incl. effekten af motorkraft og flyvehastighed",
                        "longdescription": "Eleven skal kunne descende både med og uden motor, og eleven skal lære at overvåge flyvehastighed på fartmåleren og motoromdrejninger under dyk og sikre, at fart og omdrejning holdes inden for flyets grænser."
                    },
                    {
                        "title": "Sideglidning på dertil egnede flytyper",
                        "longdescription": "Brugen af sideglidning øves i stor højde, således at teknikken er lært, så den evt. kan bruges som supplerende synk under indflyvning i tilfælde af for høj indflyvning."
                    },
                    {
                        "title": "Brug af instrumenter under nedstigningen",
                        "longdescription": "Eleven skal lære betydningen af brugen af både fartmåler, variometer og omdrejninger under nedstigning."
                    }
                ]
            },
            {
                "id": 11,
                "title": "G11: Drej",
                "longdescription": "Skyhøjden større end 1000 fod AGL og sigtbarheden 5 km eller mere.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Indgang i og fastholdelse af drej med moderat krængning og i samme højde",
                        "longdescription": "Eleven skal lære at kigge ud inden påbegyndelse af drej, og eleven skal lære at koordinere rorene – især krænge- og sideror for at flyve et rent drej."
                    },
                    {
                        "title": "Udretning af drej",
                        "longdescription": "Eleven skal lære at rette ud af et drej på en valgt kurs, og efter udretning skal flyets vinger være vandrette, og kuglelibellen skal ligge i midten."
                    },
                    {
                        "title": "Stigedrej",
                        "longdescription": "Eleven skal lære at dreje under stigning og herefter rette ud på en forudbestemt kurs. Instrumenter skal overvåges."
                    },
                    {
                        "title": "Drej under nedstigning",
                        "longdescription": "Eleven skal lære at dreje under nedstigning og herefter rette ud på en forudbestemt kurs. Instrumenter skal overvåges."
                    },
                    {
                        "title": "Drej til forudbestemte headings",
                        "longdescription": "Eleven skal lære rette ud af et drej jfr. kompas, kursgyro eller GPS."
                    },
                    {
                        "title": "Brug af instrumenter under drej",
                        "longdescription": "Der skal være opmærksomhed på kuglelibellen (ren flyvning) og fartmåler og variometer (kan indikere, at højden ikke fastholdes)."
                    }
                ]
            },
            {
                "id": 12,
                "title": "G12: Langsomflyvning",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Målet med øvelsen er at træne eleven i at være opmærksom på, når flyet nærmer sig en flyvning ved utilsigtet og kritisk lav hastighed.<br><br>I en sådan situation skal eleven kunne fastholde stabiliteten i flyvningen medens hastigheden øges til normal flyvehastighed igen.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Udkig og sikkerhedscheck",
                        "longdescription": "Udover at sikre at luftrummet omkring flyet er frit, skal eleven også sikre sig, at luftrummet under flyet er frit. Besætningens fastspænding skal sikres."
                    },
                    {
                        "title": "Introduktion til karakteristika ved langsomflyvning",
                        "longdescription": "Eleven skal have demonstreret og selv erkende symptomerne på langsomflyvning: bløde ror, høj næsestilling og ændret lydbillede."
                    },
                    {
                        "title": "Kontrolleret flyvning ved kritisk lav høj indfaldsvinkel (lav flyvehastighed)",
                        "longdescription": "Flyet skal flyves med en hastighed lige over stallingsgrænsen, hvor eleven skal kunne holde vingerne vandrette."
                    },
                    {
                        "title": "Korrekt stilling i luften når der gives fuld motorkraft for at opnå normal stigehastighed",
                        "longdescription": "Flyets næse skal grundlæggende lidt ned for at få flyvefart, og først herefter kan der gives gas, så hastigheden kan øges. Hvis der gives gas, mens flyet er stallet, kan der ske en forstærkning af stallet og i værste fald udvikle sig til et spin."
                    }
                ]
            },
            {
                "id": 13,
                "title": "G13: Stall",
                "longdescription": "Skyhøjden større end 2500 fod AGL og sigtbarheden 8 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære symptomerne på stall at kende, prøve at stalle under ligeudflyvning. Eleven skal lære at rette op, hvis den ene vinge dykker, og stall i landingskonfiguration skal øves (med evt. landingsflaps udfældet og evt. med luftbremser hvis aktuelt).",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Sikkerhedscheck og udkig",
                        "longdescription": "Før stall sikres det, at der ikke er løse genstande i cockpittet, besætningen er fastspændt samt at luftrummet er frit – også under flyet."
                    },
                    {
                        "title": "Erkendelse af symptomer på stall",
                        "longdescription": "Eleven skal opleve symptomer på stall – f.eks. rystelser, svage og bløde rortryk, for høj næse ift. horisonten, svingende udslag på fartmåleren, høj synkehastighed."
                    },
                    {
                        "title": "Erkendelse af at flyet er stallet",
                        "longdescription": "Efter ovennævnte symptomer vil flyet falde igennem, flyets næse dykker, men fartmåleren viser fortsat lav eller ingen hastighed."
                    },
                    {
                        "title": "Rent stall og opretning med og uden motorkraft",
                        "longdescription": "Opretning med motorkraft: Tryk flyets næse lidt og giv herefter behersket gas.<br>Opretning uden motorkraft: Tryk flyets næse og lad det få fart på igen således, at flyet hastighed kommer over stallingshastigheden.<br><br><strong>PAS PÅ:</strong> I UL-fly med en kraftig motor kan P-effekten medføre at flyet vrides rundt på ryggen, hvis der gives hurtigt gas, inden flyet har fået næsen ned og dermed tilstrækkelig flyvefart."
                    },
                    {
                        "title": "Opretning hvis den ene vinge dykker under stall",
                        "longdescription": "Eleven skal kunne standardproceduren for opretning fra spin: modsat sideror, styrepind lidt frem og ret ud af dykket. Generelt skal flyets håndbog følges."
                    },
                    {
                        "title": "Tæt på stall i landingskonfiguration med og uden motorstøtte med udretning i den indledende fase. FLYET MÅ IKKE STALLE",
                        "longdescription": "Eleven skal i stor højde prøve at nærme sig stallingsgrænsen, når flyet flyver med indflyvningshastighed og flaps udfældet (evt. luftbremser udfældet)."
                    }
                ]
            },
            {
                "id": 14,
                "title": "G14: Undgåelse af spin",
                "longdescription": "Skyhøjden større end 2500 fod AGL og sigtbarheden 8 km eller mere.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Sikkerhedscheck og udkig",
                        "longdescription": "Før øvelsen sikres det, at der ikke er løse genstande i cockpittet, besætningen er fastspændt samt at luftrummet er frit – også under flyet."
                    },
                    {
                        "title": "Indgang til stall i drej uden at flyet dog staller",
                        "longdescription": "Eleven skal være bevidst om, at et stall i drej er begyndelsen på et spin, og at dette derfor skal undgås. Skulle flyet alligevel stalle, skal eleven kende proceduren for udretning af spin jfr. flyets håndbog eller standardmetoden."
                    }
                ]
            },
            {
                "id": 15,
                "title": "G15: Start og stigning til downwind-positionen",
                "longdescription": "Skyhøjden større end 1000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at starte med UL-flyet samt at overholde korrekte hastigheder under stigning for herefter at placere flyet i den korrekte position til en efterfølgende landingsrunde.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Check før start",
                        "longdescription": "Følg checklisten for flyet!<br>Kig efter anden trafik, har piloten fornøden klarering? Motortest, vejret, beslutning om TEM (Threat-and-Error Management).<br>Flyet skal have en checkliste, som indeholder de punkter, der skal gennemføres lige før en start."
                    },
                    {
                        "title": "Start i nogenlunde direkte modvind",
                        "longdescription": "Eleven skal først lære at starte flyet i nogenlunde direkte modvind, så påvirkning af sidevind undgås."
                    },
                    {
                        "title": "Start i sidevind",
                        "longdescription": "Eleven skal lære at starte i sidevind og herunder holde styrepinden imod vinden samt holde baneretning efter letning."
                    },
                    {
                        "title": "Aktioner efter start",
                        "longdescription": "Eleven skal lære de aktiviteter, som skal gennemføres efter start jfr. flyets håndbog – f.eks. sluk for benzinpumpe, flaps indfældes, etablering af korrekt hastighed i stigning."
                    },
                    {
                        "title": "Procedurer for start på korte og bløde baner - incl. beregning af startstrækning",
                        "longdescription": "Eleven skal lære at starte fra korte baner efter at have beregnet nødvendig banelængde jfr. flyets håndbog og supplerende tabel over tillæg ved forskellige baneforhold."
                    },
                    {
                        "title": "Procedure for støjbegrænsning",
                        "longdescription": "Eleven skal kunne tilrette starten på en sådan måde, at der bliver mindst mulig belastning af miljøet fsva. støj.<br>Eleven skal lære sætte sig ind i støjprocedurer for den flyveplads, hvor starten foregår."
                    }
                ]
            },
            {
                "id": 16,
                "title": "G16: Landingsrunde, indflyvning og landing",
                "longdescription": "Skyhøjden større end 1200 fod AGL og sigtbarheden 5 km eller mere. Hvis instruktøren finder det forsvarligt, kan sigtbarheden reduceres til 3 km (1.5 km i trafikrunden, fri af skyer. Se AIC B 22/15)<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at etablere flyet i en korrekt landingsrunde, at etablere en stabiliseret indflyvning samt at lande UL-flyet korrekt. I løbet af øvelsen skal eleven lære mærkelandinger til et forudbestemt sætningspunkt.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Opsætning af landingsrunde",
                        "longdescription": "Eleven skal kende procedurerne for opsætning af landingsrunden og etablering af downwind, base og finale."
                    },
                    {
                        "title": "Indflyvning med motorstøtte og efterfølgende landing",
                        "longdescription": "Eleven skal lære at etablere finalen med motorstøtten samt at lande flyet, efter at motoren er sat i tomgang. Eleven skal lære at kigge frem i horisonten under udfladning for ikke at flyve flyet i jorden."
                    },
                    {
                        "title": "Aflastning af næsehjulet hvis aktuelt",
                        "longdescription": "Eleven skal lære at holde næsehjulet løftet efter sætning for at aflaste dette og sikre aerodynamisk bremsning af flyet."
                    },
                    {
                        "title": "Vindens indflydelse på indflyvnings- og sætningshastighed og brug af flaps",
                        "longdescription": "Eleven skal lære, at flyet normalt skal flyves lidt hurtigere, hvis vinden er kraftig."
                    },
                    {
                        "title": "Indflyvning og landing i sidevind",
                        "longdescription": "Flyet skal opereres indenfor begrænsningerne i flyets håndbog. Efter at have lært indflyvning og landing i direkte modvind, skal eleven lære det samme i sidevind. Flyvepladsens procedure for placering af landingsrunden skal overholdes, men hvis piloten selv kan vælge hvilken side af pladsen landingsrunden skal lægges, vil en placering i læsiden give de korteste drej på landingsrunden."
                    },
                    {
                        "title": "Glidelandinger",
                        "longdescription": "Eleven skal lære at flyve flyet ind i en glidelanding, hvor gassen tages på medvind ud for tærsklen."
                    },
                    {
                        "title": "Procedure og teknik for landing på korte og bløde baner",
                        "longdescription": "Når mærkelandinger beherskes, øves kortbanelandinger. Eleven skal kunne beregne, hvor lang bane der er behov for."
                    },
                    {
                        "title": "Landing uden flaps",
                        "longdescription": "Eleven skal lære at beherske landing af flyet uden brug af flaps."
                    },
                    {
                        "title": "Mislykket indflyvning med efterfølgende go-around",
                        "longdescription": "Eleven skal kunne afbryde en indflyvning, give gas og gå rundt igen. Flaps og evt. karburatorforvarmer skal kunne betjenes."
                    },
                    {
                        "title": "Procedure for støjbegrænsning",
                        "longdescription": "Eleven skal kunne tilrette landingsrunden på en sådan måde, at der bliver mindst mulig belastning af miljøet fsva. støj. Eleven skal lære sætte sig ind i støjprocedurer for den flyveplads, hvor landingen foregår."
                    }
                ]
            },
            {
                "id": 17,
                "title": "G17: Nødsituationer under start og landing",
                "longdescription": "Skyhøjden større end 1000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære standardprocedurer for de nødsituationer, der kan opstå under start og landing.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Afbrudt start på jorden",
                        "longdescription": "Eleven skal kunne bremse flyet ned ved en afbrudt start på banen og evt. trække ud i sikkerhedszonen eller et andet egnet område."
                    },
                    {
                        "title": "Motorfejl efter start",
                        "longdescription": "Som et væsentligt element i TEM skal eleven være bevidst om mulige nødlandingsområder lige efter start i en vinkel på op til 30° til hver side af startretningen.<br><strong>HUSK:</strong> Flyv flyet og hold hastigheden."
                    },
                    {
                        "title": "Mislykket landing med go-around",
                        "longdescription": "I tilfælde af at landingen mislykkes og flyet ”hønser”, skal eleven lære proceduren med straks at give kontrolleret gas, etablere flyvefart, ændre flapsstilling over 300 fod, evt. karburatorforvarmer og herefter lave en fornyet landingsrunde. Pas på P-effekten."
                    },
                    {
                        "title": "Mislykket indflyvning",
                        "longdescription": "Hvis en indflyvning mislykkes – enten fordi den ikke er stabil eller fordi, der opdages forhindringer på banen, skal eleven lære proceduren med at give gas igen, stabilisere flyet samt gennemføre en fornyet landingsrunde – og herunder foretage de procedurer i cockpittet, som er nødvendige."
                    }
                ]
            },
            {
                "id": 18,
                "title": "V1: Første soloflyvninger",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 8 km eller mere. Instruktøren vurderer den aktuelle vejrsituation, med særlig opmærksomhed på sidevind. Max. sidevindskomponent 10 kts.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal flyve alle soloflyvninger på skoleflyet under supervision af instruktøren.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Instruktørens briefing af eleven",
                        "longdescription": "Instruktøren skal autorisere eleven til soloflyvning i elevens logbog. Instruktøren briefer eleven om rammerne for soloflyvningen – herunder procedurer og begrænsninger. Flyvningerne skal foregå under instruktørens overvågning."
                    },
                    {
                        "title": "Brug af nødvendigt udstyr",
                        "longdescription": "Instruktøren aftaler med eleven hvilket udstyr der er nødvendigt for soloflyvningen – bl.a. aftale om to-vejs radioforbindelse mellem elev og instruktør."
                    },
                    {
                        "title": "Genopfriskning af forhold omkring flyvepladsen og området",
                        "longdescription": "Instruktøren skal sikre sig, at eleven fortsat er fortrolig med pladsen og området, så eleven under soloflyvning hele tiden ved, hvor pladsen ligger."
                    },
                    {
                        "title": "Instruktørens debriefing af eleven",
                        "longdescription": "Soloflyvningerne gennemgås med eleven af instruktøren."
                    }
                ]
            },
            {
                "id": 19,
                "title": "V2: Avancerede drej",
                "longdescription": "Skyhøjden større end 2500 fod AGL og sigtbarheden 8 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal øve drej med større krængning samt kunne rette ud fra unormale flyvestillinger.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Drej med 45°s krængning i samme højde og under nedstigning",
                        "longdescription": "Denne øvelse kan kun flyves med instruktør."
                    },
                    {
                        "title": "Udretning fra unormale flyvestillinger",
                        "longdescription": "Øvelsen flyves med instruktør, som bringer flyet ind i unormale flyvestillinger. Eleven skal kunne rette ud fra disse."
                    }
                ]
            },
            {
                "id": 20,
                "title": "V3: Nødlandingsøvelse uden motorkraft",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at finde egnede områder med nødlandingsmuligheder, at udpege en egnet mark til en nødlanding, at sætte en korrekt landingsrunde op til denne mark samt afpasse højden således, at der kan foretages en korrekt indflyvning til marken.<br><br>Nødlandingen skal afbrydes i min. 500 ft. AGL, medmindre der foreligger en skriftlig aftale med markens ejer om, at marken må benyttes til nødlandingsøvelser ned til 50 ft.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Procedure forud for nødlanding",
                        "longdescription": "Brug af nødcheckliste i den pågældende situation (Brand, motorstop, elektrisk brand osv.). Nødchecklisten skal huskes, og den skal foreligge. Hvis tiden tillader, skal eleven kontrollere, om alt er gjort."
                    },
                    {
                        "title": "Valg af landingsområde og plan for evt. ændring",
                        "longdescription": "Valg af egnet område og nogle mulige marker. Bemærk vindretning og markens overflade."
                    },
                    {
                        "title": "Mulig glideafstand",
                        "longdescription": "Hastighed reduceres til hastighed for bedste glidetal."
                    },
                    {
                        "title": "Finde egnet mark",
                        "longdescription": "Længde, indflyvningsforhold, modvind. Hvis muligt – mål evt. markens længde ved at flyve langs marken: 30 sek ved 120 km/t = ca. 1000 meter."
                    },
                    {
                        "title": "Plan for nedstigning ift. marken og evt. forhindringer",
                        "longdescription": "Vælg placering ift. marken, så der er tid til at komme ned i en sådan højde, at landingsrunden kan sættes korrekt op. Brug evt. ”engelsk landingsrunde”."
                    },
                    {
                        "title": "Nøglepunkter",
                        "longdescription": "Hvor skal drej fra medvindsben til tværben ske, og hvor skal finalen påbegyndes. Ved sidevind – læg landingsrunden i læsiden af marken. Flyets næse vil så vende ind mod marken på medvindsbenet."
                    },
                    {
                        "title": "Check af motor og køling",
                        "longdescription": "Gennemgå procedure for evt. genstart hvis muligt."
                    },
                    {
                        "title": "Radioprocedure",
                        "longdescription": "Meddel hensigt til aktuel flyvekontrol."
                    },
                    {
                        "title": "Tværben",
                        "longdescription": "Vurder vinklen ned til marken. Er der behov for flaps eller sideglidning?"
                    },
                    {
                        "title": "Finale og landing",
                        "longdescription": "Landing må kun foregå på en flyveplads. Ellers skal øvelsen afbrydes i 500 ft. AGL. Planlæg sætning af flyet på første 1/3-del af marken. Giver plads til at rulle ud og få stoppet flyet."
                    },
                    {
                        "title": "Hvad skal piloten gøre efter en rigtig nødlanding?",
                        "longdescription": "Give besked til seneste flyvekontrol, kontakte markens ejer, ringe hjem til flyvepladsen, kontakte havariberedskab i tilfælde af uheld. En rigtig nødlanding skal som minimum rapporteres til SMS-systemet."
                    }
                ]
            },
            {
                "id": 21,
                "title": "V4: Sikkerhedslanding",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal lære at håndtere en situation, hvor piloten er nødt til at lande før han havde planlagt og et andet sted end den flyveplads piloten havde planlagt at lande på. En sikkerhedslanding kan ske både på en flyveplads eller på en egnet mark.<br><br>Eleven skal trænes i at udføre de procedurer, som gør at den uventede og ikke-planlagte landing bliver en sikker landing. Først og fremmest skal piloten kunne agere således, at der slet ikke opstår behov for en sikkerhedslanding.<br><br>Eleven skal lære at vurdere markens længde ved at flyve langs den på tid inden landingsrunden.<br><br><strong>Situationer hvor en sikkerhedslanding kan være aktuel:</strong><br>Faldende olietryk<br>Stigende olietemperatur<br>Brændstofmangel<br>For sen erkendelse af dårligt vejr uden mulighed for at vende om<br>Andet",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Beslutning om at sikkerhedslanding er nødvendig",
                        "longdescription": "Bedre tid og plads til at finde egnet mark/flyveplads."
                    },
                    {
                        "title": "Cockpitcheck og engelsk landingsrunde",
                        "longdescription": "Ikke skov, vand, by mm. – men f.eks. en øde landevej. Hvis tvivl – så afgiv il-melding (Pan-Pan)."
                    },
                    {
                        "title": "Vurder egnet område",
                        "longdescription": "Flag, vindmøller, røg, drivende skyer mm."
                    },
                    {
                        "title": "Markens længde",
                        "longdescription": "30 sek. med 120 km/t = Marken er 1000 meter lang."
                    },
                    {
                        "title": "Særlige forhold på jorden",
                        "longdescription": "Mennesker, kreaturer, trafik, bebyggelse."
                    },
                    {
                        "title": "Vælg mark + alternativ",
                        "longdescription": "Vælg bedste mark mod vinden + alternativ fra samme landingsrunde. Mulighed for at gå rundt, hvis indflyvning mislykkes."
                    },
                    {
                        "title": "Hold motor i tomgang i runden",
                        "longdescription": "Flyv landingsrunden som ved nødlanding med motor i tomgang."
                    },
                    {
                        "title": "Efter landing – er alt OK?",
                        "longdescription": "Er ombordværende og flyet OK? Skade på 3. mand?"
                    },
                    {
                        "title": "Kontakt seneste flyvekontrol",
                        "longdescription": "Pr. radio eller telefon – rapporter situationen."
                    },
                    {
                        "title": "Kontakt relevante personer",
                        "longdescription": "Rapporter situationen og aftal det videre forløb. Evt. politiet eller havarikommissionen direkte. Ved alvorlig personskade – ring 112."
                    },
                    {
                        "title": "Kontakt ejeren af landingsarealet",
                        "longdescription": "Forklar situationen."
                    }
                ]
            },
            {
                "id": 22,
                "title": "V5: Navigationsflyvning – planlægning",
                "longdescription": "<strong>Formål med øvelsen:</strong><br>Eleven gennemgår sammen med instruktøren den samlede planlægning af en navigationsflyvning. Planlægningen bruges til navigationsflyvning med instruktør i god sigtbarhed og god skybase.<br><br>Formålet med øvelsen er at lade eleven navigere efter flyvekort, som er forberedt inden flyvningen. Kortarbejdet er en væsentlig del af forberedelsen til navigationen, flyvning i kontrolleret luftrum og anflyvning af andre flyvepladser.<br><br>Øvelsen indebærer ikke aktuel flyvning – det sker på øvelse V6.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Valg af rute",
                        "longdescription": "Hensyn til navigation og kontrolleret luftrum. Bør ske via NorthAviMet pga. rekordering."
                    },
                    {
                        "title": "Indhentning af vejroplysninger",
                        "longdescription": "Benyt relevante kilder som Naviair’s Briefing-site."
                    },
                    {
                        "title": "Undersøgelse af NOTAM",
                        "longdescription": "Relevante NOTAM skal læses og forstås i relation til ruten."
                    },
                    {
                        "title": "Indtegning af ruten på ICAO-flyvekort",
                        "longdescription": "Markante punkter undervejs – hvad sigter vi efter: jernbaner, motorveje, kyster osv."
                    },
                    {
                        "title": "Orienteringslinjer og tidskontrol",
                        "longdescription": "”Speed-faktor” og tidtagning. Vigtige for at holde kurs og position."
                    },
                    {
                        "title": "Bestiknavigation eller terrestrisk navigation",
                        "longdescription": "Vurder hvilken metode der er mest hensigtsmæssig afhængigt af ruten og vejret."
                    },
                    {
                        "title": "Udfærdigelse af driftsflyveplan med frekvenser",
                        "longdescription": "Diverse programmer kan anvendes. Headings, tider, delruter, brændstofforbrug og beregning af start- og landingsstrækning."
                    },
                    {
                        "title": "Planlægge anflyvning til anden flyveplads",
                        "longdescription": "Brug VFG eller lignende – vær opmærksom på evt. regler for PPR."
                    },
                    {
                        "title": "Udfærdigelse af ATC-flyveplan",
                        "longdescription": "En af flyvningerne skal indeholde en ATC-flyveplan. Husk krav: min. 1000 fod over højeste hindring i radius af 600 m."
                    },
                    {
                        "title": "Har målflyvepladsen det, som UL-flyet kræver?",
                        "longdescription": "Banelængde, mulighed for tankning, er pladsen åben?"
                    },
                    {
                        "title": "Lukning af ATC-flyveplan",
                        "longdescription": "Lukkes den af flyvekontrollen, eller skal piloten selv lukke?"
                    }
                ]
            },
            {
                "id": 23,
                "title": "V6: Navigationsflyvning – Praktisk gennemførelse",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br>En af flyvningerne på denne øvelse bør indeholde landing på anden flyveplads med TWR- eller AFIS-tjeneste. Eleven skal undervejs kunne redegøre for egnede områder til en evt. nødlanding.<br><br>Denne øvelse kan – når eleven er moden til det – gentages som solonavigationsflyvning.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Organisering af cockpitarbejdet",
                        "longdescription": "Tingene skal ligge de rigtige steder og kortet foldet rigtigt."
                    },
                    {
                        "title": "Fastholdelse af højde og heading",
                        "longdescription": "+/- 150 fod i højden - +/- 5° på heading."
                    },
                    {
                        "title": "Revision af ETA og beslutninger herefter",
                        "longdescription": "Indflydelse på brændstof og/eller solnedgang?"
                    },
                    {
                        "title": "Korrektion af driftsflyveplan efter start",
                        "longdescription": "Korrigeres med aktuelt starttidspunkt."
                    },
                    {
                        "title": "Logning af flyvningen undervejs",
                        "longdescription": "Noter tidspunkter etc."
                    },
                    {
                        "title": "Indstilling af frekvenser under flyvning",
                        "longdescription": "Hav frekvensen på næste station klar som standby-frekvens."
                    },
                    {
                        "title": "Indstilling af transponder-koder",
                        "longdescription": "Iht. klarering etc. fra flyvekontrol m.fl."
                    },
                    {
                        "title": "Radioprocedurer undervejs",
                        "longdescription": "Radiokommunikation som planlagt, evt. ændringer vedr. ATC eller FIS."
                    },
                    {
                        "title": "Turene kan flyves med GPS",
                        "longdescription": "Brug af ”go-to-funktionen” på en GPS. Fejl på GPS simuleres, så brug af kort er nødvendig. Eleven skal prøve GPS ved mistet orientering."
                    },
                    {
                        "title": "Minimum vejrforhold for at fortsætte",
                        "longdescription": "Minimum fastsættes inden start."
                    },
                    {
                        "title": "Minimum vejr for at vende om",
                        "longdescription": "Beslutning før vejret forværres."
                    },
                    {
                        "title": "Flyvning i kontrolleret luftrum",
                        "longdescription": "Eleven skal kunne flyve ind i og ud af kontrolleret luftrum."
                    },
                    {
                        "title": "Høje luftfartshindringer undervejs",
                        "longdescription": "Ændringer ift. planlægningen skal håndteres."
                    },
                    {
                        "title": "Beslutninger undervejs",
                        "longdescription": "Kontinuerlig vurdering og tilpasning under flyvningen."
                    },
                    {
                        "title": "Procedure ved usikkerhed om position",
                        "longdescription": "Sidst kendte position, kort, radio evt. GPS."
                    },
                    {
                        "title": "Procedure ved mistet orientering",
                        "longdescription": "Hjælp via radio mv."
                    },
                    {
                        "title": "Ankomst til fremmed flyveplads",
                        "longdescription": "Evt. klarering og højdemålerindstilling. Undersøges så vidt muligt før afgang."
                    },
                    {
                        "title": "Trafikmønster og landingsrunde",
                        "longdescription": "Flyvning og placering ifølge lokal procedure."
                    },
                    {
                        "title": "Parkering og sikring af UL-flyet",
                        "longdescription": "UL-flyet parkeres sikkert og efter procedurer."
                    },
                    {
                        "title": "Afsluttende administrativt arbejde",
                        "longdescription": "Føring af logbog etc."
                    }
                ]
            },
            {
                "id": 24,
                "title": "V7: Navigationsflyvning i 1000 – 1500 ft.",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal under flyvning med instruktør lære at navigere i højder mellem 1000 og 1500 fod, fordi flyvning i denne højde kræver navigationspunkter med kortere indbyrdes afstand.<br><br>Deløvelserne svarer til øvelse V6, men foregår i lavere højde. Der skal i denne øvelse lægges særlig vægt på at kunne holde højden, samtidig med at man stiller frekvens, transponderkode eller arbejder med kortet, og i forhold til V6 skal flyvningen suppleres med øvelse i at vende om, inden man når ind i alt for dårligt vejr (kan simuleres).<br><br>Øvelsen kan omfatte en eller flere flyvninger efter behov, men der er ikke krav om landing på en anden flyveplads.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Procedure før beslutning om nedstigning",
                        "longdescription": "Terrænhøjde, luftfartshindringer, anden trafik?"
                    },
                    {
                        "title": "Relevante deløvelser fra V6",
                        "longdescription": "Ikke krav om landing på anden flyveplads."
                    },
                    {
                        "title": "Brug af kortet under flyvning",
                        "longdescription": "Højdeudsving max +/- 150 fod."
                    },
                    {
                        "title": "Indstilling af frekvenser under flyvning",
                        "longdescription": "Højdeudsving max +/- 150 fod."
                    },
                    {
                        "title": "Effekten af vind og turbulens",
                        "longdescription": "På kurs, højde og hastighed over jorden."
                    },
                    {
                        "title": "Vertikal bevidsthed",
                        "longdescription": "Faren for ubevidst at ramme terræn, der stiger etc."
                    },
                    {
                        "title": "Passage af høje master etc.",
                        "longdescription": "Luftfartshindringer skal passeres i tilstrækkelig afstand."
                    },
                    {
                        "title": "Passage af byer",
                        "longdescription": "Byer skal passeres i tilstrækkelig afstand."
                    },
                    {
                        "title": "Returnering pga. simuleret dårligt vejr",
                        "longdescription": "Vend 180°, så eleven kan genkende terrænet."
                    }
                ]
            },
            {
                "id": 25,
                "title": "V8: Radio- og GPS-navigation",
                "longdescription": "Skyhøjden større end 2000 fod AGL og sigtbarheden 5 km eller mere.<br><br><strong>Formål med øvelsen:</strong><br>Eleven skal under flyvning med instruktør lære at bruge de navigationshjælpemidler, som flyet er forsynet med – primært indhentning af pejling og anvendelse af GPS. Eleven skal desuden blive fortrolig med den hjælp, som kan hentes via radar og transponder.",
                "ul_class": "B",
                "norm_type": "lesson",
                "exercises": [
                    {
                        "title": "Brug af GPS",
                        "longdescription": "a. Valg af waypoints inden flyvning<br>b. Valg af waypoints under flyvning<br>c. Orientering efter GPS’en"
                    },
                    {
                        "title": "Brug af evt. VHF-pejler og øvrige radiomuligheder",
                        "longdescription": "a. Muligheder iht. VFG’en eller AIP’en?<br>b. Radioprocedurer og ATC-forbindelse<br>c. Indhentning af QDM-pejling"
                    },
                    {
                        "title": "Brug af radarhjælp",
                        "longdescription": "a. Muligheder iht. VFG’en eller AIP’en<br>b. Procedure og ATC-forbindelse<br>c. Pilotens ansvar<br>d. Primær og sekundær radar<br>  - Transpoder<br>  - Indtastning af kode<br>  - Opfangning af signal og svar<br>"
                    },
                ]
            },

            # SKILLTEST
            {
                "id": 26,
                "title": "PRE-FLIGHT OG START",
                "longdescription": "",
                "ul_class": "B",
                "norm_type": "skilltest",
                "exercises": [
                    {"title": "Pre-flight dokumentation, NOTAM, Vejr, Driftsflyveplan", "longdescription": "Skal redegøre for:<br>1. meteorologi<br>2. love og bestemmelser<br>3. dokumenter samt<br>4. driftsflyveplanen i forbindelse med gennemgang af navigationsflyvningen: TAF, METAR, CTR, TMA, FIZ, NOTAM m.v."},
                    {"title": "Vægt og Balance beregning", "longdescription": ""},
                    {"title": "Start og Landings beregning", "longdescription": ""},
                    {"title": "Brug af checkliste", "longdescription": ""},
                    {"title": "Taxi. Start (Take-off) procedure og briefing inkl. TEM", "longdescription": "Aspiranten skal briefe starten. Aspiranten skal beskrive forholdsregler ved motorstop under start TEM (TEM skal være en integreret del af hele flyvningen fra OFF Block til ON Block) "},
                    {"title": "Start og efter start checks", "longdescription": "Brug Vy fra POH:<br>1. Max. fart for flaps (hvid bue) må ikke overskrides "},
                    {"title": "Udflyvning I henhold til ICAO og pladsregulativ", "longdescription": ""},
                    {"title": "ATC radiokorrespondance. Blev instrukser og eller intentioner fulgt?", "longdescription": ""},
                ]
            },
            {
                "id": 27,
                "title": "ENROUTE",
                "longdescription": "<strong>(Hastighed +25 /- 10 km/t. Højde +/- 150 fod)</strong><br>Navigationsflyvning med udgangspunkt i den driftsflyveplan, som aspiranten har lavet. Turen kan afbrydes på første ben, hvis kontrollanten vurderer, at aspiranten lever op til kravene.<br>Flyvningen SKAL gå igennem kontrolleret luftrum TMA/CTR/FIZ.<br>1. Aspiranten skal kunne navigere jfr. driftsflyveplanen og finde vej ved hjælp af ICAOkort. (GPS og navigations software er <strong>IKKE</strong> tilladt)<br>2. Aspiranten skal kunne redegøre for det luftrum, som turen går igennem og kunne korrespondere med ATC/FIZ i området<br>3. Aspiranten skal kunne efterleve de instruktioner, som gives af ATC/FIZ.",
                "ul_class": "B",
                "norm_type": "skilltest",
                "exercises": [
                    {"title": "Driftsflyveplan. Kortlæsning.", "longdescription": ""},
                    {"title": "Holdes højde, kurs og hastighed.", "longdescription": ""},
                    {"title": "Orientering, Luftrums struktur, timing og revidering af ETAs, føring af driftsflyveplan", "longdescription": ""},
                    {"title": "Brug af alternativ plads. Planlægning og implementering", "longdescription": ""},
                    {"title": "Positions check. Brændstof check. Brug af karburator forvarme og brændstofsystem ", "longdescription": ""},
                    {"title": "ATC radiokorrespondence. Blev ATC klarering indhentet?", "longdescription": ""},

                ]
            },
            {
                "id": 28,
                "title": "GENEREL AIRWORK",
                "longdescription": "<strong>(Hastighed +25 /- 10 km/t. Højde +/- 150 fod)</strong><br>Navigationsflyvning med udgangspunkt i den driftsflyveplan, som aspiranten har lavet. Turen kan afbrydes på første ben, hvis kontrollanten vurderer, at aspiranten lever op til kravene.<br>Flyvningen SKAL gå igennem kontrolleret luftrum TMA/CTR/FIZ.<br>1. Aspiranten skal kunne navigere jfr. driftsflyveplanen og finde vej ved hjælp af ICAOkort. (GPS og navigations software er <strong>IKKE</strong> tilladt)<br>2. Aspiranten skal kunne redegøre for det luftrum, som turen går igennem og kunne korrespondere med ATC/FIZ i området<br>3. Aspiranten skal kunne efterleve de instruktioner, som gives af ATC/FIZ.",
                "ul_class": "B",
                "norm_type": "skilltest",
                "exercises": [
                    {"title": "Stigning til 3.000 fod AGL", "longdescription": "1. bedste stigehastighed Vy<br>2. drej under stigning<br>3. udfladning til vandret flyvning"},
                    {"title": "Drej med krængning på 30° (holdes der udkig)", "longdescription": "1. Max. 10° afvigelse fra kursen for overgang fra højre drej til venstre drej<br>2. Max. 10° afvigelse fra udretningskursen<br>3. Hastigheds- og højdeafvigelse jf. Skilltest formular<br>4. Krængning må højst afvige +/- 5°"},
                    {"title": "Flyvning ved kritisk lav hastighed m/u flaps", "longdescription": ""},
                    {"title": "StalL", "longdescription": "(slut højde større end 2.500 fod AGL)<br>1. indgang til stall flap 0<br>2. indgang til stall under nedstigning og drej med krængning på 20°<br>3. indgang til stall i landingskonfiguration<br><br><strong>Krav til udførelse</strong><br>1. Flyets næse skal sænkes til under horisonten, inden der gives gas<br>2. Flyets fartmåler skal være i det grønne område inden der gives gas (når der gives gas skal det ske jævnt og ikke pludseligt)<br>3. Aspiranten skal kunne anvende procedure for udretning fra stall i drej, hvis flyet taber en vinge. Procedure: modsat sideror, pinden lidt frem, ret herefter ud og først nu må der gives gas skal beherskes. Hvis aspiranten forsøger udretning ved at give gas, er han dumpet"},
                    {"title": "Opretning fra unormal flyvestilling", "longdescription": "Aspiranten gives en opgave, eksempelvis beregning af distance til alternativ plads eller punkt på kortet. Kontrollanten overtager flyvningen og bringer på gunstigt tidspunkt flyet ind i en unormal flyvestilling, hvorefter han siger ”du har” Aspiranten skal herefter bringe flyet tilbage til vandret flyvning, holde hastigheden og sætte kursen tilbage på track."},
                    {"title": "ATC radiokorrespondence.", "longdescription": ""},
                ]
            },
            {
                "id": 29,
                "title": "NØDPROCEDURER",
                "longdescription": "<strong>(Hastighed +25 /- 10 km/t. Højde +/- 150 fod)</strong><br>1. Aspiranten skal kunne gennemføre nødprocedure for at få motoren i gang igen. Ved motor brand benytte den korrekt nødprocedure<br>2. Aspiranten skal kunne orientere pågældende ATC om situationen uden at lave et egentligt opkald.<br>3. Aspiranten skal kunne vælge en egnet mark<br>4. Landingsrunden skal sættes op i læsiden (hvis tiden tillader)<br>5. Kontrollanten skal kunne vurdere, at flyet ville blive sat i første tredjedel af marken.",
                "ul_class": "B",
                "norm_type": "skilltest",
                "exercises": [
                    {"title": "Simuleret motorstop efter start (Hvis forholdene tillader det. Skal minimum være en del af TEM)", "longdescription": ""},
                    {"title": "Simuleret motor brand en-route (fra højde større end 2.000 fod AGL)", "longdescription": ""},
                    {"title": "Nød landingsplads realistisk (landing sikker?)", "longdescription": ""},
                    {"title": "Stigning til 1.500 fod AGL. Motorstop i 1.000 AGL", "longdescription": ""},
                    {"title": "Nød landingsplads realistisk (landing sikker?) ", "longdescription": ""},
                    {"title": "Brug af checkliste ", "longdescription": ""},
                    {"title": "Mundtlige spørgsmål (eks. Procedure ved åben dør eller canopy efter start)", "longdescription": ""},
                ]
            },
            {
                "id": 30,
                "title": "ANFLYVNING OG LANDING",
                "longdescription": "Der skal samlet udføres minimum 3 landinger under Skilltesten.<br>Hvis simuleret nødlanding udføres til fuld landing (eventuel på fremmed plads), tæller denne med i de 3 landinger. ",
                "ul_class": "B",
                "norm_type": "skilltest",
                "exercises": [
                    {"title": "Korrekt anflyvning af plads jf. ICAO og pladsregulativ. Holdes der udkig? (Hastighed +25/- 10 km/t.)", "longdescription": "1. Landingsrunden skal placeres således, at aspiranten har overblik over pladsen og samtidig sådan, at denne kan glide flyet ind, hvis motoren skulle gå i stå<br>2. Hastigheder for udsætning af flaps skal overholdes (hvid bue) "},
                    {"title": "Overskydning fra lav højde (200 fod AGL)", "longdescription": ""},
                    {"title": "Ny landingsrunde. Følges proceduren og lokale restriktioner overholdes (miljø)", "longdescription": ""},
                    {"title": "Præcisions landing (50 x 25 m)", "longdescription": "1. Flyet skal sættes inden for 25 x 50 meter<br>2. Indflyvningshastighed jf. POH/AFM skal overholdes<br>3. Korrekt indflyvningshastighed jf. POH/AFM korrigeret for vind skal overholdes + 1/3 vindhastighed<br>4. Korrekt udfladning "},
                    {"title": "Touch-and-Go ", "longdescription": ""},
                    {"title": "Landing (hvis sidevind og forholdene tillader, så landing u/flaps)", "longdescription": "1. Flyet skal sættes på den første tredjedel af flyvepladsen<br>2. Indflyvningshastighed jf. POH/AFM skal overholdes<br>3. Korrekt indflyvningshastighed jf. POH/AFM korrigeret for vind skal overholdes + 1/3 vindhastighed<br>4. Korrekt udfladning "},
                    {"title": "Efter landing. Exit af bane i brug. Taxi", "longdescription": ""},
                    {"title": "Brug af TEM", "longdescription": ""},
                    {"title": "Brug af checkliste", "longdescription": ""},
                    {"title": "Radiokorrespondance", "longdescription": ""},
                ]
            },

            # PFT
            {
                "id": 31,
                "title": "PRE-FLIGHT OG START",
                "longdescription": "",
                "ul_class": "B",
                "norm_type": "pft",
                "exercises": [
                    {"title": "Pre-flight dokumentation (inkl. Medical, Certifikat)", "longdescription": ""},
                    {"title": "Vægt og Balance beregning", "longdescription": ""},
                    {"title": "Start og Landings beregning (50/70 reglen)", "longdescription": ""},
                    {"title": "Brug af checkliste", "longdescription": ""},
                    {"title": "Briefing inkl. TEM (Threat and Error Management). Start procedure inkl. afbrudt start.", "longdescription": ""},
                    {"title": "Start inkl. afbrudt start og efter start checks jf. checkliste.", "longdescription": ""},
                    {"title": "Udflyvning I henhold til ICAO / lokale regler.", "longdescription": ""}
                ]
            },
            {
                "id": 32,
                "title": "GENEREL AIRWORK",
                "longdescription": "<strong>(Hastighed max. +25/-10 km/t. Højde +/- 150 fod)</strong>",
                "ul_class": "B",
                "norm_type": "pft",
                "exercises": [
                    {
                        "title": "Stigning til 3.000 fod AGL",
                        "longdescription": "1. bedste stigehastighed<br>2. drej under stigning<br>3. udfladning til vandret flyvning med korrekt hastighed"
                    },
                    {"title": "Drej 30° krængning", "longdescription": ""},
                    {"title": "Flyvning ved kritisk lav hastighed m/u flaps", "longdescription": ""},
                    {
                        "title": "Stall ",
                        "longdescription": "Højde større end 2.500 fod AGL<br>1. indgang til stall flap 0<br>2. indgang til stall under nedstigning og drej med 20° krængning<br>3. indgang til stall i landingskonfiguration"
                    },
                    {"title": "Opretning fra unormal flyvestilling", "longdescription": ""}
                ]
            },
            {
                "id": 33,
                "title": "NØD PROCEDURE",
                "longdescription": "<strong>(Hastighed max. +25/-10 km/t. Højde +/- 150 fod)</strong>",
                "ul_class": "B",
                "norm_type": "pft",
                "exercises": [
                    {"title": "Simuleret motorbrand (fra højde ≥ 2.000 fod AGL)", "longdescription": ""},
                    {"title": "Nød landingsplads realistisk (landing sikker?)", "longdescription": ""},
                    {"title": "Stigning til 1.500 fod AGL. Motorstop i 1.000 AGL", "longdescription": ""},
                    {"title": "Nød landingsplads realistisk (landing sikker?)", "longdescription": ""},
                    {"title": "Stigning til 1.500 fod AGL", "longdescription": ""},
                    {"title": "Brug af nød checkliste (hvis tiden tillader det)", "longdescription": ""}
                ]
            },
            {
                "id": 34,
                "title": "ANFLYVNING OG LANDING",
                "longdescription": "<strong>(Hastighed max. +25/-10 km/t. Højde +/- 150 fod)</strong>",
                "ul_class": "B",
                "norm_type": "pft",
                "exercises": [
                    {"title": "Korrekt anflyvning af plads jf. ICAO og lokale regler", "longdescription": ""},
                    {"title": "Overskydning fra lav højde (200 fod AGL)", "longdescription": ""},
                    {"title": "Ny landingsrunde og landing u/flaps (Touch-and-Go) (Ldg. 25x50m)", "longdescription": ""},
                    {"title": "Landingsrunde med glidelanding", "longdescription": ""},
                    {"title": "Brug af checkliste", "longdescription": ""}
                ]
            },
            {
                "id": 35,
                "title": "RADIOKOMMUNIKATION",
                "longdescription": "",
                "ul_class": "B",
                "norm_type": "pft",
                "exercises": [
                    {"title": "Blev klareringer, instruktioner fulgt?", "longdescription": ""},
                ]
            }
        ]

        for norm_data in norms_data:
            norm, created = Norm.objects.update_or_create(
                title=norm_data["title"],
                norm_type=norm_data["norm_type"],  # Add this to disambiguate
                defaults={
                    "id": norm_data["id"],
                    "longdescription": norm_data["longdescription"],
                    "ul_class": norm_data["ul_class"],
                }
            )
            self.stdout.write(self.style.SUCCESS(
                f"{'Created' if created else 'Updated'} norm: {norm.title}"
            ))

            for index, ex_data in enumerate(norm_data["exercises"]):
                exercise, ex_created = Exercise.objects.update_or_create(
                    norm=norm,
                    title=ex_data["title"],
                    defaults={
                        "longdescription": ex_data["longdescription"],
                        "order": index
                    }
                )
                self.stdout.write(f"  {'Created' if ex_created else 'Updated'} exercise: {exercise.title}")
