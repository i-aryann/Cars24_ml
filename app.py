from flask import Flask, request
import joblib


app = Flask(__name__)

pickle_model = open('./model.pkl', 'rb')
pickle_scaler= open('./scaler.pkl','rb')
clf = joblib.load(pickle_model)
scl=  joblib.load(pickle_scaler)


@app.route('/ping',methods=['GET'])
def ping():
    return "Hello, the server is up and running"        


@app.route('/predict',methods=['POST','GET'])
def predict():
    car_price=request.get_json()
    year=car_price['year']
    km_driven=car_price['km_driven']
    mileage=car_price['mileage']
    engine=car_price['engine']
    power=car_price['max_power']
    age=car_price['age']
    Individual= car_price['Individual']
    dealer= car_price["Trustmark Dealer"]
    diesel= car_price["Diesel"]	
    electric= car_price["Electric"]
    lpg=car_price["LPG"]
    petrol=car_price["Petrol"]
    manual=car_price["Manual"]
    age1=car_price["5"]	
    age2=car_price[">5"]


    result = clf.predict(scl.transform([[year, km_driven, mileage, engine, power, age, Individual, dealer, diesel, electric, lpg, petrol, manual, age1, age2]]))
    
    return "Estimated Price of the Car is: "+ str(result[0])

