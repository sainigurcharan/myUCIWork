from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
import os

# Create an instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)

# Create route that renders index.html template
@app.route("/")
def home():

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.MARSNews()
    mars_data = scrape_mars.MARSImage()
    mars_data = scrape_mars.MARSWeather()
    mars_data = scrape_mars.MARSFacts()
    mars_data = scrape_mars.MARSHemisphere()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug= True)