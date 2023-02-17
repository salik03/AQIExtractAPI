from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

app = Flask(__name__)

@app.route("/news")
def extract_weather_news():
    a=0
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.indiatvnews.com/topic/weather')
    news_items = driver.find_elements(By.CSS_SELECTOR, "div.row.newsListBox")
    news = {"headline":[],"newsdesc":[],"daydatetime":[],"image":[],"news_url":[]}
    for item in news_items:
        headline = item.find_elements(By.CSS_SELECTOR,"h3.title")
        newsdesc = item.find_elements(By.CSS_SELECTOR,"p.dic")
        daydatetime = item.find_elements(By.CSS_SELECTOR,"span.deskTime")
        image = item.find_elements(By.CSS_SELECTOR,"img")
        news_url = item.find_elements(By.CSS_SELECTOR,"a.thumb")
        for i in headline:
            news["headline"].append(i.text)
        for i in newsdesc:
            news["newsdesc"].append(i.text)
        for i in daydatetime:
            news["daydatetime"].append(i.text)
        for i in image:
            img_url = i.get_attribute("data-original")
            news["image"].append(img_url)
        for i in news_url:
            url = i.get_attribute("href")
            news["news_url"].append(url)

    return jsonify(news)

if __name__ == "__main__":
    app.run()
