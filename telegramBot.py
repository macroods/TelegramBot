import logging
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="o chatgpt killer está ativo")

async def mano(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('nossa'):
        paulista = ['véi mó cota isso ai tio', 'esse bagulho eh loko', 'ah para mano', 'ta loko mano oas idea']
        texto = random.choice(paulista)
        await update.message.reply_text(texto)

async def capo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="A vida é um paraíso, mas os homens não o sabem e não se preocupam em sabê-lo. Decididamente não compreendo por que é mais glorioso bombardear de projéteis uma cidade do que assassinar alguém a machadadas. Não será preferível corrigir, recuperar e educar um ser humano que cortar-lhe a cabeça? A beleza salvará o mundo.")


async def menny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    games = ['left', 'gmod', 'sonic de carrinho', 'dark souls', 'hell let loose', 'fifa']
    game = random.choice(games)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=game)


async def fala(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('fala'):
        falas = ['fala mano', 'fala tio', 'oi', 'manda', 'diga']
        texto = random.choice(falas)
        await update.message.reply_text(texto)


async def conquista(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('só conquista'):
        await update.message.reply_text('só conquista mano')


async def kasino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="AEEEEEE KASINAAAAAAAAAAAAAAAAO\nhttps://www.youtube.com/watch?v=LCDaw0QmQQc")


async def frodo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('frodo'):
        fotos_frodo = ['https://s.glbimg.com/es/ge/f/300x397/2011/07/28/elano_flickr62.jpg', 
                       'https://rd1.com.br/wp-content/uploads/2020/05/20200501-rafael_portugal_-_a_multilaser_tem190415_100937.png', 
                       'https://i.pinimg.com/originals/60/59/14/60591452f4407ae32e07eae4612cfb7d.png',
                       'https://hollywoodhatesme.files.wordpress.com/2010/08/sideshow-bob.jpg',
                       'https://www.ogol.com.br/img/jogadores/32/768732_ori__20210402015635_elano.jpg']
        frodo = random.choice(fotos_frodo)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=frodo)


if __name__ == '__main__':
    application = ApplicationBuilder().token('6709085556:AAGfST-byO0ttZmkwOCR6Dq6aLQyUcrRAgQ').build()
    
    mano_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), mano)
    fala_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), fala)
    conquista_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), conquista)
    frodo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), frodo)
    start_handler = CommandHandler('start', start)
    capo_handler = CommandHandler('capo', capo)
    menny_handler = CommandHandler('menny', menny)
    kasino_handler = CommandHandler('kasino', kasino)

    application.add_handler(start_handler)
    application.add_handler(capo_handler)
    application.add_handler(menny_handler)
    application.add_handler(fala_handler)
    application.add_handler(mano_handler, group=1)
    application.add_handler(conquista_handler, group=2)
    application.add_handler(frodo_handler, group=3)
    application.add_handler(kasino_handler)
    
    application.run_polling()