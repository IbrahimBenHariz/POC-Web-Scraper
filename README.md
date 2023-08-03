<h1 align="center"><b><i>POC Web Scraper</i></b></h1>

I designed and implemented a Python-based "Web Scraper" project to delve into the realm of sneaker bots and their ability to acquire real-time information on the latest sneaker releases without being detected. The primary objective of this endeavor was to gain insights into the functioning of bot blockers as well. Through this experience, I expanded my understanding of bot systems and bot detectors !

---
</br>

## Prerequisite
First, you need to install the various libraries for the use of the web scraper (they are imported in the code, but you also need to install them, otherwise, you may encounter errors).
https://github.com/IbrahimBenHariz/POC-Web-Scraper/blob/008321be30776c1932572795aa80359c82e337b5/POC-Web-Scraper.py#L1-L11

## Setting Up Variables
https://github.com/IbrahimBenHariz/POC-Web-Scraper/blob/008321be30776c1932572795aa80359c82e337b5/POC-Web-Scraper.py#L17-L19

> max_testscrape: represents the maximum number of attempts when a sent request fails or receives a response that does not allow continuing the scraping.
> delay_testscrape: represents the delay in seconds between failed attempts.

## How Does It Work ?
The scraper is presented with a menu that allows easy navigation between the different functions. The menu consists of 5 choices:
https://github.com/IbrahimBenHariz/POC-Web-Scraper/blob/008321be30776c1932572795aa80359c82e337b5/POC-Web-Scraper.py#L165-L172

Each function allows performing a specific task. Before discussing the functions that enable scraping, let's take a closer look at the first two functions:

The first function allows uploading a .txt file with necessary headers to modify the crucial request footprint. This step is essential as some headers may be blocked by certain websites. The headers will be randomly selected by the scraper for each request to constantly modify the footprint. An example file containing headers is provided with the scraper script.

Example of headers:</br>

>{</br>
>"Accept": "/",</br>
>"Accept-Language": "en-GB",</br>
>"Cache-Control": "no-cache",</br>
>"Origin": "https://www.amazon.com",</br>
>"Referer": "https://www.google.com",</br>
>"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"</br>
>}

Finally, the second function allows specifying a folder where previously scraped pages will be saved. This helps to keep track of and maintain a history of the different websites that have been scraped.

It's important to note that the scraper cannot be used without configuring these first two functions properly. If they are not set up correctly, the scraper may not work.</br>
The last three functions are used for scraping !

"Scrape A Single URL": This is the main function used by the other two functions to scrape using a request. When you choose option 3, the scraper will prompt you to enter a URL to perform the request and will provide you with a response. It's possible that the request might be rejected, blocked, or encounter a network error, and you will receive this information in the terminal. If the scraping is successful, the page will be saved in the folder you specified earlier.

https://github.com/IbrahimBenHariz/POC-Web-Scraper/blob/008321be30776c1932572795aa80359c82e337b5/POC-Web-Scraper.py#L86-L100

"Scrape A Single URL Multiple Times": This function is complementary to the previous one; it allows you to perform the same request as many times as you wish. It is very useful when certain headers are not functional, as sometimes changing the headers can grant access to a website that previously blocked us. You will be asked to provide the URL and the desired number of executions.

"Scrape A List of URLs": This function allows you to scrape a list of websites. You will be asked to upload a .txt file containing the URLs for the scraper to work correctly. It should be noted that if the list contains the same URL multiple times, it will have the same effect as the previous function. An example file containing URLs is provided with the scraper script.

Finally, a folder is also included with examples of scraped websites!

## Reach Out To Me <img alt="Contact Icon" width="40px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/ReachOutToMe.png"/>

[<img alt="LinkedIn" align="left" width="45px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/LinkedInIcon.svg"/>][linkedin]
[<img alt="Outlook" align="left" width="48px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/OutlookIcon.svg"/>][outlook]
[<img alt="Discord" align="left" width="47px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/DiscordIcon.svg"/>][discord]
[<img alt="Reddit" align="left" width="48px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/RedditIcon.png"/>][reddit]
[<img alt="Hack The Box" align="left" width="48px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/HackTheBoxIcon.svg"/>][hackthebox]
[<img alt="Try Hack Me" align="left" width="50px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/TryHackMeIcon.png"/>][tryhackme]
[<img alt="Credly" align="left" width="48px" src="https://github.com/IbrahimBenHariz/IbrahimBenHariz/blob/main/PortfolioResources/CredlyIcon.svg"/>][credly]


[linkedin]: https://www.linkedin.com/in/ibrahim-benhariz
[outlook]: mailto:ibrahim.benhariz@outlook.com
[discord]: https://discord.com/users/1111590525066297464
[reddit]: https://www.reddit.com/user/IbrahimBenHariz
[hackthebox]: https://app.hackthebox.com/profile/1525863
[tryhackme]: https://tryhackme.com/p/IbrahimBenHariz
[credly]: https://www.credly.com/users/ibrahim-ben-hariz
