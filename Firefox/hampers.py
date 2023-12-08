from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
import time


def order():
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.bunches.co.uk/hamper-delivery")

    print("Bunches hamper home page loaded 💐")

    product_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/section[2]/div[1]/div/a/img')
    product = wait.until(EC.element_to_be_clickable(product_locator))
    product.click()
    print("Hamper (Firefox) - Product Selected ✅")

    postcode_check_locator = (By.XPATH, '//html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/form/div/input')
    postcode_check = wait.until(EC.element_to_be_clickable(postcode_check_locator))
    postcode_check.send_keys('NG15 0DQ')

    check_postcode_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/form/div/div/button')
    check_postcode_button = wait.until(EC.element_to_be_clickable(check_postcode_button_locator))
    check_postcode_button.click()
    print("Hamper (Firefox) - Postcode checked  ✅")

    place_order_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/button')
    place_order_button = wait.until(EC.element_to_be_clickable(place_order_button_locator))
    place_order_button.click()
    print("Hamper (Firefox) - Place order button pressed ✅")

    message_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/textarea')
    message = wait.until(EC.element_to_be_clickable(message_locator))
    message.click()
    message.send_keys('hello world')

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[3]/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Hamper (Firefox) - Message added ✅")

    checkout_as_guest_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/button[2]')
    checkout_as_guest_button = wait.until(EC.element_to_be_clickable(checkout_as_guest_button_locator))
    checkout_as_guest_button.click()

    email_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[1]/input')
    email_input = wait.until(EC.element_to_be_clickable(email_input_locator))
    email_input.send_keys('bot@test.com')

    name_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[2]/input')
    name_input = wait.until(EC.element_to_be_clickable(name_input_locator))
    name_input.send_keys('I am not a bot, I promise')

    telephone_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[3]/input')
    telephone_input = wait.until(EC.element_to_be_clickable(telephone_input_locator))
    telephone_input.send_keys('123456789')

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/div[2]/form/div[5]/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Hamper (Firefox) - Guess account name + email filled in ✅")

    recipient_name_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[1]/input')
    recipient_name_input = wait.until(EC.element_to_be_clickable(recipient_name_input_locator))
    recipient_name_input.send_keys('Mr Bottington Bot')

    manual_address_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[2]/a')
    manual_address_button = wait.until(EC.element_to_be_clickable(manual_address_button_locator))
    manual_address_button.click()

    address_postcode_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[6]/input')
    address_postcode = wait.until(EC.element_to_be_clickable(address_postcode_locator))
    address_postcode.send_keys('NG15 0DQ')

    address_line_1_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[2]/input')
    address_line_1 = wait.until(EC.element_to_be_clickable(address_line_1_locator))
    address_line_1.send_keys('25 Bot Street')

    address_line_2_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[3]/input')
    address_line_2 = wait.until(EC.element_to_be_clickable(address_line_2_locator))
    address_line_2.send_keys('Bot Road')

    address_line_3_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[4]/input')
    address_line_3 = wait.until(EC.element_to_be_clickable(address_line_3_locator))
    address_line_3.send_keys('Bot Town')

    town_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/div/div[5]/input')
    town = wait.until(EC.element_to_be_clickable(town_locator))
    town.send_keys('Bot Town')

    time.sleep(2)

    update_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/button')
    update_button = wait.until(EC.element_to_be_clickable(update_button_locator))
    update_button.click()

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/div/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Hamper (Firefox) - Recipient address entered ✅")

    proceed_to_payment_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/span/button')
    proceed_to_payment_button = wait.until(EC.element_to_be_clickable(proceed_to_payment_button_locator))
    proceed_to_payment_button.click()

    # print("Hamper (Firefox) - Proceeded to payment page ✅")
    print(f"{Fore.GREEN}Hampers (Firefox) - Proceeded to payment page ✅{Style.RESET_ALL}")

    driver.quit()


if __name__ == '__main__':
    order()
