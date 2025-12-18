import requests
 
word = input("Enter a word: ")
 
response = requests.get(f"https://api.datamuse.com/words?sl={word}")
data = response.json()
 
for list in data:
    print(list['word'])
 