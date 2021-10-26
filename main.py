from selenium import webdriver 
import time 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import  pyautogui

url = 'https://emulator.tp-link.com/EMULATOR_WR840NV4_BR/index.htm'
pyautogui.PAUSE = 1.0

def input_settings():
    settings  = []
    settings.append(pyautogui.prompt('Usuário PPPoE:'))
    settings.append(pyautogui.password('Senha PPPoE'))
    settings.append(pyautogui.prompt('Nome rede Wireless:'))
    settings.append(pyautogui.password('Senha Wireless'))
    return settings

def init():
    settings = input_settings()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    return settings

def setup_wan(user_ppoe,pass_ppoe):
    time.sleep(3)
    pyautogui.click(x=53, y=241)  #Rede
    pyautogui.click(x=662, y=306) #Tipo de conexão 
    pyautogui.click(x=579, y=394) #PPoE
    pyautogui.click(x=570, y=355) # User_PPoE
    pyautogui.typewrite(user_ppoe)
    pyautogui.click(x=570, y=392) # Senha_PPoE
    pyautogui.typewrite(pass_ppoe)
    pyautogui.click(x=570, y=425) # Confirm_senha_PPoE
    pyautogui.typewrite(pass_ppoe)
    pyautogui.tripleClick(x=969, y=708) #Scroll
    pyautogui.click(x=662, y=660) # Salvar

def setup_wireless(ssid_wifi,pass_wifi):
    pyautogui.click(54,343) #Wireless
    pyautogui.tripleClick(x=617, y=321) # User_WiFi
    pyautogui.typewrite(ssid_wifi)
    pyautogui.click(x=615, y=526) # Salvar

    pyautogui.click(54,343) #Segurança Wireless
    pyautogui.click(311,380) #WPA/WPA2
    pyautogui.tripleClick(x=603, y=458) # Senha_WiFi
    pyautogui.typewrite(pass_wifi)
    pyautogui.click(x=969, y=680) #Scroll
    pyautogui.click(x=621, y=664) # Salvar

def main():
    settings = init()
    setup_wan(settings[0],settings[1])
    setup_wireless(settings[2],settings[3])
main()