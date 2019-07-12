import re
wq='<appium.webdriver.webelement.WebElement (session="7db41c93-bacb-4a52-a570-3fcd49d7e7d8", element="5")>' 
print wq
ma = re.sub(r'<', "", wq)
print ma
ma = re.sub(r'\..*$', "", ma)
print ma
ma = re.search(r'\D',wq)
print ma