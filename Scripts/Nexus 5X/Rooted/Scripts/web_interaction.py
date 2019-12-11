import time
import random
import datetime


# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    print('=INTERACTION=')
    main_activity = 'org.mozilla.gecko.BrowserApp'
    package_name = 'org.mozilla.firefox'
    urls = ['www.google.nl',
            'www.wikipedia.nl',
            'www.twitter.nl',
            'www.facebook.nl',
            'www.anwb.nl',
            'www.nos.nl',
            'www.amazon.com',
            'www.loremipsum.nl',
            'www.stackoverflow.com/',
            'www.github.com',
            'www.apple.nl',
            'www.sony.nl'
            ]
    stop = datetime.datetime.now() + datetime.timedelta(seconds=55)
    while datetime.datetime.now() < stop:
        url = random.choice(urls)
        device.launch_activity(package_name, main_activity, data_uri=url,action='android.intent.action.VIEW')
        time.sleep(5)
