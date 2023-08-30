import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

cookies = {
    "JSESSIONID": "",  # <-- compila ES: "f4AxEaIO7IjmcPjNeKXr9BHI"
    "AGPID": "",  # <-- compila ES: "Ade5J5oLxwqzt4Ns2qRrUQ$$"
    "AGPID_FE": "",  # <-- compila ES: "Ade5J5oGBeqzt4Ns2qRrUQ$$"
}
Struttura = "" # Stessa descrizione che è riportata nella struttura scelta nel menù strutture ES: "Commissariato Portogruaro"
exclude_time = [] # orari che non si volgiono ES: ["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00"]
driver = webdriver.Firefox()

driver.get("https://www.passaportonline.poliziadistato.it/CittadinoAction.do?codop=backToIndex")
for cookie in cookies.keys():
    driver.delete_cookie(cookie)
    driver.add_cookie({"name": cookie, "value": cookies[cookie], "domain": "www.passaportonline.poliziadistato.it", "path": "/"})

driver.get("https://www.passaportonline.poliziadistato.it/CittadinoAction.do?codop=backToIndex")
driver.find_element(By.CSS_SELECTOR, '.button_l.inlinea').click()
#debug
#driver.get("https://www.passaportonline.poliziadistato.it/CittadinoAction.do?codop=resultRicercaRegistiProvincia&provincia=VE")
###
print("Controllo che la struttura abbia disponibilità...")
while True:
    try:
        strutt_tag = driver.find_element(By.XPATH, "//*[contains(text(), '" + Struttura + "')]").find_element(By.XPATH, "..")
    except:
        sys.exit('Struttura non trovata! ricontrolla il nome')
    proceed = strutt_tag.find_element(By.CSS_SELECTOR, '.seleziona>a>img')
    print(proceed.get_property("src"))
    if "img/go_dettaglio_storico.png" in proceed.get_property("src"):
        proceed.click()
        print("La struttura '"+Struttura+"' ha disponibilità procedo a cercare le date")
        break
    print("La struttura '"+Struttura+"' non ha disponibilità, ricontrollo tra 10s")
    sleep(10)
    driver.refresh()
    sleep(2)
while True:
    sleep(5)
    links = driver.find_elements(By.CSS_SELECTOR, '.fascia')
    for link in links:
        text = link.get_attribute("innerText")
        tag_id = link.get_attribute("id")
        time = tag_id.split(":")[0].split("-")[-1]  # id_18092023-5_mercoledi-8.00:10:10
        if time in exclude_time:  # esculdi link non nel range del tempo
            continue
        if text != "Non prenotabile" and text != "Non disponibile" and text != "Festivo":
            print("trovato!")

            link.click()

            button = driver.find_element(By.CSS_SELECTOR, ".button_l")
            button.click()

            email = driver.find_element(By.CSS_SELECTOR, "#email").get_property("value")
            email_confirm = driver.find_element(By.CSS_SELECTOR, "#email2")
            email_confirm.send_keys(email)

            button2 = driver.find_element(By.CSS_SELECTOR, "#btnSub")
            button2.click()
            input()
    print("Nessuna disponibilità trovata, ritento in 10s")
    sleep(10)
    driver.refresh()
input()
