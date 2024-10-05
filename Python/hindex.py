class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        print(citations)
        if citations[0] == 0:
            return 0
        dem = 0
        for i in range(0,len(citations)):
            if citations[i] == i+1:
                return i+1
            if citations[i] > i+1:
                dem += 1
        return dem
        
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()                   