print(f"{"Note to user: Enter data as follows ":^45}")
print(f"{10*"*"}{"Unit for height--->m":^25}{10*"*"}")
print(f"{10*"*"}{"Unit for weight--->kg":^25}{10*"*"}")
print()

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
    index=0
    for i in range(0,3):
        user_data[list_for_loop[index]]=input(f"Please enter your {list_for_loop[index]}: ")
        index+=1
    user_data["weight"]=float(user_data["weight"])
    user_data["height"]=float(user_data["height"])
    return user_data

def calc_BMI(w,h):
    """calculates the BMI

    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    bmi=w/(h**2)
    return bmi
    

def calc_BMI_category(bmi):
    """Calculates the BMI category

    Arguments:
        bmi {[float]} -- [the bmi number index]

    Returns:
        [string] -- [bmi category]
    """
    category_list=["Severely underweight","Underweight","Normal weight","Overweight","Obesity class I","Obesity class II","Obesity class III"]
    bmi_value_list=[0,16.5,18.5,24.9,29.9,34.9,39.9]
    index=0
    for i in range(0,7):
        if bmi_value_list[index]<bmi<=bmi_value_list[index+1]:
            bmi_category=category_list[index]
        index+=1
    return bmi_category

def print_results(bmi_category):
    """[Prints the BMI category to the user ]

    Arguments:
        bmi_category {[string]} -- []
    """
    print(f"{user_data["name"]}, you are {bmi_category}")


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print(f"Your bmi is {bmi:.4}")
print_results(bmi_category)