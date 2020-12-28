from slack import WebClient
from datetime import datetime
import getpass


class SendSlackMeg:
    def __init__(self):
        self.client = WebClient(
            token="xoxb-1062719850053-1168207540961-fGjdKub4V9d0Aeyyhw9Re2Nk"
        )

    def sendMsg(self, msg):
        now = datetime.now()
        time = "{}/{}/{} {}:{}:{}".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )
        response = self.client.chat_postMessage(
            channel="#server", text=time + "\n" + msg + "\n" + getpass.getuser()
        )


if __name__ == "__main__":
    SendSlackMeg().sendMsg("Test Code")
