username = input("Coloque o nome do usuário: ")
def start_frog():
    input("Aperte Enter após o Código QR")
    name = username
    msg = "<Status> Servidor Iniciado! Aguarde"
    count = 1

    user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
    print("Success")

def send_time():
    # from datetime import datetime
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")

    from getword import frase_motivacional
    frase_motivacional()
    current_time = frase_motivacional.frase

    name = username
    msg = name + " não fique triste! Fique com uma frase motivacional: " + current_time
    count = 1

    user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
start_frog()
