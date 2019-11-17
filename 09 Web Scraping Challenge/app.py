from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
import os

# FLASK APP
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)

# ROUTE TO RENDER INDEX.HTML
@app.route("/")
def home():

    # FETCHING DATA FROM MONGO
    marsInfo = mongo.db.marsInfo.find_one()

    # RENDER INDEX.HTML AND RETURN
    return render_template("index.html", marsInfo=marsInfo)

# ROUTE TO SCRAPE DATA
@app.route("/scrape")
def scrape():

    # SCRAPE FUNCTIONS FROM SCRAPE_MARS.PY
    marsInfo = mongo.db.marsInfo
    marsData = scrape_mars.MARSNews()
    marsData = scrape_mars.MARSImage()
    marsData = scrape_mars.MARSWeather()
    marsData = scrape_mars.MARSFacts()
    marsData = scrape_mars.MARSHemisphere()
    marsInfo.update({}, marsData, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug= True)