
import requests
import json

url = "https://gtest2.amocrm.ru/oauth2/access_token"

payload = json.dumps({
  "client_id": "d67dc85e-ba1e-45c1-8dfd-6845326fba5e",
  "client_secret": "bGA4rMK4XXxvOIdFsMRsAxWiKdLfkJZNLMdnoasb4VNv4BDq0tM5ejtF8UmfBjCs",
  "grant_type": "authorization_code",
  "code": "def5020040df037be86b7c7d68e559a21cf77e2f680abd15cd9f9a8e7a2c39312cab65f0338ccfabf0dc1689773040a16e48fc7417691159d8cae7051a025cbb578f572401aa59c5b73754f1b7476af9d905cbbc3aa61ffb59ea6cd7ebd2d132cab0490807fe117d09e57318f4f1233f796505d8ff89820ddc39c91475ab6e658a1beba21d04320998c3b51f84e739ab43b5690c7b6ff331e563fdcceda0b9babeb736459d090fe7ba34e57d5d666e80b559958ba730c15b3e681e781bf4e026aada7b415a6c1d44c376c74fb4136cf96d4aa6dcf3c7a5b2c4a8b874587376aa80dc5f8625dd8ed0015c5e02ac648eeab8c123697c2449d7f6fece438eb317ca0004a7f2e335ace74020a9ed0eeff39de2dd428ec60cee9199f00a4f5d9b7ccb3231b5142b53be5a65aaf3e5e4b4245bea05fd95a7bcfca91c055d16a346fa780c8005446ec12c91b4e55d23377a4851519891adb05f31df614454821718aad423964432e507ae35b7506e262dd4dcaeb56a582d660ce0e7c634847e46dfa499fc42bada11044b7fb39aaf071d6d678d50aff43b241f7ab6e7bf320b53b1bda917f111c6843aab0b361ea24aa4d8b5cbf1518dffccb24ec27a22c2",
  "redirect_uri": "https://amocrm.ru"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'user_lang=ru'
}

response = requests.post(url, headers=headers, data=payload)


