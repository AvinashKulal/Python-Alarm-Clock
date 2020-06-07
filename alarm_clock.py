from datetime import datetime
from time import sleep,ctime
import webbrowser


print('|------|-'+ctime().upper()+'-|------|')
alarm_tone = 'https://youtu.be/m-XFJpELn5U'
wakeup = True

# set alarm here
def set_alarm(alerm_at,wakeup):

    now = datetime.now()
    total_sec = (alerm_at-now).total_seconds()

    if not wakeup:
        print('SNOOZING FOR 5 MINUTE(MINUTES)')
    else:
        print('ALARM SET FOR '+str(alerm_at.time()))
    sleep(total_sec)
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(alarm_tone)

    wakeup = input('WAKEUP / SNOOZE FOR 5 MINUTE (0/1)')
    if wakeup == '1':
        global minute
        now = datetime.now() 
        minute+=5 
        alerm_at = datetime(2020,6,7,hour,minute,0)
        set_alarm(alerm_at,False) # wakeup is False
    else:
        quit()

#main
if __name__ == '__main__':
    hour = int(input('\nENTER THE HOUR '))
    minute = int(input('\nENTER THE MINUTE '))
    alerm_at = datetime(2020,6,7,hour,minute,0)
    set_alarm(alerm_at,wakeup)
