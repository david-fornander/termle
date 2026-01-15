import webbrowser

def run(flags, search_string):

    # Default is Google.com
    search_term = "https://www.google.com/search?q="
    join_string = "+"

    if "w" in flags:
        search_term = "https://www."
        join_string = " "

    if "n" in flags:
        webbrowser.open_new(search_term + join_string.join(search_string))
    else: # "t" in flags or flags == []:
        webbrowser.open_new_tab(search_term + join_string.join(search_string))

#https://www.google.se/search?q=webbrowser+python+module
