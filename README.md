# ailib
A ChatGPT driven fillable story generator in flask.

## Usage

```bash
$ python -m venv env
$ env\Scripts\active
$ pip install -r requirements.txt
$ export OPENAI_KEY="<your api key>"
$ python -m flask --app run.py run
```

## Development

There are many things that could be done to make this better.  A few of the current issues/ideas are:

* It takes awhile for the calls to openai to come back.  Like a minute or more for a long story.
* There's like 0 validation of the incoming arguments.  I did put a little token length validation, but it's hacky.
* The front end is buggy end doesn't work, but I'm currently working on it with chatgpt.
* Use the free model
* When multi modal is out, accept a picture as input and create a mad lib
* The longest prompt for the user story is roughly 600 tokens.  So there's room for more prompt engineering.  
* Plus things I don't even know about...

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.




