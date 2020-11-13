def frase_motivacional():
    from selenium import webdriver
    from googletrans import Translator
    driver = webdriver.Chrome()
    driver.get("https://randomwordgenerator.com/motivational-quote.php")
    driver.maximize_window()
    # frase_motivacional()

    button = driver.find_element_by_xpath("//*[@id='options']/table/tbody/tr[2]/td/input[2]")
    button.click()

    txt = driver.find_element_by_class_name("support-sentence").text
    driver.close();


    print("Frase Concluida")
    trans = Translator()

    t = trans.translate(
        txt, src= 'en', dest='pt'
    )

    frase = t.text
    frase_motivacional.frase = frase
    

