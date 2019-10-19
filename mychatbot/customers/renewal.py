import pandas as pd

cols = ['user_name', 'phone_no','email_id', 'location', 'vehicle_no', 'manufacturer', "model", "variant", "manufacturing_year", "policy_no", 'key']
master_db = pd.DataFrame(columns=cols)
vehicles_db = pd.read_excel("vehicles_db.xlsx")
quotes = pd.read_excel("quotes.xlsx")

def add_new_user(user_name="", phone_no="", email_id="", location="", vehicle_no="", manufacturer="", model="", variant="", manufacturing_year="", policy_no=""):
    new_row = [str(v) for v in locals().values()]
    key = [str(user_name)+" "+str(phone_no)+" "+str(email_id)]
    new_row = new_row + key
    row_index = len(master_db)
    if key in master_db.loc[:,"key"].values:
        print("user already exists")
    else:
        master_db.loc[row_index] = new_row
    return master_db

def fetch_user_details(phone_no="", login_id=""):
    try:
        if phone_no!="":
            user_details = master_db[master_db["phone_no"]==str(phone_no)]
        else:
            user_details = master_db[master_db["login_id"]==login_id]
    except IndexError:
        pass
    if user_details.empty:
        print("User doesnot exist")
    return user_details

def update_existing_user_details(new_user_name="", new_phone_no="", new_email_id="", new_location="", new_vehicle_no="", new_manufacturer="", new_model="", new_variant="", new_manufacturing_year="", new_policy_no=""):
    if current_user_details.empty:
        pass
    else:
        if new_user_name!="":
            current_user_details.at[current_user_details.index[0],"user_name"] = new_user_name
            key_user_name = new_user_name
        else:
            key_user_name = current_user_details.at[current_user_details.index[0],"user_name"]
        if new_phone_no!="":
            current_user_details.at[current_user_details.index[0],"phone_no"] = str(new_phone_no)
            key_phone_no = str(new_phone_no)
        else:
            key_phone_no = current_user_details.at[current_user_details.index[0],"phone_no"]
        if new_email_id!="":
            current_user_details.at[current_user_details.index[0],"email_id"] = new_email_id
            key_email_id = new_email_id
        else:
            key_email_id = current_user_details.at[current_user_details.index[0],"email_id"]
        if new_location!="":
            current_user_details.at[current_user_details.index[0],"location"] = new_location
        if new_vehicle_no!="":
            current_user_details.at[current_user_details.index[0],"vehicle_no"] = new_vehicle_no
        if new_manufacturer!="":
            current_user_details.at[current_user_details.index[0],"manufacturer"] = new_manufacturer
        if new_model!="":
            current_user_details.at[current_user_details.index[0],"model"] = new_model
        if new_variant!="":
            current_user_details.at[current_user_details.index[0],"variant"] = new_variant
        if new_manufacturing_year!="":
            current_user_details.at[current_user_details.index[0],"manufacturing_year"] = new_manufacturing_year
        if new_policy_no!="":
            current_user_details.at[current_user_details.index[0],"policy_no"] = new_policy_no
        current_user_details.at[current_user_details.index[0],"key"] = str(key_user_name) +" "+str(key_phone_no)+" "+str(key_email_id)
    return current_user_details

def display_user_details(user_details):
    for value in user_details.to_dict("index").values():
        for k, v in value.items():
            print("%s : %s" % (k,v))

def updated_master_db():
    try:
        x = master_db.drop(int(current_user_details.index.values))
        x = pd.concat([x, updated_user_details])
    except TypeError:
        x = master_db
    return x

def details_for_quote(manufacturer, model, variant, manufacturing_year):
    print(quotes)

def quote_selection(quote):
    print("please register")

add_new_user(user_name="rhishikesh", phone_no=8888782523, email_id = "rhishikeshjoshi@gmail.com")

current_user_details = fetch_user_details(phone_no=8888782523)

display_user_details(current_user_details)

updated_user_details = update_existing_user_details(new_email_id="rhishikesh@yahoo.com")

display_user_details(updated_user_details)

master_db = updated_master_db()

display_user_details(master_db)

details_for_quote("Honda","City","ABC", 2015)

