<h2><strong>Goal:</strong></h2> 
<ul> Analayze ios vs. Android selling prices and total apps "just sold" on <a href="https://flippa.com/apps/just-sold"> flippa.com </a>.</ul>
  
  
<h2><strong>Results:</strong></h2> 
<ul>Overall, 121 more android apps were sold than ios, however, the average ios apps sold for ~50% more ($513.00 vs $254.98), and the most expensive ios sold for $25,000.00 vs android's $15,001.00. Additional unanswered questions:  How many androioid vs. ios apps went unsold, average unique users per app, and the respective developer-hours required to build the apps.</ul>
<br>
<br>
<ul>Raw Data:</ul>
<ul><strong>iOS</strong></ul>
<ul> count --> 627</ul>
<ul> mean --> $513.00</ul>
<ul> std -->  $1,536.00</ul>
<ul> min -->  $11.00</ul>
<ul> 25% -->  $79.00</ul>
<ul> 50% -->  $165.00</ul>
<ul> 75% -->  $320.00</ul>
<ul> max -->  $25,000.00</ul>
  </ul>
  <br>
  <ul><strong>Android</strong></ul>
<ul> count--> 748</ul>
<ul> mean-->  $254.98</ul>
<ul> std -->  $928.42</ul>
<ul> min -->  $1.00</ul>
<ul> 25% -->  $45.00</ul>
<ul> 50% -->  $75.00</ul>
<ul> 75% -->  $150.00</ul>
<ul> max -->  $15,001.00</ul>
  </ul>
 
 
<h2><strong>File Setup:</strong></h2> 
<ul>1. mkdir ~/scrapers/flippa_scraper</ul>
<ul>2. cd ~/scrapers/flippa_scraper</ul>
<ul>3. virtualenv env</ul>
<ul>4. . env/bin/activate</ul>
<ul>5. pip install scrapy</ul>
 

<h2><strong>Program Components:</strong></h2>
<ul>Scraper engine installed via:<a href="https://scrapy.org/"> Scrapy</a> </ul>
<ul>Data crunching via:<a href="http://jupyter.org/"> Jupyter</a> </ul>
