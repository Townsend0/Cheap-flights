import requests
import datetime
import smtplib

TODAY = datetime.date.strftime(datetime.date.today(), "%d/%m/%Y")

class Send:
    
    def get_data(self):
        
        self.users_info = []
        d = requests.get("https://api.sheety.co/e727c248aeb3c57bae687178bfc5a928/flights/sheet1").json()["sheet1"]
        
        for b in range(100):
            try:
                self.users_info.append([d[b]["name"], d[b]["email"], d[b]["city"]])
            except IndexError:
                break
            
        for b in range(100):
            try:    
                query = { "fly_from": self.users_info[b][2], "date_from": TODAY, "date_to": TODAY,"flight_type":
                "round", "curr" : "USD", "nights_in_dst_from": 14, "nights_in_dst_to": 30}

                self.search = requests.get("https://api.tequila.kiwi.com/v2/search",
                params = query, headers = {"apikey": "1y4nL7De6Mqrin1Jc9chcSWOi9JrUy2-"}).json()["data"]
                msdg = f"Good morning {self.users_info[b][0]}\n\nwe picked a 10 random flights for today here is the list\n"
                
                for c in range(10):
                    msdg += f"\nto {self.search[c]['cityTo']} for {self.search[c]['price']} USD"
                self.snd.sendmail("obadah2109@gmail.com", self.users_info[b][1],f"Subject: Cheap flight for today\n\n{msdg}")
            
            except:
                break
            
    def set_mail(self):
        self.snd = smtplib.SMTP("smtp.gmail.com", 587)
        self.snd.starttls()
        self.snd.login("obadah2109@gmail.com", "uqygmofrjmnkdsit")        
            


a = Send()
a.set_mail()
a.get_data()