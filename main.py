from selenium import webdriver
from selenium.webdriver import ActionChains
from decouple import config
import time

chromeDriver = "G:\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(chromeDriver)
driver.get("https://www.spire.umass.edu/psp/heproda/?cmd=login&languageCd=ENG")

actions = ActionChains(driver)

id_box = driver.find_element_by_id('userid')
id_box.send_keys(config('SPIRE-USERID'))

pwd_box = driver.find_element_by_id('pwd')
pwd_box.send_keys(config('SPIRE-PWD'))

login_button = driver.find_element_by_name('Submit')
login_button.click()

time.sleep(5)
student_home_button = driver.find_element_by_xpath("//*[@id=\"pthnavbca_UM_STUDENT_HOME\"]")
student_home_button.click()

time.sleep(2)
class_schedule_button = driver.find_element_by_link_text('Class Schedule')
class_schedule_button.click()

time.sleep(2)
classes_list = driver.find_element_by_xpath('//*[@id="win0divSTDNT_ENRL_SSV2$0"]')
