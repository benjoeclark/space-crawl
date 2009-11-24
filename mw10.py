#!/usr/bin/env python

from mw10 import galaxy

def main():
    home = galaxy.Galaxy()
    print home
    print home.get_current_view()

if __name__ == '__main__':
    main()
