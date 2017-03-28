<h2><strong>Goal:</strong></h2> 
<ul> To analayze iOS vs. Android selling prices by scraping, "just sold" data from<a href="https://flippa.com/apps/just-sold" target="_blank"> flippa.com</a> (an online marketplace to buy/sell: apps, websites, and domains).</ul>
  
  
<h2><strong>Results:</strong></h2> 
<ul>Overall, 121 more android apps were sold than iOS, however, the average iOS app sold for ~50% more ($513.00 vs. $254.98), and the most expensive iOS sold for $25,000.00 vs. android's $15,001.00. Additional unanswered questions:  How many android vs. iOS apps were listed, but went unsold, the average unique users per app, and the respective developer-hours required to build the apps.</ul>

<h2><strong>"Just Sold" Price Data (*as of 25/03/2017):</strong></h2>
<table class="tg">
  <tr>
    <th class="tg-yw4l">mobile operating systems</th>
    <th class="tg-yw4l">count</th>
    <th class="tg-yw4l">mean</th>
    <th class="tg-yw4l">std</th>
    <th class="tg-yw4l">min</th>
    <th class="tg-yw4l">25%</th>
    <th class="tg-yw4l">50%</th>
    <th class="tg-yw4l">75%</th>
    <th class="tg-yw4l">max</th>
  </tr>
  <tr>
    <td class="tg-yw4l">iOS</td>
    <td class="tg-yw4l">627</td>
    <th class="tg-yw4l">$513.00</th>
    <th class="tg-yw4l">$1,536.00</th>
    <th class="tg-yw4l">$11.00</th>
    <th class="tg-yw4l">$79.00</th>
    <th class="tg-yw4l">$165.00</th>
    <th class="tg-yw4l">$320.00</th>
    <th class="tg-yw4l">$25,000.00</th>
  </tr>
  <tr>
    <td class="tg-yw4l">Android</td>
    <td class="tg-yw4l">748</td>
    <td class="tg-yw4l">$254.98</td>
    <td class="tg-yw4l">$928.42</td>
    <td class="tg-yw4l">$1.00</td>
    <td class="tg-yw4l">$45.00</td>
    <td class="tg-yw4l">$75.00</td>
    <td class="tg-yw4l">$150.00</td>
    <td class="tg-yw4l">$15,001.00</td>
  </tr>
</table>

<h2><strong>Scrapy Setup:</strong></h2> 
<ul>1. mkdir ~/scrapers/flippa_scraper</ul>
<ul>2. cd ~/scrapers/flippa_scraper</ul>
<ul>3. virtualenv env</ul>
<ul>4. . env/bin/activate</ul>
<ul>5. pip install scrapy</ul>
 

<h2><strong>Project Components:</strong></h2>
<ul>Scraper engine installed via:<a target="_blank" href="https://scrapy.org/"> Scrapy</a> </ul>
<ul>Data crunching via:<a target="_blank" href="http://jupyter.org/"> Jupyter</a> </ul>
