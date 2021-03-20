import requests # for future jt, https://www.pythonforbeginners.com/requests/using-requests-in-python#
from flask import render_template, Blueprint #https://search.yahoo.com/search?fr=mcafee&type=E210US1249G0&p=what+is+a+blueprint+in+flask%3F#

bp = Blueprint('video_game', __name__, )#https://www.afternerd.com/blog/python-__name__-__main__/#:~:text=__name__%20is%20simply%20a%20built-in%20variable%20in%20Python,go%20through%20a%20series%20of%20examples.%20Example%201#


@bp.route('/')#https://flask.palletsprojects.com/en/1.1.x/blueprints/#
def index():#https://www.quora.com/Why-home-page-of-a-website-is-always-named-as-the-index-page#
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
    return "all good" #render_template('base.html', consoleNames = platforms, sales=sales)#

    #return render_template('video_game/Index.html', message=message, response=response)#



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
    return render_template('Trial.html', game_data=message)


@bp.route('/test')
def test():
    return "All good all day!"

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
