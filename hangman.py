import random

def choose_movie():
    # List of movie titles for the game
    movies = [
        "avatar", "titanic", "inception", "theshawshankredemption", "forrestgump",
        "thegodfather", "pulpfiction", "thelionking", "starwars", "jurassicpark",
        "harrypotter", "backtothefuture", "thematrix", "frozen", "braveheart",
        "gladiator", "schindlerslist", "casablanca", "gonegirl", "interstellar",
        "gravity", "batman", "spiderman", "superman", "avengers", "jurassicworld",
        "blackpanther", "thor", "ironman", "captainamerica", "thefellowshipofthering",
        "thetwotowers", "thereturnoftheking", "thegreatgatsby", "fightclub",
        "incredibles", "findingnemo", "moulinrouge", "et", "jaws", "madmax",
        "silenceofthelambs", "bridgetjonesdiary", "glory", "gonein60seconds",
        "independenceday", "killbill", "twilight", "unbreakable", "zombieland",
        "lifeofpi", "djangounchained", "whiplash", "lalaland", "ferrisbuellersdayoff",
        "shrek", "brokebackmountain", "ragingbull", "rocky", "jumanji", "spectre",
        "casinoroyale", "halloween", "theterminator", "hungergames", "mib",
        "sherlockholmes", "thegrandbudapesthotel", "theexorcist", "theshining",
        "backdraft", "reservoirdogs", "scream", "thebreakfastclub", "thefly",
        "thefugitive", "grease", "therockyhorrorpictureshow", "jaws",
        "thenotebook", "eclipse", "thewizardofoz", "frozen", "zootopia"
        # Add more movie titles as needed
    ]
    
    
    #choose a random movie title
    return random.choice(movies)

def display_word(word, guessed_letters):
    #display the word with underscores for letters not guessed
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display+= "_"
            return display
        
        
    