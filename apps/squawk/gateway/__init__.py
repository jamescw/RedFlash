# Copyright (c) 2010 the RedFlash project contributors
# All Rights Reserved
# See LICENSE for details
""" SMS gateway implementations
"""
from squawk.gateway.tweet import TwitterGateway
from squawk.gateway.email import EmailGateway
from squawk.gateway.webhook import WebhookGateway
# needed for settings.SMS_GATEWAY to eval
# @todo move to settings, something like PERMITTED_GATEWAYS
# like apps listings
from squawk.gateway.dummy import DummyGateway
from squawk.gateway.nexmo import NexmoGateway
from squawk.gateway.clickatell import ClickatellGateway
from django.conf import settings

# singleton SMS Gateway instance
def gateway(break_cache = False, new_gateway = None):
    if new_gateway:
        settings.SMS_GATEWAY = new_gateway
        gateway._cache = None

    if break_cache or (not getattr(gateway, '_cache', None)):
        gateway._cache = eval(settings.SMS_GATEWAY)()
    return gateway._cache


def twitter(break_cache = False):
    if break_cache or (not getattr(twitter, '_cache', None)):
        twitter._cache = TwitterGateway()
    return twitter._cache

def email(break_cache = False):
    if break_cache or (not getattr(email, '_cache', None)):
        email._cache = EmailGateway()
    return email._cache

def webhook(break_cache = False):
    if break_cache or (not getattr(webhook, '_cache', None)):
        webhook._cache = WebhookGateway()
    return webhook._cache
