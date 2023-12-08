from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def order():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    # driver.set_window_position(2000, 0)
    # driver.set_window_size(1100, 1200)

    driver.get("https://www.bunches.co.uk/category/birthday-cards")

    print("Bunches card home page loaded 💐")

    product_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[5]/div[2]/div/a')
    product = wait.until(EC.presence_of_element_located(product_locator))
    product.click()
    print("Card (Chrome)  - Product Selected ✅")

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Card (Chrome) - Size picked ✅")

    place_order_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/button')
    place_order_button = wait.until(EC.element_to_be_clickable(place_order_button_locator))
    place_order_button.click()
    print("Card (Chrome) - Place order button pressed ✅")

    message_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div')
    message = wait.until(EC.element_to_be_clickable(message_locator))
    message.click()
    message.send_keys('hello world')

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[1]/section/div[4]/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Card (Chrome) - Message added ✅")

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
    print("Card (Chrome) - Guess account name + email filled in ✅")

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

    update_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/form/button')
    update_button = wait.until(EC.element_to_be_clickable(update_button_locator))
    update_button.click()

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/div/div/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Card (Chrome) - Recipient address entered ✅")

    proceed_to_payment_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/span/button')
    proceed_to_payment_button = wait.until(EC.element_to_be_clickable(proceed_to_payment_button_locator))
    proceed_to_payment_button.click()

    print("Card (Chrome) - Proceeded to payment page ✅")

    driver.close()


if __name__ == '__main__':
    order()
