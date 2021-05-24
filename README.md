# Vaccine-Notifier
It collects the data from the Cowin API and sends the email if the vaccine is available<br>
It'll continuously run after every 20 seconds and will notify the user via-email if vaccine is available.<br>
after it mailed you about the vaccine availability at a particular center, it'll again check after 5 hours for the same center. <br>
and if any other center opens in between it'll notify you in less than 20 seconds<br>

<i>
example . <br>
<b> Center  a </b> open with capacity of 10 - you'll get a mail<br>
but now again for the <b> Center  a </b> it will mail you after 5 hours if vaccine is still available<br>
and at <b> Center  b </b> it'll again mail you in less than 20 seconds if vaccine slot opens <br>
but now again for the <b> center  b </b> it will mail you after 5 hours if it's still available there<br>
</i>

<i>pip install fake_useragent</i>

All other libraries used here are already available in python by default

<h3>Steps to run:</h3>

1. Clone the library
2. Install python
3. Open send_email.py (using any editor)
4. Changes these 3 fields in the code <br>
    <b>sender_email = "your@gmail.com"</b> <br>
    <b>receiver_email = "receiver_email@gmail.com"</b><br>
    <b>password = 'password@123'</b><br>
4. open cmd -> go the location where files is saved
5. enter <i> python Vaccine-Notifier.py
  6. <b> enter your post code </b><br>
<b> enter your age</b><br>
<b> for how many dates you want to look for <i> eg enter 1 for today , enter 2 for today and tomorrow</i></b><br>
  
<b> REFERENCE </b>  : https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability


