import os
from flask import Blueprint, render_template
from ailib.models.prompts import STORY_TYPES, STORY_LENGTHS
import markdown

web_bp = Blueprint('story', __name__)

@web_bp.route('/')
def story_page():
    return render_template('index.html', STORY_LENGTHS=STORY_LENGTHS, STORY_TYPES=STORY_TYPES)

#@web_bp.route('/words')
#def story_page():
#    return render_template('words.html', STORY_LENGTHS=STORY_LENGTHS, STORY_TYPES=STORY_TYPES)
#
#@web_bp.route('/story')
#def story_page(): # create a new story with a UID<not here>,  save it to a file-azure-storage then create a public link for sharing. auto append a link back to the website
#    return render_template('story.html', STORY_LENGTHS=STORY_LENGTHS, STORY_TYPES=STORY_TYPES)

@web_bp.route('/about')
def about():
    # Read the README.md file
    with open(os.path.dirname(os.path.abspath(__file__)) + '/README.md', 'r') as f:
        content = f.read()

    # Convert to HTML
    content_html = markdown.markdown(content)

    return render_template('about.html', content=content_html)
