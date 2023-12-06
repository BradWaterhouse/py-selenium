from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def order():
    driver = webdriver.Firefox()

    driver.set_window_position(2000, 0)
    driver.set_window_size(1100, 1200)

    driver.get("https://www.bunches.co.uk")

    print("Bunches home page loaded 💐")

    time.sleep(10)

    product = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/section[2]/div[1]/div/a/img')
    product.click()
    print("Flowers - Product Selected ✅")
    time.sleep(1)

    continue_button = driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/section[2]/div[4]/div[2]/button')
    continue_button.click()
    time.sleep(1)
    print("Flowers - Variant picked ✅")

    place_order_button = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[4]/div[2]/div[3]/button')
    place_order_button.click()
    time.sleep(1)
    print("Flowers - Place order button pressed ✅")

    skip_button = driver.find_element(By.XPATH, '//*[@id="extras"]/div/div[3]/button')
    skip_button.click()
    time.sleep(1)
    print("Flowers - Extras Skipped ✅")

    card_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/button')
    card_select.click()
    free_card = driver.find_element(By.XPATH, '/html/body/dialog/div/div/div[2]/div[3]/button')
    free_card.click()
    time.sleep(1)
    print("Flowers - Default Card Selected ✅")

    message = driver.find_element(By.XPATH,
                                  '// *[ @ id = "message"] / section / div[1] / div[1] / div[2] / div[3] / div[2] / div / div / div')
    message.click()
    message.send_keys('hello world')
    continue_button = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/main/div[3]/section[3]/section/div[4]/button[2]');
    continue_button.click()
    print("Flowers - Message added ✅")

    checkout_as_guest_button = driver.find_element(By.XPATH, '//*[@id="details"]/div/div[2]/form/button[2]')
    checkout_as_guest_button.click()

    time.sleep(0.5)

    email_input = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[1]/input')
    email_input.send_keys('bot@test.com')
    name_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[2]/input')
    name_input.send_keys('I am not a bot, I promise')
    telephone_input = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[3]/input')
    telephone_input.send_keys('123456789')
    continue_button = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[5]/button')
    continue_button.click()
    print("Flowers - Guess account name + email filled in ✅")

    time.sleep(0.5)

    recipient_name_input = driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[1]/input')
    recipient_name_input.send_keys('Mr Bottington Bot')
    manual_address_button = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[2]/a')
    manual_address_button.click()

    address_line_1 = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[2]/input')
    address_line_1.send_keys('25 Bot Street')
    address_line_2 = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[3]/input')
    address_line_2.send_keys('Bot Road')
    address_postcode = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[6]/input')
    time.sleep(1)
    address_postcode.send_keys('NG15 0DQ')

    update_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/button')
    update_button.click()

    continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/div/button')
    continue_button.click()
    print("Flowers - Recipient address entered ✅")

    proceed_to_payment_button = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[1]/main/div[3]/section[6]/div/div[2]/span/button')
    proceed_to_payment_button.click()

    time.sleep(2)

    print("Flowers - Proceeded to payment page ✅")

    time.sleep(4)

    driver.close()
