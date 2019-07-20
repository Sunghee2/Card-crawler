from selenium import webdriver
import csv
import time

link = 'https://datalab.naver.com/local/card_result.naver'
card_btn_xpath = '//div[@class="trend_tab"]/strong[@class="tab_list _by_category"]/a'
search_btn_xpath = '//a[@class="com_btn_srch"]'

f = open('result.csv', 'w', encoding='utf-8')
csvfile = csv.writer(f)
csvfile.writerow(['지역', '성별', '연령', '기간', '업종', '값'])

driver = webdriver.Chrome('./chromedriver')
driver.get(link)

driver.find_element_by_xpath(card_btn_xpath).click()
time.sleep(5)

# 지역 선택
for i in range(1, 18):
    area_option_xpath = '((//div[@class="analysis_filter"]/div[@class="filter_area"])[1]/div[@class="filter_option scroll_cst"]/ul[@class="option_list _list1"]/li)[' + str(i) + ']'
    driver.find_element_by_xpath(area_option_xpath).click()
    
    area = driver.find_element_by_xpath(area_option_xpath + '/a').text
    print(area)

    if i == 1:
        industry_option_xpath = '((//div[@class="analysis_step v2"]/div[@class="analysis_filter"]/div[@class="filter_area"])[1]/div[@class="filter_option scroll_cst"]/ul/li)[2]/span/label'
        industry_all_option_xpath = '((//div[@class="analysis_step v2"]/div[@class="analysis_filter"]/div[@class="filter_area"])[2]/div[@class="filter_option scroll_cst"]/ul/li)[1]/span/label'
        driver.find_element_by_xpath(industry_option_xpath).click()
        time.sleep(3)
        driver.find_element_by_xpath(industry_all_option_xpath).click()

    # 성별 선택
    for j in range(2, 4):
        gender_option_xpath = '((//div[@class="add_filter_area"]/div[@class="step_group"])[1]/div[@class="filter_group"]/span)[' + str(j) + ']'
        driver.find_element_by_xpath(gender_option_xpath).click()

        gender = driver.find_element_by_xpath(gender_option_xpath + '/label').text
        print(gender)

        # 나이 선택
        for k in range(3, 8):
            age_option_xpath = '((//div[@class="add_filter_area"]/div[@class="step_group"])[2]/div[@class="filter_group"]/span)[' + str(k) + ']'
            driver.find_element_by_xpath(age_option_xpath).click()

            age = driver.find_element_by_xpath(age_option_xpath + '/label').text
            print(age)

            # 조회 버튼 클릭
            driver.find_element_by_xpath(search_btn_xpath).click()

            # 그래프 월별 선택
            for l in range(1, 14):
                time.sleep(2)
                graph_click_xpath = '(//div[@class="section_graph"]/div[@class="com_box_inner"]/div[@class="graph_area"]/div[@class="inner_graph_area _trend_graph bb"]/*[name()="svg"]/*[name()="g"]/*[name()="g" and @class="bb-chart"]/*[name()="g" and @class="bb-event-rects bb-event-rects-single"]/*[name()="rect"])[' + str(l) + ']'
                driver.find_element_by_xpath(graph_click_xpath).click()
                
                period = driver.find_element_by_xpath('//div[@class="tooltip_period"]').text

                print(period)

                # 그래프 내의 카테고리별 값 가져오기
                for m in range(1, 9):
                    category_xpath = '(//div[@class="graph_tooltip"]/div[@class="tooltip"])[' + str(m) + ']'
                    category = driver.find_element_by_xpath(category_xpath + '/span[@class="info"]').text
                    value = driver.find_element_by_xpath(category_xpath + '/span[@class="value"]').text

                    csvfile.writerow([area, gender, age, period, category, value])

f.close()







