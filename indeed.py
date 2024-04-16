from selenium import webdriver
from faulthandler import is_enabled
import time
from tkinter import Button
from xmlrpc.client import boolean
from selenium import webdriver
from selenium.webdriver.chrome.options import Options    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuzzywuzzy import fuzz
from selenium.common.exceptions import NoSuchElementException
import csv
import sys
 
class Indeed:
     
    def __init__(self):
        
        # self.value = "samsung electronics"
        company = ' '.join([str(elem) for elem in sys.argv[1:]])
        self.value =company
        self.company_names = [];
        self.company_names_score = [];
        options = webdriver.ChromeOptions() 
        # options.add_argument("--start-maximized");

        # options.headless = True
        options.add_argument("user-data-dir=C:\\Users\\vrish\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\vrish\\public\\glassdoor\\chromedriver.exe", chrome_options=options)
        # self.driver.get("https://www.indeed.com/companies")
        self.driver.set_window_rect(width=1920, height=1080)

    def _login(self):
        # siliy69430@corylan.com
        # root@123
        driver = self.driver
        # driver.get("https://www.indeed.com/companies")
        driver.get("https://in.indeed.com/companies")
        time.sleep(2);
        print("123121221")
  
  
    def search(self):
        driver = self.driver;
        # driver.get("https://www.indeed.com/companies")
        time.sleep(2);
        # try:
        #     element = WebDriverWait(driver, 5).until(
        #         EC.element_to_be_clickable((By.XPATH,'//*[@id="ifl-InputFormField-3"]'))
        #         )

        # except Exception as e:
        #     print(e)
        
        
        #  doing the above code but now using css selector 
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#ifl-InputFormField-3'))
                )

        except Exception as e:
            print(e)
            
        #  clicking on submit
        element.send_keys(self.value);
        time.sleep(2)
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[1]/form/div/div[2]/button'))
                ).click();

        except Exception as e:
            print(e)
        time.sleep(2)


    def select_company(self):
        driver = self.driver;
        isPresent = True
        while(isPresent):
      
            try:
                
                    
                dropdown = driver.find_elements(By.CSS_SELECTOR,'#main > div > div.css-evzha8.eu4oa1w0 > section.css-kyg8or.eu4oa1w0>div.css-bfl6ls.e37uo190')
                              
                for i in dropdown:
 
                    try:                 
                        name = i.find_element(By.CSS_SELECTOR,'#main > div > div.css-evzha8.eu4oa1w0 > section.css-kyg8or.eu4oa1w0 >div > div >div >div.css-11ksq3.eu4oa1w0>div>a>div')
                        self.company_names.append(name.text)
                        print(name.text)
                    except Exception as e:
                        print("no  company name")
            except Exception as e:
                    
                    print("no listing inside area")     
            
            # this code is here if next button comes to being 
            # try:
            #     element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'Next'))).is_displayed()
            #     isPresent = True;
            #     try:
            #         s = driver.find_element(By.LINK_TEXT,'Next')
            #         # perform click with execute_script method
            #         driver.execute_script("arguments[0].click();",s)
            #     except Exception as e:
            #             print("was not able to click")
            # except Exception as e:         
            #     isPresent = False;
            #     print("no next button")
            isPresent =False
            print(isPresent)            
            print(self.company_names)
        for value in (self.company_names):            
            self.company_names_score.append(fuzz.ratio(self.value.lower(), value.lower()));
        time.sleep(2);
        print(self.company_names_score)
        try:
            driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div[1]/form/div/div[1]/div/div/div/span/input').send_keys(Keys.CONTROL + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
        except Exception as e:
            print("issue while cleaning search bar")
            print(e)
        try:
            element = WebDriverWait(driver, 5).until(
                  EC.element_to_be_clickable((By.XPATH,'//*[@id="ifl-InputFormField-3"]'))

            )
            #  entering again while making exactly like drop down values
            element.send_keys(self.company_names[self.company_names_score.index(max(self.company_names_score))])
            
            element.send_keys(Keys.RETURN);
            
        except Exception as e:
            print(e)
        #  checking if we are getting unique value or not 
        try:
            dropdown = driver.find_element(By.CLASS_NAME,'css-1s5eo7v.eu4oa1w0').click();
        except Exception as e:
            print(e)
        time.sleep(5);   


    # def general_score(self):
        driver = self.driver;
        
        # getting basic information here 
        try:
            work_happiness_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[1]/div[1]/div[1]')
            for i in work_happiness_score:
                print(i.get_attribute("innerText"))
        except Exception as e:
            print(e)

        time.sleep(2);

        try:
            appreciation_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[2]/div[1]/div[1]')
            for i in appreciation_score:
                print(i.get_attribute("innerText"))
        except Exception as e:
            print(e)
        time.sleep(2);

        try:
            learning_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[3]/div[1]/div[1]')
            for i in  learning_score:
                print(i.get_attribute("innerText"))
        except Exception as e:
            print(e)
        time.sleep(2);


    # def more_detailed_review(self):
        driver = self.driver;
        #cmp-skip-header-desktop > div > ul > li:nth-child(3) > a > span
        try:
            element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#cmp-skip-header-desktop > div > ul > li:nth-child(3) > a > span')))
            element.click()
        except Exception as e:
            print(e)
        # try:
        #     element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[6]/section/div/div[1]/div[2]/a')))
        #     element.send_keys(Keys.RETURN);
        # except Exception as e:
        #     print(e)
            
        time.sleep(2);
        
        #  here we are star and info from the first page dont know where will i use it again
        
        # get star rating
        # css-rr5fiy eu4oa1w0
        # try:
        #     rating_score = driver.find_elements(By.CLASS_NAME,'css-1c33izo.e1wnkr790')
        #     for i in rating_score:
        #         print(i.get_attribute("innerText").split("\n"))
        # except Exception as e:
        #     print(e)

        # try:
        #     review_heading_info = driver.find_elements(By.CLASS_NAME,'css-82l4gy.eu4oa1w0')
        #     for i in review_heading_info:
        #         print(i.get_attribute("innerText"))
        # except Exception as e:
        #     print(e)
        
        time.sleep(2);


    def more_detailed_review(self):
        print("::::::::::::")
        driver = self.driver
        try:
            dropdown = driver.find_elements(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys')          
            for i in dropdown:
                # print(i)
                try:
                    rating = i.find_element(By.CLASS_NAME,'css-1c33izo.e1wnkr790')
                   
                    print(rating.text)
                except Exception as e:
                    print("no rating")
                    pass
                try :
                    #  i have updated my main_Data to the new css selector as it was printing whole values instead of printing only main data it was also showing pros and cons 
                    # main_Data = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0')
                    
                    
                    
                    main_Data = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>span>span>span:nth-child(1)')
                   
                    
                    print(main_Data.text)
                except Exception as e:
                    print("no main_data")
                    pass
                #  checking pros and cons here 
                
                try:
                    
                    
                    # change the pros path here and updated with new path as with old path the first value was not being  shwoed
                    # pros = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div >h2.css-yuegbt.e1tiznh50') 
                    pros = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-yuegbt.e1tiznh50') 
                    
                     #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-yuegbt.e1tiznh50
                    
                    # print(pros.text)
                    try:
                        if pros.text == "Pros":
                            # pros_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(1) > div >span')
                            pros_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div:nth-child(1)>div.css-1z0411s.e1wnkr790>span>span.css-82l4gy.eu4oa1w0')
                            print(pros_value.text)    
                           
                    except Exception as e:
                        print("no pros data")
                        # pass
                except Exception as e:
                    print("no pros element")
                    pass
                try:
                    # also  i have chnaged the path as first value was shown wrong 
                    # cons = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(2)>h2.css-i6a6qi.e1tiznh50') 
                    
                    cons = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-i6a6qi.e1tiznh50') 
                    
                    try:
                        if cons.text == "Cons":
                            cons_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div:nth-child(2)>div.css-1z0411s.e1wnkr790>span>span.css-82l4gy.eu4oa1w0')
                            print(cons_value.text)    
                    except Exception as e:
                        print("no cons data")        
                except Exception as e:
                    print("no cons element")
                    pass
                time.sleep(5)
        except Exception as e:
                    print("no listing")
                    pass
            # data =[]
            # data.append([rating.text,main_Data.text,pros_value.text,cons_value.text])
            # # time.sleep(5)
            # fields = ['rating', 'data' , 'pros' , 'cons' ] 
            # with open('export.csv', 'w') as f:
            #     write = csv.writer(f)
                
            #     write.writerow(fields)
            #     write.writerows(data)
            #     print(data)
    
    def looping_on_all_pages(self):
        print("no i am trying to loop")
        driver = self.driver
        time.sleep(2)
        isPresent = True
        data = []
        fields = ['rating', 'main_data' ,'likes' , 'dislikes'] 
        star_value=''
        pros_data=''
        cons_data=''
        main_data = ''
        while(isPresent):
            try:
                
               
                dropdown = driver.find_elements(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys')          
                for i in dropdown:
                    # print(i)
                    try:
                        rating = i.find_element(By.CLASS_NAME,'css-1c33izo.e1wnkr790')
                        star_value = rating.text
                        # print(rating.text)
                    except Exception as e:
                        # print("no rating")
                        star_value ="No rating "
                        # pass
                    try :
                        #  i have updated my main_Data to the new css selector as it was printing whole values instead of printing only main data it was also showing pros and cons 
                        # main_Data = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0')
                        
                        
                        
                        main_Data = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>span>span>span:nth-child(1)')
                    
                        main_data = main_Data.text
                        # print(main_Data.text)
                    except Exception as e:
                        main_data = "No main_data"
                        # print("no main_data")
                        # pass
                    #  checking pros and cons here 
                    
                    try:
                        
                        
                        # change the pros path here and updated with new path as with old path the first value was not being  shwoed
                        # pros = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div >h2.css-yuegbt.e1tiznh50') 
                        pros = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-yuegbt.e1tiznh50') 
                        
                        #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-yuegbt.e1tiznh50
                        
                        # print(pros.text)
                        try:
                            if pros.text == "Pros":
                                # pros_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(1) > div >span')
                                pros_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div:nth-child(1)>div.css-1z0411s.e1wnkr790>span>span.css-82l4gy.eu4oa1w0')
                                # print("pros: "+pros_value.text)    
                                pros_data = pros_value.text
                            
                        except Exception as e:
                            pros_data = "no pros data"
                            # print("no pros data")
                            # pass
                    except Exception as e:
                        pros_data="no pros element"
                        # print("no pros element")
                        pass
                    try:
                        # also  i have chnaged the path as first value was shown wrong 
                        # cons = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(2)>h2.css-i6a6qi.e1tiznh50') 
                        
                        cons = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div>h2.css-i6a6qi.e1tiznh50') 
                        
                        try:
                            if cons.text == "Cons":
                                cons_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0>div>div:nth-child(2)>div.css-1z0411s.e1wnkr790>span>span.css-82l4gy.eu4oa1w0')
                                cons_data = cons_value.text
                                # print("cons: "+cons_value.text)    
                        except Exception as e:
                            cons_data = "no cons data"
                            # print("no cons data")        
                    except Exception as e:
                        cons_data = "no cons element "
                        # print("no cons element")
                        pass
                    time.sleep(2)
                    data.append([star_value,main_data,pros_data,cons_data])
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            except Exception as e:
                        print("no listing")
                        pass
           
            
            try:
                element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'Next'))).is_displayed()
                isPresent = True;
                try:
                    s = driver.find_element(By.LINK_TEXT,'Next')
                    # perform click with execute_script method
                    driver.execute_script("arguments[0].click();",s)
                except Exception as e:
                        print("was not able to click")
            except Exception as e:         
                isPresent = False;
                print("no next button")
           
            print(isPresent)
        with open('export_indeed.csv', 'w') as f:
            
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(data)
            # print(data) 
    
if __name__ == '__main__':  
    kt = Indeed()
    kt._login()
    kt.search()
    kt.select_company()
    # # kt.general_score()
    # # kt.more_detailed_review()
    kt.looping_on_all_pages()