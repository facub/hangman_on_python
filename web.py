import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from player import *
from selenium.webdriver.common.action_chains import ActionChains

# Getting definition from Google translate
def web_definition(play):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://translate.google.com/?hl=es&tab=TT&authuser=0#view=home&op=translate&sl=" + play.language[10] + "&tl=de&text=" + play.game_f_word)

    time.sleep(2.5) #Waiting Chrome to search the page

    list_ = []

    # Trying to press "More definitions" if it exists
    try:
        button = browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/section/div/div/div[1]/div[1]/div/div[2]/div[1]")
        time.sleep(2)
        ActionChains(browser).move_to_element(button).click(button).perform()
    except:
        pass

    # Getting all the definition if they exist
    gt_tag = browser.find_elements_by_class_name("fw3eif")
    # Putting all the definitions on a list to close the browser
    for i in range(len(gt_tag)):
        list_.append(gt_tag[i].text)

    # Closing the browser
    browser.quit()

    return list_

# Getting translation from Google translate
def web_translate(play, msg):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://translate.google.com/?hl=es&tab=TT&authuser=0#view=home&op=translate&sl=" + play.language[10] + "&tl=" + msg + "&text=" + play.game_f_word)

    time.sleep(2) #Waiting Chrome to search the page

    # Trying to get the translation from the right square of the page
    try:
        word = browser.find_element_by_class_name("VIiyi").text
    except:
        # Trying to get the translation from the bottom right square of the page
        try:
            word = browser.find_element_by_class_name("kgnlhe").text
        # if it didn't work, the Bot'll send a message of "Trying again"
        except: 
            word = ""

    # Closing the browser
    browser.quit()

    return word
