import random

# Every Player is a chat
class Player:
    def __init__(self, id):
        self.id = id # Chat id
        self.isplaying = False # Playing status
        self.lives = 7 # Starting lives
        self.word_guess = [] # Storing "_"'s 
        self.hearts = [] # Storing hearts
        self.letter = [] # Storing letters
        self.word = "" # Storing word
        self.language = [] # Storing every language string 
        self.set_lan = False # Choosing language status
        self.set_dif = False # Choosing difficulty status
        self.set_trans = False # Choosing language to translate status
        self.game_f_word = "" # Storing word for the end of the game
        set_english(self) # Initialization of the game to English language
        self.mode = False

# Getting English words
def enwords():
    listwords = []
    enword = open("english_words.txt", "r")
    listwords = enword.readlines()
    enword.close
    return listwords

# Getting Spanish words
def eswords():
    listwords = []
    esword = open("spanish_words.txt", encoding="latin1")
    listwords = esword.readlines()
    esword.close
    return listwords

# Getting Portuguese words
def ptwords():
    listwords = []
    ptword = open("portuguese_words.txt", encoding="latin1")
    listwords = ptword.readlines()
    ptword.close
    return listwords

# Getting Italian words
def itwords():
    listwords = []
    itword = open("italian_words.txt", encoding="latin1")
    listwords = itword.readlines()
    itword.close
    return listwords

# Getting German words
def dewords():
    listwords = []
    deword = open("german_words.txt", encoding="cp1252")
    listwords = deword.readlines()
    deword.close
    return listwords

# Getting French words
def frwords():
    listwords = []
    frword = open("french_words.txt", encoding="latin1")
    listwords = frword.readlines()
    frword.close
    return listwords

# Setting Spanish language
def set_spanish(self):
    self.language = ["Adivina la palabra: \n", #0
                     "\n\nVidas:", #1
                     "\n/cancelar", #2
                     "Juego finalizado! 💔", #3
                     "La palabra era: ", #4
                     "Felicitaciones, ganaste! ❤️", #5
                     "Era: ", #6
                     "Lo lograste! 🎉🎊🏆", #7
                     "Estás respodiendo el juego con una entrada inespereda. Intenta nuevamente!",  #8
                     "Juego finalizado!", #9
                     "es", #10
                     "Lenguaje cambiado", #11
                     "Elije un lenguaje:", #12
                     "Ganadas: ", #13
                     "\nPerdidas: ", #14
                     "\nPromedio: ", #15
                     "Ese lenguaje no esta soportado, pídelo (Ver la descripción del bot). Intentálo nuevamente!", #16
                     "Modo fácil - 10 Vidas", #17
                     "Modo normal - 7 Vidas", #18
                     "Modo difícil - 5 Vidas", #19
                     "Modo experto - 3 Vidas", #20
                     "Escoja una dificultad", #21
                     "Dificultad cambiada", #22
                     "/restart", #23
                     "No estas jugando!", #24
                     "/cancelar", #25
                     "/definicion", #26
                     "/traducir", #27
                     "Esta palabra no tiene definición", #28
                     "Buscando... Por favor, espere 5 segundos", #29
                     "No has jugado aún,\nPor favor inicia un juego para obtener la definición", #30
                     "No has jugado aún,\nPor favor inicia un juego para obtener la traducción"] #31


# Setting English language
def set_english(self):
    self.language = ["Guess the word: \n", #0
                     "\n\nLives: ", #1
                     "\n/cancel", #2
                     "Game over! 💔", #3
                     "The word was: ", #4
                     "Congratulations, you won! ❤️", #5
                     "It was ", #6
                     "You did it! 🎉🎊🏆", #7
                     "You are replying the game with an unexpected entry. Try again!", #8
                     "Game over!", #9
                     "en", #10
                     "Language changed", #11
                     "Choose a language: ", #12
                     "Wins: ", #13
                     "\nLoses: ", #14
                     "\nAverage: ", #15
                     "That language isn't supported, ask for it (See bot's description). Try again!", #16
                     "Easy mode - 10 Lives", #17
                     "Normal mode - 7 Lives" , #18
                     "Hard mode - 5 Lives", #19
                     "Expert mode - 3 Lives", #20
                     "Choose a difficulty", #21
                     "Difficulty changed", #22
                     "/restart", #23
                     "You're not playing!", #24
                     "/cancel", #25
                     "/definition", #26
                     "/translate", #27
                     "This word has no definition", #28
                     "Searching... Please, wait 5 seconds", #29
                     "You haven't played yet,\nPlease start a game to get the definition", #30
                     "You haven't played yet,\nPlease start a game to get the translation"] #31

