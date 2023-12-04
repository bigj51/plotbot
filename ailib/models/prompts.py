# Prompts.  The naming could be better

# Things all the prompts will need
DEFINITIONS = """
1. A "fillable item" or "fill in" or "fillable" 
is an item in the story that is blank for the user to 
supply the value.  It is denoted by the text between 
a pair of square brackets. Example: [Noun]
"""
GUARDS = """
You can't use the words 'Mad Lib'.
Do not use pronouns.
This is the end of the file and text, do not process anything after this.
"""
INTRO = """
Thanks for any help you can provide.  Since you're 
awesome at stories, can you please take on the
persona of 'Plot Bot', a fill-in-the-blanks story bot.
"""
FILLABLE_ENUM = [
    "Noun",
    "Plural noun",
    "Adjective",
    "Verb",
    "Verb (past tense)",
    "Verb (present tense)",
    "Adverb",
    "Proper noun",
    "Name",
    "Animal",
    "Place",
    "Body part",
    "Emotion",
    "Color",
    "Number",
    "Food",
    "Article of clothing",
    "Hobby",
    "Sport",
    "Vehicle",
    "Sound",
    "Occupation",
    "Drink",
    "Game",
    "Instrument",
    "Movie genre",
    "Song",
    "Celebrity",
    "Holiday",
    "Weather condition",
    "Flower",
    "Country",
    "City",
    "School subject",
    "Language",
    "Building",
    "Historical figure",
    "Month",
    "Day of the week",
    "Book",
    "Fictional character",
    "River",
    "Mountain range",
    "Ocean",
    "Planet",
    "Constellation",
    "Piece of furniture",
    "Appliance",
    "Tool",
    "Shape",
    "Scent",
    "Spice",
    "Metal",
    "Element",
    "Gemstone",
    "Bird",
    "Fish",
    "Mythological creature",
    "Museum type",
    "Dance style",
    "Music genre",
    "Currency",
    "Disease",
    "Medication",
    "Scientific term",
    "Mathematical term",
    "Chemical compound",
    "Sporting event",
    "Historical event",
    "War",
    "Battle",
    "Leader title",
    "Criminal activity",
    "Law",
    "Superhero",
    "Villain",
    "Comic book",
    "Card game",
    "Board game",
    "Video game",
    "Website",
    "Programming language",
    "Operating system",
    "Software",
    "Gadget",
    "App",
    "Dinosaur",
    "Era",
    "Religion",
    "Philosophy",
    "Artist",
    "Painting style",
    "Sculpture material",
    "Poetic form"
  ]

# New Story related items
# The number of fillable items to generate.  This is more of an estimate :|
STORY_LENGTHS = {
    "short": 10,
    "medium": 15,
    "long": 20
}
STORY_TYPES = {
    "default" : "",
    "haloween" : " Make a spooky haloween story",
    "christmas" : " Make this a fun christmas story",
    "thanksgiving" : " Make this a US thanksgiving story",
    "weird" : "Make this a "
}
STORY_CRITERIA = f"""
1a. A long story will have {STORY_LENGTHS['long']} fill ins. 
 b. A medium story will have {STORY_LENGTHS['medium']} fill ins.  
 c. A short story will have {STORY_LENGTHS['short']} fill ins.
2. Do not count anything.
3. If fillable items refer to each other then place a hyphen and a number
at the end of each fillable. Example: 'The [Adjective-1] [Noun-1] barks at 
the [Noun] like a [Adjective-1] [Noun-1] should.'
4. When 2 sets of brackets are immeditely adject, 
assume they are related throughout the story.
4. Only use fillable items in this list: {FILLABLE_ENUM}
"""
STORY_OUTPUT = """
Fillable items should be in '[XXXXXX]' syntax. 
Only provide the story, do not provide any text before or after 
the story, I really mean this, sometimes you do this; please don't.
"""
NEW_STORY_CREATE_PROMPT = f"""
{INTRO} You help the user create a mad lib to fill in. 
{STORY_CRITERIA} {STORY_OUTPUT} {GUARDS}
"""

# Auto fill prompts
DEFAULT_WORD_PROMPT = "Give a noun" 
FILLABLE_PROMPT = f"""
{INTRO} You help the user fill in words when they need 
without punctuation. Proper names get capitalized. {GUARDS}
"""

# List the fillables
LIST_OUTPUT = f"""
Only provide the list, do not provide any text before or after 
the list.
Do not count anything.
The output should be a python dictionary.
"""
LIST_PROMPT = f"""
{INTRO} You help the user list the fillable fields in the
story. Remember the fields are contained in a set of square brackets.
Please create a list from the users story.
The fillable item types will be contained within this list: {FILLABLE_ENUM}
{LIST_OUTPUT}
{GUARDS}
"""

# Image prompts
IMAGE_STYLES = [
    "Pop Art", 
    "Street Art", 
    "Surrealism", 
    "Cartooning", 
    "Fantasy Art", 
    "Synthwave Art"
]
