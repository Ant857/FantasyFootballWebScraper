from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import requests

url = "https://www.fantasypros.com/nfl/start/"

#create seperate lists sorting players into lists by positions
qbs = []
rbs = []
wrs = []
tes = []
ks = []
injured = []
questionable = []

def main():
    #loop through all players
    for i in sys.argv[1:]:
        print(i.replace("_", " "))
        #determine if players are injured --done
        #leave out players who are on ir --done
        #include players that are questionable --done
        #put questionable players into list to later display warning --done
        #put injured players into list to later display warning --done
        #remove if players are out
        html = urlopen("https://www.espn.com/nfl/injuries").read()
        soup = BeautifulSoup(html, features="lxml")
        player = soup.find("a", class_="AnchorLink", text=i.replace("-", " "))
        if player is not None:
            playerName = soup.find("a", class_="AnchorLink", text=i.replace("-", " ")).getText()
            status = player.parent.parent.getText()
            if "Injured Reserve" in status:
                injured.append(playerName)
            else:
                pos = player.parent.find("td", class_="col-pos Table__TD").getText()
                if "Questionable"  in status:
                    questionable.append(playerName)
                    if pos == "QB":
                        qbs.append(playerName)
                    elif pos == "RB":
                        rbs.append(playerName)
                    elif pos == "WR":
                        wrs.append(playerName)
                    elif pos == "TE":
                        tes.append(playerName)
                    elif pos == "PK":
                        ks.append(playerName)
        else:
            html = urlopen("https://www.fantasypros.com/nfl/players/" + i.lower() + ".php").read()
            soup = BeautifulSoup(html, features="lxml")
            bio = soup.find("div", class_="pull-left primary-heading-subheading")
            playerName = bio.find("h1").getText()
            pos = bio.find("h2").getText()
            if "QB -" in pos:
                qbs.append(playerName)
            elif "RB -" in pos:
                rbs.append(playerName)
            elif "WR -" in pos:
                wrs.append(playerName)
            elif "TE -" in pos:
                tes.append(playerName)
            elif "K - " in pos:
                ks.append(playerName)
            

    print("Quarter Backs: ")
    for qb in qbs:
        print(qb)
    print("Running Backs: ")
    for rb in rbs:
        print(rb)
    print("Wide Receivers: ")
    for wr in wrs:
        print(wr)
    print("Tight Ends: ")
    for te in tes:
        print(te)
    print("Kickers: ")
    for k in ks:
        print(k)

def open_browser():
    driver = webdriver.Chrome()
    driver.get(url)

def find_comparison():

    #take two players from the same position
    
    return player1, player2

def compare():
    driver.find_element_by_id('fast1').send_keys(player1)
    driver.find_element_by_id('fast2').send_keys(player2)


def warnings():
    #iterate through injured and questionable players and display a warning
    pass
if __name__ == "__main__":
   main()
