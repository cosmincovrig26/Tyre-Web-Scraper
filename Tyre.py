import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tyredatabase"
)

def dbtosql():  # everytime a new user request for tyres is made, the data will get REPLACED with all the { existing + new data scraped }
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM tyres")
    data = mycursor.fetchall()
    header = ['Brand', 'Pattern', 'Size', 'Price', 'Season', 'Wet Grip', 'Fuel Efficiency']

    with open('tyreinfo.csv', 'w') as x:
        writer = csv.writer(x)
        writer.writerow(header)
        writer.writerows(data)




class Tyre:
    def __init__(self, brand, pattern, size, price, season, wetGrip, fuelEfficiency):
        self.brand = brand
        self.pattern = pattern
        self.size = size
        self.price = price
        self.season = season
        self.wetGrip = wetGrip
        self.fuelEfficiency = fuelEfficiency
        self.dbexport()

    def dbexport(self):
        mycursor = db.cursor()
        sql = "INSERT INTO tyres (brand, pattern, size, price, season, wet_grip, fuel_efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (
            self.brand.capitalize(), self.pattern, self.size, self.price, self.season, self.wetGrip,
            self.fuelEfficiency)
        mycursor.execute(sql, val)
        db.commit()