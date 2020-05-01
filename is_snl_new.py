import requests
from bs4 import BeautifulSoup
import date_to_sat as ds

# Sets the page to crawl, set the correct date for the upcoming Saturday
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
    new_index = shorter_html.index('data-new_show="')
    #a "1" here indicates that the show is new
    if shorter_html[new_index+15] == '1':
        return True
    else:
        return False

#this finds who the guests are of the week's episode
def snl_guests(html):
    #cuts the html down to just the show
    snl_ind = html.index('11:00 PM')
    lp_ind = html.index('1:00:00')
    shorter_html = html[snl_ind:lp_ind]
    #finds where the guests are in the html
    guest_ind = shorter_html.index('data-guest="')
    guest_str = shorter_html[guest_ind+12:]
    guest_end = guest_str.index('"')
    guests = guest_str[:guest_end]
    #splits host and musical guest
    host, music_guest = guests.split(',')
    return host, music_guest

#prints whether or not snl is new this week and who the guests are
def snl_this_week():
    if new_snl(text):
        print("SNL is new this week! The host is "+snl_guests(text)[0]+", and the musical guest is"+snl_guests(text)[1]+".")
    else:
        print("SNL is a rerun this week. The host is "+snl_guests(text)[0]+", and the musical guest is"+snl_guests(text)[1]+".")

snl_this_week()