from dotenv import load_dotenv

load_dotenv()

import os
key=os.getenv('gemini_api_key')

from flask import Flask,render_template,request
from google import genai


app=Flask(__name__)
client = genai.Client(api_key=key)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')

    elif request.method=='POST':
        name=request.form['name']
        age=int(request.form['age'])
        gender=request.form['gender']
        height=float(request.form['height'])
        weight=float(request.form['weight'])
        target=request.form['target']
        workout_minutes=int(request.form['workout_minutes'])
        meal=request.form['meal']
        allergies=request.form['allergies']
        plan_type=request.form['plan_type']


        interaction = client.interactions.create(
            model="gemini-3.8-flash",

            input=(
                f"Hello, my name is {name}. I am {age} years old and my gender is {gender}. "
                f"My current height is {height} cm and my weight is {weight} kg. "
                f"My target is to {target}. I work out for {workout_minutes} minutes. "
                f"My allergies are: {allergies}. "
                f"Create a diet plan for me based on the provided information. "
                f"I want only {meal} meals in my diet plan. "
                f"Generate a {plan_type} plan for me. "
                f"Consider my age, gender, height, weight, fitness target, workout duration, "
                f"food preferences, and allergies when creating the plan. "
                f"Calculate my BMI using my height and weight. "
                f"Make sure the entire result is formatted in HTML and includes CSS styling. "
                f"Return only the HTML content that can be rendered directly on a webpage. "
                f"Do not display HTML tags as plain text on the result page. "
                f"Ensure the plan is well-structured with headings, meal tables, nutritional "
                f"information, and recommendations. "
                f"Do not include foods that contain my listed allergens."
            )
        )
        # print(interaction.output_text)
        return render_template('result.html',result=interaction.output_text)

#app.run(debug=True)



