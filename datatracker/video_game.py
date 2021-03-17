from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

bp = Blueprint('video_game', __name__)



@bp.route('/')
def index():
    #get info saved as a variable and pass variable into view
    message = "video game index"
    return render_template('video_game/Index.html', message=message)


@bp.route('/CopiesSoldPerConsole')
def CopiesSoldPerConsole():
    message = "video game index"
    return render_template('video_game/index.html', message=message)


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

