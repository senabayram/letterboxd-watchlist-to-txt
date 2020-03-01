# -*- coding: utf-8 -*-
"""
02-mar-2020

@author: senabayram
"""
import urllib.request

username = input("Your username: ")
userpage = urllib.request.urlopen("https://letterboxd.com/" + username + "/watchlist/page/1/")
userpagehtml = userpage.read().decode("utf-8")
page_num = 1

while "\n" in userpagehtml:
        userpagehtml = userpagehtml.split("\n")
        
for line in userpagehtml:
    if "paginate-current" in line:
        pos = line.find("paginate-current") + len("paginate-current")
        if line.find("page/3", pos) == -1:
            page_num = 2
        else:
            page_pos = line.find("page/3", pos) + len("page/3")
            if line.find("page/", page_pos) != -1:
                reduced = line[line.find("page/", page_pos) + len("page/"):]
                page_num = int(reduced.split("/")[0])
            else:
                page_num = 3
    
films_lst = open(username + "_watchlist.txt", 'w', encoding="utf-16-le")
              
for page in range(1, page_num + 1):
    watchlist = urllib.request.urlopen("https://letterboxd.com/" + username + "/watchlist/page/" + str(page) + "/")
    watchlisthtml = watchlist.read().decode("utf-8")
    while "\n" in watchlisthtml:
        watchlisthtml = watchlisthtml.split("\n")
    for line in watchlisthtml:
        if "film-poster" in line:
            film_strt = line.find("alt=") + len("alt=")
            film_end = line.find("/>", film_strt)
            films_lst.write(line[film_strt:film_end])
            films_lst.write("\n")
            
films_lst.close()      

            

    
    
    