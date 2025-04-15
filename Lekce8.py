import os
from openai import OpenAI
from dotenv import load_dotenv

# Načtení proměnných z .env souboru
load_dotenv()

# Získání API klíče z prostředí
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Vstupní text – prozatím přímo v kódu
input_text = """
# Pivo - Zlatavý odkaz lidské civilizace z českého pohledu

Pivo, tento zlatavý mok, který je nedílnou součástí české kultury a identity, má za sebou fascinující cestu trvající tisíce let. Nápoj, který Češi milují a který nás proslavil po celém světě, se zrodil dávno před vznikem našeho národa, ale právě v českých zemích dosáhl jedné ze svých nejušlechtilejších podob. Následující řádky vás provedou bohatou historií piva od jeho dávných počátků až po současnost, technologií výroby i jeho významu pro českou kulturu.

## Historie piva ve světě - od prvních kapek ke kulturnímu fenoménu

### Nejstarší doklady a první civilizace

Výroba piva je stará jako historie civilizovaného lidstva. Jedná se o jeden z nejstarších lidmi vyrobených kvašených nápojů, stejně jako medovina a datlové víno[1]. Podle současných archeologických nálezů ve starověké Mezopotámii znali výrobu piva již předsumerští obyvatelé Sumeru před více než 4000 lety, přičemž dokonce byly v Izraeli nalezeny znaky vaření piva staré až 13000 let[1]. 

Existuje několik teorií o tom, jak lidé objevili pivo. Nejpravděpodobnější je, že k tomu došlo náhodou při skladování obilí v hliněných nádobách, kdy do některých nádob natekla voda a došlo ke kvašení[4]. Po tomto náhodném objevu se vždy našel nějaký odvážlivec, který nápoj ochutnal a zjistil jeho opojné účinky[6].

Sumerové nazývali své pivo "kaš" a vyráběli ho z namočeného ječného chleba a sladu, které byly společně umístěny do velikého džbánu, ve kterém docházelo ke kvašení[4]. Je zajímavé, že znali celou řadu piv různých vlastností - piva silná i slabá, filtrovaná i nefiltrovaná, osm druhů vařili z ječmene, osm z pšenice a tři byly míchané[3]. To svědčí o vyspělé pivovarské kultuře, která v mnohém předčila i některé moderní pivovarské tradice.

### Starověký Egypt a další civilizace

Další významné doklady o výrobě piva pocházejí ze starověkého Egypta, který byl spolu s Mezopotámií považován za kolébku piva. První doklady o pivu v Egyptě pocházejí z období kolem roku 3000 př. n. l., kdy byly stopy piva zjištěny v nádobách první a druhé dynastie[3]. Egypťané používali pro výrobu piva ječmen, ze kterého vyráběli slad, a různé typy pšenice[4]. 

Pivo bylo v Egyptě považováno za dar boha Re a bylo nedílnou součástí každodenního života i náboženských rituálů[1]. Stalo se také významným obchodním artiklem oblíbeným v celém Středomoří a přinášelo královské pokladně nezanedbatelné zisky. Později se stalo dokonce samostatným státním oborem a stát monopolním výrobcem[3].

### Antika a středověk - rozšíření po Evropě

V době antiky stálo pivo spíše na okraji zájmu, jelikož konzumaci v oblasti Středomoří jasně dominovalo víno. Staří Řekové pivo téměř nepili a mezi Římany bylo oblíbeno pouze u vojáků, zvláště v pohraničních oblastech, kde byl nedostatek vína[4]. 

Oproti tomu v severních částech Evropy bylo pivo mnohem populárnější. Germánské kmeny preferovaly výrobu a konzumaci piva před jinými alkoholickými nápoji[1]. Římský historik Publius Cornelius Tacitus (55-120) píše o Germánech:

"… polehávajíce na medvědích kožešinách nestřídmě holdují strašnému nápoji vyrobenému z ječmene či pšenice, velmi nepodobnému ušlechtilému vínu… a tento ohavný nápoj pijí až do němoty z velkých tuřích rohů."[1]

Keltové, žijící na britských ostrovech, vyráběli kvašený nápoj z obilí, který ochucovali medem[1]. Vikingové v severní Evropě pili pivo teplé a vynalezli metodu vymrazování piva, během které pivo zmrzlo, což vedlo k nárůstu obsahu alkoholu[4].

Galové vyráběli pivo z ječmene nebo pšenice a nejspíše jako první na světě ho čepovali ze sudů. V prvním století před n. l. seznámili se svým pivem, které nazývali "korma", také Římany[1].

## Historie piva v českých zemích - od prvních várků po pivní velmoc

### Nejstarší doklady a příchod Slovanů

První zmínky o vaření piva na území dnešní České republiky pocházejí ze čtvrtého století před n. l. Předpokládá se, že v té době přišel do střední Evropy keltský kmen Bójů ze severní Itálie a přinesl s sebou znalost vaření piva[1]. 

Od třetího století našeho letopočtu přicházeli na území dnešní České republiky Slované z východu. Ti s sebou přinesli znalost výroby piva z ječmene, pšenice a ovsa včetně chmelení[1]. Tím položili základ české pivovarské tradici, která se postupně rozvíjela a zdokonalovala.

### Rozvoj ve středověku - cechy a privilegia

Velký význam pro rozvoj pivovarství a kvalitu piva měly v českých zemích sladovnické cechy. Určovaly, kolik piva a z jakého množství sladu smí jeden dům vyrobit, kontrolovaly jeho kvalitu a na rozdíl od okolních zemí dohlížely i na to, aby pivo vařil jen ten, kdo se v tom oboru řádně vyučil. Proto byla česká piva již ve středověku velmi kvalitní a v hojné míře se vyvážela do okolních zemí i na dvory jiných panovníků[4].

Z technologického hlediska byla výroba v raném středověku poměrně primitivní. Jak uvádí svatovítský spis z let 1380-1400, pivo se vařilo ze sladového ječmene nebo pšenice. Vše se vyrábělo v kuchyni ve varných hrncích. Kvašení probíhalo také v hrncích a ty byly uloženy v pivních komorách[5].

Vařila se piva bílá, většinou s pšenicí, a piva ječná zvaná červená, obě svrchním kvašením. Města královská pokládala vaření piva za svou živnost a výsadu. Šlechta a rytíři původně vaření piva odmítali jako činnost poškozující čest jejich erbů. Když však začali pivo vařit a šenkovat, cítila se města poškozena. Vznikl spor, který trval 33 roků (1484–1517) a řešilo ho bez úspěchu 33 zemských sněmů[5].

### Průmyslová revoluce a modernizace

Zpočátku se pivo vyrábělo podomácku, což následně vystřídala řemeslná výroba, která přetrvala až do poloviny 19. století. Sladovny a pivovary byly stavěny blízko vodních zdrojů, neboť při výrobě piva se spotřebuje velké množství vody[7].

Procesem industrializace prošlo pivovarnictví v 19. století, kdy došlo k rozvoji průmyslové výroby. To umožnilo masovou produkci piva a jeho širší dostupnost pro běžné obyvatelstvo.

## Technologie a chemie výroby piva

### Základní suroviny a procesy

V základu se pivo vyrábí z vody, sladu (naklíčené a usušené obilí, nejčastěji ječmen), chmele a kvasinek. Výrobní proces se skládá z několika klíčových kroků.

Nejprve se slad šrotuje (rozemele) a smísí se s vodou. V této směsi se za zvyšující se teploty vlivem enzymů štěpí v zrně obsažené složky[4]. Vytváří se tzv. sladina, která se následně vaří s chmelem, který dodává pivu charakteristickou hořkost a aroma.

Historicky se sladová drť polévala horkou vodou a promíchala. Pak byl rmut povařen v kotli a přes síto (kadečku s dírkovaným dnem vyloženým slámou) se cedil. Čistá sladina byla opět povařena s chmelem a nalita na troky[5].

Po vychladnutí se do mladiny přidávaly kvasnice a mladé pivo bylo naplněno do beček a necháno vykvasit ("až se kvasnice vypotily")[5]. Takto vznikalo pivo ve středověku a s různými vylepšeními se tento postup používá dodnes.

### Historické metody vs. moderní postupy

Starověká piva se výrazně lišila od těch dnešních. Sumerské pivo kaš bylo na rozdíl od současného piva připravováno bez chmele, který v té době ještě nebyl znám. Bez přítomnosti chmele kaš nezískával hořkou chuť a pro její dodání se muselo využívat jiného postupu. Většinou se využívalo pražení chleba v horkém popelu či přidávání zelené hořčice či sezamových semínek[4].

Tehdejší pivo nepodstupovalo proces filtrace, což mělo za následek přítomnost velkého množství mechanických částic a to, že pivo nebylo čiré. Z tohoto důvodu se pro pití využívalo obilné stéblo, které fungovalo jako slámka[4].

Chmel se začal používat k dochucování piva mnohem později. Pěstoval se v západní Evropě od 8.-9. století, u Slovanů od 11. století, zobecněl však až v pozdním středověku[3].

## Typy piv a jejich původ

### Svrchně a spodně kvašená piva

Historicky se piva rozdělovala na bílá (pšeničná) a červená (ječná), obě vyráběná svrchním kvašením[5]. Převratnou změnou bylo objevení spodního kvašení, které se stalo základem pro výrobu českého ležáku - piva plzeňského typu.

České pivo je charakteristické používáním spodního kvašení při nižších teplotách, což vytváří čisté a harmonické chutě. Tento výrobní postup se z Čech rozšířil do celého světa.

### Nejznámější české pivo - plzeňský ležák

Plzeňský ležák, který změnil světové pivovarnictví, vznikl v Plzni v roce 1842. Jeho charakteristickými vlastnostmi jsou zlatavá barva, harmonická hořkost, plné tělo a bohatá pěna. Díky měkké plzeňské vodě, kvalitnímu moravskému sladu, žateckému chmelu a spodnímu kvašení vyniká svou vyrovnanou chutí.

## Zdravotní přínosy a rizika konzumace piva

### Příznivé účinky umírněné konzumace

Pivo obsahuje řadu prospěšných látek - vitamíny skupiny B, polyfenoly, minerály a antioxidanty. Umírněná konzumace může mít kardioprotektivní účinky, podporovat trávení a fungovat jako prevence některých civilizačních onemocnění.

Již ve středověku bylo pivo považováno za zdravý nápoj a nabízelo se i dětem, nejspíše proto, že v tehdejších hygienických podmínkách bylo pivo, vařené s chmelem, zdravější než voda z některých zdrojů[1].

### Rizika nadměrné konzumace

Nadměrná konzumace piva vede k řadě zdravotních problémů - od obezity přes poškození jater až po riziko závislosti. Alkohol obsažený v pivu může při dlouhodobé nadměrné konzumaci poškodit prakticky všechny orgánové systémy.

## Významné osobnosti spojené s pivem

### Ve světě

Důležitou postavou v historii výzkumu piva byl český orientalista Bedřich Hrozný, který jako první na světě v roce 1913 rozluštil chetitské písmo a ve své knize "Obilí ve staré Babylonii" uvedl, že staré národy Sumerů a Babyloňanů nejen že znaly postup výroby piva a sladu, ale na svých tabulkách uváděly i prastaré recepty na různé druhy piv[1].

### V českých zemích

K rozvoji českého pivovarnictví přispěla řada osobností, od středověkých sládků po průmyslníky 19. století, kteří modernizovali výrobu a přispěli k vysoké kvalitě českého piva.

## Česká pivní kultura v současnosti

Česká republika drží primát nikoli ve výrobě piva, kde jsme klesli na sedmnácté místo ve světě, ale ve spotřebě piva na osobu a rok – asi 160 litrů[1]. To svědčí o hlubokém zakořenění piva v české kultuře.

V České republice dnes najdeme stovky pivovarů od velkých průmyslových podniků po malé řemeslné minipivovary. Česká pivní kultura je natolik významná, že byla v roce 2008 zapsána na seznam nehmotného kulturního dědictví UNESCO.

## Závěr - Pivo jako součást české identity

Pivo není jen nápojem, ale součástí české kulturní identity. Prošlo vývojem od primitivních postupů až po sofistikovanou průmyslovou výrobu, od rituálního nápoje k běžné součásti společenského života. Česká pivní kultura je unikátním fenoménem, který spojuje historickou tradici s moderní gastronomií a představuje jeden z našich nejvýznamnějších příspěvků světové kultuře.

Zlatavý mok vyráběný a konzumovaný již tisíce let zůstává symbolem pohostinnosti, společenského života a národní hrdosti. Pivo bylo, je a zůstane nedílnou součástí české kultury a identity, odkazem našich předků, který stále žije a vyvíjí se.

Citations:
[1] https://cs.wikipedia.org/wiki/Historie_piva
[2] https://statistikaamy.csu.gov.cz/historie-piva-je-poutavym-pribehem
[3] https://beerweb.cz/o-pivu/historie-piva
[4] https://cs.wikipedia.org/wiki/Pivo
[5] https://beerweb.cz/o-pivu/historie-piva-v-cechach
[6] https://www.alkoholium.cz/historie-piva-strucne-jasne-prehledne/
[7] https://is.muni.cz/th/w7r50/Pivovarnictvi_2.poloviny_19.stoleti_a_pocatku_20.stoleti_na_prikladu_Rolnickeho_akcioveho_pivovaru_se_sladovno.pdf
[8] http://www.romicus.cz/spqr/articles/rim_a_pivo_2.html
[9] https://archiv.hn.cz/c1-21049340-nejstarsi-kulturni-napoj-lidstva
[10] https://www.nepijubrecky.cz/tak-chutna-stredovek-lucky-bastard-uvaril-starodavne-pivo/

"""

