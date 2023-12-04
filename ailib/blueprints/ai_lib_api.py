import tiktoken 
from flask import request, jsonify
from flask.views import MethodView
from ailib.models.prompts import NEW_STORY_CREATE_PROMPT, FILLABLE_PROMPT, LIST_PROMPT, DEFAULT_WORD_PROMPT, STORY_TYPES
from flask import Blueprint, current_app

api_bp = Blueprint('api', __name__)

enc = tiktoken.encoding_for_model("gpt-4")

class AutoGenWordView(MethodView):
    def post(self):
        word_prompt = DEFAULT_WORD_PROMPT
        if request.args and request.args['prompt']: 
            # TODO sanitize input
            # TODO: put tokenizer initialization logic here (doesn't really go here,  should be in custom validator)          
            if len(enc.encode(request.args['prompt'])) > 10:
                raise RuntimeError('prompt too long')
            
            word_prompt = request.args['prompt']

        messages = [
            {"role": "system", "content": FILLABLE_PROMPT},
            {"role": "user", "content": word_prompt}
        ]

        response = current_app.openai.oai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )

        word = response.choices[0].message.content.strip()
        return jsonify({"word": word, "prompts": messages})

class GenLibView(MethodView):
    def get(self):
        # TODO sanitize input
        LENGTH = "short"
        type = STORY_TYPES["default"]
        story_prompt = NEW_STORY_CREATE_PROMPT
        if request.args and request.args['length']:
            if len(enc.encode(request.args['length'])) > 1:
                raise RuntimeError('prompt too long')
            LENGTH = request.args['length']

        if request.args and request.args['type'] is not None:
            if len(enc.encode(request.args['type'])) > 7:
                raise RuntimeError('type prompt too long')
            
            if request.args['type'] in STORY_TYPES.keys():
                story_prompt = story_prompt + STORY_TYPES[request.args['type']]

        story_messages = [
            {"role": "system", "content": story_prompt},
            {"role": "user", "content": f"Create a {LENGTH} mad lib."}
        ]

        story_response = current_app.openai.oai.ChatCompletion.create(
            model="gpt-4",
            messages=story_messages
        )
        story = story_response.choices[0].message.content.strip()
        return jsonify({"story": story, "story_prompts": story_messages})

    def post(self):
        return self.get()

class ListFillsView(MethodView):
    def post(self):
        # TODO: Handle the case when there's no list
        # set a max story size (token size) on creation for large so we can put a guard rail in place?
        STORY = "oops i forgot to add the story"
        if request.args and request.args['story']:
            STORY = request.args['story']

        messages = [
            {"role": "system", "content": LIST_PROMPT},
            {"role": "assistant", "content": "\{ 1 : \"location\", 2 : \"verb\" \}"},
            {"role": "user", "content": STORY}
        ]
        response = current_app.openai.oai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        list = response.choices[0].message.content.strip()
        return jsonify({"list": list, "prompts": messages})

api_bp.add_url_rule('/auto_gen_word', view_func=AutoGenWordView.as_view('auto_gen_word'))
api_bp.add_url_rule('/gen_lib', view_func=GenLibView.as_view('gen_lib'))
api_bp.add_url_rule('/list_fills', view_func=ListFillsView.as_view('list_fills'))
