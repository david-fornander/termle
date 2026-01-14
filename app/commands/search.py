import webbrowser

def run(search_string):
    print(f"Searching for: \"{" ".join(search_string)}\"")
    webbrowser.open_new_tab("https://www.google.se/search?q=" + "+".join(search_string))

#https://www.google.se/search?q=webbrowser+python+module
