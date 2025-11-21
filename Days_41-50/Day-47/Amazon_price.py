import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/Samsung-Odyssey-LS27CG552EUXXU-Gaming-Monitor/dp/B0CP851QXD/?_encoding=UTF8&pd_rd_w=UO7Xs&content-id=amzn1.sym.680698ed-bc66-46f2-85ad-886c3afe07e6&pf_rd_p=680698ed-bc66-46f2-85ad-886c3afe07e6&pf_rd_r=1PSCD16DWZ595R1V8ZAG&pd_rd_wg=4oAhW&pd_rd_r=de074a26-2c11-488e-a30a-de5dd39d8e3b&ref_=pd_hp_d_atf_th_BFW25&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the price element
item_name = soup.find(id="productTitle").get_text().strip()
price_whole = soup.find(class_="a-price-whole")
price_fraction = soup.find(class_="a-price-fraction")
if price_whole and price_fraction:
    price = float(price_whole.get_text() + price_fraction.get_text())
    print(f"Current price: £{price} for {item_name}")
    
    if price < 100:
        print("📧 Email sent: Great deal! Instant Pot is now $" + str(price))
    else:
        print("Don't buy it yet")
else:
    print("Price not found")
