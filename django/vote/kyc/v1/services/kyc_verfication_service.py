import http.client
import requests
from kyc.models import KycInfo
class Kyc(object):

    @classmethod
    def send_otp(cls, mob_number):
        print ("inside function")
        # conn = http.client.HTTPConnection("2factor.in")
        # payload = ""
        # data = { "esummit_id": self.esummit_id,
        #         "email": self.email}
        data = {}
        # headers = { 'content-type': "application/x-www-form-urlencoded" }
        r = requests.get('https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/7021558628/AUTOGEN', params = data)
        fetched_data = r.json()
        print ("inside otp function ")
        print (fetched_data)
        # conn.request("GET", "https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/7021558628/AUTOGEN", payload, headers)

        # res = conn.getresponse()
        # data = res.read()
 	
        # print(data.decode("utf-8"))
        return fetched_data

    @classmethod
    def verify_otp(cls, session_id, otp_input):
        data = {}
        url = 'https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/VERIFY/'+session_id+'/'+otp_input
        print (url)
        r = requests.get(url, params = data)
        fetched_data = r.json()
        print ("inside otp function ")
        print (fetched_data)
        return fetched_data
        