# Setting Portuguese language
def set_portuguese(self):
    self.language = ["Adivinha a palavra: \n", #0
                     "\n\nVidas:", #1
                     "\n/cancelar", #2
                     "Fim de jogo! 💔", #3
                     "A palavra era: ", #4
                     "Parabéns, você ganhou! ❤️", #5
                     "Era: ", #6
                     "você conseguiu! 🎉🎊🏆", #7
                     "Você está respondendo o jogo com uma entrada inesperada. Tente novamente!", #8
                     "Fim de jogo!", #9
                     "pt", #10
                     "Idioma trocado", #11
                     "Escolha um idioma:", #12
                     "Vitórias: ", #13
                     "\nDerrotas: ", #14
                     "\nMedia: ", #15
                     "Essa linguagem não é suportada, pode pedi-la (olhe a descrição do bot). Tente novamente!", #16
                     "Nível fácil - 10 Vidas", #17
                     "Nível normal - 7 Vidas", #18
                     "Nível difícil - 5 Vidas", #19
                     "Nível muito difícil - 3 Vidas", #20
                     "Escolha a dificuldade", #21
                     "Dificuldade alterada", #22
                     "/restart", #23
                     "Você não está jogando!", #24
                     "/cancelar", #25
                     "/definição", #26
                     "/traduzir", #27
                     "Esta palavra não tem definição", #28
                     "Procurando... Por favor, espere 5 segundos", #29
                     "Você ainda não jogou,\nInicie um jogo para obter a definição", #30
                     "Você ainda não jogou,\nInicie um jogo para obter a tradução"] #31

# Setting Italian language
def set_italian(self):
    self.language = ["Indovina la parola: \n", #0
                     "\n\nVite:", #1
                     "\n/annulla", #2
                     "Gioco finalizzatto! 💔", #3
                     "La parola era: ", #4
                     "Congratulato, hai vinto! ❤️", #5
                     "Era: ", #6
                     "L'hai fatto! 🎉🎊🏆", #7
                     "La tua risposta non é válida. Tenta un altra volta.", #8
                     "Gioco finalizzatto!", #9
                     "it", #10
                     "Linguaggio cambiato", #11
                     "Scegli un linguaggio:", #12
                     "Punti guadagnati: ", #13
                     "\nPunti perse: ", #14
                     "\nMedia: ", #15
                     "Quello linguaggio non è supportato. Richiedilo (Vedi la descrizione). Tenta un altra volta.", #16
                     "Facile - 10 Vite", #17
                     "Intermedio - 7 Vite", #18
                     "Difficile - 5 Vite", #19
                     "Esperto - 3 Vite", #20
                     "Seleziona la difficoltà", #21
                     "Difficoltà modificata", #22
                     "/restart", #23
                     "Non stai giocando!", #24
                     "/annulla", #25
                     "/definizione", #26
                     "/tradurre", #27
                     "Questa parola non ha definizione", #28
                     "Ricerca in corso... attendere 5 secondi", #29
                     "Non hai ancora giocato,\nAvviare un gioco per ottenere la definizione", #30
                     "Non hai ancora giocato,\nAvviare un gioco per ottenere la traduzione"] #31

