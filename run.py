#! /usr/bin/env python
# -*- coding: utf-8 -*

from app import app

def main():
  app.run(host = app.config.get('HOST'), \
    debug = app.config.get('DEBUG'), \
    port = app.config.get('PORT'))

if __name__ == "__main__":
  main()
