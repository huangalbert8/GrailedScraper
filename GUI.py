from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class P(FloatLayout):
    pass

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))
    popupWindow.open()

class MainWindow(Screen):
    item = ObjectProperty(None)

    def clean(self):
        self.item.text = ""

    def submit(self):
        name = self.item.text
        #shoe = self.manager.ids.shoesWindow
        #self.cost_output.text = str(shoe.sz)
        shirtSize = [False] * 7
        shirtSize[0] = self.manager.screens[1].ids.szXXS.active
        shirtSize[1] = self.manager.screens[1].ids.szXS.active
        shirtSize[2] = self.manager.screens[1].ids.szS.active
        shirtSize[3] = self.manager.screens[1].ids.szM.active
        shirtSize[4] = self.manager.screens[1].ids.szL.active
        shirtSize[5] = self.manager.screens[1].ids.szXL.active
        shirtSize[6] = self.manager.screens[1].ids.szXXL.active
        for x in shirtSize:
            print(x)
        pantSize = [False] * 9
        pantSize[0] = self.manager.screens[2].ids.sz26.active
        pantSize[1] = self.manager.screens[2].ids.sz27.active
        pantSize[2] = self.manager.screens[2].ids.sz28.active
        pantSize[3] = self.manager.screens[2].ids.sz29.active
        pantSize[4] = self.manager.screens[2].ids.sz30.active
        pantSize[5] = self.manager.screens[2].ids.sz31.active
        pantSize[6] = self.manager.screens[2].ids.sz32.active
        pantSize[7] = self.manager.screens[2].ids.sz33.active
        pantSize[8] = self.manager.screens[2].ids.sz34.active
        for x in pantSize:
            print(x)
        shoeSize = [False] * 11
        shoeSize[0] = self.manager.screens[3].ids.sz7.active
        shoeSize[1] = self.manager.screens[3].ids.sz7_5.active
        shoeSize[2] = self.manager.screens[3].ids.sz8.active
        shoeSize[3] = self.manager.screens[3].ids.sz8_5.active
        shoeSize[4] = self.manager.screens[3].ids.sz9.active
        shoeSize[5] = self.manager.screens[3].ids.sz9_5.active
        shoeSize[6] = self.manager.screens[3].ids.sz10.active
        shoeSize[7] = self.manager.screens[3].ids.sz10_5.active
        shoeSize[8] = self.manager.screens[3].ids.sz11.active
        shoeSize[9] = self.manager.screens[3].ids.sz11_5.active
        shoeSize[10] = self.manager.screens[3].ids.sz12.active
        for x in shoeSize:
            print(x)

        filename = "grailed.csv"
        csv_header = "Designer; Name; New_Price; Old_Price; Size; Last_Bump; Link\n"
        f = open(filename, "w")
        f.write(csv_header)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1920,1080")
        PATH = "/Users/alberthuang/Desktop/chromedriver"
        driver = webdriver.Chrome(options=chrome_options, executable_path=PATH)
        URL = "https://www.grailed.com/shop/"
        driver.get(URL)
        search = driver.find_element_by_id("globalheader_search")
        button = driver.find_element_by_class_name("Button._small._secondary.Page-Header-Search-Button")
        home = driver.find_element_by_class_name("Page-Header-Logo")
        home.click()
        out = driver.find_element_by_class_name("close")
        out.click()
        time.sleep(1)
        search.send_keys(name)
        button.click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ais-Panel-body")))
        sizes = driver.find_elements_by_class_name("Filters--GroupHeader")
        used = False
        for x in shirtSize:
            if x:
                used = True
                break
        if used:
            sizes[0].click()
            if(shirtSize[0]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.xxs_XXS/40").click()
            if (shirtSize[1]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.xs_XS/42").click()
            if (shirtSize[2]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.s_S/44-46").click()
            if (shirtSize[3]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.m_M/48-50").click()
            if (shirtSize[4]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.l_L/52-54").click()
            if (shirtSize[5]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.xl_XL/56").click()
            if (shirtSize[6]):
                driver.find_element_by_id("FilterToggle_checkbox_tops.xxl_XXL/58").click()
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        used = False
        for x in pantSize:
            if x:
                used = True
                break
        if used:
            sizes[1].click()
            time.sleep(2)
            if (pantSize[0]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.26_26").click()
            if (pantSize[1]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.27_27").click()
            if (pantSize[2]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.28_28").click()
            if (pantSize[3]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.29_29").click()
            if (pantSize[4]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.30_30").click()
            if (pantSize[5]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.31_31").click()
            if (pantSize[6]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.32_32").click()
            if (pantSize[7]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.33_33").click()
            if (pantSize[8]):
                driver.find_element_by_id("FilterToggle_checkbox_bottoms.34_34").click()
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        used = False
        for x in shoeSize:
            if x:
                used = True
                break
        if used:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            sizes[3].click()
        if (shoeSize[0]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.7_7").click()
        if (shoeSize[1]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.7.5_7.5").click()
        if (shoeSize[2]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.8_8").click()
        if (shoeSize[3]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.8.5_8.5").click()
        if (shoeSize[4]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.9_9").click()
            time.sleep(1)
        if (shoeSize[5]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.9.5_9.5").click()
            time.sleep(1)
        if (shoeSize[6]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.10_10").click()
            time.sleep(1)
        if (shoeSize[7]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.10.5_10.5").click()
            time.sleep(1)
        if (shoeSize[8]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.11_11").click()
            time.sleep(1)
        if (shoeSize[9]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.11.5_11.5").click()
            time.sleep(1)
        if (shoeSize[10]):
            driver.find_element_by_id("FilterToggle_checkbox_footwear.12_12").click()
            time.sleep(1)

        time.sleep(2)
        listing = driver.find_elements_by_class_name("ais-Panel-body")[0].text
        print(listing)
        listing = int(listing.split(" ")[0].replace(",", ""))
        print(listing)
        max = 40
        time.sleep(4)
        if listing > max:
            listing = max
        print(listing)
        scrolls = round(listing / 40) + 1
        for i in range(0, scrolls):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            print("still going")

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "feed-item")))
            items = driver.find_elements_by_class_name("feed-item")
            count = 0
            print(len(items))
            for i in range(0, listing):
                count = count + 1
                # print(len(items))
                print(count)
                # print(items[i].text)
                link = items[i].find_element_by_xpath('./a').get_attribute("href")
                # print(link)
                price = items[i].find_element_by_class_name("listing-price-and-heart")
                # print(price.text)
                last_bump = items[i].find_element_by_class_name("date-ago").text
                designer = items[i].find_element_by_class_name("listing-designer.truncate").text
                size = items[i].find_element_by_class_name("listing-size.sub-title").text
                name = items[i].find_element_by_class_name("truncate.listing-title").text
                try:
                    new_price = price.find_element_by_class_name("sub-title.new-price").text
                    old_price = price.find_element_by_class_name("sub-title.original-price.strike-through").text
                except:
                    new_price = price.find_element_by_class_name("sub-title.original-price").text
                    old_price = "none"

                print(last_bump, designer, size, name, new_price)
                f.write(
                    designer + ";" + name + ";" + new_price + ";" + old_price + ";" + size + ";" + last_bump + ";" + link + "\n")
                # driver.get(link)
                # desc = driver.find_element_by_id("listing-description-text")
                # print(desc.text)
                # driver.back()
                # time.sleep(5)

        finally:
            f.close()
            driver.quit()


def printSizes(self):
        self.shirtsWindow.insert_data()


class ShirtsWindow(Screen):
    szXXS = ObjectProperty(None)
    szXS = ObjectProperty(None)
    szS = ObjectProperty(None)
    szM = ObjectProperty(None)
    szL = ObjectProperty(None)
    szXL = ObjectProperty(None)
    szXXL = ObjectProperty(None)

    def selectAll(self):
        self.szXXS.active = True
        self.szXS.active = True
        self.szS.active = True
        self.szM.active = True
        self.szL.active = True
        self.szXL.active = True
        self.szXXL.active = True

    def clean(self):
        self.szXXS.active = False
        self.szXS.active = False
        self.szS.active = False
        self.szM.active = False
        self.szL.active = False
        self.szXL.active = False
        self.szXXL.active = False


    def checkbox_click(self, instance, value):
        if value is True:
            print(self.szXXL.id)
        else:
            print("Checkbox Unchecked")

    def insert_data(self):
        shirtSize = [False]*7
        if self.szXXS.active:
            shirtSize[0] = True
        else:
            shirtSize[0] = False
        if self.szXS.active:
            shirtSize[1] = True
        else:
            shirtSize[1] = False
        if self.szS.active:
            shirtSize[2] = True
        else:
            shirtSize[2] = False
        if self.szM.active:
            shirtSize[3] = True
        else:
            shirtSize[3] = False
        if self.szL.active:
            shirtSize[4] = True
        else:
            shirtSize[4] = False
        if self.szXL.active:
            shirtSize[5] = True
        else:
            shirtSize[5] = False
        if self.szXXL.active:
            shirtSize[6] = True
        else:
            shirtSize[6] = False
        for shirt in shirtSize:
            print(shirt)


class PantsWindow(Screen):
    sz26 = ObjectProperty(None)
    sz27 = ObjectProperty(None)
    sz28 = ObjectProperty(None)
    sz29 = ObjectProperty(None)
    sz30 = ObjectProperty(None)
    sz31 = ObjectProperty(None)
    sz32 = ObjectProperty(None)
    sz33 = ObjectProperty(None)
    sz34 = ObjectProperty(None)

    def selectAll(self):
        self.sz26.active = True
        self.sz27.active = True
        self.sz28.active = True
        self.sz29.active = True
        self.sz30.active = True
        self.sz31.active = True
        self.sz32.active = True
        self.sz33.active = True
        self.sz34.active = True

    def clean(self):
        self.sz26.active = False
        self.sz27.active = False
        self.sz28.active = False
        self.sz29.active = False
        self.sz30.active = False
        self.sz31.active = False
        self.sz32.active = False
        self.sz33.active = False
        self.sz34.active = False

    def insert_data(self):
        global pantSize
        pantSize = [False]*9
        if self.sz26.active:
            pantSize[0] = True
        else:
            pantSize[0] = False
        if self.sz27.active:
            pantSize[1] = True
        else:
            pantSize[1] = False
        if self.sz28.active:
            pantSize[2] = True
        else:
            pantSize[2] = False
        if self.sz29.active:
            pantSize[3] = True
        else:
            pantSize[3] = False
        if self.sz30.active:
            pantSize[4] = True
        else:
            pantSize[4] = False
        if self.sz31.active:
            pantSize[5] = True
        else:
            pantSize[5] = False
        if self.sx32.active:
            pantSize[6] = True
        else:
            pantSize[6] = False
        if self.sx33.active:
            pantSize[7] = True
        else:
            pantSize[7] = False
        if self.sx34.active:
            pantSize[8] = True
        else:
            pantSize[8] = False


class ShoesWindow(Screen):
    sz8 = ObjectProperty(None)
    sz8_5 = ObjectProperty(None)
    sz9 = ObjectProperty(None)
    sz9_5 = ObjectProperty(None)
    sz10 = ObjectProperty(None)
    sz10_5 = ObjectProperty(None)
    sz11 = ObjectProperty(None)
    sz11_5 = ObjectProperty(None)
    sz12 = ObjectProperty(None)

    def selectAll(self):
        self.sz8.active = True
        self.sz8_5.active = True
        self.sz9.active = True
        self.sz9_5.active = True
        self.sz10.active = True
        self.sz10_5.active = True
        self.sz11.active = True
        self.sz11_5.active = True
        self.sz12.active = True

    def clean(self):
        self.sz8.active = False
        self.sz8_5.active = False
        self.sz9.active = False
        self.sz9_5.active = False
        self.sz10.active = False
        self.sz10_5.active = False
        self.sz11.active = False
        self.sz11_5.active = False
        self.sz12.active = False

    def insert_data(self):
        global shoeSize
        shoeSize = [False] * 9
        if self.sz8.active:
            shoeSize[0] = True
        else:
            shoeSize[0] = False
        if self.sz8_5.active:
            shoeSize[1] = True
        else:
            shoeSize[1] = False
        if self.sz9.active:
            shoeSize[2] = True
        else:
            shoeSize[2] = False
        if self.sz9_5.active:
            shoeSize[3] = True
        else:
            shoeSize[3] = False
        if self.sz10.active:
            shoeSize[4] = True
        else:
            shoeSize[4] = False
        if self.sz10_5.active:
            shoeSize[5] = True
        else:
            shoeSize[5] = False
        if self.sz11.active:
            shoeSize[6] = True
        else:
            shoeSize[6] = False
        if self.sz11_5.active:
            shoeSize[7] = True
        else:
            shoeSize[7] = False
        if self.sz12.active:
            shoeSize[8] = True
        else:
            shoeSize[8] = False
        for sho in shoeSize:
            print(sho)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv



if __name__ == "__main__":
    MyMainApp().run()

