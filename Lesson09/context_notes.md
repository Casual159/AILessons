

 # 🧠 Kontextové poznámky k projektu Lexi – kamarád zvířátek
 
 ## ✅ Refactoring (stav k 18. 4. 2025)
 - Backend je rozdělen do modulů:
   - `chat_backend.py` – orchestrátor a rozhraní pro Gradio
   - `agent_tools/profile_tools.py` – profil dítěte (jméno, věk, zvíře)
   - `agent_tools/animal_utils.py` – práce se zvířaty (info, obrázky)
 - Všechny importy ošetřeny, moduly se úspěšně načítají.
 
 ## 🔁 Nedokončené body
 - 💡 Zavedení testů: smoke testy připraveny, ale nejsou doplněny do projektu.
 - 🧪 Funkce `get_animal_data()` by měla být otestována napříč věkovými scénáři.
 
 ## 🦊 Vizuální rozvoj (plán)
 - [x] Zobrazení obrázku při detekci zvířete pomocí GPT
 - [x] Zůstane zobrazen při navazující konverzaci (opraveno)
 - [ ] Přidání popisu zvířete vedle obrázku
 - [ ] Podpora formátu 2 sloupce: levá půlka konverzace, pravá obrázek + info
 - [ ] Možnosti rozšíření:
   - Ken Burns efekt (zoom + posun obrázku)
   - Parallax efekt při pohybu myši
   - Tilt.js: 3D náklon na hover
   - SVG overlay (např. vlnky nad obrázkem)
   - Videa/GIFy podle detekovaného tématu (pexels, giphy)
 
 ## 🗣️ Interakce s dětmi
 - Zohlednění věku v system promptu (4leté dítě – obrázky, 10leté – fakta)
 - ⚠️ Děti nad 7 let: otázka na oblíbené zvíře může být „moc dětská“
 - Alternativy první otázky:
   - „Jaké zvíře tě naposledy zaujalo?“
   - „O kterém zvířeti bys dnes chtěl mluvit?“
 - System prompt reaguje i na styl odpovědi a preferovaný tón dítěte
 
 ## 🤖 Agentní rozšíření
 - Agent analyzuje složky a radí (status, code review, testy, struktura)
 - Má přístup k API (tools_api.py), umí validovat `.env` a venv
 - CLI: `assistant_cli.py --status`, `--check`, `--code-review`
 - Další možnosti rozšíření:
   - Asistent pro obsah (vytváření popisků, kuriozit)
   - Scheduler/Planner pro nové funkce
   - Konverzační paměť (zatím není přímá)
 
 ## 📦 Deploy (zatím neřešeno)
 - Projekt není nasazen
 - Vhodné varianty: HuggingFace Spaces, Railway.app, Replit