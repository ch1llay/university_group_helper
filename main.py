from modules import  *

from Bot.bot import *

app = Flask(__name__)


@app.route('/bot', methods=["POST"])
def bot():
    if request.data:
        data = json.loads(request.data)
        if data["type"] in ["message_new", "message_event"]:
            r = Bot.msg_processing(data)
            if r != "ok":
                return r
    return "ok"


@app.route('/', methods=["GET", "POST"])
def site():
    return "ok"

if __name__ == "__main__":
    app.run()