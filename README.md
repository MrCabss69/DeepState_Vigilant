# DeepState_Vigilant

DeepState_Vigilant is a Python script designed to monitor the ongoing war situation in Ukraine. It has been tested and verified on Linux, Fedora 38.

The script utilizes data from Deep State Map, a live map that provides real-time updates on the conflict.

Data Source: https://deepstatemap.live

##  What it does?

DeepState_Vigilant is designed to periodically scrape the Deep State Map and save a screenshot of the current state of the map in a designated 'images' folder. Each screenshot is timestamped for easy reference. By default, the script captures and saves a screenshot every 12 hours.

The script employs the Selenium WebDriver for Firefox (GeckoDriver) to automate the browser interactions required for the scraping process. It is designed to run in headless mode, meaning it operates without opening a physical browser window. However, it can also be run in a non-headless mode for debugging purposes.

## Examples: 


## Suggestion
To ensure that the script runs continuously without the need for manual intervention, consider implementing it as an operating system service. This will allow the script to automatically restart with your computer.

For Linux users, you can use the systemctl services to achieve this.

## Improvements and debugging
Pending to add filters to monitor recent attacks on the web scrapping.

For debugging replace:

        web_navigator = DeepstateNavigator()

with:
        web_navigator = DeepstateNavigator(False)

This will exec the script on main thread, and you will see the actions live on your browser


We are currently working on adding filters to monitor recent attacks and it's types and damages during the web scraping process. Any contributions or suggestions for improvements are welcome.
