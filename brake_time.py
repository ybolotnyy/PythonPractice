import time
import webbrowser

toRemindTimes = 3

for i in range(0, toRemindTimes):
    time.sleep(1)
    print 'reminder #%d' % (i + 1)
    #webbrowser.open_new("https://inbox.google.com/")
