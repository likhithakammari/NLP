from flask import Flask,render_template,request
from transformers import pipeline
app=Flask(__name__)
qa_bot=pipeline("question-answering")
pc_context = """
A computer's CPU (Central Processing Unit) is often called the brain of the computer.
It performs calculations, runs programs, and processes instructions. RAM (Random Access Memory)
is the memory used to store active tasks, which helps the computer multitask smoothly.
An SSD (Solid State Drive) is a storage device that is much faster than traditional HDDs.
For gaming, at least 16GB of RAM is recommended. A GPU (Graphics Processing Unit) handles
graphics rendering, especially important for gaming and video editing tasks. A power supply unit (PSU)
converts electricity from the wall into usable power for the internal components.
"""
def chatbot_response(message):
    message=message.lower()
    result=qa_bot(question=message,context=pc_context)
    answer=result['answer']
def message():
    user_input=request.args.get("ques")
    return chatbot_response(user_input)






@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")
   


if __name__=="__main__":
    app.run(debug=True)
