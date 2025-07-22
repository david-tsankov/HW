def get_user_data():
    """retrieves user data from the command line

    Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in meters",
                "weight": "user weight in kilograms"
            }
    """
    user_data={
        
    }
    list_for_loop=["name","height","weight"]
    
    def validate_name():
        if len(user_data["name"])>2:
            return True
        else:
            return False
    
    def validate_height():
        if 50<user_data["height"]<250:
            return True
        else:
            return False
    def validate_weight():
        if 5<user_data["weight"]<300:
            return True
        else:
            return False


    while False:
        index=0
        for i in range(0,3):
            user_data[list_for_loop[index]]=input(f"Please enter your {list_for_loop[index]}: ")
            index+=1
        if validate_name()==True and validate_height==True and validate_weight==True:
            True
        else:
            False
    
    user_data["weight"]=float(user_data["weight"])
    user_data["height"]=float(user_data["height"])


    print(user_data)
    return user_data
user_data=get_user_data()
