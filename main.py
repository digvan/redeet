#!/usr/bin/env python
from bottle import route, request, response, view, run,send_file,redirect
import tweepy
import redis

KEY = "7F1pCkQVAY88a2s3xNQ"
SECRET = "7qeFMC6kyAI9RJvoimX4hF8NJOx6YQ6DsWRgTFSxQ"
R = redis.Redis('localhost',db='twitter')
API = None

@route('/twitter/signin')
@view('twitter')
def getToken():
	auth = tweepy.OAuthHandler(KEY,SECRET)
	try:
		redirect_url = auth.get_authorization_url()
		response.set_cookie('key',auth.request_token.key)
		response.set_cookie('secret',auth.request_token.secret)
	except tweepy.TweepError:
		print 'Error! Failed to get request token.'
	redirect(redirect_url)

@route('/twitter/return/')
@view('twitter')	
def returnfromtwitter():
	try:
		request_token = request.GET.get('oauth_token', 'Stranger')
		key = request.COOKIES['key']
		secret = request.COOKIES['secret']
		auth = tweepy.OAuthHandler(KEY, SECRET)
		auth.set_request_token(key, secret)
		auth.get_access_token(request_token)
	except tweepy.TweepError:
		return dict(title="failed! bad oauth_token",name= None)
	except KeyError:
		return dict(title="failed due to session error", name= None)
	print "yes"
	auth.set_access_token(auth.access_token.key, auth.access_token.secret)
	api = tweepy.API(auth)
	print api
	API = api
	user = api.me()
	print user
	adduser(user,auth.access_token.key,auth.access_token.secret)
	return dict(title="success",name=user.name,user=user)

def adduser(user,key,secret):
	if R.sadd("users", user.screen_name):
		R.hset('user:%s' %user.screen_name,'id', user.id)
		R.hset('user:%s' %user.screen_name,'screen_name', user.screen_name)
		R.hset('user:%s' %user.screen_name,'name', user.name)
		R.hset('user:%s' %user.screen_name,'key', key)
		R.hset('user:%s' %user.screen_name,'secret', secret)
		return True
	else:
		return False
	
@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='/home/kdehdash/Downloads/twitter/static')
	
@route('/twitter')
@view('twitter')
def template_twitter():
	return dict(title='Twitter',name=None)

@route('/twitter/status/', method='POST')
@view('twitter')
def template_twitterpost():
	if 'name' in request.POST:
		name = request.POST['name']
	if 'secret' in request.POST:
		secret = request.POST['secret']
	api = twitter.Api(username=name, password=secret)
	if 'tweet' in request.POST:
		tweet = request.POST['tweet']
		status_update = api.PostUpdate(tweet)
	return dict(title='Twitter')


run(host='localhost', port=8080)
