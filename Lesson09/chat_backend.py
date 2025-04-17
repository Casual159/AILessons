import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import json

# Načti lookup tabulku z Excelu (jen jednou při spuštění)
# xlsx_path = "Katalog zvířátek.xlsx"  # nebo absolutní cesta
# df = pd.read_excel(xlsx_path)
# lookup_df = df[["title", "image_src"]].dropna()
# animal_lookup = dict(zip(lookup_df["title"].str.lower(), lookup_df["image_src"]))
with open("zvirata.json", "r", encoding="utf-8") as f:
    animal_data = json.load(f)

### --- PROFIL GPT START ---
session_profile = {}

last_animal = {"zvíře": None}

functions = [
    {
        "name": "uloz_profil",
        "description": "Získá jméno, věk a oblíbené zvíře od dítěte.",
        "parameters": {
            "type": "object",
            "properties": {
                "jméno": {"type": "string", "description": "Jméno dítěte"},
                "věk": {"type": "integer", "description": "Věk dítěte"},
                "zvíře": {"type": "string", "description": "Oblíbené zvíře"},
            },
            "required": []
        }
    },
    {
        "name": "uloz_zvire_tema",
        "description": "Určí zvíře, které je hlavním tématem věty nebo otázky dítěte.",
        "parameters": {
            "type": "object",
            "properties": {
                "zvíře": {
                    "type": "string",
                    "description": "Zvíře, o kterém dítě mluví (přesně dle katalogu Zoo Praha)"
                }
            },
            "required": ["zvíře"]
        }
    }
]

def extract_profile_via_gpt(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4-0613",
            messages=[{"role": "user", "content": user_input}],
            functions=functions,
            function_call={"name": "uloz_profil"}
        )
        arguments = response.choices[0].message.function_call.arguments
        data = json.loads(arguments)
        session_profile.update(data)
        print("🎯 GPT PROFIL:", session_profile)
    except Exception as e:
        print("⚠️ Nepodařilo se extrahovat profil:", e)
### --- PROFIL GPT END ---

load_dotenv()

client = OpenAI()
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

thread = client.beta.threads.create()
### --- GPT ZVÍŘE FUNCTION START ---
def extract_animal_topic(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4-0613",
            messages=[{"role": "user", "content": user_input}],
            functions=functions,
            tool_choice="auto"  # 🔄 GPT rozhoduje, kdy funkci volat
        )

        message = response.choices[0].message

        if hasattr(message, "function_call") and message.function_call:
            arguments = message.function_call.arguments
            data = json.loads(arguments)
            zvire = data.get("zvíře")
            print("🦁 GPT ZVÍŘE (auto):", zvire)
            return zvire

        # 🔁 fallback – použij zvíře z profilu
        print("🦁 GPT ZVÍŘE: žádné nové → používám profilové:", session_profile.get("zvíře"))
        return session_profile.get("zvíře")

    except Exception as e:
        print("⚠️ Nepodařilo se extrahovat zvíře:", e)
        return session_profile.get("zvíře")
### --- GPT ZVÍŘE FUNCTION END ---

### --- ZVÍŘECÍ OBRÁZKY START ---
def get_animal_image(zvire_nazev):
    info = get_animal_info(zvire_nazev)
    return info["image"] if info else None

def get_animal_info(zvire_nazev):
    """
    Vrátí dict s klíči 'image' a 'popis' pro dané zvíře.
    Pokud nenajde přesně, zkusí částečné shody.
    """
    if not zvire_nazev:
        return None
    zvire_nazev = zvire_nazev.lower()

    # 1. Přesná shoda
    if zvire_nazev in animal_data:
        return animal_data[zvire_nazev]

    # 2. Částečná shoda (např. 'slon' → 'slon africký')
    for klic in animal_data.keys():
        if zvire_nazev in klic:
            return animal_data[klic]

    return None
### --- ZVÍŘECÍ OBRÁZKY END ---

def send_message(user_input):
    ### --- PROFIL GPT START ---
    extract_profile_via_gpt(user_input)
    ### --- PROFIL GPT END ---

    # Přidej zprávu od uživatele do threadu
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Spusť asistenta
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )

    # Počkej na odpověď
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_status.status == "completed":
            break

    # Získej odpověď
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    last_message = messages.data[0].content[0].text.value
    return last_message