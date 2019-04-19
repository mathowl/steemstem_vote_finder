from beem import Steem
from beem.account import Account
from beem.instance import set_shared_steem_instance
from beem.comment import Comment
from unidecode import unidecode

# outputs a .txt of steemstem voted and tagged links of a steem user. The .txt file is titled USER_steemstem where USER is the requested user. The .txt file is html coded and contains refs to the corresponding posts. It makes use of blog_history available which can only only retrieve posts up until a specific point

def steemstem_vote_finder(user):
    stm=Steem(node=['https://rpc.steemviz.com', 'https://api.steem.house', 'https://gtg.steem.house:8090', 'wss://gtg.steem.house:8090', 'https://steemd-appbase.steemit.com', 'wss://steemd.privex.io', 'https://steemd.privex.io', 'wss://anyx.io', 'https://anyx.io', 'wss://rpc.curiesteem.com', 'https://rpc.buildteam.io', 'https://rpc.steemliberator.com', 'https://appbasetest.timcliff.com', 'wss://rpc.steemviz.com', 'https://steemd.minnowsupportproject.org'])
    set_shared_steem_instance(stm)

    steemstem_user = user
    acc=Account(steemstem_user)
    for post in acc.blog_history():
        if post['parent_author'] == '' and post['author']==steemstem_user:
            p_link = post['author'] +   '/' + post['permlink']
            com_link = Comment(p_link)
            if 'steemstem' in com_link.get_votes(): 

                html_link = '<a href= \"https://steemit.com/' +'@'+ p_link  + '\"' +'>' +  unidecode(post['title'])  + '</a>'  
                print(html_link)
                f = open(user +"_" + "steemstem.txt","a")
                f.write(html_link + '\n')
                f.close()
