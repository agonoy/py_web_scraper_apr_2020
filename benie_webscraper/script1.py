from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from pandas import pandas as pd


# this will request to get HTTPS URL
# then it will put it in a container
cdc = requests.get("https://covidtracking.com/data", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

# just reply a respose, but nothing of important as of yet
# print(cdc)

# then it will put it in a container
cdc_content = cdc.content
# print(cdc_content) # print the whole container. . does not even filter yet

parse_data = BeautifulSoup(cdc_content, "html.parser") # html.parser will just get rid of "/n" and junk and show
# you much like an html tags. .

# print(parse_data)

# all <div elements>. will filter "data-state" and put it in a dictionary. .
cdc_all = parse_data.find_all("div",{"class":"module"})

# print(cdc_all)
# how many items on the container
print(len(cdc_all))

#print what type it is
print(type(cdc_all))

# print((cdc_all))  # print all


## Alabama is the first item
# print(cdc_all[0])

# creates a foor loop
cdc_data = []

# this will go through the array and create tuple
for item in cdc_all:
    #     print("state ", "     Deaths", "      Cases")
    # print(item.find_all("a")[0].text, "   ", item.find_all("td")[11].text, "        ", item.find_all("td")[1].text)
    cdc_data_ = []
    cdc_data_.append(item.find_all("a")[0].text)
    cdc_data_.append(item.find_all("td")[11].text)
    cdc_data_.append(item.find_all("td")[1].text)

    #     np_cdc_data = [item.find_all("a")[0].text,item.find_all("td")[11].text,item.find_all("td")[1].text]
    #     newArray2 = np.append(cdc_numpy_data, [np_cdc_data], axis = 0)

    #     leave alone
    cdc_data.append(cdc_data_)

# print(newArray2)


#  should look like this [['Alabama', '212', '6,137'], ['Alaska', '9', '339'],...]]
# print(cdc_data)


#  Converts data into table using pandas
# create the columns name
new_columns = ["State", "Deaths", "Cases"]

#  row of data
new_data = pd.DataFrame(data = cdc_data, columns = new_columns )
# print(new_data)




app=Flask(__name__)

all_posts = [{"title": "post 1",
              "content": "post 2"},

             {"thirdkey": "shit 2",
              "ast": "last"}]


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# making list of pokemons
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]




# @app.route('/home')
# def posts():
#     return render_template('home.html', posts= all_posts )


@app.route('/')
def home():
    return render_template("home.html", pok=cdc_data)

@app.route('/about/')
def about():
    return render_template("about.html", myposts=all_posts)

if __name__=="__main__":
    app.run(debug=True)