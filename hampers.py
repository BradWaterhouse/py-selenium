from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


def order():
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 10)

    driver.set_window_position(2000, 0)
    driver.set_window_size(1100, 1200)

    driver.get("https://www.bunches.co.uk/hamper-delivery")

    print("Bunches hamper home page loaded 💐")

    time.sleep(10)

    product = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/section[2]/div[1]/div/a/img')
    product.click()
    print("Hamper - Product Selected ✅")
    time.sleep(1)

    postcode_check = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/div[2]/div/form/div/div[1]/input')
    postcode_check.send_keys('NG15 0DQ')
    check_postcode_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/div[2]/div/form/div/div[2]/button')
    check_postcode_button.click()
    print("Hamper - Postcode checked  ✅")
    time.sleep(0.5)


    place_order_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/div[2]/button')
    place_order_button.click()
    time.sleep(1)
    print("Hamper - Place order button pressed ✅")

    message = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/textarea')
    message.click()
    message.send_keys('hello world')
    continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[3]/button')
    continue_button.click()
    print("Hamper - Message added ✅")

    checkout_as_guest_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/button[2]')
    checkout_as_guest_button.click()

    time.sleep(0.5)

    email_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[1]/input')
    email_input.send_keys('bot@test.com')
    name_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[2]/input')
    name_input.send_keys('I am not a bot, I promise')
    telephone_input = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[3]/input')
    telephone_input.send_keys('123456789')
    continue_button = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[5]/button')
    continue_button.click()
    print("Hamper - Guess account name + email filled in ✅")

    time.sleep(0.5)

    recipient_name_input = driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[1]/input')
    recipient_name_input.send_keys('Mr Bottington Bot')
    manual_address_button = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[2]/a')
    manual_address_button.click()

    address_line_1 = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[2]/input')
    address_line_1.send_keys('25 Bot Street')
    address_line_2 = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[3]/input')
    address_line_2.send_keys('Bot Road')
    address_postcode = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[6]/input')
    time.sleep(1)
    address_postcode.send_keys('NG15 0DQ')

    update_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/button')
    update_button.click()

    continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/div/button')
    continue_button.click()
    print("Hamper - Recipient address entered ✅")

    proceed_to_payment_button = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/span/button')
    proceed_to_payment_button.click()

    print("Hamper - Proceeded to payment page ✅")

    time.sleep(4)

    driver.close()
