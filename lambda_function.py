import os
import time
import boto3

SECONDS_IN_WEEK = 604800

def lambda_handler(event, context):
    numbers = os.environ['NUMBERS'].split(',')
    odd_week = bool(int((time.time()) / SECONDS_IN_WEEK) % 2)

    if odd_week:
        message = 'Garbage day tomorrow: Blue & Green'
    else:
        message = 'Garbage day tomorrow: Clear & Green'

    for number in numbers:
        sns = boto3.client('sns')
        response = sns.publish(
            PhoneNumber=number,
            Message=message
        )
        print(f'Sent "{message}" to {number}')
        print(f'response: {response}')
