import requests
from bs4 import BeautifulSoup
import date_to_sat as ds

# Sets the page to crawl, set the correct date for the upcoming Saturday
# Could not crawl nbc, so I had to use a secondary site. Unfortunately, it does not update as quickly
url = "https://www.tvpassport.com/tv-listings/stations/nbc-network-eastern/1227/"+ds.get_sat()
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, "lxml")
text = str(soup.find("body").get_text)

#determines if the snl episode for the week is new or not
def new_snl(html):
    #cuts html down to just the snl episode
    snl_ind = html.index('11:00 PM')
    lp_ind = html.index('1:00:00')
    shorter_html = html[snl_ind:lp_ind]
    if 'data-new_show="' in shorter_html:
        new_index = shorter_html.index('data-new_show="')
    else:
        return "TBD"
    #a "1" here indicates that the show is new
    if shorter_html[new_index+15] == '1' or '<span class="show-label live">' in shorter_html:
        return True
    else:
        return False

#this finds who the guests are of the week's episode
def snl_guests(html):
    #cuts the html down to just the show timeslot
    snl_ind = html.index('11:30 PM')
    lp_ind = html.index('1:00 AM')
    shorter_html = html[snl_ind:lp_ind]
    #finds the show description within this shorter html
    descrip = shorter_html[shorter_html.index('<p>')+3:]
    descrip = descrip[:descrip.index('</p>')]
    #looks for the host and musical guest within this text
    if 'hosts' in descrip:
        host = descrip[:descrip.index(' host')]
        music_guest = descrip[descrip.index('and')+4:descrip.index(' is')]
        return host, music_guest
    #returns TBD if hosts for the week are not yet reported
    else:
        return['TBD', 'TBD']   

#prints whether or not snl is new this week and who the guests are
def snl_this_week():
    if new_snl(text)==True:
        print("SNL is new this week! The host is "+snl_guests(text)[0]+", and the musical guest is"+snl_guests(text)[1]+".")
    elif new_snl(text)==False:
        print("SNL is a rerun this week. The host is "+snl_guests(text)[0]+", and the musical guest is"+snl_guests(text)[1]+".")
    else:
        print("SNL is still TBD this week.")

snl_this_week()
