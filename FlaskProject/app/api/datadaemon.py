from datetime import datetime
import time
import polling
import requests
import os

basedir = os.path.abspath(os.path.dirname(__file__))  # pylint: disable=invalid-name
print(basedir)
from dotenv import load_dotenv
from models import Videodirectoy

# load_dotenv(".env")
# print(os.environ['APIKEY'])


def insert_db(data):
    try:
        for data_dic in data:
            pubb_at = datetime.strptime(data_dic["published_at"], "%Y-%m-%dT%H:%M:%SZ")
            vd = Videodirectoy(
                video_title=data_dic["title"],
                video_discription=data_dic["description"],
                thumbnail_links=data_dic["thumbnail"],
                published_at=pubb_at,
                created_at=datetime.now()
            )

         # save the data in database
            vd.save()

        # conn = mysql.connector.connect(user= os.environ['MYSQL_USER'],
        #                                password= os.environ['MYSQL_PASSWORD'],
        #                                host=os.environ['MYSQL_HOST'],
        #                                database=os.environ['MYSQL_DATABASE'],
        #                                port=os.environ['MYSQL_PORT'],
        #                                auth_plugin='mysql_native_password')
        # cursor = conn.cursor(dictionary=True)
        # for data_dic in data:
        #     insert_sql = "insert into video_directory (video_title, video_discription," \
        #         " thumbnail_links, published_at, created_at) VALUES (%s, %s, %s, %s, %s)"
        #     pubb_at = datetime.strptime(data_dic["published_at"], "%Y-%m-%dT%H:%M:%SZ")
        #     cursor.execute(insert_sql, (data_dic["title"], data_dic["description"], data_dic["thumbnail"], pubb_at, datetime.now()),)
        # conn.commit()
        print("Data updated")
    except Exception as e:
        print("insert_db expection", e)


def fetch_data():
    list_of_data_dic = list()
    try:
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=cricketworldcup2022&type=video&key=AIzaSyAyJCvbrNy3xMuKmC7SwNgEPICa0n__mKk"

        headers = {}

        response = requests.request("GET", url, headers=headers)

        output = response.json()
        for dic in output["items"]:
            data_dic = dict()
            data_dic["published_at"]= dic["snippet"]["publishedAt"]
            data_dic["title"] = dic["snippet"]["title"]
            data_dic["description"] = dic["snippet"]["description"]
            data_dic["thumbnail"] = dic["snippet"]["thumbnails"]["high"]["url"]
            list_of_data_dic.append(data_dic)
        insert_db(list_of_data_dic)
    except Exception as e:
        print("Check_records expection", e)
    finally:
        sleep_time = 10
        print("Sleeping for {} seconds".format(sleep_time))
        time.sleep(sleep_time)

def init_daemon():

    polling.poll(
        lambda: fetch_data(),
        step=10,
        poll_forever=True)