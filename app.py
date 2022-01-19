from flask import Flask, render_template, request, redirect, jsonify, json, session, url_for, make_response, send_file, send_from_directory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="driver/geckodriver")
driver.get("https://blog.rapidpack.it/blog/")


app = Flask(__name__)
app.secret_key='ffdbbbf98ijtpoijg'

@app.get("/")
def Home():
    fetched_posts = driver.find_elements_by_class_name('hitmag-post')
    posts = []
    for post in fetched_posts: 
        new_post = {"category":post.find_element_by_class_name("cat-links").text,"datetime":post.find_element_by_class_name("posted-on").text,"description":post.find_element_by_class_name("entry-summary").text,"link":post.find_element_by_class_name("entry-summary").find_element_by_tag_name("a").get_attribute("href"),"image":post.find_element_by_class_name("wp-post-image").get_attribute("src")}
        posts.append(new_post)

    print(posts)

    return render_template("index.html", posts = posts)

if __name__ == '__main__':
    app.run(debug=True,host="localhost", port=3000)