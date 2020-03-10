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

def getValueBySectionAndKeyDefValue(section, key, defaultValue):
    value = getValueBySectionAndKey(section, key)
    return value if value != None else defaultValue


def getValueBySectionNameAndKey(sectionName, key):
    section = getSection(sectionName)
    return None if section == None else getValueBySectionAndKey(section, key)

def getValueBySectionNameAndKeyDefValue(sectionName, key, defaultValue):
    value = getValueBySectionNameAndKey(sectionName, key)
    return value if value != None else defaultValue
