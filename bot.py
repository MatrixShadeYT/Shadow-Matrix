from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatbot = ChatBot('Shadow')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def response(user_input):
    bot_response = chatbot.get_response(user_input)
    return bot_response