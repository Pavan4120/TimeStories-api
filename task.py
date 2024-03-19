from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_latest_stories():
    url = "https://time.com/"
    response = requests.get(url)
    latest_stories = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        story_items = soup.find_all('li', class_='tout__list-item')

        for item in story_items[:6]:
            link_element = item.find('a', class_='tout__list-item-link')
            title_element = item.find('h3', class_='headline')
            if link_element and title_element:
                link = link_element['href']
                title = title_element.text.strip()
                latest_stories.append({"link": f"https://time.com{link}", "title": title})

    return latest_stories


@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    latest_stories = get_latest_stories()
    return jsonify(latest_stories)

if __name__ == '__main__':
    app.run(debug=True)
