from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot('Amine')
trainer = ChatterBotCorpusTrainer(bot)
trainer = ListTrainer(bot)
#trainer.train("chatterbot.corpus.english")


#trainer.train(['What is your name?', 'My name is Chatty'])
#trainer.train(['I need a doctor', 'Okay ! I think I can help you !' ])
#trainer.train(['Can you find me a dentist ?', 'Yes ofc ! Enter region please !'])
#trainer.train(['Who created you ?', 'Amin & Abdo'])
#trainer.train(['manar', 'manar'])
#trainer.train(['ghazela', 'ghazela'])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tt3")
def caret():
    return render_template("tt3.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
