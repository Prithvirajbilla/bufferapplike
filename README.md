bufferapplike
=============

This app is a clone of [buffer app](https://bufferapp.com/).

What is a bufferapp?
====================

Bufferapp schedules all the content which you find on internet to be posted all day to increase social presence.

Idea
=====

Its simple actually.

Things you might need.

* [IFTTT account] (https://ifttt.com)
* dropbox account
* server which can run cron jobs

First whenever I want to schedule a post or the content i find on the internet, i save them in text files in the dropbox folder with certain format like 

The filename should be yyyy-mm-dd HH:MM | name_of_the_post.txt

so it is scheduled to be posted on that time.

Now we can create  IFTTT recipes for the posting action.
whenever i send a mail to trigger@ifttt.com the post is posted to fb | twitter | other social media.

What i did was, i was using a free mailgun account. I made a ifttt recipe such that whenever i recieve a new mail from XXX@mailgun.com i'm posting the mail to the social media.

I'm running a cron job for every few seconds.

Other ideas
===========
There exists an IFTTT recipe,
While we store a link (or mark it as view later in pocket) =>  a txt file will be saved to dropbox (but with different name). if we work a way around such that we can save it directly save with the required name we wanted.
that would be great.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/Prithvirajbilla/bufferapplike/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

