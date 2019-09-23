from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
from datetime import date, timedelta


options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)


with open('dates.txt', 'r') as f:
    dates = f.read().splitlines()
depDate_from_list = dates[0].split('-')
depDate_from_list = [int(a) for a in depDate_from_list]
depDate_to_list = dates[1].split('-')
depDate_to_list = [int(a) for a in depDate_to_list]
arrDate_from_list = dates[2].split('-')
arrDate_from_list = [int(a) for a in arrDate_from_list]
arrDate_to_list = dates[3].split('-')
arrDate_to_list = [int(a) for a in arrDate_to_list]

depCity = dates[4]
arrCity = dates[5]

depDate_from = date(depDate_from_list[0], depDate_from_list[1], depDate_from_list[2])
depDate_to = date(depDate_to_list[0], depDate_to_list[1], depDate_to_list[2])

delta = depDate_to - depDate_from
depDates = []
for i in range(delta.days + 1):
    day = depDate_from + timedelta(days=i)
    depDates.append(str(day))

arrDate_from = date(arrDate_from_list[0], arrDate_from_list[1], arrDate_from_list[2])
arrDate_to   = date(arrDate_to_list[0], arrDate_to_list[1], arrDate_to_list[2])

delta = arrDate_to - arrDate_from
arrDates = []
for i in range(delta.days + 1):
    day = arrDate_from + timedelta(days=i)
    arrDates.append(str(day))

print(depDates, '\n', arrDates)
msgs = ''
for depDate in depDates:
    for arrDate in arrDates:
        try:
            driver.get("https://www.csair.com/au/en/index.shtml")

            # Switch to csair-china
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='My account'])[1]/following::span[1]").click()

            driver.find_element_by_link_text("China").click()
            driver.find_element_by_link_text(u"简体中文").click()
            driver.find_element_by_link_text(u"往返").click()   # round-trip

            driver.find_element_by_id("fDepCity").click()
            driver.find_element_by_id("fDepCity").clear()
            driver.find_element_by_id("fDepCity").send_keys(depCity)

            driver.find_element_by_id("fArrCity").click()
            driver.find_element_by_id("fArrCity").clear()
            # wait to finish the key sending
            time.sleep(2)
            driver.find_element_by_id("fArrCity").send_keys(arrCity)
            time.sleep(3)

            # Use js to remove the readonly att of the calendar
            driver.find_element_by_xpath("//body").click()
            js1 = 'document.getElementById("fDepDate").removeAttribute("readonly")'
            js2 = 'document.getElementById("fArrDate").removeAttribute("readonly")'
            driver.execute_script(js1)
            driver.execute_script(js2)

            driver.find_element_by_id('fDepDate').click()
            driver.find_element_by_id('fDepDate').clear()
            driver.find_element_by_id('fDepDate').send_keys(depDate)
            driver.find_element_by_id('fArrDate').click()
            driver.find_element_by_id('fArrDate').clear()
            driver.find_element_by_id('fArrDate').send_keys(arrDate)

            driver.find_element_by_link_text(u"立即查询").click()
            price = driver.find_element_by_xpath(
                '//div[@id="sh-trip-item-0-0"]//div[@class="price totalPrc z-active"]//'
                'strong[@class="num sh-prc-fare"]').text
            duration = driver.find_element_by_xpath(
                '//div[@id="sh-trip-item-0-0"]//div[@class="sh-duration"]').text

            msg = '{}({} 到 {})  {}({} 到 {})   {}   {}'.format(
                depDate, depCity, arrCity, arrDate, arrCity, depCity, duration, price)
            msgs = msgs + msg + '\n'
            print(msg)

        except:
            print('{}({} 到 {})  {}({} 到 {})   No flight found'.format(
                depDate, depCity, arrCity, arrDate, arrCity, depCity))

msg_head = "============== Searched at " + str(date.today()) + " ==============\n"
msg_tail = "====================================================\n"
msgs = msg_head + msgs + msg_tail
with open('prices.txt', 'a') as f:
    f.write(msgs)
driver.quit()
