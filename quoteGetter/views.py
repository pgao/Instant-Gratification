from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
import hashlib
import random
from random import choice

import dropbox_util

quotes = None
quotes_dict = None
music = None


def get_quotes():
    global quotes, quotes_dict
    if not quotes or random.random() < 0.005:
        quotes = dropbox_util.get_quotes()
        for i, quote in enumerate(quotes):
            quotes[i] = quote.strip().replace('\r\n', '\n')
            if '(' in quote:
                leftParen = quote.find('(')
                rightParen = quote.find(')')
                firstslash = quote.find('/')
                if (leftParen < firstslash < rightParen
                        and rightParen > leftParen):
                    quotes[i] = quote[rightParen + 1:]
            quotes[i] = quotes[i].decode('utf8')

        quotes_dict = dict(
            (hashlib.md5(quote.encode('utf8')).hexdigest(),
                quote) for quote in quotes)


def get_specific_quote(request, quote_hash):
    get_quotes()
    response_data = {}
    if quote_hash in quotes_dict:
        response_data['quotes'] = quotes_dict[quote_hash]
    else:
        response_data['quotes'] = None

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def get_music():
    global music
    if not music or random.random() < 0.005:
        music = dropbox_util.get_music()


def index(request):
    return render_to_response('index.html')


def new_quote(request):
    get_quotes()
    quote = [choice(quotes)]
    print quote
    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def search_for(request, search_string):
    get_quotes()
    returnable = filter(lambda a: search_string.lower() in a.lower(), quotes)

    if len(returnable) > 100:
        quote = returnable[-100:]
    else:
        quote = returnable

    print quote

    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = None

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def profanity_filter(request):
    get_quotes()
    returnable = filter(
        lambda a: ("shit" in a or "fuck" in a or "hell" in a or "damn" in a
                   or "bitch" in a or "bastard" in a
                   or "prick" in a or "piss" in a or "cunt" in a
                   or "cocksucker" in a or "tits" in a),
        quotes)

    quote = [choice(returnable)]

    print quote

    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def link_filter(request):
    get_quotes()
    returnable = filter(lambda a: "http://" in a, quotes)
    quote = [choice(returnable)]

    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def quote_filter(request):
    get_quotes()
    returnable = filter(lambda a: "http://" not in a, quotes)
    quote = [choice(returnable)]

    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def music_filter(request):
    get_music()
    print "music is ", music
    quote = ""
    while "http" not in quote:
        quote = choice(music)

    quote = [quote]
    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def new_filter(request):
    get_quotes()
    returnable = quotes[-50:]
    quote = [choice(returnable)]

    response_data = {}
    response_data['quotes'] = quote
    response_data['hash'] = hashlib.md5(quote[0].encode('utf8')).hexdigest()

    return HttpResponse(
        simplejson.dumps(response_data), mimetype="application/json")


def style(request):
    return render_to_response("style.css")


def channel(request):
    return render_to_response("channel.html")