# Funkce pro získání nadpisu a shrnutí textu
def get_title_and_summary(client, text):
    prompt = f"""
Na základě následujícího textu vygeneruj:

1. Nadpis (maximálně 1 věta). Zde se hlavně řiď zvýrazněním a značkováním textu hvězdičkami. Nadpis neinterpretuj.
2. Shrnutí textu (5-6 vět). Zde chci tvoji interpretaci. Snaž se ji držet spíše kratší.

Text:
{text}
"""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Funkce pro extrakci historických a kulturních entit ve formátu YAML
def extract_entities_yaml(client, text):
    prompt = f"""
    Z textu níže vytáhni a vypiš ve formátu YAML všechny významné historické a kulturní entity (např. osoby, národy, oblasti, období, techniky, pojmy, vynálezy, pivovary, události).

    Text:
    {text}
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Funkce pro generování kvízových otázek typu A–D na základě textu
def generate_quiz(client, text):
    prompt = f"""
    Na základě textu níže vytvoř 5 kvízových otázek typu A, B, C, D. Uveď správnou odpověď a vysvětlení, proč je správná - zde uveď název "kapitoly", která o tématu referuje.

    Text:
    {text}
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Funkce pro vytvoření osnovy prezentace (slidy s hlavním obsahem)
def create_presentation_structure(client, text):
    prompt = f"""
    Vytvoř osnovu prezentace (na 5 slidů) na základě vstupníhojícího textu. Každý slid popiš 1 větou, co bude hlavním obsahem. Důležité je, aby z popisu bylo jasný obsah a jak se liší od jiných slidů.

    Text:
    {text}
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Funkce pro vygenerování otevřené otázky k diskuzi
def ask_follow_up_question(client, text):
    prompt = f"""
    Navrhni 1 zajímavou a otevřenou otázku k diskuzi, která logicky navazuje na text níže.

    Text:
    {text}
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


 
# Hlavní běh programu – nabídka funkcí v menu
if __name__ == "__main__":
    while True:
        print("\nZvol akci:")
        print("1 - Nadpis a shrnutí")
        print("2 - YAML entity")
        print("3 - Kvízové otázky")
        print("4 - Osnova prezentace")
        print("5 - Otázka k diskuzi")
        print("0 - Konec")
        volba = input("Tvoje volba: ")

        if volba == "1":
            print("\n--- Nadpis a shrnutí ---")
            print(get_title_and_summary(client, input_text))
        elif volba == "2":
            print("\n--- YAML pojmy ---")
            print(extract_entities_yaml(client, input_text))
        elif volba == "3":
            print("\n--- Kvíz ---")
            print(generate_quiz(client, input_text))
        elif volba == "4":
            print("\n--- Osnova prezentace ---")
            print(create_presentation_structure(client, input_text))
        elif volba == "5":
            print("\n--- Otázka k diskuzi ---")
            print(ask_follow_up_question(client, input_text))
        elif volba == "0":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkus to znovu.")