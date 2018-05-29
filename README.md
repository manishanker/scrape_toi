## scrape_data_for_speech

This repo consists of the scripts that can be used to scrape data from TOI(Time of India) which can be used for training speech.

1. collect_news_data_toi.py

This is the main python process which uses Goose and BeautifulSoup to
scrape the content and parse the divs of the given url page.

You can find more information about Goose here  (
https://github.com/grangier/python-goose) and BeautifulSoup here(
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
)

2.deamon_collect_urls.sh

This is a shell script to check if above process is running, if not
start the process. Using this shell script, we can run the above python
process and make sure python processes are running always for collecting
large amount of text data from newspapers.

3.log_collecturls_toi.txt

This is a text file for reference. In the above python script, random
dates (an archive page like
http://timesofindia.indiatimes.com/2011/11/28/archivelist/year-2011,month-11,starttime-40875.cms
) are picked to collect individual urls. This txt serves would help
in recognizing the random data that was picked and from which the text
from which url was extracted.

4.TOI_CONTENT.txt

This txt file has the extracted content. This has been cleaned using sed
and the delimiter
(###########################################################) has been
removed

5.TOI_URLS.txt

This text file consists of all the URLS that were used to extract
information from.


6.catvar/

This folder contains the categorichal database for english words.
For instance using `CVsearch.pl kill`, we can find all the  words
that are various word forms like killed, killer etc.

7. TOI_CONTENT_BADWORDS_REMOVED.txt
This file has the content with all the bad words removed.

8.remove_bad_words.py

python script to create the words from a list and then remove the
sentences containing those words from the input passages.


