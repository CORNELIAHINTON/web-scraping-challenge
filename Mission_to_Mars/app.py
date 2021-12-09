from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)



# Create connection and Pass connection to the pymongo instance.
#client = PyMongo.MongoClient(conn)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MarsDB"
mongo = PyMongo(app)

collection = mongo.db.mars 

#index route to render mongo database
@app.route("/")
def home():

    # Find data from the mongo database
    mars = collection.find_one()

    # Return template and data
    return render_template("index.html",mars=mars )


#route to render scrape template
@app.route("/scrape")
def scraper():
    mars_data = scrape_mars.scrape_all()
    
    collection.update({},mars_data,upsert=True)

    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)
