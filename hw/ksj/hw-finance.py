#pick locator도 활용..
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

###--------------------------------------------------### browser와 page
page.goto("https://finance.naver.com/")
page.pause()

###--------------------------------------------------### url로 이동
page.get_by_role("link", name="국내증시").click()
page.get_by_role("link", name="시가총액").first.click()
page.pause()

###--------------------------------------------------### 클릭 두번
# print(page.locator("table").nth(1).locator("thead > tr > th").all_inner_texts())
# page.pause()
# print(page.locator("table").nth(1).locator("tbody > tr").nth(1).locator("td").all_inner_texts())
# page.pause()
###--------------------------------------------------###
tag_table = page.locator("table").nth(1) #page.locator("table",has_text="코스피") 도 가능, 클래스 활용해서 해도 가능
tag_header = tag_table.locator("thead > tr > th").all_inner_texts()
# tag_body = tag_table.locator("tbody > tr").nth(1).locator("td").all_inner_texts()       #리스트형식 반환
###--------------------------------------------------### 시가총액 table에서 column name과 첫번째 데이터 추출(하나만 추출함)

tag_body = []
for tag_tr in tag_table.locator("tbody > tr").all():
    tag_td = tag_tr.locator("td").all_inner_texts()
    tag_body.append(tag_td)
    print(tag_td)
    
page.pause()

import json
dumped = json.dumps({"header" : tag_header, "body": tag_body},indent=2,ensure_ascii=False)
with open("page_1.json","w",encoding="utf-8") as fp:
    fp.write(dumped)
    pass
samsung_row = tag_table.locator("tbody > tr").filter(has=page.locator("a.tltle", has_text="삼성전자")).first
samsung_name = samsung_row.locator("a.tltle").inner_text()
samsung_price = samsung_row.locator("td").nth(2).inner_text()

print("종목명 :", samsung_name)
print("현재가 :", samsung_price)

page.pause()