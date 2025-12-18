Payment = input('Enter Phonepe or paytm or card')
if Payment == 'Phonepe':
    print("Initiating phonepe transaction")
elif Payment == 'Paytm':
    print("Initiating paytm transaction")
elif Payment == 'Card' :
    print("Initiating card  transaction")
else:
    print("Not Suppourted")