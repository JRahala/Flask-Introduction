import pickle
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/template')
def home_page(user = False):

    if not user: user = pickle.load(open('myUser.prb', 'rb'))
    print(user['posts'])
    return render_template('index.html', user = user)


@app.route('/add_post', methods = ['POST'])
def add_post():

    user = pickle.load(open('myUser.prb', 'rb'))
    data = request.get_json()

    post = {'Title': data['Title'],
            'Content': data['Content']}
    
    user['posts'].append(post)
    pickle.dump(user, open('myUser.prb', 'wb'))

    return 'Successfully loaded post'


if __name__ == '__main__':
    app.run(debug = True)
