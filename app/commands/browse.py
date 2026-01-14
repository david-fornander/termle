import webbrowser

def run(flag, search_string):
    if flag == "t" or flag == None:
        webbrowser.open_new_tab("https://www.google.se/search?q=" + "+".join(search_string))
    elif flag == "n":
        webbrowser.open_new("https://www.google.se/search?q=" + "+".join(search_string))

#https://www.google.se/search?q=webbrowser+python+module
