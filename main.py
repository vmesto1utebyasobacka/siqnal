from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 25116728
api_hash = "8fef459b63e30e0d4c7febd57d036648"
phone = "+994707909293"

# The channel/Group name that you want to get messages from
source_channel_name = 'Swing Trades | CST 🎯'

# The channel/Group that you want to send messages to
destination_channel_link = -1001511628499

# The channel to send specific messages
specific_messages_channel_link = -1001887840544  # Updated specific channel link

# Additional channel for specific messages based on keywords
additional_channel_link = -1001894835989

client = TelegramClient(phone, api_id, api_hash)

# Define the Convert_msg function
def Convert_msg(data):
    coin = ''
    Direction = ''
    entry = ''
    lev = ''
    tt = ''
    t1 = ''
    t2 = ''
    t3 = ''
    t4 = ''
    t5 = ''
    t6 = ''
    t7 = ''
    t8 = ''
    t9 = ''
    stoploss = ''

    lines = data.split('\n')
    for line in lines:
        if "Pair:" in line:
            coin = line.split("Pair:")[1]
        if "Direction:" in line:
            Direction = line.split("Direction:")[1]
        if "Leverage :" in line:
            lev = line.split("Leverage :")[1]
        if "Trade Type" in line:
            tt = line.split("Trade Type:")[1]
        if "ENTRY : " in line:
            entry = line.split("ENTRY : ")[1]
        if "Target 1" in line:
            t1 = line.split("Target 1")[1]
        if "Target 2" in line:
            t2 = line.split("Target 2")[1]
        if "Target 3" in line:
            t3 = line.split("Target 3")[1]
        if "Target 4" in line:
            t4 = line.split("Target 4")[1]
        if "Target 5" in line:
            t5 = line.split("Target 5")[1]
        if "Target 6" in line:
            t6 = line.split("Target 6")[1]
        if "Target 7" in line:
            t7 = line.split("Target 7")[1]
        if "Target 8" in line:
            t8 = line.split("Target 8")[1]
        if "Target 9" in line:
            t9 = line.split("Target 9")[1]
        if "STOP LOSS:" in line:
            stoploss = line.split()[2]
    msg = f"""
🚨 NEW ALERT

Pair:{coin}
Direction:{Direction}
➖➖➖➖➖➖➖
Position Size: 1-5% of your deposit
Leverage : {lev} (Double it if you like taking risk)
Leverage Mode: Cross Margin
Trade Type: {tt}
    ➖➖➖➖➖➖➖
🏦 ENTRY: {entry}

🔘Target 1  {t1}
🔘Target 2  {t2}
🔘Target 3  {t3}
🔘Target 4  {t4}
🔘Target 5  {t5}
🔘Target 6  {t6}
🔘Target 7  {t7}
🔘Target 8  {t8}
🔘Target 9  {t9}
🔴Stop = {stoploss}

Your Truly,
Elon Shelby
➖➖➖➖➖➖➖
- Crypto Moon®.
"""
    return msg

# Define Convert_msg_2 function for the second set of keywords
def Convert_msg_2(data):
    coin = ''
    Direction = ''
    entry = ''
    Short_Term = ''
    Mid_Term = ''
    stoploss = ''

    lines = data.split('\n')
    for line in lines:
        if "COIN:" in line:
            coin = line.split()[1]
        if "Direction:" in line:
            Direction = line.split()[1]
        if "ENTRY:" in line:
            entry = line.split("ENTRY:")[1]
        if "Short Term:" in line:
            Short_Term = line.split("Short Term:")[1]
        if "Mid Term:" in line:
            Mid_Term = line.split("Mid Term:")[1]
        if "STOP LOSS:" in line:
            stoploss = line.split()[2]
        if "COIN:" in line:
            coin = line.split()[1]
        if "Direction:" in line:
            Direction = line.split()[1]

    # Extracting data after /USDT
    leverage = data.split("/USDT ")[1].split()[0]

    msg = f"""
📣 CRYPTO ALERT📣

🚨 Pair: {coin}
Direction: {Direction}📈 

🏦 ENTRY: {entry}

🎯 SHORT-TERM TARGETS: {Short_Term}
🎯 MID-TERM TARGETS: {Mid_Term}
🚨 STOP-LOSS: {stoploss}

Leverage - {leverage}  (Double if you are a pro trader)
Leverage Mode: Cross Margin
Position Size: 1%-5% account value

💡 Remember 💡 Always conduct your own analysis and risk assessment before entering any trade. Monitor market conditions and adjust your strategy accordingly. Trading involves risks, and past performance is not indicative of future results.

NOT A FINANCIAL ADVICE
Happy trading! 📈💰💹
-LEE's Trade
➖➖➖➖➖➖➖
- Crypto Moon®.
    """

    return msg


# Function to modify messages with specified keywords
def modify_message(text):
    # Replace '- Bitcoin Bullets® Trading' with 'Crypto Moon® analytics'
    modified_text = text.replace("- Bitcoin Bullets® Trading", "Crypto Moon® analytics")
    # Remove the word 'Trading'
    modified_text = modified_text.replace("Trading", "")
    return modified_text

# Continue with the rest of your code
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))

async def send_to_destination(message, channel):
    await client.send_message(entity=channel, message=message)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title == source_channel_name:
            message = event.message
            text = message.text

            # Check for specific keywords in the message
            keywords_1 = ["VIP Trade ID", "ENTRY :", "Fed. Russian Insiders®"]
            keywords_2 = ["$", "ENTRY", "- Bitcoin Bullets® Trading"]
            keywords_3 = ["SIGNAL ID:", "ENTRY", "- Binance Killers®"]

            if all(keyword in text for keyword in keywords_1):
                # Convert message using Convert_msg function
                converted_message = Convert_msg(text)
                # Send converted message to another channel
                await client.send_message(entity=specific_messages_channel_link, message=converted_message)

            elif all(keyword in text for keyword in keywords_2):
                # Modify message based on keywords
                modified_message = modify_message(text)
                # Send modified message to additional channel
                await send_to_destination(modified_message, additional_channel_link)

            elif all(keyword in text for keyword in keywords_3):
                # Convert message using Convert_msg_2 function
                converted_message = Convert_msg_2(text)
                # Send converted message to specific channel for this case
                await client.send_message(entity=-1001594041839, message=converted_message)

            else:
                # Forward the message as is to the destination channel
                media = message.media  # Get media (photos, etc.)
                if text or media:
                    await send_to_destination(text, destination_channel_link)
    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit

client.start()
client.run_until_disconnected()