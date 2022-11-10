# Name:Kerry Flowers
# Prog Purpose: This program computes college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https:www.pvcc.edu/tuition-and-fees
#   NOTE: All fees are PER CREDIT
#   In-state tuition: $155, Out-of-state tuition: $331.60
#   Capital Fee: $23.50 (out-of-state sturdents only)
#   Institution fee: $1.75
#   Activity fee: $2.90

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 155
RATE_TUITION_OUT = 331.60
RATE_CAPITAL = 23.50
RATE_INSTITUTION = 1.75
RATE_ACTIVITY = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0

############## define program functions ################
def main() :
    get_user_data()
    perform_calculations
    display_results()

def get_user_data():
    global inout, numcredits, scholorshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for our OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholorshipamt = float(input("Scholorship amount received: "))

def perform_calculations():
    global tuitionfee, capitalfee, institionfee, activityfee, totalowed,balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL

    institutionfee = numcredits * RATE_INSTITUTION
    activitiyfee = numcredits * RATE_ACTIVITY
    totalowed = totalowed - scholorshipamt

def display_results():
    print ('\n----------------------------------')
    print ('Number of credits : ' + str (numcredits))
    print ('----------------------------------------')
    print ('Tuition           $ ' + format(tuitionfee, '10, .2f'))
    print ('Capital Fee       $ ' + str(capitalfee))
    print ('Institution Fee   $ ' + str(institutionfee))
    print ('Activity Fee      $ ' + str(activityfee))
    print ('Total             $ ' + str(totalowed))
    print ('scholorship       $ ' + str(scholorshipamt))
    print ('---------------------------------------')
    print ('balance Owed      $ ' + str(balance))
    print ('---------------------------------------')
    print (str(datetime.datetime.now()))
    print ("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")


########## call on main proram to execute ############
main()

    



