from flask import Flask as F,render_template as rt,request as r
lis = ""

class all:
    def __init__(self,Name,Heading,Story):
        self.name = Name
        self.heading = Heading
        self.story = Story
app = F(__name__,template_folder="templates")

@app.route('/')
def home():
    if lis != "":
        return rt('index.html',name = lis.name,heading = lis.heading,story = lis.story)
    else:
        return rt('no.html')  
    
@app.route('/addstory',methods = ["POST","GET"])
def addStory():
    if r.method == "POST":
        name = r.form['name']
        heading = r.form['email']
        story = r.form['story']
        lis = all(name,heading,story)
        return rt('index.html', name=lis.name, heading=lis.heading, story=lis.story)
    else:
        return rt('add.html')

if __name__ == "__main__":
    app.run(debug = True)