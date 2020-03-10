#!/usr/bin/python
# -*- coding:utf-8 -*-

import configparser

__config = configparser.ConfigParser()

def init(configFile):
    __config.read(configFile)

def getSection(sectionName):
    sections = __config.sections()
    if(sectionName in sections):
        return __config[sectionName]
    else:
        return None

def getValueBySectionAndKey(section, key):
    return section.get(key)

def getValueBySectionNameAndKey(sectionName, key):
    section = getSection(sectionName)
    if(section == None):
        return None
    else:
        return getValueBySectionAndKey(section, key)
