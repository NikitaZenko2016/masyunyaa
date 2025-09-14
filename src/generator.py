import random
import src.config as cfg

def id_from_ping(command):
    return command[0:2] == "<@" and command[-1] == '>'

def author_is_cool(id):
    if id in cfg.cool_people:
        return True
    if id in cfg.stupid_people:
        return False
    return None

def choice(person):
    status = author_is_cool(person)
    if status == True:
        name = "src\\cool_people.txt"
    elif status == False:
        name = "src\\bad_people.txt"
    else:
        return " мне нечего сказать о тебе"
    file = open(name, 'r', encoding="utf-8")
    choiced = random.choice(file.read().split("\n"))
    file.close()
    return choiced

words_dict = {}
words = set([])

def process_message(message):
    if len(message) < 3:
        return
    pair = []
    for word in message.split(" "):
        pair.append(word)
        words.add(word)
        
        if len(pair) == 2:
            if pair[0] in words_dict.keys():
                words_dict[pair[0]].append(pair[1])
            else:
                words_dict[pair[0]] = [pair[1]]
            
            pair = [pair[1]]

def initialization(messages):
    for message in messages.split("\n"):
        process_message(message)
        
                
def generate_chain():
    word = random.choice(list(words_dict.keys()))
    chain = [word]

    for i in range(random.randint(5, 12)):
        if chain[-1] not in words_dict.keys():
            break
        
        chain.append(random.choice(words_dict[chain[-1]]))    
    answer = ' '.join(chain)    
    return answer


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'a+', encoding='utf-8')

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

    def read_logs(self):
        self.file.seek(0)   
        content = self.file.read()
        self.file.seek(0, 2)
        return content

    def close(self):
        self.file.close()

def anime():
    return random.choice(cfg.video_playlist)


