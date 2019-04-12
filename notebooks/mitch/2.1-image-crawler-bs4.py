def get_images_links(twitter_url):

    import requests
    import shutil
    import os
    from bs4 import BeautifulSoup

    d = requests.get(twitter_url).text
    soup = BeautifulSoup(d, 'html.parser')

    img_tags = soup.find_all('img')

    imgs_urls = []
    for img in img_tags:
        try:
            if img['src'].startswith("http"):
                imgs_urls.append(img['src'])
        except KeyError:
            pass

    for url in imgs_urls:
        img_data = requests.get(url).content
        filename = url.split('/')[-1]
        dest = 'image_test_1'
        try:
            with open('{}/{}'.format(dest, filename), 'wb') as handler:
                handler.write(img_data)
        except FileNotFoundError:
            if not os.path.exists(dest + '/'):
                os.makedirs(dest)

    return imgs_urls

x = get_images_links('https://twitter.com/hogwspider/status/1116479598252806145')

import pdb; pdb.set_trace()
