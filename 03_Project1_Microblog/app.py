from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

def create_app():

    app = Flask(__name__)
    client = MongoClient("mongodb+srv://codemonk:Vds#24!Y!4ffKNR@microblog.8jpj8hn.mongodb.net/?retryWrites=true&w=majority&appName=microblog")
    # Database Name
    db = client.microblog
    # Collection Name
    entrycollection = db.entrycollection


    @app.route("/", methods=["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formated_date = datetime.datetime.today().strftime("%Y-%m-%d")
            #  Inserting Data to MongoDB
            entrycollection.insert_one({"content": entry_content, "date" :formated_date})
        
        entries_with_date = [
            (entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            # Retriving All data from database and traverssing it.
            for entry in entrycollection.find({})
        ]
        
        return render_template("home.html", entries=entries_with_date)
    
    return app