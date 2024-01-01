import logging
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="O bot está ativo!")


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('ajuda'):
        frases = ['Como posso ajudar?', 'O que deseja?', 'Clique no bot para mais informações']
        texto = random.choice(frases)
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
        falas = ['fala mano', 'oi', 'manda', 'diga']
        texto = random.choice(falas)
        await update.message.reply_text(texto)


async def conquista(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('só conquista'):
        await update.message.reply_text('só conquista galera')


async def kasino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="AEEEEEE KASINAAAAAAAAAAAAAAAAO\nhttps://www.youtube.com/watch?v=LCDaw0QmQQc")


async def programacao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text.lower()
    if text.startswith('frodo'):
        fotos = ['https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 
                       'https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 
                       'https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                       'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                       'https://plus.unsplash.com/premium_photo-1661963212517-830bbb7d76fc?q=80&w=1986&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D']
        foto = random.choice(fotos_frodo)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=foto)


if __name__ == '__main__':
    application = ApplicationBuilder().token('6709085556:AAGfST-byO0ttZmkwOCR6Dq6aLQyUcrRAgQ').build()
    
    ajuda_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), ajuda)
    fala_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), fala)
    conquista_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), conquista)
    programacao_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), programacao)
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
