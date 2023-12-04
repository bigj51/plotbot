from flask import Flask, request, jsonify
import openai
from keys import OPENAI_KEY
from prompts import NEW_STORY_CREATE_PROMPT, FILLABLE_PROMPT, LIST_PROMPT, DEFAULT_WORD_PROMPT

app = Flask(__name__)

openai.api_key = OPENAI_KEY

@app.route('/auto_gen_word', methods=['POST'])
def auto_gen_word():
    # TODO sanitize input
    if request.args and request.args['prompt']:
        DEFAULT_WORD_PROMPT = request.args['prompt']

    messages = [
        {"role": "system", "content": FILLABLE_PROMPT},
        {"role": "user", "content": DEFAULT_WORD_PROMPT}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    word = response.choices[0].message.content.strip()
    
    return jsonify({"word": word})

@app.route('/gen_lib', methods=['GET', 'POST'])
def gen_lib():
    LENGTH = "short" 
    # TODO sanitize input
    if request.args and request.args['length']:
        LENGTH = request.args['length']

    messages = [
        {"role": "system", "content": NEW_STORY_CREATE_PROMPT},
        {"role": "user", "content": f"Create a {LENGTH} mad lib."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    story = response.choices[0].message.content.strip()
    
    return jsonify({"story": story})

@app.route('/list_fills', methods=['POST'])
def list_fills():
    #throw  err if no list
    STORY = "oops i forgot to add the story"
    if request.args and request.args['length']:
        STORY = request.args['length']
    
    messages = [
    {"role": "system", "content": LIST_PROMPT},
    {"role": "user", "content": STORY}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    list = response.choices[0].message.content.strip()
    
    return jsonify({"list": list})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
