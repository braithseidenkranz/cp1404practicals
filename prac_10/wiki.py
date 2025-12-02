import wikipedia

def main():
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        else:
            print(page.title)
            print(page.summary)
            print(page.url)
        title = input("Enter page title: ")
    print("Thank you")

main()