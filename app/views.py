from django.http import HttpResponse
from django.shortcuts import render
import json
import tweepy
from app.models import TwitterUsernameNftMap


def nft_view(request, token_id):
    data = {
        "description": "test desc",
        "image": "https://ipfs.io/ipfs/QmSxjHzZM7gkufj7VstLkCCGjbT2DPv95q7XMW7mZ13zcT?filename=img1.png",
        "name": f"Test nft #{token_id}",
        "tokenId": token_id,
        "attributes": []
    }
    if TwitterUsernameNftMap.objects.filter(token_id=token_id).exists():
        twitterUsernameNftMap = TwitterUsernameNftMap.objects.get(token_id=token_id)
        if twitterUsernameNftMap.is_following:
            data['image'] = 'https://ipfs.io/ipfs/Qmf8V6Qt45ALX8LudadkFyRygcpPB28jyGgoNE9Ze5s7M3?filename=img2.png'
        # else:
        #     if check_if_user_is_following(twitterUsernameNftMap):
        #         data['image'] = 'image2'
    return HttpResponse(json.dumps(data))


def check_if_user_is_following(twitterUsernameNftMap):
    twitter_username = twitterUsernameNftMap.twitter_username
    auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAALn0QAEAAAAAqogw80rOAMJgMUNjWiP%2Bq3PMwd8%3DKd6x7VFS2E7IlW0gyI1vmD15swYUhTZsngUKtw8LpfQ2jxNTYq")
    screen_names = ["mishrakanika3", twitter_username]
    api = tweepy.API(auth, wait_on_rate_limit=True)
    rel = api.lookup_friendships(screen_names=screen_names)[0]
    print(f'name:{rel.screen_name} isFollowedBy? {rel.is_followed_by} ')
    if rel.is_followed_by:
        twitterUsernameNftMap.is_following = True
        twitterUsernameNftMap.save()
        return True
    return False
