import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/Anticonsumption/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

with open("reddit_subreddit_info.txt", "w") as file:
    account_name = soup.find(class_="flex items-center font-bold text-18 xs:text-32 mb-0")
    if account_name:
        file.write(f"Account Name: {account_name.string.strip()}\n")
    else:
        file.write("Account Name not found\n")
    ranking = soup.find("strong")
    if ranking:
        file.write(f"Ranking: {ranking.string.strip()}\n")
    else:
        file.write("Ranking not found\n")
    members = soup.find("faceplate-number")
    if members:
        file.write(f"Members: {members.attrs['number']}\n")
    else:
        file.write("Members not found\n")
    created = soup.find("faceplate-timeago")
    if created:
        file.write(f"Created Date: {created['ts'].split('T')[0]}\n")
    else:
        file.write("Created Date not found\n")
    time = soup.find("faceplate-timeago")
    if time:
        file.write(f"Time: {time['ts'].split('T')[1]}\n")
    else:
        file.write("Time not found\n")
    online = soup.find_all("faceplate-number")
    if len(online) > 1:
        file.write(f"Online Members: {online[1]['number']}\n")
    else:
        file.write("Online Members not found\n")
print("Data has been saved to 'reddit_subreddit_info.txt'.")
