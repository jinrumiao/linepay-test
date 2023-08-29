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


def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 17,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]

    text_message = TextSendMessage(text='''$ Master RenderP $
Hello! 您好，歡迎您成為 Master RenderP 的好友！

我是Master 支付小幫手 

-這裡有商城，還可以購物喔~
-直接點選下方【圖中】選單功能

-期待您的光臨！''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])


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
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    message_text = str(event.message.text).lower()

    if message_text == "@使用說明":
        about_us_event(event)

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Hi! Welcome to LSTORE.'))


if __name__ == "__main__":
    app.run()
