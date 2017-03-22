<h2><strong>Goal:</strong></h2> 
<ul> Analayze ios vs. Android selling prices and total apps "just sold" on <a href="https://flippa.com/apps/just-sold"> flippa.com </a>.</ul>
  
  
<h2><strong>Results:</strong></h2> 
<ul>iOS</ul>
<ul> "              price\n",
       "count    627.000000\n",
       "mean     513.159490\n",
       "std     1536.857766\n",
       "min       11.000000\n",
       "25%       79.000000\n",
       "50%      165.000000\n",
       "75%      320.000000\n",
       "max    25000.000000"
  </ul>
  
  <ul>Android</ul>
<ul>   "              price\n",
       "count    748.000000\n",
       "mean     254.983957\n",
       "std      928.427175\n",
       "min        1.000000\n",
       "25%       45.000000\n",
       "50%       75.000000\n",
       "75%      150.000000\n",
       "max    15001.000000"
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
