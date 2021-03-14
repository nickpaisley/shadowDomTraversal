import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/nicholas.paisley/tools/chromedriver89")

#define inception function
#this allows a Shadow Root to be expanded to search elements.
def expand_shadow_element(element):
  
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root


driver.get("https://www.chromestatus.com/features/schedule")

time.sleep(5)

#this expands the shadow-root who's section is 'chromedash-schedule'
root1 = driver.find_element_by_tag_name('chromedash-schedule')
shadow_root1 = expand_shadow_element(root1)

#search for specific titles in the expanded shadow-root
rootVersionStable = shadow_root1.find_element_by_css_selector("a[title*='Download Chrome stable']")
print('rootVersionStable')
print(rootVersionStable.get_attribute('innerText'))

rootVersionNextUp = shadow_root1.find_element_by_css_selector("a[title*='Download Chrome Beta']")
print('rootVersionNextUp')
print(rootVersionNextUp.get_attribute('innerText'))

rootVersionDev = shadow_root1.find_element_by_css_selector("a[title*='Download Chrome Canary']")
print('rootVersionDev')
print(rootVersionDev.get_attribute('innerText'))

#still haven't been able to target specific dates, so we are itterating through all classes named 'release-stable'
#and adding them to a list. The 2nd element of the allDates list will be the 'Next Up' browser release date.
allDates = []
allDates = shadow_root1.find_elements_by_css_selector("span[class*='release-stable']")

for dates in allDates:
    print(dates.get_attribute('textContent'))

driver.close()    


