import openai

class ailib_openai():
    oai = openai
    def __init__(self, app=None):
        self.oai.api_key = app.config.OPENAI_KEY
