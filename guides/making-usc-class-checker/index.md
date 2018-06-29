---
title: Making USC Class Checker
layout: single

sidebar:
  nav: making-usc-class-checker-nav
---

## Repository Page

[https://github.com/neutonfoo/usc-class-checker-public](https://github.com/neutonfoo/usc-class-checker-public)

## Introduction

I wanted to write a class checker I could run in the Terminal and would alert me whenever a class opened up.

## Important Dependencies

In order for the program to run in the Terminal, it would have to run headless (with a hidden browser). To achieve this, I used [Selenium](https://www.seleniumhq.org/) (for browser automation) and [PhantomJS](http://phantomjs.org/) (a headless web driver to work with Selenium).

Development for PhantomJS has recently stopped, however, it was the easiest way to achieve headless automation (you can try using [ChromeDriver](http://chromedriver.chromium.org/) or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) but they may require additional setup). Using PhantomJS was also the easiest way to run the script on my Raspberry Pi (ChromeDriver and GeckoDriver had compatibility issues).

I installed Selenium and PhantomJS with [pip](https://pypi.org/project/pip/) and [Homebrew](https://brew.sh/) on my MacBook respectively.

## Overview

In order for the script to run, it would have to:
1. Log into Web Registration.
2. Click on the correct term (Summer 2018, Fall 2018 etc.)
3. Navigate to the department page for the class (For example [https://webreg.usc.edu/Courses?DeptId=CSCI](https://webreg.usc.edu/Courses?DeptId=CSCI))
4. Paginate through the pages to find the class then check for the availability.
	* Requires parsing of the HTML.
5. If the class is available, alert the user.

For my program, I chose to alert by opening a YouTube link. The audio from the video would be the "alert".

## Config File

We start by creating a config file. Important values to include are: the term, an alert link and the classes to check. We can save this file as `config.py` and, later, import it into the main program.

```python
term = 20183
alertLink = 'https://youtu.be/3M_5oYU-IsU?t=50s'
timeoutInterval = 30

classes = [
	{
		'depCode': 'ITP',
		'classCode': '125',
		'sectionNumber': '32039'
	}, {
		'depCode': 'ITP',
		'classCode': '125',
		'sectionNumber': '31842'
	}
]
```

## Logging into myUSC

Logging into Web Registration requires the user to log into myUSC first. Navigating to [http://my.usc.edu](http://my.usc.edu) redirects me to USC's Shibboleth login page. In order to sign in, a user would have to fill in the *USC NetID* and *Password* field then click the *Sign In*.

Inspecting the HTML of these fields, the *USC NetID* text box has `id="username"`, the *Password* text box has `id="password"`. The *Sign In* button has `name="_eventId_proceed"`. These values will can be used by Selenium to manipulate the page.

The username and password would be received through user input and then the text boxes would be filled with these values. Then a click on the *Sign In* box can be simulated. It takes a second for the DOM to load so a short delay will be added after the page is opened.

```python
import getpass
import time
import webbrowser
from selenium import webdriver
import config

username = input('Username: ')
password = getpass.getpass('Password: ')

driver = webdriver.PhantomJS()
driver.get('https://my.usc.edu')
time.sleep(1)

driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_name('_eventId_proceed').click()
```

## Navigating to Web Registration

After successfully logging into myUSC, the next step is to navigate to Web Registration. First, we redirect to the main Web Registration page then to the appropriate term page from our config file. We can then check to see the page was successfully loaded by checking `driver.current_url`.

```python
driver.get('https://my.usc.edu/portal/oasis/webregbridge.php')
driver.get('https://webreg.usc.edu/Terms/termSelect?term=' + str(config.term))

if driver.current_url == 'https://webreg.usc.edu/Departments':
	pass
else:
	quit()
```

## Prepping `classes`

Before we move onto checking class availability, it may be useful to modify `classes` to store some metadata, specifically, to store values regarding class availability (so we stop checking the class when it opens) and the page the class is on (so we can jump directly to it instead of paginating through all the pages to find it every interval).

```python
for c in classes:
	c['open'] = False
	c['onPage'] = 0
```

## Checking for Class Availability

Now that we have successfully logged into Web Registration, we have to check for class availability. This is were the bulk of our code will be written. As you can imagine, we will be writing most code in a loop.

We can create a variable to store the number of opened classes, which we will initialize to `0`. When a class opens, we will increment this value by `1` and the script stops running once the number of opened classes equals the size of `classes`. During each loop, we have to loop through each `c` in `classes` where `c['open'] == False`.

It may also be useful to print a timestamp every iteration of the loop. For this, we will also need to `import datetime`.

```python
numberOfOpenedClasses = 0
while numberOfOpenedClasses < len(config.classes):
	print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
```
