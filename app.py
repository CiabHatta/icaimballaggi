from flask import Flask, render_template, request, redirect, jsonify, json, session, url_for, make_response, send_file, send_from_directory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from flask_mail import Mail,Message

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="driver/geckodriver")
driver.get("https://blog.rapidpack.it/blog/")


app = Flask(__name__)
app.secret_key='ffdbbbf98ijtpoijg'

supported_languages = ["fr", "it"]

app.config.update(
    MAIL_SERVER = "mail.arredorealistico.com" ,
    MAIL_PORT = 465,
    MAIL_USERNAME = "jacopo@arredorealistico.com",
    MAIL_PASSWORD = "Ciuchino1998",
    MAIL_USE_SSL = True,
    MAIL_USE_TLS=False,
    MAIL_DEFAULT_SENDER = "jacopo@arredorealistico.com",
)

mail = Mail()
mail.init_app(app)

def send_mail(to,subject,text,template, **kwargs):
    msg = Message(subject=subject,sender='jacopo@arredorealistico.com', recipients=to)
    msg.body = text
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)


@app.get("/")
@app.get("/<language>")
def Home(language = "it"):
    fetched_posts = driver.find_elements_by_class_name('hitmag-post')
    posts = []
    for post in fetched_posts: 
        new_post = {"category":post.find_element_by_class_name("cat-links").text,"datetime":post.find_element_by_class_name("posted-on").text,"description":post.find_element_by_class_name("entry-summary").text,"link":post.find_element_by_class_name("entry-summary").find_element_by_tag_name("a").get_attribute("href"),"image":post.find_element_by_class_name("wp-post-image").get_attribute("src")}
        posts.append(new_post)

    #lang = request.accept_languages.best_match(supported_languages)
    #if lang not in supported_languages:
    #    language = "it"
    
    print(language)
    return render_template( language + "/index.html", posts = posts)
        


@app.get('/registra-anagrafica')
def angrafica_template():

    return render_template("new-customer.html")

@app.post('/registra-anagrafica')
def registerAnagrafica():

    data = request.form
    if "tk" in data != "" and data["tk"] != "":
        print("bot")
    else:
        try:
            send_mail(["jacopo@icaimballaggi.it"],"Nuova anagrafica ICA", "Nuova angrafica ICA","email", data=data)
        except:
            print("errore con la mail")
            return jsonify(msg = "Errore con la registrazione dell'anagrafica"),200

    return jsonify(msg = "Anagrafica creata correttamente"),200
    
@app.post('/new-contact')
def newContact():

    data = request.form
    if "tk" in data != "" and data["tk"] != "":
        print("bot")
    else:
        try:
            send_mail(["jacopo@icaimballaggi.it"],"Nuova richiesta di contatto dal sito " + data["Paese"], "Nuova richiesta di contatto dal sito " + data["Paese"],"email", data=data)
        except:
            print("errore con la mail")
            return jsonify(msg = "Errore con la registrazione del contatto"),200

    return jsonify(msg = "Contatto inviato con successo, verrai ricontattato a breve"),200

if __name__ == '__main__':
    app.run(debug=True,host="localhost", port=3000)