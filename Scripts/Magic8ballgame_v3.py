#Instead of the randint() function, we can also use the choice() 
#function defined in the random module to implement the magic 8-ball game. 


import random
answer_list=['It is certain.', 
             'It is decidedly so.', 
             'Without a doubt.',
             'Yes definitely.', 
             'You may rely on it.', 
             'As I see it, yes.',
             'Most likely.',
             'Outlook good.', 
             'Yes.', 
             'Signs point to yes.',
             'Reply hazy, try again.', 
             'Ask again later.', 
             'Better not tell you now.',
             'Cannot predict now.', 
             'Concentrate and ask again.',
             "Don't count on it.", 
             'My reply is no.', 
             'My sources say no.', 
             'Outlook not so good.',
             'Very doubtful.']
while True:
    question=input("Ask the magic 8 ball a question: (press enter to quit) ")
    if question=="":
        print("Stopping the Game.")
        break
    answer_string=random.choice(answer_list)
    print(answer_string)