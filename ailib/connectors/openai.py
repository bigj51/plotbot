import openai
import tiktoken

class ailib_openai():
    oai = openai
    def __init__(self, app=None):
        self.oai.api_key = app.config["OPENAI_KEY"]
        self.model = app.config['OPENAI_MODEL']
        self.enc = tiktoken.encoding_for_model(app.config['OPENAI_MODEL']) 

    def send_gpt_message(self, messages=None):
        try:
            if messages is not None:
                return self.oai.ChatCompletion.create(
                    model=self.model,
                    messages=messages
                )
            else:
                raise RuntimeError("""Messages must be in this format and contain 1 or more types: 
                    [
                        {"role": "system", "content": CONTENT },
                        {"role": "assistant", "content": CONTENT},
                        {"role": "user", "content": CONTENT},
                        {"role": "function", "content": CONTENT}
                    ]
                    """)
        except Exception as e:
            raise e
