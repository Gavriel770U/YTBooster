from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def click_play_video_button(driver) -> None:
    play_video_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[4]/button')
    play_video_button.click()

def run_ytbooster() -> None:
    video_urls = ['your videos urls here']
  
    driver = webdriver.Chrome()
    driver.maximize_window()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    start = True
    tab_counter = 0

    for url in video_urls:
        if start:
            driver.get(url)
            start = False
        else:
            new_tab_name = "tab"+str(tab_counter)
            driver.execute_script(f"window.open('about:blank','{new_tab_name}');")
            driver.switch_to.window(new_tab_name)
            driver.get(url)
            tab_counter+=1
        driver.execute_script("window.document.mute = true;")

        try:
            click_play_video_button(driver)
        except:
            print("No need of play button")

    time.sleep(22+len(video_urls))

    driver.close()