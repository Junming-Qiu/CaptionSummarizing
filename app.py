import gradio as gr
from summarize import GPTSummarizer
from processing import SummaryParser, YTCaptioner
import time

def submit(prompt, task, temperature):
        # Summary can take lengths of text longer than the token limit and concat
        if task == "summary":
            prompt = SummaryParser.get_transcript(prompt)

            store = ""
            cost = 0
            for i, segment in enumerate(prompt):
                s = GPTSummarizer.get_completion(segment, task, temperature)
                cost += s[1]
                print(f"Segment {i+1} Done!")
                time.sleep(0.2)
                store += " " + s[0]

        # Prompts are restricted by the token limit but are free form
        elif task == "prompt":
            s = GPTSummarizer.get_completion(prompt, task, temperature)
            store = s[0]
            cost = s[1]
        
        return store, cost / 1000 * 0.002

def upload_file(file):
    prompt = ""
    with open(file.name, "r") as f:
        read_l = f.readlines()

    for line in read_l:
        prompt += line
    return prompt

def upload_yt_caption(link):
    id = link.split("=")[-1]
    cc = YTCaptioner.get_transcript(id) 
    return cc


with gr.Blocks() as app:
    gr.Markdown("Access Different ChatGPT Functions Here")
    with gr.Tab("Prompting"):
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(label="Input", lines=5, placeholder="Enter Prompt Here")
                with gr.Row():
                    usage_selection = gr.Dropdown(["prompt", "summary"], label="Usage", value="prompt", allow_custom_value=False)
                    temperature = gr.Slider(0, 1, label="Temperature")
                file_output = gr.File(file_count="single", file_types=[".txt"])

                with gr.Row():
                    yt_id = gr.Text(placeholder="Enter Youtube Link", label="Link")
                    yt_button = gr.Button("Caption Youtube Video")

                    yt_button.click(upload_yt_caption, inputs=yt_id, outputs=text_input)
                    

                input_button = gr.Button("Submit")

                file_output.upload(upload_file, inputs=file_output, outputs=text_input)

            with gr.Column():
                text_output = gr.Text(label="Output", interactive=False)
                cost = gr.Number(label="Cost in $", interactive=False)
                transfer = gr.Button("<- Transfer to Input")

    input_button.click(submit, inputs=[text_input, usage_selection, temperature], outputs=[text_output, cost])

app.launch() 