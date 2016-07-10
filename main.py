#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import time
import sys

def runforcity(place,url):
    baseurl = url
    mydriver = webdriver.Firefox()
    mydriver.get(baseurl)
    mydriver.maximize_window()
    html_source = mydriver.page_source
    re.sub(r'[^\x00-\x7F]+',' ', html_source)
    soup = BeautifulSoup(html_source,'html.parser')

    c = 2
    while True:
        detail_button = mydriver.find_elements(By.XPATH, '//button[@class="h3d-button h3d-button--primary"]')
        for but in detail_button:
            try:

                mydriver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', but)
                time.sleep(2)
                but.click()
                tempsrc = mydriver.page_source
                re.sub(r'[^\x00-\x7F]+',' ', tempsrc)
                stemp = BeautifulSoup(tempsrc,'html.parser')

                out = ""
                out = out + place +"|"

                out = out + stemp.find('div',{"class":"h3d-grid__column h3d-grid__column--small-11 h3d-grid__column--unspaced"}).find('div',{"class":"ng-binding"}).find(text=True).replace(",","")
                out = out +"|"
                #name
                out = out + stemp.find('div',{"class":"h3d-hub-card__heading ng-binding"}).find(text=True)[:-6]

                out = out + "|"
                #material
                xtemp = stemp.find('select',{"id":"material"}).find('optgroup').findAll('option')
                for o in xtemp:
                    out = out + o.find(text=True)

                out = out + "|"
                #rating
                out = out + stemp.find('div',{"class":"h3d-hub-card__body"}).find('div',{"class":"h3d-rating ng-isolate-scope h3d-rating--highlight"}).find('div',{"class":"h3d-rating__suffix"}).find('span').find(text=True)

                out = out +"|"
                #summary
                out = out + stemp.find('div',{"class":"h3d-card__body"}).find('div',{"class":"ng-binding ng-scope"}).find(text=True).replace('\n', ' ').replace('\r', '')

                print out


                j = mydriver.find_element(By.XPATH, '//div[@data-ng-click="closeThisDialog()"]')
                j.click()
                time.sleep(2)
            except:
                pass
        try:
            k = mydriver.find_elements(By.XPATH, '//button[@title="Go to page '+str(c)+'"]')
            c = c + 1
            mydriver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', k[len(k)-1])
            k[len(k)-1].click()
            time.sleep(2)
        except:
            break



runforcity("southamerica","https://www.3dhubs.com/3dprint#/3dprint?place=South%20America&latitude=-8.783195000000001&longitude=-55.49147700000003")

