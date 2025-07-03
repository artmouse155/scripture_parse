import webbrowser
import re
from sys import argv

#OLD_SCRIPTURE_REGEX = r"((?:[\d] )?[\w&\.]+) ((?:(?:[;,] ?)?(?:[\d]{1,3}(?::(?:[\d]{1,3}[–-][\d]{1,3}|[\d]{1,3})|[–-][\d]{1,3})?))+)"
SCRIPTURE_REGEX = r"((?:[\d] )?[\w&\.]+) ((?:(?:[;,] ?)?(?:[\d]{1,3}(?::(?:[\d]{1,3}[–-][\d]{1,3}|[\d]{1,3})|[–-][\d]{1,3})?))+)(?:[\";\b.$\n]|$)"
#SCRIPTURE_REGEX = r"((?:[\d] )?[\w&\.]+) ((?:(?:[;,] ?)?(?:[\d]{1,3}(?::(?:[\d]{1,3}[–-][\d]{1,3}|[\d]{1,3})|[–-][\d]{1,3})?))+)(?:[^\w]|$)"

#https://www.churchofjesuschrist.org/study/scriptures/quad/quad/abbreviations?lang=eng
#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#https://rsc.byu.edu/sites/default/files/web_content/guidelines/pdf/Church_Style_Guide_for_Editors_and_Writers.pdf

TITLE = r"""
Hi there! Welcome to...
   _____  _____ _____  _____ _____ _______ _    _ _____  ______ 
  / ____|/ ____|  __ \|_   _|  __ \__   __| |  | |  __ \|  ____|
 | (___ | |    | |__) | | | | |__) | | |  | |  | | |__) | |__   
  \___ \| |    |  _  /  | | |  ___/  | |  | |  | |  _  /|  __|  
  ____) | |____| | \ \ _| |_| |      | |  | |__| | | \ \| |____ 
 |_____/ \_____|_|  \_\_____|_|      |_|   \____/|_|  \_\______|
              ______         _____ _______ ______
  _|_    .    |  __ \ /\    / ____|__   __|  ____|       +    .  
   |        + | |__) /  \  | (___    | |  | |__    . _|_         
    +   _|_   |  ___/ /\ \  \___ \   | |  |  __|      |     +    
         |  . | |  / ____ \ ____) |  | |  | |____        .      
              |_| /_/    \_\_____/   |_|  |______|  TM    v1.2.0
"""

HELP = """
<HELP>
Welcome to Scripture Paste!

"What does this program do?"
Scripture Paste scans a block of text for valid scriptures in either the Old Testament, New Testament, Book of Mormon, Doctrine & Covenants, or Pearl of Great Price.
Then, Scripture Paste creates hyperlinks to those scriptures for easy reading.
Scripture Paste was created to help Chase open links for the reading in his BYU religion class.

How to use (USE 1 of 2 | Short sequence):
First, run "py scripture_paste.py" in your terminal to bring up the Scripture Paste terminal.
Then, paste in a block of text containing the scriptures that you want Scripture Paste to scan.
The program will then search the block of text you pasted for valid scriptures.
If it finds valid scriptures, it will generate a hyperlink to the scripture on churchofjesuschrist.org.
Type either "Y" or "N" to automatically bring up all the scriptures in your browser.

How to use (USE 2 of 2 | Longer sequence):
First, paste a block of text you want Scripture Paste to scan into a text file in the same folder as scripture_paste.py.
Then, run "py scripture_paste.py <text_file_name_here.txt> <y or n for showing links>(optional)" in the terminal.
The program will then search the block of text you pasted for valid scriptures.
If it finds valid scriptures, it will generate a hyperlink to the scripture on churchofjesuschrist.org.
If you didn't include a Y or N flag, Type either "Y" or "N" to automatically bring up all the scriptures in your browser.
</HELP>
"""

link_key = {}

#i began this project at 6:55 pm on 10/16/24.

class Scripture:

    domain = "https://www.churchofjesuschrist.org/study/scriptures"

    book = None
    chapter = None
    verse_start = None
    verse_end = None

    testament = None
    shorthand_book = None
    
    def __init__(self, _book, _chapter, _verse_start=None, _verse_end=None):
        self.book = _book

        try:
            _key = link_key[self.book.lower()]
            self.testament = _key["TESTAMENT"]
            self.shorthand_book = _key["BOOK"]
        except KeyError:
            raise TypeError(f"Sorry! Looks like the book of scripture \"{self.book}\" wasn't recognized.")

        self.chapter = _chapter
        self.verse_start = _verse_start
        self.verse_end = _verse_end

    def get_link(self):
        return f"{self.domain}/{self.testament}/{self.shorthand_book}/{self.chapter}{f"/?lang=eng&id=p{self.verse_start}{f"-p{self.verse_end}" if self.verse_end else ""}#p{self.verse_start}" if self.verse_start else ""}"

    def __str__(self):
        return f"{self.book} {self.chapter}{f":{self.verse_start}{f"–{self.verse_end}" if self.verse_end else ""}" if self.verse_start else ""}"

    @staticmethod
    def is_book_valid(b):
        return b.lower() in link_key.keys()


#break it down into scripture parts
def parse_input(user_input):
    #print(user_input)
    scriptures = re.findall(SCRIPTURE_REGEX, user_input)
    return scriptures

