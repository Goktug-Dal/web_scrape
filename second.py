from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,"lxml")

    courses_html_tags = soup.find_all("h5", attrs= {"class": "card-title"})
    course_cards = soup.find_all("div", attrs={"class": "card"})

    for course in courses_html_tags:
        print(course.text + "\n")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        print(course_name + " " + course_price)