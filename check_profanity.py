import os
import urllib

def read_text():
    # filepath = "/usr/local/google/home/ybolotnyy/PycharmProjects/PythonPractice/resourses"
    # filename = "movie_quotes.txt"
    # quotes = open(filepath + "/" + filename)
    home_directory = os.path.expanduser('~')
    mypath = home_directory + '/PycharmProjects/PythonPractice/Photos'
    quotes = open(home_directory + "/PycharmProjects/PythonPractice/resourses/movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("No course words. Looks good!")
    else:
        print("Could not scan the doc properly")
read_text()