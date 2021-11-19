import time

from helium import *
from bs4 import BeautifulSoup

url = "https://ethermine.org/miners/72d5714e7f7da9dF3D7F064bA83EB36752b92C38/dashboard"
browser = start_chrome(url,headless=True)#
time.sleep(1)
soup = BeautifulSoup(browser.page_source, 'html.parser')

#test = soup.find_all('div', {'class': 'dashboard-overview'}) #balance card
current_balance = soup.find('span', {'class': 'current-balance'}) #balance card
current_earnings = soup.find('span', {'class': 'current-earnings'}) #balance card
print(current_balance.text)
print(current_earnings.text)


hashrate_current_average = soup.find('div', {'class': 'charts'})
#print(hashrate_current_average.text)
hashrate_current_average = hashrate_current_average.text.split(" ")
#print(hashrate_current_average)
current_hashrate =[]
average_hashrate =[]
reported_hashrate =[]
valid_shares, stale_shares, invalid_shares = [], [], []
for i in range(len(hashrate_current_average)):
    if "Current" in hashrate_current_average[i]:
        current_hashrate.append(hashrate_current_average[i+1])
    if "Average" in hashrate_current_average[i]:
        average_hashrate.append(hashrate_current_average[i+1])
    if "Reported" in hashrate_current_average[i]:
        reported_hashrate.append(hashrate_current_average[i+1])
    if "Valid" in hashrate_current_average[i]:
        valid_shares.append(hashrate_current_average[i+1])
    if "Stale" in hashrate_current_average[i]:
        stale_shares.append(hashrate_current_average[i+1])
    if "Invalid" in hashrate_current_average[i]:
        invalid_shares.append(hashrate_current_average[i+1])
print(current_hashrate, average_hashrate, reported_hashrate)
print(valid_shares, stale_shares, invalid_shares)

miners_stats = soup.find('div', {'class': 'table-container'})
print(miners_stats)
miners_stats = miners_stats.text.split(" ")

miners = ["kaelas_first_miner", "testdesktop"]
miners_reported_hashrate =[]
miners_current_hashrate =[]
miners_valid_shares, miners_stale_shares, miners_invalid_shares = [], [], []
test = []
for miners_count in range(len(miners)):
    for i in range(len(miners_stats)):
        if miners[miners_count] in miners_stats[i]:
            test.append(miners_stats[i])
            break
print(test)
b = test[0].replace(miners[0], '')
print(b)

test








#for item in soup.find('div', {'class': 'stat-card-body'}):
   # print(item)


