# tfl-monitor
To build an interface with TFL to display bus and tube times



#todo
    get sid to apply ruff
    line legnth 100 etc
    get sid to discuss poetry with this

python requests api library

***
 
_ Steps performed_ 
download kiota - import this json https://api.tfl.gov.uk/swagger/docs/v1
each API route has a class - import the class
you can pass your request adaptor and paramters through there.
need to think about how asynch io works
https://api.tfl.gov.uk/swagger/ui/index.html#!/Line/Line_MetaModes

***

Update 02/11/2025
I think the swagger (unified API) is the legacy system. 
I believe we need the following:
https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_MetaModes

under line there is a dropdown with the text saying "API definition"
On the drop down is Open API 3 JSON
I will use Kiota to try and install line

***
Ideal end result 
The touchscreen display would have at all times (refreshing every second or so) the following pieces of information
- the status of the northern line
- the ETA of the next two trains on the northern line (northbound)
- the ETA of the following busses
  - 35 southbound (to CJ)
  - 37 southbound (to CJ)
  - 155 northbound (to Elephant and Castle)
  - 155 southbond (from Elephant and Castle)
- status details from two nearby "Borris Bike" stations
  - how many bikes are available
  - how many spaces are available

stretch goal
- If I can get train timetables, the time for next two trains from CJ to Portsmouth and Alton.
