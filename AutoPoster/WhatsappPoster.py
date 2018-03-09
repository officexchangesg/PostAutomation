from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
import time
import os
from urllib.parse import quote_plus

driver = webdriver.Chrome()                     # Needs to be global for all classes to use
driver.get('https://web.whatsapp.com')

class WhatsappBotConfig(object):
    last_msg = False
    last_msg_id = False

    command_history = []
    last_command = ""

    def __init__(self, contact_list):
        self.contacts = contact_list

    def get_contacts(self):
        return self.contacts

    def set_last_chat_message(self, msg, time_id):
        self.last_msg = msg
        self.last_msg_id = time_id

    def get_last_chat_message(self):
        return self.last_msg, self.last_msg_id

    def set_last_command(self, command):
        self.last_command = command
        self.command_history.append(command)

    def get_command_history(self):
        return "You have asked the following commands: " + ", ".join(self.command_history)

def send_message(msg):
    whatsapp_msg = driver.find_element_by_class_name('_2S1VP')
    whatsapp_msg.send_keys(msg)
    whatsapp_msg.send_keys(Keys.ENTER)

# Get all the contacts
def whatsapp_contacts():
    contacts = driver.find_elements_by_class_name("chat-title")

    return [contact.text for contact in contacts]

def chat_history():
    text_bubbles = driver.find_elements_by_class_name("message-out")  # message-in = receiver, message-out = sender
    tmp_queue = []

    try:
        for bubble in text_bubbles:
            msg_texts = bubble.find_elements_by_class_name("copyable-text")
            for msg in msg_texts:
                #raw_msg_text = msg.find_element_by_class_name("selectable-text.invisible-space.copyable-text").text.lower()
                # raw_msg_time = msg.find_element_by_class_name("bubble-text-meta").text        # time message sent
                tmp_queue.append(msg.text.lower())

        if len(tmp_queue) > 0:
            return tmp_queue[-1]  # Send last message in list

    except StaleElementReferenceException as e:
        print(str(e))
        # Something went wrong, either keep polling until it comes back or figure out alternative

    return False

def poll_chat(self):
    last_msg = chat_history()

    if last_msg:
        time_id = time.strftime('%H-%M-%S', time.gmtime())

        last_saved_msg, last_saved_msg_id = self.config.get_last_chat_message()
        if last_saved_msg != last_msg and last_saved_msg_id != time_id:
            self.config.set_last_chat_message(msg=last_msg, time_id=time_id)

            print(self.config.get_last_chat_message())
'''
                is_action = is_action_message(last_msg=last_msg)
                if is_action:
                    self.config.set_last_command(last_msg)
                    self.bot_options(action=last_msg)'''

class WhatsappPoster(object):
    def __init__(self):
        self.config = WhatsappBotConfig(contact_list=whatsapp_contacts())
        self.init_bot()

    def init_bot(self):
        while True:
            self.poll_chat()

if __name__ == "__main__":
    print("Bot is active, scan your QR code from your phone's WhatsApp")
    #whatsapp_contacts()
    #Bot()
    WhatsappPoster()


'''
friend_name = 'Mr Kelvin'
elem = web.find_element_by_xpath('//span[contains(text(),{friend_name})]'.format(friend_name=friend_name))
elem.click()
elem1 = web.find_elements_by_class_name('input')
while True:
    elem1[1].send_keys('hahahahahahaha')
    web.find_element_by_class_name('send-container').click()
'''

