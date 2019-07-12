#在线生成schema：https://jsonschema.net/
#jsonschema验证方法：https://blog.csdn.net/junli_chen/article/details/52965763
#https://blog.csdn.net/m0_37920188/article/details/72846226
schema = {
   "$schema": "http://json-schema.org/draft-07/schema#",
   "type": "object",
   "required": [
         "term_month",
         "total_principal",
         "total_interest",
         "total_fee",
         "interest_rate",
         "fund_rate",
         "plan",
         "total"
       ],
   "properties": {
     "term_month": {
           "type": "string"
         },
     "total_principal": {
           "type": "number"
         },
     "total_interest": {
           "type": "number"
         },
     "total_fee": {
           "type": "number"
         },
     "interest_rate": {
           "type": "number"
         },
     "fund_rate": {
           "type": "number"
         },
     "plan": {
       "type": "array",
       "items": {
         "type": "object",
         "required": [
               "current_term",
               "principal",
               "interest",
               "fee",
               "repay_day",
               "monthly_amount"
             ],
         "properties": {
           "current_term": {
                 "type": "number"
               },
           "principal": {
                 "type": "number"
               },
           "interest": {
                 "type": "number"
               },
           "fee": {
                 "type": "number"
               },
           "repay_day": {
                 "type": "string"
               },
           "monthly_amount": {
                 "type": "number"
               }
         }
       }
     },
     "total": {
       "type": "number"#string
     }
   }
 }
