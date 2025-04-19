# 📊 Stav projektu Lexi – kamarád zvířátek

Poslední aktualizace: *duben 2025*

## 🧱 Struktura projektu

- `chat_backend.py` – hlavní orchestrátor konverzace
- `agent_tools/profile_tools.py` – zpracování profilu dítěte (jméno, věk, oblíbené zvíře)
- `agent_tools/animal_utils.py` – práce se zvířaty, informace, obrázky
- `tools.py`, `tools_api.py` – podpůrné funkce a jednoduché API pro agenty
- `app.py` – hlavní frontend přes Gradio

## 🧠 Funkčnost

- GPT se ptá na jméno, věk a oblíbené zvíře dítěte (4–10 let)
- Odpovědi jsou zpracovány přes OpenAI function calling
- Zobrazují se obrázky zvířat podle tématu (dle `zvirata.json`)
- Proběhl refactoring do modulární podoby
- Detekce aktivního zvířete funguje přes GPT s pamětí

## 🎨 Vizualizace

- Zobrazení obrázků v pravé části aplikace
- Plán: Ken Burns efekt, hot-swap videa/GIFy (Pexels, Giphy)
- Bude rozšířeno o plynulé přechody a animace při změně tématu

## 🚀 Deployment a prostředí

- `.env` obsahuje OpenAI klíče (API + Assistant ID)
- Projekt běží lokálně (Gradio + Uvicorn)
- Plán: připravit deploy na HuggingFace / Railway
- Verzováno přes GitHub: [repozitář AILessons](https://github.com/Casual159/AILessons)

## 🛠 Agenti

- `dev_assistant_agent.py` – sleduje stav projektu, generuje návrhy
- `assistant_cli.py` – rozhraní pro kontrolu a interakci přes terminál

## ✅ ToDo / Roadmap

- [ ] Dokončit refactoring (ověřit `profile_tools` + `animal_utils`)
- [ ] Přidat základní testy (`test_smoke.py`)
- [ ] Vytvořit projektový soubor `context_notes.md` pro trvalý kontext
- [ ] Vylepšit vizuální efekty (Ken Burns, videa)
- [ ] Nasadit na veřejné prostředí (HF / Railway)

---
*Tento soubor může být udržován ručně nebo aktualizován pomocí agenta.*
