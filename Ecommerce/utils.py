from http.client import HTTPException
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6369754F686E4C7A73396143576F2F7954533372554F7A4948614A686C504A4742384A415858684D6A50413D')
        params = {
            'sender': '',
            'receptor':phone_number,
            'message':f'{code}کد تایید شما'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
