import logging
from telegram.ext import Updater, CommandHandler
from modules import ip_scanner, system_info, dns_lookup, whois_lookup, reverse_shell

# 🔐 Your Telegram Bot Token
BOT_TOKEN = "7790165200:AAFEaFCXOyiotBmGkcZWX0X1WfxFK-2dPMs"
AUTHORIZED_USER_ID = 7790165200

# 🛠 Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 🔐 Decorator to restrict commands to you only
def restricted(func):
    def wrapper(update, context):
        if update.effective_user.id != AUTHORIZED_USER_ID:
            return update.message.reply_text("Access Denied.")
        return func(update, context)
    return wrapper

@restricted
def start(update, context):
    update.message.reply_text("👾 BUGZKINGZ-MD ONLINE\n\nUse:\n/scanip [ip]\n/sysinfo\n/dns [domain]\n/whois [domain]\n/shell [ip] [port]")

@restricted
def scanip(update, context):
    try:
        ip = context.args[0]
        result = ip_scanner.scan(ip)
        update.message.reply_text(result)
    except:
        update.message.reply_text("Usage: /scanip [ip]")

@restricted
def sysinfo(update, context):
    result = system_info.get_info()
    update.message.reply_text(result)

@restricted
def dns_registry(update, context):
    try:
        domain = context.args[0]
        result = dns_lookup.lookup(domain)
        update.message.reply_text(result)
    except:
        update.message.reply_text("Usage: /dns [domain]")

@restricted
def whois_registry(update, context):
    try:
        domain = context.args[0]
        result = whois_lookup.whois_query(domain)
        update.message.reply_text(result[:4000])  # Telegram message limit
    except:
        update.message.reply_text("Usage: /whois [domain]")

@restricted
def shell_command(update, context):
    try:
        ip, port = context.args
        result = reverse_shell.generate_shell(ip, port)
        update.message.reply_text(f"Reverse Shell:\n`{result}`", parse_mode='Markdown')
    except:
        update.message.reply_text("Usage: /shell [ip] [port]")

def unknown(update, context):
    update.message.reply_text("❓ Unknown command.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("scanip", scanip))
    dp.add_handler(CommandHandler("sysinfo", sysinfo))
    dp.add_handler(CommandHandler("dns", dns_registry))
    dp.add_handler(CommandHandler("whois", whois_registry))
    dp.add_handler(CommandHandler("shell", shell_command))
    dp.add_handler(CommandHandler(None, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