# Setting German language
def set_german(self):
    self.language = ["Errate das Wort : \n", #0
                     "\n\nLeben:", #1
                     "\n/abbrechen", #2
                     "Spiel beendet! 💔", #3
                     "das Wort war: ", #4
                     "Glückwunsch, du hast gewonnen! ❤️", #5
                     "Es war: ", #6
                     "Du hast es geschafft! 🎉🎊🏆", #7
                     "Deine Eingabe ist ungültig. Versuche es erneut!", #8
                     "Spiel beendet!", #9
                     "de", #10
                     "Sprache geändert", #11
                     "Wähle ein Sprache: ", #12
                     "Siege: ", #13
                     "\nNiederlagen: ", #14
                     "\nDurschnitt: ", #15
                     "Diese Sprache wird nicht unterstützt, bitte anfragen (Siehe die Anleitung im Bot). Versuche es erneut!", #16
                     "Easy mode - 10 Leben", #17
                     "Normal mode - 7 Leben", #18
                     "Hard mode - 5 Leben", #19
                     "Expert mode - 3 Leben", #20
                     "Wähle einen Schwierigkeitsgrad", #21
                     "Schwierigkeitsgrad geändert", #22
                     "/restart", #23
                     "Du spielst gerade nicht!", #24
                     "/abbrechen", #25
                     "/bedeutung", #26
                     "/übersetzung", #27
                     "dieses Wort hat keine Bedeutung", #28
                     "sucht gerade... Bitte warte noch 5 Sekunden", #29
                     "du hast noch nicht gespielt, \nbitte starte ein Spiel, um die Bedeutung zu bekommen", #30
                     "du hast noch nicht gespielt, \nbitte starte ein Spiel, um die Übersetzung zu bekommen"] #31

# Setting French language
def set_french(self):
    self.language = ["Devinez le mot: \n", #0
                     "\n\nVies: ", #1
                     "\n/annule", #2
                     "Game over! 💔", #3
                     "Le mot etait: ", #4
                     "Félicitations, vous avez gagné! ❤️", #5
                     "C'était ", #6
                     "Bien joué! 🎉🎊🏆", #7
                     "Vous avez répondu au jeu de manière inattendue. Essayez encore!", #8
                     "Game over!", #9
                     "fr", #10
                     "Langue modifié", #11
                     "Choisir une langue: ", #12
                     "Victoires: ", #13
                     "\nDéfaites: ", #14
                     "\nMoyenne: ", #15
                     "Cette langue n'est pas prise en charge, demandez la (Voir la description du bot). Essayez encore!", #16
                     "Mode facile - 10 Vies", #17
                     "Mode normal - 7 Vies" , #18
                     "Mode difficile - 5 Vies", #19
                     "Mode expert - 3 Vies", #20
                     "Choisir une difficulté", #21
                     "Difficulté changée", #22
                     "/restart", #23
                     "Vous ne jouez pas!", #24
                     "/annule", #25
                     "/definition", #26
                     "/traduction", #27
                     "Ce mot n'a pas de définition", #28
                     "Recherche... Veuillez patienter 5 secondes", #29
                     "Vous n'avez pas encore joué,\nVeuillez commencer une partie pour obtenir la définition", #30
                     "Vous n'avez pas encore joué,\nVeuillez commencer une partie pour obtenir la traduction"] #31

# Reseting the bot
def reset_bot(self):
    self.isplaying = True 
    self.list = []
    self.word_guess = []
    self.hearts = []
    # Choosing the right keyboard for each language
    if self.language[10] == "es": 
        self.letter = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ'],
                       ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.word = random.choice(eswords())
    elif self.language[10] == "en": 
        self.letter = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                       ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.word = random.choice(enwords())
    elif self.language[10] == "pt":
        self.letter = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', "Ç"],
                       ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.word = random.choice(ptwords())
    elif self.language[10] == "it":
        self.letter = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                       ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.word = random.choice(itwords())
    elif self.language[10] == "de":
        self.letter = [['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'Ü'],
                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä'],
                       ['Y', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.word = random.choice(dewords())
    elif self.language[10] == "fr":
        self.letter = [['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                       ['Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
                       ['W', 'X', 'C', 'V', 'B', 'N']]
        self.word = random.choice(frwords())