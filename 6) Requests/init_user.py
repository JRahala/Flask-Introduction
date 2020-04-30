import pickle

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


pickle.dump(myUser, open('myUser.prb', 'wb'))

myUser = pickle.load(open('myUser.prb', 'rb'))
print(myUser, '\n has been successfully pickled')
