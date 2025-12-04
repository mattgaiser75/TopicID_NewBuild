import gradio as gr
def run_topicid(topic):
    return f"[NewBuild 10.0.5] Topic processed: {topic}"

with gr.Blocks() as app:
    gr.Markdown("# TopicID NewBuild 10.0.5")
    t = gr.Textbox(label="Enter Topic")
    o = gr.Textbox(label="Output")
    t.submit(run_topicid, t, o)
app.launch()
