import gradio as gr
import sys
from chat_backend import (
    send_message,
    extract_animal_topic,
    get_animal_info,
    last_animal
)

def shutdown_app():
    print("Aplikace se ukončuje...")
    sys.exit()

def chat(user_input, history, current_img, current_desc):
    reply = send_message(user_input)
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": reply})

    zvire = extract_animal_topic(user_input)

    if not zvire:
        # GPT zatím neurčilo nové zvíře → zachovej aktuální obrázek a popis
        return "", history, gr.update(value=current_img, visible=bool(current_img)), gr.update(value=current_desc, visible=bool(current_desc)), current_img, current_desc

    info = get_animal_info(zvire)
    last_animal["zvíře"] = zvire

    if info:
        img = info["image"]
        desc = info["popis"]
        return "", history, gr.update(value=img, visible=True), gr.update(value=desc, visible=True), img, desc
    else:
        return "", history, gr.update(visible=False), gr.update(visible=False), None, None

# --- UI layout ---
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):  # CHAT PANEL
            chatbot = gr.Chatbot(type="messages")
            msg = gr.Textbox(label="Zeptej se zvířecího kamaráda:")
            clear = gr.Button("Vymazat konverzaci")
            shutdown = gr.Button("🛑 Vypnout aplikaci")

        with gr.Column(scale=1):  # INFO PANEL
            image = gr.Image(label="Zvíře, o kterém mluvíme", visible=False)
            description = gr.Markdown(visible=False)

    # --- vnitřní stavy ---
    state = gr.State([])  # konverzace
    img_state = gr.State(value=None)  # poslední známý obrázek
    desc_state = gr.State(value=None)  # poslední známý popis

    # --- propojení logiky ---
    msg.submit(
        chat,
        [msg, state, img_state, desc_state],
        [msg, chatbot, image, description, img_state, desc_state]
    )
    clear.click(lambda: [], None, chatbot)
    shutdown.click(fn=shutdown_app)

demo.launch()