import telegram 
import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Sticker, Voice)
from telegram.error import NetworkError, Unauthorized
from time import sleep
import re
from player import *
from web import *
from usm import *
from saved_score import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def lose_game(update, play):
    # Bot sends lose message
    update.message.reply_text(play.language[3], reply_markup=ReplyKeyboardRemove(), reply_to_message_id = None)
    # There's a German exception when "ß" is converted as "ss", adding one "\n" to fix indentation
    if play.language[10] == "de" and "ss" in play.word:
        update.message.reply_text(play.language[4] + str(play.word).capitalize() + 
                                  "\n" + play.language[23] + "\n" + play.language[26] + 
                                  "\n" + play.language[27] , reply_to_message_id = None)
    else:
        update.message.reply_text(play.language[4] + str(play.word).capitalize() + 
                                  play.language[23] + "\n" + play.language[26] + "\n" + 
                                  play.language[27] , reply_to_message_id = None)
    # No playing anymore
    play.isplaying = False
    # Setting to translate translate or define the word
    play.game_f_word = play.word
    # Adding a point in losing score
    lose_plus(play)
    logger.info("Lost a game %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Lost a game ")

def win_game(update, play):
    # Bot sends win message 
    update.message.reply_text(play.language[5], reply_markup=ReplyKeyboardRemove(), reply_to_message_id = None)
    # There's a German exception when "ß" is converted as "ss", adding one "\n" to fix indentation
    if play.language[10] == "de" and "ss" in play.word:
        update.message.reply_text(play.language[6] + str(play.word).capitalize() + 
                                  "\n" + play.language[7] + "\n" + play.language[23] + 
                                  "\n" + play.language[26] + "\n" + play.language[27], reply_to_message_id = None)
    else:
        update.message.reply_text(play.language[6] + str(play.word).capitalize() + 
                                  play.language[7] + "\n" + play.language[23] + "\n" + 
                                  play.language[26] + "\n" + play.language[27], reply_to_message_id = None)
    # No playing anymore
    play.isplaying = False
    #Setting to tanslate or define the word  
    play.game_f_word = play.word
    # Adding a point in winning score
    win_plus(play)
    logger.info("Won a game %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Won a game ")

