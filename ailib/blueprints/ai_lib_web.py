import os
from flask import Blueprint, render_template
from ailib.models.prompts import STORY_TYPES, STORY_LENGTHS
import markdown

web_bp = Blueprint('story', __name__)

@web_bp.route('/')
def story_page():
    return render_template('index.html', STORY_LENGTHS=STORY_LENGTHS, STORY_TYPES=STORY_TYPES)

@web_bp.route('/about')
def about():
    # Read the README.md file
    with open(os.path.dirname(os.path.abspath(__file__)) + '/README.md', 'r') as f:
        content = f.read()

    # Convert to HTML
    content_html = markdown.markdown(content)

    return render_template('about.html', content=content_html)
