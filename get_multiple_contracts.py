
import time
import pyperclip
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os
load_dotenv()


def delete_extra_info(entrance):
    try:
        pattern = r'pragma.*;' \
                  r'|import.*;' \
                  r'|// SPDX-License-Identifier:.*\n'
        return True, re.sub(pattern, "", entrance)
    except:
        return False, entrance

def writeTheData(file, entrance, index):
    preEntrance = "\n\n\n//####################################################################     " + str(index) + ".\n\n"
    patternStatus, entrance = delete_extra_info(entrance)

    file.write(preEntrance)

    try:
        file.write(entrance)
        return patternStatus, True
    except:
        return patternStatus, False

def saveTheData(check, file, entrance, actualIndex):
    if check == True:
        patternStatus, writeStatus = writeTheData(file, entrance, actualIndex)

        if patternStatus == True and writeStatus == True:
            situation = "OKAY"
        elif patternStatus == True and writeStatus == False:
            situation = "write ERROR!"
        elif patternStatus == False and writeStatus == True:
            situation = "replace ERROR!"
        else:
            situation = "replace and write ERROR!"

        print("###########################################      Contract: ", actualIndex, "   status: ", situation)
        print(" ")
        print(" ")
    else:
        print("###########################################      Contract", actualIndex, "   status: Call ERROR!")
        print(" ")
        print(" ")

def scrollWebpage(driver, n):
    input_a = "window.scrollTo(0,"
    input_b = ");"
    complete_input = input_a + str(n) + input_b
    # Scroll down to bottom
    driver.execute_script(complete_input)
    # Wait to load page
    time.sleep(0.39)

def callTheElement(driver, textillo):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, textillo))).click()
        return True, pyperclip.paste()
    except:
        return False, None

def executeTheCode(driver, nContracts, nIncrements, solFileNameToCompile):
    pathToSaveTheFile = os.getenv("WORK_PATH")
    fileName = pathToSaveTheFile + solFileNameToCompile + ".sol"
    f = open(fileName, "a")

    pattern_a = 'div.d-flex:nth-child('
    pattern_b = ') > span:nth-child(2) > a:nth-child(1) > i:nth-child(1)'

    increment = nIncrements
    counter = increment

    for i in range(nContracts):
        textillo = pattern_a + str((i + 1) * 3) + pattern_b

        if i == 0:
            toCheck, gotten = callTheElement(driver, textillo)
            counter += increment
            saveTheData(toCheck, f, gotten, i + 1)
            continue

        scrollWebpage(driver, counter)
        toCheck, gotten = callTheElement(driver, textillo)
        counter += increment
        saveTheData(toCheck, f, gotten, i + 1)

    f.close()




def scraperWebDriver(url_link, nContracts, nPixelsIncrements, solFileNameToCompile):
    driver = webdriver.Firefox(
        executable_path=os.getenv("DRIVER_PATH"))

    driver.get(url_link)
    driver.maximize_window()
    time.sleep(4)

    executeTheCode(driver, nContracts, nPixelsIncrements, solFileNameToCompile)
    driver.quit()

def main(input_url, nContracts, nPixelsIncrements, solFileNameToCompile):
    # search = driver.find_element_by_css_selector(textillo_2)
    # search.click()

    print("----------------     Contract: ", solFileNameToCompile)
    scraperWebDriver(input_url, nContracts, nPixelsIncrements, solFileNameToCompile)







if __name__ == "__main__":
    ## Note: You scroll down, but just a little bit, almost nothing before the program starts to execute
    url = "https://etherscan.io/address/0x20e5e35ba29dc3b540a1aee781d0814d5c77bce6#code"
    number_of_contracts = 13
    pixels = 392
    file_name = "TransparentUpgradeableProxy"

    main(url, number_of_contracts, pixels, file_name)