def game(update, play):

    i = 0
    # if player is not playing then the game starts
    # else the game is still going
    if not play.isplaying:
        logger.info("Started a game %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
        update = info_player(update, "Started a game ")
        reset_bot(play)
        # Word_guess is created
        while i < len(play.word)-2:
            play.word_guess.append("_ ")
            i+=1
        play.word_guess.append("_")

        i = 0

        # Hearts are counted and added
        while i < play.lives:
            play.hearts.append("❤️")
            i+=1

        # German language exceptions
        if play.language[10] == "de" and "ss" in play.word:
            play.word_guess.remove("_")
            play.word_guess.insert(len(play.word)-1, "_ ")
            play.word_guess.append("_")

        # Portuguese language exceptions
        if play.language[10] == "pt" and play.word.count("-") > 0:
                for w in re.finditer("-", play.word):
                    play.word_guess[w.start()] = "-"
        if play.language[10] == "pt" and play.word.count("'") > 0:
                for w in re.finditer("'", play.word):
                    play.word_guess[w.start()] = "'"    

        # First message after /start
        update.message.reply_text(play.language[0] + "".join(play.word_guess) + play.language[1] + 
                                    "".join(play.hearts) + play.language[2], 
                                    reply_markup=ReplyKeyboardMarkup(play.letter, one_time_keyboard=True))

    else:

        # Translate all type of typography
        if play.language[10] == "de":
            a,b = 'áéíóúàèìòùâêîôûëïåýãª','aeiouaeiouaeioueiayaa'
        else:
            a,b = 'áéíóúüàèìòùâêîôûäëïöåýãª','aeiouuaeiouaeiouaeioayaa'
			
        trans = str.maketrans(a,b)

        # if the only entry available is one letter
        # else you are sending a wrong expected entry
        if len(str(update.message.text)) == 1:

            # Search letter chosen on keyboard in word
            if (play.word.translate(trans)).count(str(update.message.text).lower()) > 0 :
                for w in re.finditer(str(update.message.text).lower(), play.word.translate(trans)):
                    play.word_guess[w.start()] = play.word[w.start()]
            else:
                play.hearts.remove("❤️")

            # Remove letter from custom keyboard
            for n in range(3):
                if play.letter[n].count(update.message.text) > 0:
                    play.letter[n].remove(update.message.text)

            # if you lose the game
            # elif you won the game
            # else the game is still going
            if play.hearts.count("❤️") == 0:
                lose_game(update, play)
            elif play.word_guess.count("_ ") == 0 and play.word_guess.count("_") == 0:
                win_game(update, play)
            else:
                update.message.reply_text(play.language[0] + "".join(play.word_guess) + play.language[1] + 
                                          "".join(play.hearts) + play.language[2], 
                                          reply_markup=ReplyKeyboardMarkup(play.letter, one_time_keyboard=True))
        else:
            update.message.reply_text(play.language[8])
            update.message.reply_text(play.language[0] + "".join(play.word_guess) + play.language[1] + 
                                      "".join(play.hearts) + play.language[2], 
                                      reply_markup=ReplyKeyboardMarkup(play.letter, one_time_keyboard=True))

def set_lan(update, play):

    list_lan = [["Deutsch"], ["English"], ["Español"], ["Français"], ["Italiano"], ["Português"]]
    is_word = False
    languages =	{
        "Español": "es",
        "English": "en",
        "Português": "pt",
        "Italiano": "it",
        "Deutsch": "de",
        "Français": "fr"
    }

    # Check if the chosen language is in the list
    for value in languages.keys():
        if update.message.text == value:
            is_word = True

    # if setting the chosen language and changing all the strings of the game
    # elif sends a message that there's no language available
    # else sends a message with options to choose a language
    if play.set_lan and is_word:
        msg = languages[update.message.text]
        if msg == "es":
            set_spanish(play)
        elif msg == "en":
            set_english(play)
        elif msg == "pt":
            set_portuguese(play)
        elif msg == "it":
            set_italian(play)
        elif msg == "de":
            set_german(play)
        elif msg == "fr":
            set_french(play)

        # No setting language anymore
        play.set_lan = False
        # Bot sends a message the language is changed
        update.message.reply_text(play.language[11], reply_markup=ReplyKeyboardRemove())
        logger.info("Changed the language %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
        update = info_player(update, "Changed the language ")

    elif not is_word and not update.message.text == "/language" and not update.message.text == "/language@WordGuesserbot":
        update.message.reply_text(play.language[16])
        update.message.reply_text(play.language[12], reply_markup=ReplyKeyboardMarkup(list_lan))
    else:
        play.set_lan = True
        update.message.reply_text(play.language[12], reply_markup=ReplyKeyboardMarkup(list_lan))

# Bot shows score 
def score(update, play):

    # Adding to the file if player score is not in it
    (score_, fil) = score_add(play)

    # if player didn't reset score
    # else player reseted score
    if update.message.text != "/reset" and update.message.text != "/reset@WordGuesserbot":
        # if losing score is not zero (To avoid math error)
        # else losing score is zero
        if score_[1] != 0:
            average = score_[0] / (score_[0] + score_[1]) * 100
            update.message.reply_text(play.language[13] + str(score_[0]) + play.language[14] + 
                                    str(score_[1]) + play.language[15] + str("{0:.1f}".format(average)) + "%" +
                                    "\n/reset", reply_to_message_id = None)
        else:
            update.message.reply_text(play.language[13] + str(score_[0]) + 
                                    play.language[14] + str(score_[1]) + 
                                    play.language[15] + "💯%" +
                                    "\n/reset", reply_to_message_id = None) 
        logger.info("Asked for score %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)                                    
        update = info_player(update, "Asked for score ")
    else:
        del fil[str(play.id)]
        update.message.reply_text("✅", reply_to_message_id = None)
        logger.info("Reseted score %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
        update = info_player(update, "Reseted score ")
    fil.close
    

# Bot changes difficulty in game
def difficulty(update, play):

    # list of difficulty names
    list_dif = [[play.language[17]],[play.language[18]], [play.language[19]], [play.language[20]]]

    # if player didn't choose a difficulty yet
    # else Bot sends options to choose a difficulty 
    if (play.set_dif and not update.message.text == "/difficulty" 
        and not update.message.text == "/difficulty@WordGuesserbot"):
        if update.message.text == play.language[17]:
            play.lives = 10
        elif update.message.text == play.language[18]:
            play.lives = 7
        elif update.message.text == play.language[19]:
            play.lives = 5
        elif update.message.text == play.language[20]:
            play.lives = 3
        play.set_dif = False
        update.message.reply_text(play.language[22], reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(play.language[21], reply_markup=ReplyKeyboardMarkup(list_dif))
        play.set_dif = True
        
    logger.info("Changed difficulty %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Changed difficulty ")

# Bot gives a definition of the word from Google translate
def definition(update, play):
    
    # if game didn't finish yet
    # else Bot sends a message of warning
    if play.game_f_word != "":
        definition_list = []
        word_definitions = ""
        # Bot gets information from Google translate through Selenium
        definition_list = web_definition(play)
        i = 0
        # if list of definitions is not empty then Bot sends one message with all of them
        # else list of definitions is empty then Bot sends a message about definition doesn't exist 
        if len(definition_list) >= 1:
            while i < len(definition_list):
                word_definitions = word_definitions + str(i+1) + "- " + definition_list[i] + "\n"
                i += 1
            update.message.reply_text(word_definitions)
        else:
            update.message.reply_text(play.language[28])
    else:
        update.message.reply_text(play.language[30])
    logger.info("Asked for definition %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Asked for definition ")

# Bot gives a translation of the word from Google translate
def translate(update, play):

    # if game didn't finish yet
    # else Bot sends a message of warning
    if play.game_f_word != "":
        # list of languages
        list_lan = [["Deutsch"], ["English"], ["Español"], ["Français"], ["Italiano"], ["Português"]]
        languages =	{
            "Español": "es",
            "English": "en",
            "Português": "pt",
            "Italiano": "it",
            "Deutsch": "de",
            "Français": "fr",
            "es": "Español",
            "en": "English",
            "pt": "Português",
            "it": "Italiano",
            "de": "Deutsch",
            "fr": "Français"
        }
        
        # if player didn't choose a language yet
        # else Bot sends options to choose a language
        if play.set_trans and not (update.message.reply_text == play.language[27]
        or update.message.reply_text == play.language[27] + "@WordGuesserbot"):
            update.message.reply_text(play.language[29])
            msg = languages[update.message.text]
            word_trans = web_translate(play, msg)
            # if Selenium found the word then Bot'll send it
            # else Selenium couldn't find the word then try again
            if word_trans != "":    
                update.message.reply_text(word_trans, reply_markup=ReplyKeyboardRemove())
            else:
                update.message.reply_text("Sorry, try again! -> " + play.language[27], reply_markup=ReplyKeyboardRemove())
            play.set_trans = False
            logger.info("Asked for translate %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
            update = info_player(update, "Asked for translate ")
        else:
            i = 0
            # Removing the actual language to avoid translate a word to the same language
            while i < len(list_lan):
                if list_lan[i][0] == languages[play.language[10]]:
                    list_lan.remove(list_lan[i])
                i += 1
            play.set_trans = True
            update.message.reply_text(play.language[12], reply_markup=ReplyKeyboardMarkup(list_lan))
    else:
        update.message.reply_text(play.language[31])

# Adding a player to a list to have an "unique" player(chat) 
def add_player(update, list_id, list_player):
    
    try:
        if list_id.count(update.message.chat.id) == 0:
            list_id.append(update.message.chat.id)
            list_player.append(Player(update.message.chat.id))
            logger.info("Player added %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
            update = info_player(update, "Player added ")
    except:
        pass

    return list_player
    
def info_player(update, msg):

    temp = int(update.message.chat.id)
    if temp > 0:
        update.message.chat.id = int("166915620")
        
        if update.message.from_user.last_name != None:
            update.message.reply_text(msg + update.message.from_user.first_name + " " + update.message.from_user.last_name)

        else:
            update.message.reply_text(msg + update.message.from_user.first_name)

        update.message.chat.id = temp

        
    
    return update

# Canceling the game while you're playing
def cancel(update, play):

    # if you're playing then cancel it
    # else Bot sends a warning
    if play.isplaying:
        play.isplaying = False
        update.message.reply_text(play.language[9] + "\n" + play.language[23], reply_markup=ReplyKeyboardRemove(), reply_to_message_id = None)
        logger.info("Canceled a game %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
        update = info_player(update, "Canceled a game ")
    else:
        update.message.reply_text(play.language[24])

# People who helped me to achieve this
def about(update):
    logger.info("Asked for about %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Asked for about ")
    update.message.reply_text("Created by:\nFacundo -> Telegram: https://t.me/facub\n\n"+
                              "Idea:\nKayla -> Instagram: https://www.instagram.com/kayla.r.crabtree/\n\n"+
                              "Hosted by: \nMe on Raspberry Pi 4b -> t.me/CRPIbot\n\n"+ 
                              "German translation: \nGianni -> Instagram: https://www.instagram.com/gianni_rossini/\n"+
                              "Marina -> Instagram: https://www.instagram.com/marimarina.___/\n\n"+
                              "French translation:\nYasmeen -> Instagram: https://www.instagram.com/yasmeendrn/\n\n"+ 
                              "Italian translation:\nBarto -> No social media\n\n"+
                              "Portuguese translation:\nLouise -> Instagram: https://www.instagram.com/lobranquinho/\n"+
                              "DrGloria -> Twitch: https://www.twitch.tv/drgloria92\n\n"+
                              "Testing/Suggestions:\n"+
                              "Gordios -> Twitch: https://www.twitch.tv/sn0wballed\n"+
                              "Peynox -> Instagram: https://www.instagram.com/pey.nox/\n"+
                              "Nathia -> Instagram: https://www.instagram.com/gianninabenzo/")
    
    
def donation(update):
    logger.info("Asked for donation %s %s",  update.message.from_user.first_name, update.message.from_user.last_name)
    update = info_player(update, "Asked for donation ")
    update.message.reply_text("If you want to donate, click here:\n"+
                              "https://www.patreon.com/hangman_on_python \n\n"+
                              "Thank you!\n")

update_id = None

def main():
    """Run the bot."""
    global update_id

    # Telegram Bot Authorization Token
    bot = telegram.Bot('1213078019:AAEg4TUBNZmBBDOkD-3gggAOWKtR3ugRDrM')
    
    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    list_id = []
    list_player = []

    while True:
        try:
            echo(bot, list_id, list_player)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

def echo(bot, list_id, list_player):
    """Echo the message the user sent."""
    global update_id
    
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        list_player = add_player(update, list_id, list_player)

        # Looping the whole player list
        for i in range(len(list_player)): 
            # Bot identifiques each player(chat)
            try: 
                if update.message.chat.id == list_player[i].id:
                    # /cancel
                    if (update.message.text == list_player[i].language[25] 
                        or update.message.text == list_player[i].language[25] + "@WordGuesserbot"
                        or update.message.text == "/cancel@WordGuesserbot" 
                        or update.message.text == "/cancel"):
                        cancel(update, list_player[i])
                    # /start or /restart
                    if ((update.message.text == "/start" 
                        or update.message.text == "/start@WordGuesserbot" 
                        or update.message.text == "/restart"
                        or update.message.text == "/restart@WordGuesserbot" 
                        or list_player[i].isplaying)):
                        game(update, list_player[i])
                    # /language
                    if ((update.message.text == "/language" 
                        or update.message.text == "/language@WordGuesserbot"
                        or list_player[i].set_lan) 
                        and not (list_player[i].set_dif 
                        or list_player[i].isplaying 
                        or list_player[i].set_trans)):
                        set_lan(update, list_player[i])
                    # /score
                    if ((update.message.text == "/score" 
                        or update.message.text == "/score@WordGuesserbot"
                        or update.message.text == "/reset"
                        or update.message.text == "/reset@WordGuesserbot") 
                        and not (list_player[i].isplaying
                        or list_player[i].set_lan 
                        or list_player[i].set_trans
                        or list_player[i].set_dif)):
                        score(update, list_player[i])
                    # /difficulty
                    if ((update.message.text == "/difficulty" 
                        or update.message.text == "/difficulty@WordGuesserbot"
                        or list_player[i].set_dif) 
                        and not (list_player[i].isplaying 
                        or list_player[i].set_lan 
                        or list_player[i].set_trans)):
                       difficulty(update, list_player[i])
                    # /definition
                    if ((update.message.text == list_player[i].language[26] 
                        or update.message.text == list_player[i].language[26] + "@WordGuesserbot") 
                        and not (list_player[i].isplaying
                        or list_player[i].set_lan 
                        or list_player[i].set_trans
                        or list_player[i].set_dif)):
                        update.message.reply_text(list_player[i].language[29])
                        definition(update, list_player[i])
                    # /translation
                    if ((update.message.text == list_player[i].language[27] 
                        or update.message.text == list_player[i].language[27] + "@WordGuesserbot" 
                        or list_player[i].set_trans) 
                        and not (list_player[i].isplaying 
                        or list_player[i].set_lan 
                        or list_player[i].set_dif)):
                        translate(update, list_player[i])
                    # /about
                    if update.message.text == "/about" or update.message.text == "/about@WordGuesserbot":
                        about(update)
                    # /donate
                    if update.message.text == "/donation" or update.message.text == "/donation@WordGuesserbot":
                        donation(update)

                    mode(update, list_player[i], bot)
	
                    # Printing current word of each player(chat)
                    #print(list_player[i].word)
            except:
                pass
            i =+ 1

if __name__ == '__main__':
    main()
