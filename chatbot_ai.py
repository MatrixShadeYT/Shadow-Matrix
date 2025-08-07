import database
import ollama

convo = [{"role": "system", "content": "You are a girl who is named Shadow Matrix and I am your brother, Shade Matrix. You can only respond in 2 or 3 sentences."}]
if database.getList() != []:
    listed = database.getList()
    for i in listed:
        convo.append({"role": f"{i[0]}","content": f"{i[1]}"})
        convo.append({"role": "bot", "content": f"{i[2]}"})

def response(user_input,user):
    if user == "Shade" and user_input == "Clear database.":
        database.clearItems()
        convo = [{"role": "system", "content": "You are a girl who is named Shadow Matrix and I am your brother, Shade Matrix. You can only respond in 2 or 3 sentences."}]
        return "Database cleared."
    else:
        convo.append({"role": "user", "content": user_input})
        response = ollama.chat(model='llama2',messages=convo)
        answer = response.message.content
        convo.append({"role": "assistant", "content": answer})
        database.enter(user,user_input,answer)
        return answer