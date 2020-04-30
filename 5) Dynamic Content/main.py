from flask import Flask, render_template
app = Flask(__name__)


myUser = {'name': 'Jasamrit Rahala',
        'posts': [
            
            {'Title': 'Title of the post',
             'Content': 'Content of the post',
             'Date': '10th March 2020'},
            
            {'Title': 'First day at Teens In AI 2020',
             'Content': 'Wow I had the best day today, I learnt all about the ethics of technology and the process of design thinking',
             'Date': '25th March 2020'}
            
            ]
        }


@app.route('/template')
def flexible(user = myUser):
    return render_template('index.html', user = user)


if __name__ == '__main__':
    app.run(debug = True)
