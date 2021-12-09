import json
import urllib.parse
import boto3
import time
import re
import datetime
import dateutil.tz

print('Loading function')

s3 = boto3.resource('s3')


def lambda_handler(event, context):

    oh = str(event['message'])
    eastern = dateutil.tz.gettz('US/Eastern')
    last_updated = datetime.datetime.now(tz=eastern).strftime("%m/%d/%Y, %H:%M:%S")
    message = '''<html>
    <head></head>
    <h1>Welcome to Cloud Computing Office Hours!</h1>
    <body><p> Office Hours are currently: '''+ oh + '<p> Last updated: ' + last_updated + '</p> </p></body></html>'''
    encoded_string = message.encode('utf-8')
    s3.Bucket('ag5yy-cs4740-pa6').put_object(ACL='public-read', Key='index.html', Body=encoded_string, ContentType = 'text/html') 
    return event['message']
