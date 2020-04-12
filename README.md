# CardmarketEggSearch
This python script is for automating the tedious task of locating the hidden easter egg during the 2020 [Cardmarket easter egg hunt](https://www.cardmarket.com/en/Vanguard/News/Cardmarket-Easter-Eggs-Have-Arrived).  
The script automatically finds the hidden easter egg by searching through each unique product page for a single game. It searches for the egg via it's css style and img src url. When found the script will stop searching and output into a text file the product page where the egg is located.

## Guide
1. Install requirements with `pip install -r requirements.txt`
2. Run the script with `py EggSearch.py`
3. Follow the script prompts

## FAQ
How to get your cookie values:
* Login to [Cardmarket](https://www.cardmarket.com/en/) on a browser
* Inspect element and navigate to the Storage tab for Firefox, or Application for Chrome
* Here you'll find the values for `__cfduid` and `PHPSESSID`

How to get your User-Agent value:
* Inspect element and navigate to the network tab
* Visit a new page to generate a request in the network log
* Click on the request and scroll down to Request headers
* Here you'll find the User-Agent value used in the request
  * Example: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36`

## Troubleshooting
Q: I keep getting ` -- Not Logged In! -- `  
A: Make sure the cookies you provide the script are when your logged into Cardmarket and that the User-Agent value is also the same as the one which was used when logging into Cardmarket.
