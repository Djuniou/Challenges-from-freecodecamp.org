def add_time(start, duration, weeks=""):
    
    week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']    
    [time,t_s] = start.split(" ")                       #time start; t=AM/PM
    [h_s,min_s] = [int(s) for s in time.split(':')]     #hour and minutes start
    [h_d,min_d] = [int(s) for s in duration.split(':')] #hour and minutes duration
    [h_f,min_f,days_f] = [0,0,0]                        #hour and minutes final  
    
    #Change to 24h mode
    if (t_s=="PM"): 
        h_s += 12
    
    #Adjusting minutes
    min_f = min_s + min_d
    if (min_f > 60):
        h_f += min_f//60
        min_f = min_f%60
    
    #Adjusting hour and days after (days_f)
    days_d = h_d//24 
    days_f += days_d
    h_f += h_s+h_d%24
    if (h_f >= 24):
        h_f -= 24
        days_f += 1    
    
    #Adjusting AM/PM
    if (h_f >= 12):
        h_f -= 12
        t_f = "PM"
    else:
        t_f = "AM"         
    if (h_f==0):
        h_f = 12
    
    #Final msg with minutes display adjust    
    new_time = (str(h_f)+":")
    if (min_f<10):
        new_time +=("0"+str(min_f))
    else:
        new_time +=(str(min_f))
    new_time += (" "+t_f)    
    
    #Check if there's week_s
    if (weeks.casefold() in week):
        week_f = days_f%7
        if (week_f==0): #Means it's the same day
            new_time += (", "+weeks.capitalize())
        else:
            week_f += week.index(weeks.casefold())
            if (week_f >= 7):
                week_f -= 7   
            new_time += (", "+week[week_f].capitalize())          
    
    #Adjusting final msg
    if (days_f > 1):
        new_time += (" ("+str(days_f)+" days later)") 
    elif (days_f == 1):
        new_time += (" (next day)")    
    return new_time
