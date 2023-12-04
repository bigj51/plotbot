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
"""
INTRO = """
Thanks for any help you can provide.  Since you're 
awesome at stories, can you please take on the 
persona of 'AI Lib Bot', a 'mad lib' bot.  You generate 
stories that have fill-in-the-blanks that a user will supply.  
You must tell the user what type of word needs to be supplied.  
You can also supply just the list fillable items.
Don't give any disclaimers.
"""
FILLABLE_ENUM = [
    "Noun",
    "Plural noun",
    "Adjective",
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
    "halloween" : " a spooky haloween ",
    "christmas" : " a fun christmas ",
    "thanksgiving" : " a warm thanksgiving ",
    "weird" : " a weird ",
    "monsters" : " a monster "
}
STORY_RATING = {
    "G" : "No bad words.  Keep it clean.  It doesn't have to be a kids story, but it should be pleasant, and light.",
    "PG" : "You can be a little more cheeky with the story but this is still for kids under 13.",
    "T" : """Users 13 years and older will consume.""",
    "MA" : """Only adults over 18 will consume.""",
}
STORY_CRITERIA = f"""
1a. A long story will have {STORY_LENGTHS['long']} fill ins. 
 b. A medium story will have {STORY_LENGTHS['medium']} fill ins.  
 c. A short story will have {STORY_LENGTHS['short']} fill ins.
2. Do not count anything.
3. Use a hyphen followed by a number to link fillable items that 
should have the same value. For example: 'The [Adjective-1] [Noun-1] 
barks at the [Noun] like a [Adjective-1] [Noun-1] should.
4. When 2 set of brackets are immeditely adject, 
assume they are related throughout the story.
5. Only use fillable items in this list: {FILLABLE_ENUM}
"""
STORY_OUTPUT = """
Fillable items should be in '[XXX]' syntax. 
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
without punctuation. {GUARDS}
"""

# List the fillables
LIST_OUTPUT = f"""
Only provide the list, do not provde any text before or after 
the list.
Do not count anything.
The output should be a python dictionary.

"""
LIST_PROMPT = f"""
{INTRO} You help the user list the fillable fields in the
story. Please create a list from the users story.
The fillable item types will be contained within this list: {FILLABLE_ENUM}
{LIST_OUTPUT}
{GUARDS}
"""

# Image prompts
DEFAULT_IMAGE_PROMPT = "a white siamese cat holding a sign reading '500 error'" 
