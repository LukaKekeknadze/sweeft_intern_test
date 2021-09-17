#დავალება 1
# def palindrom(text):
#     if text == text[::-1]: #ფუნქციაზე მიწოდებული ტექსტის შემობრუნება ხდება შემდეგი ინდექსაციით [საწყისი , საბოლოო და ნაბიჯი)
#         return True
#     else:
#         return False
# str1 = palindrom("luka")
# str2 = palindrom("ana")
# print(str1,str2)



#დავალება 2
# def change(money):
#     x = money
#     list_change = []
#     while x!=0:
#         if x >= 50:
#             x -=50
#             list_change.append(50)
#         if x >= 20 and x<50:
#                 x-=20
#                 list_change.append(20)
#         if x>=10 and x<20:
#                 x -= 10
#                 list_change.append(10)
#         if x>=5 and x<10:
#             x -= 5
#             list_change.append(5)
#         if x>=1 and x<5:
#             x -= 1
#             list_change.append(1)
#     return len(list_change)
# money1 = change(80)
# print(money1)


#დავალება 3
# def brackets(bracks):
#     bracket1 = []
#     bracket2 = []
#     for x in range(0,len(bracks)):
#         index = bracks[x]
#         if index == ')':
#             bracket1.append(')')
#         if index == '(':
#             bracket2.append('(')
#     if len(bracket1) == len(bracket2):
#         return 'სწორი მიმდევრობაა'
#     else:
#         return 'არასწორი მიმდევრობაა'
# x = brackets("(()())((()))")
# print(x)



#დავალება 4 #დაუსრულებელი
# def steps(n):
#     if n == 1:
#         return n
#     elif n==2:
#         return n
#     else:
#         return False
# quantity = steps(5)
# print("ასვლის რაოდენობა:" , quantity)



#დავალება 5

# import sqlite3
# conn = sqlite3.connect("uni.sqlite")
# cursor = conn.cursor()

# cursor.execute('''create table if not EXISTS  teacher(
#             First_Name VARCHAR(50),
#             Last_Name VARCHAR(50),
#             Gender VARCHAR,
#             Subject Varchar(100))
# ''' )
# conn.commit()
#
# cursor.execute('''create table if not EXISTS  pupil(
#             First_Name VARCHAR(50),
#             Last_Name VARCHAR(50),
#             Gender VARCHAR,
#             class Varchar(100))
# ''' )
# conn.commit()
# first_name = input("შეიყვანეთ მასწავლებლის სახელი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# last_name = input("შეიყვანეთ მასწავლებლის გვარი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# gender = input("შეიყვანეთ მასწავლებლის სქესი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# subject = input("შეიყვანეთ საგანი,რომელსაც ასწავლის მასწავლებელი,ეს უნდა ჩაიწეროს ბაზაში: ")
# cursor.execute("INSERT INTO teacher(First_Name,Last_Name,Gender,Subject) VALUES (? , ? , ? , ?)",(first_name,last_name,gender,subject))
# conn.commit()
#
# first_name = input("შეიყვანეთ მოსწავლის სახელი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# last_name = input("შეიყვანეთ მოსწავლის გვარი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# gender = input("შეიყვანეთ მოსწავლის სქესი,რომელიც უნდა ჩაიწეროს ბაზაში: ")
# class1= input("შეიყვანეთ მოსწავლის კლასი,რომელშიც სწავლობს იგი,ეს უნდა ჩაიწეროს ბაზაში: ")
# cursor.execute("INSERT INTO pupil(First_Name,Last_Name,Gender,class) VALUES (? , ? , ? , ?)",(first_name,last_name,gender,class1))
#
# conn.commit()
#2
# x = cursor.execute('''SELECT
#                     p.First_Name,p.Last_Name,t.First_Name , t.Last_Name , t.subject
#                     FROM pupil p INNER JOIN teacher t
#                     ON p.gender = t.gender
#                     where p.First_Name LIKE 'giorgi'
#                     ''')
# for i in x:
#     print("იმ მასწავლებლების სახელები,რომლებიც ასწავლიან გიორგის:", i)


#დავალება 6 Done
# import requests
# import json
# from flask import Flask , render_template
# app = Flask(__name__)
#
#
#
# @app.route('/')
# def home():
#     return 'დაგენერირებული ხუმრობები(/random_joke) და შენახული ხუმრობები (/saved_joks)'
# @app.route('/random_joke')
# def jokes():
#     file = open('file_joke.txt', 'a+', encoding='UTF-8')
#     url = 'https://api.chucknorris.io/jokes/random'
#     r = requests.get(url)
#     print(r)
#     result_json = r.text
#     res = json.loads(result_json)
#     joke_list = []
#     for i in range(1):
#         x = res['value']
#         joke_list.append(x)
#     for y in joke_list:
#         content = file.write(y+'\n')
#     file.close()
#     return render_template('index.html', list_joke = y )
#
#
# @app.route('/saved_joks')
# def saved_joks():
#     saved_jokes = []
#     file1 = open('file_joke.txt', 'r', encoding='UTF-8')
#     for x in range(1):
#         content1 = file1.read()
#         split = content1.split('\n')
#         saved_jokes.append(split)
#     file1.close()
#     return render_template('saved_joks.html', saved_joke=saved_jokes)
#
# if __name__ == '__main__':
#     app.run(debug=True)









