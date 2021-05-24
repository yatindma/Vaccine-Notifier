import requests
import datetime
import json
from fake_useragent import UserAgent
from send_email import send_email_func
import sched, time


dict_ = {}
prev_dict_ = {}


def jab_checker():
    global prev_dict_
    temp_user_agent = UserAgent()
    browser_header = {'User-Agent': temp_user_agent.random}

    global POST_CODE
    global age
    global numdays

    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    def check_prev_dict(dict_):
        global prev_dict_
        print(dict_)
        for element in dict_:
            print(element)
            if element not in prev_dict_:
                send_email_func(str(dict_))
                prev_dict_ = dict_


    def get_vaccine_email(vaccine, avl_capacity, vac_center, date_):
        if int(avl_capacity) > 0:
            dict_[vac_center] = [{"available_capacity": str(avl_capacity)},
                                 {"vaccine center": str(vac_center)},
                                 {"Available on": date_}]
            check_prev_dict(dict_)

    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            resp_json = response.json()
            if resp_json["centers"]:
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            vac_center = center["name"]
                            # vac_center_block = center["block_name"]
                            avl_capacity = session["available_capacity"]
                            vaccine = session['vaccine']
                            if(vaccine != ''):
                                get_vaccine_email(vaccine,
                                                  avl_capacity,
                                                  vac_center,
                                                  str(INP_DATE))
            else:
                print("No available slots on {}".format(INP_DATE))



global POST_CODE
global age
global numdays
POST_CODE = str(input("please enter your post code : "))
age = int(input("please enter your age : "))
numdays = int(input("for how many next dates you want to check : "))

s = sched.scheduler(time.time, time.sleep)
z = sched.scheduler(time.time, time.sleep)


def counter_checker(sc):
    """ 
        this function will run after every 20 seconds to check for Jabs
    """
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Checking JABS", current_time)
    jab_checker()
    s.enter(20, 1, counter_checker, (sc,))


def clean_timer(sc):
    """
        this function will clean the dictionary after every 5 hours
    """
    global prev_dict_
    # Cleaning the previous dictionary after 5 hours
    prev_dict_ = {}
    z.enter(18000, 1, clean_timer, (sc,))


s.enter(1, 1, counter_checker, (s,))
s.run()

z.enter(18000, 1, clean_timer, (s,))
z.run()
