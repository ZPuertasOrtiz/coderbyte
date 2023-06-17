import datetime
def countingMinutesI(s):
    hour_1=datetime.datetime.strptime(s.split("-")[0],'%I:%M%p' )
    hour_2=datetime.datetime.strptime(s.split("-")[1],'%I:%M%p' )
    
    difference = abs(hour_1-hour_2).total_seconds()/60  
    print (difference)
    
countingMinutesI('9:00am-10:00am')


