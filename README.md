# Webscraping 3dhubs

Gather details of all the 3D printers of any given location by crawling 3dhubs.com. The data collected are,
  - Printer name
  - Address 
  - Materials 
  - Size
  - Color
  - Mobile Number


> Built for gathering 3D printer information. Just input the city names and let the program gather all the information you need to find your perfect 3D printer 


### Version
1.0

### Tech

open source projects to work properly:

* Selenium - Browser Automation Framework
* lxml - processing XML with python
* BeautifulSoup4(BS4) - parsing HTML and XMl
* Python - 2.7

### Installation


You need python installed globally:
Add the cities you want to scrap for in the cities.txt file in the project directory,

```sh
$ python main.py
```
### Todos

 - Print to file
 - Add interface
 - Move to a headless browser
