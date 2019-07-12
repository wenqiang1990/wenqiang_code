import schema2
from jsonschema import validate
import jsonschema
import requests
import json

schema = schema2.schema
#print(schema)

url = "http://develop.rmbfapi.test.youxinjinrong.com/in_loan/repay_plan"
querystring = {"debug":"1","loan_period":"3","loan_money":"5000","product_id":"1","cuser_id":"1495"}
response = requests.request("GET", url, params=querystring)
data = json.loads(response.text)['data']
#print(data)


if data is None:
   print(json.loads(response.text)['msg'])
else:
    try:
       validate(data, schema)
    except jsonschema.ValidationError as ex:
       msg = ("HTTP response body is invalid (%s)") % ex
       #raise exceptions.InvalidHTTPResponseBody(msg)
       print(msg)
