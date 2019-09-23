from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
try:
    driver.get("https://www.ctrip.com")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='酒店'])[2]/following::b[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='国内机票'])[2]/following::a[1]").click()
    driver.find_element_by_id("fl_txtDDatePeriod1").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[2]/following::a[43]").click()
    driver.find_element_by_id("fl_txtDDatePeriod1").clear()
    driver.find_element_by_id("fl_txtDDatePeriod1").send_keys("2019-11-08")
    driver.find_element_by_id("fl_txtADatePeriod1").click()
    driver.find_element_by_id("fl_flight_way_s").click()
    driver.find_element_by_id("fl_btnSearchFlight").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='周四'])[1]/following::div[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='周六'])[1]/following::div[1]").click()
finally:
    driver.close()