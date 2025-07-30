user_data={
    "name":"Da",
    "height":1.88,
    "weight":75
    }

def validate_name():
        if len(user_data["name"])>2:
            return True
        else:
            return False
    
def validate_height():
    if 0.50<user_data["height"]<2.50:
        return True
    else:
        return False
        
def validate_weight():
    if 5<user_data["weight"]<300:
        return True
    else:
        return False
print(validate_name())
print(validate_height())
print(validate_weight())
x=False
while x==False:
    if validate_name()==True and validate_height()==True and validate_weight()==True:
        x=True
    else:
        x=False
print(x)