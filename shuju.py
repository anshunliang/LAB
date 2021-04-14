#!/usr/bin/python
# -*- coding: utf-8 -*-

class GlobalVar:
    
  db_handle = None



def set(db):

  GlobalVar.db_handle = db

def get():

  return GlobalVar.db_handle
