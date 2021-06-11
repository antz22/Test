from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import os

driver = webdriver.Chrome()
driver.get("https://www.malacards.org/")

iput = open("inputTextDiagnosis.txt", "r")
oput = open("outputText.txt", "w")

rawRawDiagnosis = iput.read() # Common Cold
diagnosis = rawRawDiagnosis.title() # Common Cold

driver.find_element_by_xpath('//*[@id="search-box-input"]').send_keys(diagnosis)
driver.find_element_by_xpath('//*[@id="the-basics2"]/div[3]/input').click()  
driver.find_element_by_link_text(diagnosis).click()
textInSummary = []
textInSummary = driver.find_element_by_xpath('//*[@id="Summary"]').text

numberOfTimesSeenPunctuation = 0
i = 0

while True:
	if numberOfTimesSeenPunctuation == 4:
		break
	if textInSummary[i] == '?' or textInSummary[i] == '.' or textInSummary[i] == '!':
		numberOfTimesSeenPunctuation += 1
	oput.write(textInSummary[i])
	i += 1


iput.close()
oput.close()