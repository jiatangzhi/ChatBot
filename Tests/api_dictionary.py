import requests
import json

app_id = "4b11e51d"
app_key = "2f0e4476e477e029212ade1463481b90"
while True:
    chose = input("\nDo you want to write a word or a sentence? (type 1 for a word or 2 for a sentence): \n")
    while True:
        if chose == "1":
            word_id = input("\nEnter a Word: \n")
            if word_id != "":
                break 
        elif chose == "2":
            word_id = input("\nEnter a Sentence: \n")
            if word_id != "":
                break 
        else:
            chose = input("\nWrite just 1 for a word or 2 for a sentence please: \n")

    endpoint = "entries"
    language = "en-gb"
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/' + endpoint + '/'  + language + '/'  + word_id.lower()

    r = requests.get(url, headers={"app_id": "4b11e51d", "app_key": "2f0e4476e477e029212ade1463481b90"})
    
    oxford_dict = json.loads(json.dumps(r.json()))

    x = json.dumps(r.json())
    error = '{"error": "No entry found matching supplied source_lang, word and provided filters"}'
    if x != error:

        print("\nCategory: ")             
        print(oxford_dict["results"][0]["lexicalEntries"][0]["lexicalCategory"]["text"])
        print("\nDefiniton: ")
        definition = oxford_dict["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
        print(definition)
        print("\nExample: ")
        if len(word_id) == 1:               
            print("None")
        else:
            print(oxford_dict["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"] + "\n")
            print(v["definitions"])
        break
    else:
        print("\nError, None Result!")