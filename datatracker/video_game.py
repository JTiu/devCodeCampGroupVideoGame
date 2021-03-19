import requests, json
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from types import SimpleNamespace

from datatracker.Models.video_games import Video_Games

bp = Blueprint('video_game', __name__, )


@bp.route('/')
def index():
    # get info saved as a variable and pass variable into view
    message = "Welcome to The DataTracker"
    response = requests.get('https://api.dccresource.com/api/games')
    # print(response.json())#1. this should call json to the terminal step 2. comment out json object direct print#
    content = response.json()#function call#
    print(type(content))#option, also dir(content) this is a list, go to th right to see options#
    print(dir(content))  # option, also dir(content)#
    print(len(content))  # gets length of list 16598
    print(content[0])  # prints first index [0] of list# or -1 prints last element
    sales_count = dict()
    for game in content:
        game_year = game["year"]
        print("year of the game ", game_year)
        if (game_year is not None) and (game_year>=2013):
            game_platform = game["platform"]
            game_global = game["globalSales"]
            if game_platform in sales_count:
                sales_count[game_platform] = sales_count[game_platform] + game_global
            else:
                sales_count[game_platform] = game_global
            print("sales count now is: ", sales_count)
            print("\n\n\n")
    items = sales_count.items()
    print(items)
    platforms = [i[0] for i in items]
    sales = [i[1] for i in items]
    print("platforms: ", platforms)
    print("sales: ", sales)
    return render_template('base.html', consoleNames = platforms, sales=sales)
    #return render_template('video_game/Index.html', message=message, response=response)#



@bp.route('/CopiesSoldPerConsole')
def CopiesSoldPerConsole(json_data=None):
    # use 3 lines from above to get games data in here
    #goal
    # loop through entire data and build a new dictionary to represent sales per console
    # { 'ps3': 1000, 'ps4': 20000...} 
    #steps
    # exclude entries prior to 2013
    # create a dictionary with key for each console in the data
    # loop through and add up total sales in appropraite key

    response = requests.get('https://api.dccresource.com/api/games', json_data)
    game = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    print(game[0].platform)
    print(type(game))
    return render_template('video_game/index.html', game_data=json_data, response=response)




@bp.route('/test')
def test():
    return "All good!"



# @bp.route('/postform', methods=('GET', 'POST'))
# def other_example():
#     if request.method == 'POST':
#         page_title = request.form['title']
#         error = None
#
#         if not page_title:
#             error = 'You must enter a title'
#
#         if error is not None:
#             flash(error)
#         elif request.form['title'] == "go home":
#             return redirect(url_for('sample.index'))
#         else:
#             return render_template('sample/postform.html', page_title=page_title)
#
#    else:
#       return render_template('sample/postform.html', page_title="PostForm from Module Function")
