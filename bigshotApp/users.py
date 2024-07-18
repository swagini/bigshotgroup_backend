
import json
from django.core.mail import send_mail
from django.db import connection 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from bigshotApp.common import dbfunction, dbconnect

from crequest.middleware import CrequestMiddleware
from bigshotApp.common.logger import *
import smtplib
from email.mime.text import MIMEText

class GetUserDetails(APIView):
    def post(self, request):
        try: 
            params = {
                'user_emailid': request.data['emailid'],
                'user_password': request.data['password'],
            }
            
            getallemployee = dbconnect.query_executer.post(dbfunction.fn_get_userdetails, params)
            
            # if getallemployee and len(getallemployee) > 0:
              
            return HttpResponse(json.dumps(getallemployee))
            # else:
            # return HttpResponse(json.dumps({"emp_details": []}))
        
        except Exception as err:
            error_response = {
                'error': str(err)
            }
            return HttpResponse(err)
        
class InsertUserDetails(APIView):

    def post(self,request):
        try:
            CrequestMiddleware.set_request(request)
            
            log_request(request)
            params={
                "user_id":request.data['userid'],
                  "user_firstname":request.data['userfirstname'],
                   "user_lastname":request.data['userlastname'],
                    "user_emailid":request.data['useremailid'],
                     "user_mobile":request.data['usermobile'],
                  "user_password":request.data['userpassword'],
                   "user_confirmpassword":request.data['userconfirmpassword'],
            }
            userdetails= dbconnect.query_executer.post(dbfunction.fn_insertusers,params)
            
            log_request(userdetails)
            return HttpResponse(json.dumps(userdetails))

        except Exception as err:

            return HttpResponse(err)



# class GetOtpGeneration(APIView):
#
#     def post(self, request):
#         try:
#             CrequestMiddleware.set_request(request)
#             log_request(request)
#
#             useremailid = request.data.get('useremailid')  # Fetch useremailid from request data
#             params = {"email_id": useremailid}
#
#             userdetails = dbconnect.query_executer.post(dbfunction.fn_otp_generation, params)
#             log_request(userdetails)
#             new_otp = (userdetails['otp'])  # Assuming 'otp' is a key in userdetails
#
#             print(new_otp)
#             if new_otp:
#                 otp_value = userdetails['otp']
#
#                 subject = 'Your OTP for Verification'
#                 message = f'Your OTP is: {otp_value}'
#                 from_email = 'swaginilucky@gmail.com'  # Replace with your email address
#                 recipient_list = [useremailid]  # Ensure recipient_list is a list
#                 send_custom_email(subject, message, from_email, recipient_list)
#
#                 return HttpResponse(json.dumps(userdetails))  # Return userdetails as JSON
#
#             else:
#                 return HttpResponse(json.dumps({'error': 'OTP not found in user details'}), status=404)
#
#         except Exception as err:
#             print(f"Exception occurred: {str(err)}")
#             return HttpResponse(json.dumps({'error': 'Failed to generate OTP or send email'}), status=500)
#
#
# def send_custom_email(source_email, target_email, subject, message):
#     send_mail(
#         subject,
#         message,
#         source_email,  # From email address
#         [target_email],  # List containing the target email address
#     )


class GetOtpGeneration(APIView):

    def post(self, request):
        try:
            CrequestMiddleware.set_request(request)
            log_request(request)

            useremailid = request.data.get('useremailid')  # Fetch useremailid from request data
            params = {"email_id": useremailid}

            userdetails = dbconnect.query_executer.post(dbfunction.fn_otp_generation, params)
            log_request(userdetails)
            new_otp = (userdetails['otp'])  # Assuming 'otp' is a key in userdetails

            print(new_otp)
            if new_otp:
                otp_value = userdetails['otp']
                subject = 'Your OTP for Verification'
                message = f'Your OTP is: {otp_value}'  # Replace with your actual OTP
                msg = MIMEText(message, 'plain')  # Set message type as plain text
                msg['Subject'] = subject
                msg['From'] = 'swagini@gmail.com'  # Replace with your sender email address
                msg['To'] = [useremailid]



                return HttpResponse(json.dumps(userdetails))  # Return userdetails as JSON

            else:
                return HttpResponse(json.dumps({'error': 'OTP not found in user details'}), status=404)

        except Exception as err:
            print(f"Exception occurred: {str(err)}")
            return HttpResponse(json.dumps({'error': 'Failed to generate OTP or send email'}), status=500)

class UpdatePassword(APIView):
    def post(self,request):
        try:
           CrequestMiddleware.set_request(request)
           log_request(request)
           params = {"email_id":request.data['useremailid'],
                     "user_password":request.data['userpassword']
                     }
           userdetails = dbconnect.query_executer.post(dbfunction.fn_update_password, params)
           return HttpResponse(json.dumps(userdetails))
           
        except Exception as err:
            print(f"Exception occurred: {str(err)}")
            return HttpResponse(json.dumps({'error': 'Failed to Fetch the data'}), status=500)