from player import *
import telegram 

l1 = ["/huevito", "/gon", "/barratrampa", "/bobilinda", "/nobobi", "/puto"]

def mode(update, play, bot):

    if update.message.text == "/huevito":
        bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAIFP1-c14RRVz2FU8rv_HgLrEg6LjZeAAIsAAP3AsgPvEHgyPvhQNMbBA')
    
    if update.message.text == "/gon":
        bot.send_voice(chat_id=update.message.chat_id, voice='AwACAgEAAxkBAAIK1l-gMSVwutG1zMLlwMD9dMbzf0PpAALfAAMaVfhEq9uVQ-1YzUYeBA')

    if update.message.text == "/barratrampa":
        update.message.reply_text(play.word)

    if update.message.text == "/bobilinda":
        bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAILXF-gOJVD5r_J9ZZNpmWxC3DeTSaWAAK9AAMw1J0RnMLcRDVhgXseBA')

    if update.message.text == "/nobobi":
        bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAILXV-gOOFRKVj8DVN03zqY7sFL70UEAAIJAAPANk8T780bokr_cZUeBA')

    if update.message.text == "/puto":
        update.message.reply_text("el que lee")

