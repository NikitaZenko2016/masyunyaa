import json
import os
from dotenv import load_dotenv

#cool_people = [799230352723148811, 1044297636393537637, 1280624947567263824, 862753833208905728, 1391438435440660531]
#stupid_people = [1010653340931207308, 871637164113399818, 719494025685630977, 1254443521218318487, 1053661292910612560, 737745724392865902]
#video_playlist = [' \'Лимонные девочки\'', ' \'Переполнение\'', ' \'Эйфория\'',' \'Реинкарнация безработного\'']
#test_guilds=[1065221749706334269, 1259207760005038212]

chance = 8
class Config:
    def __init__(self, cool_people, stupid_people, test_guilds, video_playlist):
        self.cool_people = cool_people
        self.stupid_people = stupid_people
        self.test_guilds = test_guilds
        self.video_playlist = video_playlist

    @classmethod
    def json_read(cls, path):
        with open(path, 'r', encoding='utf-8') as config:
            data = json.load(config)
        return cls(**data)
    
    def get_ids(self):
        cool_people, stupid_people, test_guilds = [], [], []
        try:
            for id in self.cool_people.split(', '):
                cool_people.append(int(id))
            self.cool_people = cool_people
            
            for id in self.stupid_people.split(', '):
                stupid_people.append(int(id))
            self.stupid_people = stupid_people

            for id in self.test_guilds.split(', '):
                test_guilds.append(int(id))
            self.test_guilds = test_guilds
        except Exception as e:
            print(f"Error by getting ids: {e}")
    pass

config = Config.json_read("src\\config\\config.json")
config.get_ids()
load_dotenv()
TOKEN = os.getenv("TOKEN")



        