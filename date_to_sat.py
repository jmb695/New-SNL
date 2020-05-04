from datetime import date

#finds todays date and determines the date of the following saturday
def get_sat():
    #gets todays date
    today = date.today()
    weekday = today.weekday()
    s_today = str(today)
    #weekday = 6 signals it is a saturday
    if weekday != 6:
        #splits, converts date to numbers
        year, mo, d = s_today.split('-')
        d_num = int(d)
        mo_num = int(mo)
        year_num = int(year)
        #finds how many days until the next saturday
        day_to_sat = 6 - weekday
        #these are months with 31 days
        if mo_num == 1 or 3 or 5 or 7 or 8 or 10:
            if d_num + day_to_sat > 31:
                #takes the end of the month into account, finds date if saturday is in the next month
                d_num = d_num + day_to_sat - 31
                mo_num += 1
                d_str = str(d_num)
                mo_str = str(mo_num)
                #formats the date, month into the same format as the target url
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                #returns in proper formatting
                return str(year_num)+"-"+mo_str+"-"+d_str
            else:
                #if its not the end of the month...
                d_num = d_num + day_to_sat
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
        #and repeat with other months...
        if mo_num == 4 or 6 or 9 or 11:
            if d_num + day_to_sat > 30:
                d_num = d_num + day_to_sat - 30
                mo_num += 1
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
            else:
                d_num = d_num + day_to_sat
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
        if mo_num == 2:
            if d_num + day_to_sat > 28:
                d_num = d_num + day_to_sat - 28
                mo_num += 1
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
            else:
                d_num = d_num + day_to_sat
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
        #takes the end of the year into account
        if mo_num == 12:
            if d_num + day_to_sat > 30:
                d_num = d_num + day_to_sat - 30
                mo_num = 1
                year_num += 1
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
            else:
                d_num = d_num + day_to_sat
                d_num = d_num + day_to_sa
                d_str = str(d_num)
                mo_str = str(mo_num)
                if len(d_str) < 2:
                    d_str = '0'+d_str
                if len(mo_str) < 2:
                    mo_str = '0'+mo_str
                return str(year_num)+"-"+mo_str+"-"+d_str
    else:
        return s_today
