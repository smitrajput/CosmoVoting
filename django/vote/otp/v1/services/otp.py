import http.client
import requests
from otp.models import Otp_session
from kyc.models import KycInfo
from rest_framework.response import Response
class Otp(object):

    @classmethod
    def send_otp(cls, mob_number):
        print ("inside function")

        data = {}
        # headers = { 'content-type': "application/x-www-form-urlencoded" }
        # r = requests.get('https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/'+str(mob_number)+'/AUTOGEN', params = data)
        r = requests.get('https://2factor.in/API/V1/7e1f0dc5-c3bc-11e9-ade6-0200cd936042/SMS/'+str(mob_number)+'/AUTOGEN', params = data)
        fetched_data = r.json()
        print ("inside otp function ")
        print (fetched_data)

        try:
            
            otp = Otp_session.objects.get(mobile= mob_number)
            otp.session_id = fetched_data.get('Details')
            otp.save()
            print("present")
        except:
            Otp_session.objects.create(mobile= mob_number, session_id= fetched_data.get('Details'))
            print("creating new")
        
        # conn.request("GET", "https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/7021558628/AUTOGEN", payload, headers)

        # res = conn.getresponse()
        # data = res.read()
 	
        # print(data.decode("utf-8"))
        return fetched_data

    @classmethod
    def send_otp_uuid(cls, uuid):
        print ("inside function")
        print (uuid)
        try:
            kyc_info = KycInfo.objects.get(uuid=uuid)
            mob_number = kyc_info.mobile
            print(mob_number)
            result = cls.send_otp(mob_number)
            return result 
        except:
            result={result:" mobile number not in the database "}
            return result

    @classmethod
    def verify_otp(cls, mob_number, otp_input):
        print(mob_number)
        otp_session = Otp_session.objects.get(mobile=int(mob_number))
        session_id = otp_session.session_id
        print(session_id)
        
        data = {}
        # url = 'https://2factor.in/API/V1/580908f5-7fe1-11e9-ade6-0200cd936042/SMS/VERIFY/'+session_id+'/'+str(otp_input)
        url = 'https://2factor.in/API/V1/7e1f0dc5-c3bc-11e9-ade6-0200cd936042/SMS/VERIFY/'+session_id+'/'+str(otp_input)
        print (url)
        r = requests.get(url, params = data)
        fetched_data = r.json()
        print ("inside otp function ")
        print (fetched_data)
        return fetched_data
        
    @classmethod
    def verify_otp_uuid(cls, uuid, otp_input):
        print ("inside function")
        print (uuid)
        try:
            kyc_info = KycInfo.objects.get(uuid=uuid)
            mob_number = kyc_info.mobile
            print(mob_number)
            result = cls.verify_otp(mob_number, otp_input)
            return result 
        except:
            result={result:" mobile number not in the database "}
            return result
