from selenium import webdriver
import time

class WhastAppBot:
    def __init__(self):
        self.msg = "teste, zap bot python"
        self.grps = ["Fã clube do Romanelli"]
        option = webdriver.ChromeOptions()
        option.add_argument("lang=pt-bt")
        self.driver = webdriver.Chrome(executable_path=r'./Driver/chromedriver.exe')


    def EnviarMensagens(self):
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(20)
        for g in self.grps:
            #click no chat
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{g}']")
            time.sleep(2)
            grupo.click()

            #click na caixa de texto
            chatBox = self.driver.find_element_by_class_name("DuUXI")
            time.sleep(2)
            chatBox.click()
            #digitar mensagem
            chatBox.send_keys(self.msg)

            #click no botao enviar
            btnEnviar = self.driver.find_element_by_xpath("//span[@data-testid='send']")
            time.sleep(2)
            btnEnviar.click()

            time.sleep(5)

bot = WhastAppBot()
bot.EnviarMensagens()