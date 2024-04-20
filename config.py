#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5237792370:AAFzQctwwuMwkAoExcFmUBv8deV2ioS-HCY")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "5606197"))
    API_HASH = os.environ.get("API_HASH", "e705c08cb069aa050e4397721fbeaa45")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5237792370").split())
    
