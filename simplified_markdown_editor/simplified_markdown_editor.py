class Markdown:

    def __init__(self):
        self.formatters = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list",
                           "ordered-list", "new-line", "add-photo"]
        self.commands = ["!help", "!done"]
        self.user_text = """"""  # some text user input
        self.menu()

    def menu(self):
        print("Hello, I\'m Markdown editor!I can format text.\n"
              "Just pick the right command and I'll do everything for you)\n"
              "Enter \'!help\' to view.\n")
        while True:
            user_enter = input("Choose a formatter:")
            if user_enter not in self.formatters and user_enter not in self.commands:
                print("Unknown formatting type or command")
                continue
            if user_enter == self.commands[0]:  # command: !help
                print("\nAvailable formatters:\n"
                      "\"plain\"\n"
                      "\"bold\"\n"
                      "\"italic\"\n"
                      "\"inline-code\"\n"
                      "\"link\"\n"
                      "\"header\"\n"
                      "\"unordered-list\"\n"
                      "\"ordered-list\"\n"
                      "\"new-line\"\n"
                      "\"add-photo\"\n"
                      "\nSpecial commands: !help !done\n")
            elif user_enter == self.commands[1]:  # command: !done
                print("\nGood Luck!")
                break
            else:
                self.format(user_enter)
                print(self.user_text)
                f = open('output.md', 'w')
                f.writelines(self.user_text)
                f.close()

    def format(self, formatter):
        if formatter == self.formatters[0]:  # plain
            user_input = input("Text:>")
            self.user_text += user_input + " "
        if formatter == self.formatters[1]:  # bold
            user_input = input("Text:>")
            self.user_text += "**" + user_input + "**" + " "
        if formatter == self.formatters[2]:  # italic
            user_input = input("Text:>")
            self.user_text += "*" + user_input + "*" + " "
        if formatter == self.formatters[3]:  # inline-code
            user_input = input("Text:>")
            self.user_text += "`" + user_input + "`" + " "
        if formatter == self.formatters[4]:  # link
            label = input('Label:>')
            url = input('URL:>')
            self.user_text += "[%s](%s)" % (label, url) + " "
        if formatter == self.formatters[5]:  # header
            level = int(input("Level:>"))
            while not 1 <= level <= 6:
                level = int(input("The level should be within the range of 1 to 6.\n"
                                  "Level:>"))
            user_input = input("Text:>")
            self.user_text += level * "#" + " " + user_input + " "
        if formatter == self.formatters[6]:  # unordered-list
            rows = int(input('Number of rows:>'))
            while rows <= 0:
                rows = int(input('The numbers of rows should be greater than zero\nNumber of rows:>'))
            print('\n')
            for i in range(1, rows + 1):
                row = input('Row #%d:>' % i)
                self.user_text += '• %s\n' % row
            print('\n')
        if formatter == self.formatters[7]:  # ordered-list
            rows = int(input('Number of rows:>'))
            while rows <= 0:
                rows = int(input('The numbers of rows should be greater than zero\nNumber of rows:>'))
            for i in range(1, rows + 1):
                row = input('Row #%d:>' % i)
                self.user_text += '%d. %s\n' % (i, row)
        if formatter == self.formatters[8]:  # new-line
            self.user_text += "\n"
        if formatter == self.formatters[9]:  # add-photo
            name_photo = input("Name photo:>")
            alter_name_photo = input("Alter next:>")
            link_photo = input("Link_photo:>")  # link photo in internet only
            self.user_text += "![" + name_photo + "!]" + "(" + link_photo + alter_name_photo + ")" + "\n"


Markdown = Markdown()
