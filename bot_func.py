from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from time import sleep


def getRaceText(wd):

    uns = None
    first = None
    last = None
    res = None

    while first == None and last == None:
        try:
            #wd.find_element_by_xpath('//*[@title="Keyboard shortcut: Ctrl+Alt+O"]').click()
            uns = wd.find_elements_by_xpath('//*[@unselectable="on"]')
            
            if (len(uns) < 1):
                continue
            
            if (len(uns) >= 3 and first == None):
                first = uns[0].text
                first += uns[1].text
                last = uns[len(uns) - 1].text
                res = first + " " + last
            else:
                if (first == None and last == None):
                    first = uns[0].text
                    last = uns[len(uns) - 1].text
                    res = first + " " + last
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException) as ex:
            pass
        
        sleep(1)
    return res

def waitForGameToStart(wd, txt):

    status = wd.find_element_by_class_name("gameStatusLabel")

    while status.text != "The race is on! Type the text below:":
        status = wd.find_element_by_class_name("gameStatusLabel")
        sleep(0.1)

    for letter in txt:
        wd.find_element_by_class_name("txtInput").send_keys(letter)
    
    wd.find_element_by_class_name("txtInput").send_keys(" ")
    
    

def hasGameStarted(wd):
    if (wd.find_element_by_class_name("gameStatusLabel").text == "The race is on! Type the text below:"):
        return True
    else:
        return False