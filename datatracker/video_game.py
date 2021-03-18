import requests, json
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from types import SimpleNamespace
bp = Blueprint('video_game', __name__, )


@bp.route('/')
def index():
    # get info saved as a variable and pass variable into view
    message = "Welcome to The DataTracker"
    response = requests.get('https://api.dccresource.com/api/games')
    json_data = '{"name": "Nintendogs", "platform": "DS"}'
    game = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    print(game[0].name)
    print(type(game))
    return render_template('video_game/Index.html', message=message, response=response)


@bp.route('/CopiesSoldPerConsole')
def CopiesSoldPerConsole():
    # use 3 lines from above to get games data in her
    #goal
    # loop through entire data and build a new dictionary to represetn sales per console
    # { 'ps3': 1000, 'ps4': 20000...}
    #steps
    # exclude entries prior to 2013
    # create a dictionary with key for each console in the data
    # loop through and add up total sales in appropraite key
    message = "This is the chart for video game copies sold per console since 2013 "
    response = requests.api('https://api.dccresource.com/api/games')
    json_data = '{"date": "13", month : may }'
    return render_template('video_game/index.html', game_data=message)


@bp.route('/test')
def test():
    return "All good!"

# @bp.route('/VideoGameBluePrint')
# def index():
#     message = "welcome to DataTracker"
#     phrase = "Python is cool!"
#     return render_template('/index.html', message=message, word=phrase)


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
