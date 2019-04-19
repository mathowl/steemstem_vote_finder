from beem import Steem
from beem.account import Account
from beem.instance import set_shared_steem_instance
from beem.comment import Comment
from unidecode import unidecode
from beem.nodelist import NodeList

#checks whole history of steem user for steemstem votes and outputs this to a .txt file as hrefs

def steemstem_vote_finder_full(user):
    nodes = NodeList().get_nodes()
    stm=Steem(node=nodes)
    set_shared_steem_instance(stm)
    steemstem_user = user
    acc=Account(steemstem_user)
    perm_link_set=set()
    for post in acc.history_reverse(only_ops=['comment']):
        if post['parent_author'] == '' and post['author']==steemstem_user and post['permlink'] not in perm_link_set:
            perm_link_set.add(post['permlink'])
            p_link = post['author'] +   '/' + post['permlink']

            print(p_link)
            print(post['timestamp'])
            com_link = Comment(p_link,steem_instance=Steem(node=['https://rpc.steemviz.com', 'https://api.steem.house', 'https://gtg.steem.house:8090', 'wss://gtg.steem.house:8090', 'https://steemd-appbase.steemit.com', 'wss://steemd.privex.io', 'https://steemd.privex.io', 'wss://anyx.io', 'https://anyx.io', 'wss://rpc.curiesteem.com', 'https://rpc.buildteam.io', 'https://rpc.steemliberator.com', 'https://appbasetest.timcliff.com', 'wss://rpc.steemviz.com', 'https://steemd.minnowsupportproject.org']))
            if 'steemstem' in com_link.get_votes(): 
                print('+')
            
                html_link = '<a href= \"https://steemit.com/' +'@'+ p_link  + '\"' +'>' +  unidecode(post['title'])  + '</a>'  
                print(html_link)
                f = open(user +"_" + "steemstem.txt","a")
                f.write(html_link + '\n')
                f.close()