def generate_scripture_objects(scriptures):
    scripture_objects = []
    for scripture in scriptures:
        #print(scripture)
        book = scripture[0]
        if not Scripture.is_book_valid(book):
            print(f"= ❌ The scripture passage \"{scripture[0]} {scripture[1]}\" wasn't recognized.")
            continue
        sections = scripture[1]
        i = 0
        reader = ""
        data_type = "CHAPTER"
        scripture_dict = {
        "CHAPTER" : None,
        "VERSE_START" : None,
        "VERSE_END" : None,
        }

        while i < len(sections):
            char = sections[i]
            #print("🌻",char)
            i += 1
            if char.isdigit():
                reader += char
                #print(f"Reader is {reader}")
            elif char in "–-":
                
                scripture_dict[data_type] = int(reader)

                reader = ""
                if data_type == "VERSE_START":
                    data_type = "VERSE_END"
                elif data_type == "CHAPTER":
                    data_type = "CHAPTER_END" #getting several chapters at once
                else:
                    raise ValueError("non chapter or non verse start before dash.")
            elif char == ":":
                assert data_type == "CHAPTER"
                scripture_dict[data_type] = int(reader)
                
                reader = ""
                data_type = "VERSE_START"
            elif char == ";":
                if data_type == "CHAPTER_END": #getting several chapters at once
                    for i in range(scripture_dict["CHAPTER"], int(reader) + 1):
                        scripture_objects.append(Scripture(book,i))
                else:
                    scripture_dict[data_type] = int(reader)
                    scripture_objects.append(Scripture(book,scripture_dict["CHAPTER"],scripture_dict["VERSE_START"],scripture_dict["VERSE_END"]))
                scripture_dict["VERSE_START"] = None
                scripture_dict["VERSE_END"] = None    

                reader = ""
                data_type = "CHAPTER"
            elif char == ",":
                assert data_type in ["VERSE_START","VERSE_END"], "Error: Comma following a chapter isn't correct syntax."

                scripture_dict[data_type] = int(reader)
                

                scripture_objects.append(Scripture(book,scripture_dict["CHAPTER"],scripture_dict["VERSE_START"],scripture_dict["VERSE_END"]))
                scripture_dict["VERSE_START"] = None
                scripture_dict["VERSE_END"] = None

                reader = ""
                data_type = "VERSE_START"
            elif char == " ":
                pass
            else:
                raise ValueError(f"Unrecognized character \"{char}\"")
        if data_type == "CHAPTER_END": #getting several chapters at once
            for i in range(scripture_dict["CHAPTER"], int(reader) + 1):
                scripture_objects.append(Scripture(book,i))
        else:
            scripture_dict[data_type] = int(reader)
            scripture_objects.append(Scripture(book,scripture_dict["CHAPTER"],scripture_dict["VERSE_START"],scripture_dict["VERSE_END"]))
    return scripture_objects

if __name__ == "__main__":

    #get string from user
    with open("key.csv", "r", encoding='utf-8') as open_file:
        lines = open_file.readlines()
        for line in lines:
            line = line.strip()
            elements = line.split(',')
            #print(line)
            link_key[elements[0].lower()] = {"BOOK" : elements[1], "TESTAMENT" : elements[2]}

        

    assert len(argv) in [1,2,3], "Only include at most two optional argument, a filename with the links you want to open, and then Y or N if you want to open the links."
    user_input = ""
    
    open_links = False
    valid_response = False
    if len(argv) in [2,3]:
        with open(argv[1], "r", encoding='utf-8') as open_file:
                user_input = open_file.read()
        if len(argv) == 3:
            if argv[2] in ["y", "Y"]:
                valid_response = True
                open_links = True
            elif argv[2] in ["n", "N"]:
                valid_response = True
            else:
                print(f"argument {argv[3]} not recognized. It should match either 'y','Y','n', or 'N'.")
    else:
        print(TITLE)
        while user_input == "":
            print("Paste a block of text containing scriptures, and then press enter. ('h' for help, 'q' to quit)")
            user_input = input("")
            if user_input == "h":
                print(HELP)
                user_input = ""
    
    if user_input != "q":
        print("Parsing Input...")
        scriptures = parse_input(user_input)
        scripture_objects = generate_scripture_objects(scriptures)
        links = [obj.get_link() for obj in scripture_objects]
        if len(scripture_objects) == 0:
            print("No scriptures found.")
        else:
            print(f"⭐ {len(scripture_objects)} scripture(s) found:")
            for obj in scripture_objects:
                print(f"{obj}\t({obj.get_link()})")

            while not valid_response:
                response = input("Open Links in Browser? (Y/N) --> ")
                if response in ["y", "Y"]:
                    valid_response = True
                    open_links = True
                elif response in ["n", "N"]:
                    valid_response = True
            
            if open_links:
                for i in range(len(links)):
                    link = links[i]
                    if i == 0:
                        webbrowser.open(link, new=1, autoraise=True)
                    else:
                        webbrowser.open_new_tab(link)
    input("👋 Goodbye!\n(Press enter to exit)\n")
        
        #     scripture_objects = generate_scripture_objects(scriptures)
        #     links = [obj.get_link() for obj in scripture_objects]
        #     for link in links:
        #         webbrowser.open_new_tab(link)