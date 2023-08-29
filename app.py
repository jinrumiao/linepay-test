from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('FodjM2t1CPtpwbASYaro4QZ1imRri8LnN7x9E9JHS0I6mD8IBDhHfypxWAlkfYWErlERTX8BHZKNjUtZfud4YDT5aoTfOCg5jV0XmBNKU87uN1hwVcMI7ovnTukh7pD5V1eCI91nBDARs86eKXVhWgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1dbcb5c802532d8a5455e44d206af583')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # event有什麼資料？詳見補充

    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Hi! Welcome to LSTORE.'))


if __name__ == "__main__":
    app.run()
