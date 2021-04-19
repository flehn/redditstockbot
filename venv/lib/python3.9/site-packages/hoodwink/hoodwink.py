#import/dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#NOTE: data may be slightly delayed in current version of Hoodwink, as logging-in is not yet supported!


class HoodwinkDriver:

    def __init__(self, chromedriver_path):
        #webdriver options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    #get full name from ticker symbol
    def getFullName(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/h1").text
        except:
            raise Exception("ERROR: Couldn't get full name.")
        self.browser.close()

    #get description
    def getDescription(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[1]/h3").text
        except:
            raise Exception("ERROR: Couldn't get description.")
        self.browser.close()

    #get list of tags/collections
    def getCollections(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            collections_div = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[4]/div")
            collections_a_tags = collections_div.find_elements_by_tag_name('a')
            collections = []
            for a in collections_a_tags:
                try:
                    collection = a.get_attribute('href')
                    collections.append(collection)
                except:
                    pass
            return collections
        except:
            raise Exception("ERROR: Couldn't get collections.")
        self.browser.close()
             

    #get number of owners of stock on RH
    def getOwnerCount(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return int(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/div/a/div/div/span/span/span").text.replace(',',''))
        except:
            raise Exception("ERROR: Couldn't get owner count.")
        self.browser.close()
        
    #get current price
    def getPrice(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            price = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/span[2]").text
            return float(price[1:])
        except:
            raise Exception("ERROR: Couldn't get current price.")
        self.browser.close()

    #get percentage change in price (periods: daily, weekly, monthly, 3-month, annual, 5-year)
    def getPercentChange(self, ticker, period="daily"):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            if period == "daily" or period == "1d" or period == "today":
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
            elif period == "weekly" or period == "1w" or period == "week":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[2]").click()
                time.sleep(0.5)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
            elif period == "monthly" or period == "1m" or period == "1-month":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[3]").click()
                time.sleep(0.5)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
            elif period == "3-month" or period == "3m":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[4]").click()
                time.sleep(0.5)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
            elif period == "annual" or period == "year" or period == "1-year" or period == "1yr" or period == "yr":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[5]").click()
                time.sleep(0.5)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
            elif period == "5-year" or period == "5yr":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[6]").click()
                time.sleep(0.5)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
                change = change.replace('%','')
                change = change.replace('(','')
                change = change.replace(')','')
                return float(change)
        except:
            raise Exception("ERROR: Couldn't get percentage price change.")
        self.browser.close()

    #get numeric price change in USD (periods: daily, weekly, monthly, 3-month, annual, 5-year)
    def getNumericChange(self, ticker, period="daily"):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            if period == "daily" or period == "1d" or period == "today":
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
            elif period == "weekly" or period == "1w" or period == "week":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[2]").click()
                time.sleep(0.75)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
            elif period == "monthly" or period == "1m" or period == "1-month":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[3]").click()
                time.sleep(0.75)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
            elif period == "3-month" or period == "3m":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[4]").click()
                time.sleep(0.75)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
            elif period == "annual" or period == "year" or period == "1-year" or period == "1yr" or period == "yr":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[5]").click()
                time.sleep(0.75)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
            elif period == "5-year" or period == "5yr":
                self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[6]").click()
                time.sleep(0.75)
                change = self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
                change = change.replace('$','')
                return float(change)
        except:
            raise Exception("ERROR: Couldn't get numeric price change.")
        self.browser.close()

    #get market cap (AS STRING)
    def getMarketCap(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[1]/div[3]").text
        except:
            raise Exception("ERROR: Couldn't get market cap.")
        self.browser.close()
            
    #get today's open price (AS FLOAT IN USD)
    def getOpen(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[7]/div[3]").text[1:])
        except:
            raise Exception("ERROR: Couldn't get open price.")
        self.browser.close()

    #get high (periods: today, 52w)
    def getHigh(self, ticker, period="today"):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            if period == "today" or period == "day" or period == "daily" or period == "1d":
                high = float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[5]/div[3]").text[1:])
            elif period == "52w" or period == "1yr" or period == "annual" or period == "year":
                high = float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[9]/div[3]").text[1:])
            return high
        except:
            raise Exception("ERROR: Couldn't get high for "+period+".")
        self.browser.close()

    #get low (periods: today, 52w)
    def getLow(self, ticker, period="today"):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            if period == "today" or period == "day" or period == "daily" or period == "1d":
                return float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[6]/div[3]").text[1:])
            if period == "52w" or period == "1yr" or period == "annual" or period == "year":
                return float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[10]/div[3]").text[1:])
        except:
            raise Exception("ERROR: Couldn't get low for "+period+".")
        self.browser.close()

    #get P/E ratio
    def getPE(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[2]/div[3]").text)
        except:
            raise Exception("ERROR: Couldn't get P/E ratio.")
        self.browser.close()

    #get dividend yield
    def getDivYield(self, ticker):
        try:
            self.browser.get("https://robinhood.com/stocks/"+ticker)
            return float(self.browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[3]/div[3]").text)
        except:
            raise Exception("ERROR: Couldn't get dividend yield.")
        self.browser.close()
