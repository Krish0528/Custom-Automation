# import required modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Input From Place to To Place for maps
print("Google Maps")
from_place = input("Enter from place: ").title()
to_place = input("Enter to place: ").title()

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# assign url in the webdriver object
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(5)


# search locations
def searchplace():
    place = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    place.send_keys(to_place)
    submit = driver.find_element(
        By.XPATH, '//*[@id="searchbox-searchbutton"]')
    submit.click()


searchplace()


# get directions
def directions():
    sleep(10)
    direction = driver.find_element(
        By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
    direction.click()


directions()


# find place
def find():
    sleep(6)
    find = driver.find_element(
        By.XPATH, '//*[@id="sb_ifc50"]/input')
    find.send_keys(from_place)
    sleep(2)
    search = driver.find_element(
        By.XPATH, '//*[@id="directions-searchbox-0"]/button[1]')
    search.click()


find()


# get transportation details
def kilometers():
    sleep(5)
    search_bike = driver.find_element(
        By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[3]/button')
    search_bike.click()
    sleep(2)
    total_travel_time = driver.find_element(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[1]')
    total_kilometers = driver.find_element(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
    print(f"Total Kilometers: {total_kilometers.text}\nTotal Travel Time: {total_travel_time.text}")
    sleep(5)
    search_bus = driver.find_element(
        By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button')
    search_bus.click()
    sleep(2)
    bus_travel_km = driver.find_element(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
    bus_travel_time = driver.find_element(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[1]')
    print(f"Bus Travel: {bus_travel_km.text}\nBus Travel Time: {bus_travel_time.text}")
    sleep(7)
    search_train = driver.find_element(
        By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[4]/button')
    search_train.click()
    sleep(2)
    train = driver.find_element(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div')
    print("Train Travel:", train.text)
    sleep(7)


kilometers()
