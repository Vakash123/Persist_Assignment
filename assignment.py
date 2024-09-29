from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # Replace with your token

def start(update, context):
    update.message.reply_text('Welcome! Send me a job ID and I will apply for you!')

def apply_job(update, context):
    job_id = update.message.text
    # Assuming LinkedIn's API request setup, as mentioned earlier
    url = "https://www.linkedin.com/jobs-apply-endpoint"
    cookies = {
        'li_at': 'YOUR_LINKEDIN_SESSION_COOKIE',  # Replace with real cookie value
    }
    data = {
        'jobId': job_id,
        'applicantDetails': {
            'name': 'Your Name',
            'email': 'your.email@example.com',
        }
    }

    response = requests.post(url, cookies=cookies, json=data)
    if response.status_code == 200:
        update.message.reply_text('Successfully applied!')
    else:
        update.message.reply_text(f'Failed to apply: {response.text}')

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, apply_job))

    updater.start_polling()
    updater.idle()
