from flask import Flask, render_template
# added render_template!
app = Flask(__name__)                     
    
@app.route("/")
def hello():
    print("in the hello function")
    return render_template("index.html", multiply=int(3) )

@app.route("/index/<times>")
def index(times):
    return render_template("index.html",multiply=int(times))	# notice the 2 new named arguments!

    
      # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
if __name__=="__main__":
    app.run(debug=True)

 


#localhost:5000
# @app.route("/")
# def hello():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


