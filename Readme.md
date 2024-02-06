
# AGGIORNAMENTO 06/02/2024
**il sito del ministero è stato aggiornato, questo script non è stato testato per la nuova versione, potrebbe non funzionare.**

  A meno di contributi tramite PR, questo script non verrà aggiornato

***
# Passaporto Sniper Bot

Non sono responsabile dell'uso da parte di terzi di questo software, che è stato creato esclusivamente a scopi didattici.


https://github.com/AlexZorzi/PassaportoBot/assets/47613715/84e53a81-ea9c-4105-a728-13bb6db0de73



# Guida
1) andare su https://www.passaportonline.poliziadistato.it ed accedere con SPID
2) Inserire richiedente
3) Aprire modalità developer/ispeziona del browser, su Chrome `Ctrl+Shift+J` oppure tasto destro ispeziona. Firefox `Ctrl+Shift+I`
4) Cliccare sulle due freccie e poi su Applicazione
   
    ![image](https://github.com/AlexZorzi/PassaportoBot/assets/47613715/b1e58344-7c10-4612-a9e2-690c023030ea)

5) Copiare i valori dei cookies `JSESSIONID`, `AGPID`, `AGPID_FE`

    ![image](https://github.com/AlexZorzi/PassaportoBot/assets/47613715/342c10e4-6c2b-4740-a933-8f991b0873e8)

6) Incollare i valori in main.py

    ![image](https://github.com/AlexZorzi/PassaportoBot/assets/47613715/ba055786-300b-4538-b979-5be2a009126c)
   
8) Installare Firefox, scarica pachetto a https://www.mozilla.org/it/firefox/new/
9) Installare Python3, scarica pachetto a https://www.python.org/downloads/
10) Installa Selenium con pip, `pip install selenium`
11) Scegliere copiare ed inserire in main.py il nome della struttura desiderata (I nomi si trovano nel campo descrizione in "inserisci appuntamento"

    ![image](https://github.com/AlexZorzi/PassaportoBot/assets/47613715/1d99b2dd-7800-43df-bf55-632c3aa91525)

12) Avvia programma `python main.py`
