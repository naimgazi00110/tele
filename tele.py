from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define the command handler for '/start'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("YouTube Channel", url="https://www.youtube.com/@GyaaniNaim"),
            InlineKeyboardButton("Telegram Channel", url="https://t.me/GNScriptZone")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_message = """**BlumAuto Installation Guide**  
Author: [@Androidunlocking](https://t.me/Androidunlocking)  

**Features:**
- ✅ Auto Claim
- ✅ Daily Auto Claim
- ✅ Automated Gameplay (with random user inputs)

**How to Register:**
To start, click the link below:  
[Register Here](https://t.me/blum/app?startapp=ref_5nFz4GuA4k)

**How to Use:**

1. Download either **Kiwi Browser** or **Mises Browser** from Google Play:
   - [Kiwi Browser](https://play.google.com/store/apps/details?id=com.kiwibrowser.browser)
   - [Mises Browser](https://play.google.com/store/apps/details?id=site.mises.browser)

2. In the browser, install the following extensions from the Chrome Web Store:
   - [Ignore X-Frame Headers](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe)
   - [Violentmonkey](https://chromewebstore.google.com/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=be)

3. Download the script by joining the channel below:  
   - [GNScriptZone Channel](https://t.me/GNScriptZone)  

4. Finally, open Telegram and go to [BlumCryptoBot](https://web.telegram.org/k/#@BlumCryptoBot).

For full guidance, join our Telegram channel:  
- [GNScriptZone](https://t.me/GNScriptZone)
    """
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='Markdown')

if __name__ == '__main__':
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    app = ApplicationBuilder().token('7735525920:AAFxANKXUhIHWJGSrJcWI7hj9BRwEqsBeng').build()

    # Add a handler for the /start command
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    app.run_polling()
