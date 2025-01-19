import asyncio
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery,LabeledPrice, PreCheckoutQuery, ChatJoinRequest
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter
import logging
from aiogram import Router, types
from aiogram.enums.chat_type import ChatType


import config
import keyboards as kb
from db.mongo_db import MongoDB
from db.admins import create_database_and_collection

bot = Bot(token=config.token)
router = Router()
mongo = MongoDB()

#!LANGUAGE
@router.message(CommandStart())
async def start(message: Message):
        await mongo.set_user(message.from_user.id)
        try:
            language = await mongo.get_user_language(message.from_user.id)
            if language:
                if language == 'ru':
                    await message.answer('Привет! Я @bot - я буду отправлять сообщения о покупке/продаже монеты fov. \nВстатавьте в чат ваш токен:',reply_markup=kb.start_ru)
                elif language == 'isp':    
                    await message.answer('Hola! Soy @bot: enviaré mensajes de compra/venta de monedas fov. \nenvíenos al chat su token:',reply_markup=kb.start_isp)
                elif language == 'uzb':    
                    await message.answer("Salom! Men @bot-men FOV tanga sotib olish/sotish haqida xabar yuboraman. \nsizning tokeningizni suhbatga qo'shing:",reply_markup=kb.start_uzb)
                elif language == 'ukr':    
                    await message.answer('Привіт! Я @bot-я буду надсилати повідомлення про купівлю/продаж монети fov. \nВстатавьте в чат ваш токен:',reply_markup=kb.start_ukr)
                elif language == 'kore':    
                    await message.answer('안녕! 나는@봇입니다-나는 동전 구매/판매에 대한 메시지를 보낼 것입니다. \n채팅에 토큰 추가:',reply_markup=kb.start_kore)
                elif language == 'port':    
                    await message.answer('Olá! Eu @bot-vou enviar mensagens de compra/venda de moedas fov. \nVocê pode conversar com seu token:',reply_markup=kb.start_port)
                elif language == 'kitay':    
                    await message.answer('嗨！ 我是@bot-我将发送有关购买/出售fov硬币的消息。 \n将您的令牌添加到聊天中:',reply_markup=kb.start_kitay)
                elif language == 'germ':    
                    await message.answer('Hallo! Ich bin @bot - Ich werde Nachrichten über den Kauf/Verkauf einer fov-Münze senden. \nStellen Sie Ihr Token in den Chat ein:',reply_markup=kb.start_germ)
                elif language == 'need':    
                    await message.answer('Hoi! Ik ben @bot - Ik zal berichten sturen over het kopen/verkopen van fov-munten. \nVoeg je token toe aan de chat:',reply_markup=kb.start_need)
                elif language == 'franc':    
                    await message.answer("Bonjour! Je suis @bot - je vais envoyer des messages sur l'achat/vente de pièces fov. \nEntrez votre jeton dans le chat:",reply_markup=kb.start_franc)
                elif language == 'turk':    
                    await message.answer('Merhaba! Ben @bot - fov coininin alım/satımıyla ilgili mesajlar göndereceğim. \nTokeninizi sohbete ekleyin:',reply_markup=kb.start_turk)
                elif language == 'itali':    
                    await message.answer("Ciao! Sono @bot-invierò messaggi sull'acquisto / vendita di monete fov. \nInserisci il tuo Token nella chat:",reply_markup=kb.start_itali)
                elif language == 'yap':    
                    await message.answer('こんにちは! 私は@botです-私はfovコインの購入/販売に関するメッセージを送信します。 \トークンをチャットに追加する:',reply_markup=kb.start_yap)
                elif language == 'indo':    
                    await message.answer('Hai! Saya @bot - Saya akan mengirim pesan tentang membeli / menjual koin fov. \nTambahkan token Anda ke obrolan:',reply_markup=kb.start_indo)
                elif language == 'vet':    
                    await message.answer('Chào! Tôi là @ bot-tôi sẽ gửi tin nhắn về việc mua/bán tiền fov. \nThêm mã thông báo của bạn vào cuộc trò chuyện:',reply_markup=kb.start_vet)
                elif language == 'pol':    
                    await message.answer('Cześć! Jestem @ bot-będę wysyłać wiadomości o kupnie / sprzedaży monety fov. \nWpisz swój token na czacie:',reply_markup=kb.start_pol)
                elif language == 'venger':    
                    await message.answer('Sziasztok! @Bot vagyok-üzeneteket fogok küldeni a FOV érmék vásárlásáról/eladásáról. \nAdja hozzá a tokent a csevegéshez:',reply_markup=kb.start_venger)
                else:    
                    await message.answer('Hi! I am @bot - I will send messages about buying/selling fov coins \nAdd your token to the chat:',reply_markup=kb.start_us)
            else:
                    await message.answer('Выберите язык: | Select a language:', reply_markup=kb.language)
        except Exception as e:
            print(f"Ошибка в обработчике start: {e}")
            await message.reply("Произошла ошибка. Пожалуйста, попробуйте позже.")


@router.message(Command("access"))
async def access(message: Message):
    price = [LabeledPrice(label='XTR',amount=99)]
    await message.answer_invoice(
        title='Оплата',
        description='Оплатите вход в частный тг канал',
        prices=price,
        provider_token='',
        payload='chanel_support',
        currency='XTR',
        reply_markup=kb.access)


@router.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@router.message(F.successful_paymant)
async def successful_pay(message: Message):
    await mongo.set_user_balance(tg_id=message.from_user.id,balance=99)
    await message.answer(f'Успех. Ваш баланс: {mongo.get_user_balance}\nХотите купить подписку за 99р?',reply_markup=kb.buy_chat)


@router.callback_query(F.data == 'buy')
async def buy(message: Message):
    balance = await mongo.get_user_balance(tg_id=message.from_user.id)
    if balance >= 99:
        await mongo.set_user_balance(tg_id=message.from_user.id, balance=-99)
        await message.answer('Вы успешно купили доступ')
        await mongo.user_buy_chat(tg_id=message.from_user.id,buy=True)
        await test(ChatJoinRequest)
    else:
        await message.answer('Не хватает денег на балансе')


@router.chat_join_request()
async def test(chat_join_request: ChatJoinRequest):
    try:
        await chat_join_request.bot.send_message(chat_join_request.from_user.id, 'цыц, узбекиии спятт')
        if mongo.user_buy_chat == True:
            await chat_join_request.approve(hide_requester=False)
        else:
            await chat_join_request.bot.send_message(chat_join_request.from_user.id, 'Вы должный оплатить доступ')
    except Exception as ex:
        print(ex)


@router.message(Command('profile'))
async def profile(message: Message):
    language = await mongo.get_user_language(message.from_user.id)
    try:
        if language:
            if language == 'ru':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_ru)
            elif language == 'us':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_us)
            elif language == 'port':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_port)
            elif language == 'kitay':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_kitay)
            elif language == 'germ':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_germ)
            elif language == 'ukr':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_ukr)
            elif language == 'turk':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_turk)
            elif language == 'isp':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_isp)
            elif language == 'kore':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_kore)
            elif language == 'uzb':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_uzb)
            elif language == 'need':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_need)
            elif language == 'franc':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_franc)
            elif language == 'itali':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_itali)
            elif language == 'yap':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_yap)
            elif language == 'indo':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_indo)
            elif language == 'vet':
                await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_vet)
            elif language == 'pol':
                await message.answer('Cześć! Jestem @ bot-będę wysyłać wiadomości o kupnie / sprzedaży monety fov. \nWpisz swój token na czacie:',reply_markup=kb.start_pol)
            elif language == 'venger':    
                await message.answer('Sziasztok! @Bot vagyok-üzeneteket fogok küldeni a FOV érmék vásárlásáról/eladásáról. \nAdja hozzá a tokent a csevegéshez:',reply_markup=kb.start_venger)
            else:    
                await message.answer('Hi! I am @bot - I will send messages about buying/selling fov coins \nAdd your token to the chat:',reply_markup=kb.start_us)
        else:
            await message.answer('Выберите язык: | Select a language:', reply_markup=kb.language)
    except Exception as e:
        print(f"Ошибка в обработчике start: {e}")
        await message.reply("Произошла ошибка. Пожалуйста, попробуйте позже.")



#!АДМИН ПАНЕЛЬ 
@router.message(Command('admin'))
async def start(message: Message):
    collection = await create_database_and_collection()
    if collection is not None:
        admin = await collection.find_one({"tg_id": message.from_user.id})
        if admin:
            await message.answer('Добро пожаловать в админ панель!', reply_markup=kb.admin)
        else:
            await message.answer('Мая твоя не понимать')
    else:
        await message.answer('Ошибка доступа к базе данных.')



@router.message(Command('profile'))
async def profile(message: Message):
    language = await mongo.get_user_language(message.from_user.id)
    try:
        if language == 'ru':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_ru)
        elif language == 'us':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_us)
        elif language == 'port':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_port)
        elif language == 'kitay':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_kitay)
        elif language == 'germ':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_germ)
        elif language == 'ukr':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_ukr)
        elif language == 'turk':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_turk)
        elif language == 'isp':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_isp)
        elif language == 'kore':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_kore)
        elif language == 'uzb':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_uzb)
        elif language == 'need':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_need)
        elif language == 'franc':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_franc)
        elif language == 'itali':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_itali)
        elif language == 'yap':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_yap)
        elif language == 'indo':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_indo)
        elif language == 'vet':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_vet)
        elif language == 'pol':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_pol)
        elif language == 'venger':
            await message.answer('Выбранный язык: ' + language, reply_markup=kb.profile_venger)
        else:
            await message.answer('Выберите язык: | Select a language:', reply_markup=kb.language)
    except:
        print('Ошибка')
    

#!СМЕНА ЯЗЫКА ЧЕРЕЗ ПРОФИЛЬ
@router.callback_query(F.data == 'change_language_ru')
async def change_lang_ru(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Ваш текущий язык:'+ language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_us')
async def change_lang_us(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Your current language is:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_port')
async def change_lang_port(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Seu idioma atual é:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_kitay')
async def change_lang_kitay(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('您当前的语言是：' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_germ')
async def change_lang_germ(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Ihre aktuelle Sprache ist:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_ukr')
async def change_lang_ukr(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Ваша поточна мова:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_turk')
async def change_lang_turk(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Mevcut diliniz:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_isp')
async def change_lang_isp(callback: CallbackQuery):
    
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Tu idioma actual es:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_kore')
async def change_lang_kore(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('현재 언어는:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_uzb')
async def change_lang_uzb(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Hozirgi tilingiz:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_need')
async def change_lang_need(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Uw huidige taal is:' + language, reply_markup=kb.language)
    except:
        print('ошибка')



@router.callback_query(F.data == 'change_language_franc')
async def change_lang_franc(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Votre langue actuelle est:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_itali')
async def change_lang_itali(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('La tua lingua attuale è:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_yap')
async def change_lang_yap(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('現在の言語は:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_indo')
async def change_lang_indo(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Bahasa Anda saat ini:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_vet')
async def change_lang_vet(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Ngôn ngữ hiện tại của bạn là:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_pol')
async def change_lang_pol(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Twój aktualny język to:' + language, reply_markup=kb.language)
    except:
        print('ошибка')

@router.callback_query(F.data == 'change_language_venger')
async def change_lang_venger(callback: CallbackQuery):
    language = await mongo.get_user_language(callback.from_user.id)
    try:
        await callback.message.answer('Az Ön jelenlegi nyelve:' + language, reply_markup=kb.language)
    except:
        print('ошибка')







#!Ответ при выборе языка
@router.callback_query(F.data == 'ru')
async def ru(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='ru')
    await callback.message.answer('Привет! Я @bot - я буду отправлять сообщения о покупке/продаже монеты fov. Встатавьте в чат ваш токен:')
   
        
@router.callback_query(F.data == 'us')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='us')
    await callback.message.answer('Hi! I am @bot - I will send messages about buying/selling fov coins \nAdd your token to the chat:')

    
@router.callback_query(F.data == 'isp')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='isp')
    await callback.message.answer('Hola! Soy @bot: enviaré mensajes de compra/venta de monedas fov. \nenvíenos al chat su token:')


@router.callback_query(F.data == 'uzb')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='uzb')
    await callback.message.answer("Salom! Men @bot-men FOV tanga sotib olish/sotish haqida xabar yuboraman. \nsizning tokeningizni suhbatga qo'shing:")


@router.callback_query(F.data == 'ukr')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='ukr')
    await callback.message.answer('Привіт! Я @bot-я буду надсилати повідомлення про купівлю/продаж монети fov. \nВстатавьте в чат ваш токен:')



@router.callback_query(F.data == 'kore')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='kore')
    await callback.message.answer('안녕! 나는@봇입니다-나는 동전 구매/판매에 대한 메시지를 보낼 것입니다. \n채팅에 토큰 추가:')
    
@router.callback_query(F.data == 'port')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='port')
    await callback.message.answer('Olá! Eu @bot-vou enviar mensagens de compra/venda de moedas fov. \nVocê pode conversar com seu token:')


@router.callback_query(F.data == 'kitay')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='kitay')
    await callback.message.answer('嗨！ 我是@bot-我将发送有关购买/出售fov硬币的消息。 \n将您的令牌添加到聊天中')


@router.callback_query(F.data == 'germ')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='germ')
    await callback.message.answer('Hallo! Ich bin @bot - Ich werde Nachrichten über den Kauf/Verkauf einer fov-Münze senden. \nStellen Sie Ihr Token in den Chat ein:')
  

@router.callback_query(F.data == 'need')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='need')
    await callback.message.answer('Hoi! Ik ben @bot - Ik zal berichten sturen over het kopen/verkopen van fov-munten. \nVoeg je token toe aan de chat:')


@router.callback_query(F.data == 'franc')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='franc')
    await callback.message.answer("Bonjour! Je suis @bot - je vais envoyer des messages sur l'achat/vente de pièces fov. \nEntrez votre jeton dans le chat:")


@router.callback_query(F.data == 'turk')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='turk')
    await callback.message.answer('Merhaba! Ben @bot - fov coininin alım/satımıyla ilgili mesajlar göndereceğim. \nTokeninizi sohbete ekleyin:')


@router.callback_query(F.data == 'itali')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='itali')
    await callback.message.answer("Ciao! Sono @bot-invierò messaggi sull'acquisto / vendita di monete fov. \nInserisci il tuo Token nella chat:")


@router.callback_query(F.data == 'yap')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='yap')
    await callback.message.answer('こんにちは! 私は@botです-私はfovコインの購入/販売に関するメッセージを送信します。 \トークンをチャットに追加する:')


@router.callback_query(F.data == 'indo')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='indo')
    await callback.message.answer('Hai! Saya @bot - Saya akan mengirim pesan tentang membeli / menjual koin fov. \nTambahkan token Anda ke obrolan:')


@router.callback_query(F.data == 'vet')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='vet')
    await callback.message.answer('Chào! Tôi là @ bot-tôi sẽ gửi tin nhắn về việc mua/bán tiền fov. \nThêm mã thông báo của bạn vào cuộc trò chuyện:')


@router.callback_query(F.data == 'pol')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='pol')
    await callback.message.answer('Cześć! Jestem @ bot-będę wysyłać wiadomości o kupnie / sprzedaży monety fov. \nWpisz swój token na czacie:')
    
    
@router.callback_query(F.data == 'venger')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='venger')
    await callback.message.answer('Sziasztok! @Bot vagyok-üzeneteket fogok küldeni a FOV érmék vásárlásáról/eladásáról. \nAdja hozzá a tokent a csevegéshez:')

@router.callback_query(F.data == 'kore')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='kore')
    await callback.message.answer('안녕! 나는@봇입니다-나는 동전 구매/판매에 대한 메시지를 보낼 것입니다. \n채팅에 토큰 추가:')
    
@router.callback_query(F.data == 'port')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='port')
    await callback.message.answer('Olá! Eu @bot-vou enviar mensagens de compra/venda de moedas fov. \nVocê pode conversar com seu token:')


@router.callback_query(F.data == 'kitay')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='kitay')
    await callback.message.answer('嗨！ 我是@bot-我将发送有关购买/出售fov硬币的消息。 \n将您的令牌添加到聊天中')


@router.callback_query(F.data == 'germ')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='germ')
    await callback.message.answer('Hallo! Ich bin @bot - Ich werde Nachrichten über den Kauf/Verkauf einer fov-Münze senden. \nStellen Sie Ihr Token in den Chat ein:')
  

@router.callback_query(F.data == 'need')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='need')
    await callback.message.answer('Hoi! Ik ben @bot - Ik zal berichten sturen over het kopen/verkopen van fov-munten. \nVoeg je token toe aan de chat:')


@router.callback_query(F.data == 'franc')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='franc')
    await callback.message.answer("Bonjour! Je suis @bot - je vais envoyer des messages sur l'achat/vente de pièces fov. \nEntrez votre jeton dans le chat:")


@router.callback_query(F.data == 'turk')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='turk')
    await callback.message.answer('Merhaba! Ben @bot - fov coininin alım/satımıyla ilgili mesajlar göndereceğim. \nTokeninizi sohbete ekleyin:')


@router.callback_query(F.data == 'itali')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='itali')
    await callback.message.answer("Ciao! Sono @bot-invierò messaggi sull'acquisto / vendita di monete fov. \nInserisci il tuo Token nella chat:")


@router.callback_query(F.data == 'yap')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='yap')
    await callback.message.answer('こんにちは! 私は@botです-私はfovコインの購入/販売に関するメッセージを送信します。 \トークンをチャットに追加する:')


@router.callback_query(F.data == 'indo')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='indo')
    await callback.message.answer('Hai! Saya @bot - Saya akan mengirim pesan tentang membeli / menjual koin fov. \nTambahkan token Anda ke obrolan:')


@router.callback_query(F.data == 'vet')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='vet')
    await callback.message.answer('Chào! Tôi là @ bot-tôi sẽ gửi tin nhắn về việc mua/bán tiền fov. \nThêm mã thông báo của bạn vào cuộc trò chuyện:')


@router.callback_query(F.data == 'pol')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='pol')
    await callback.message.answer('Cześć! Jestem @ bot-będę wysyłać wiadomości o kupnie / sprzedaży monety fov. \nWpisz swój token na czacie:')
    
    
@router.callback_query(F.data == 'venger')
async def us(callback: CallbackQuery):
    await mongo.set_user_language(callback.from_user.id, language='venger')
    await callback.message.answer('Sziasztok! @Bot vagyok-üzeneteket fogok küldeni a FOV érmék vásárlásáról/eladásáról. \nAdja hozzá a tokent a csevegéshez:')

logging.basicConfig(level=logging.INFO)

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет!  Этот бот приветствует новых участников.")

@router.chat_member(ChatMemberUpdatedFilter(member_status_changed=True)) 
async def chat_member_updated(update: types.ChatMemberUpdated):
    """Обрабатывает обновления информации о участниках чата."""
    if update.new_chat_member.status == "member":
        await update.bot.send_message(
            chat_id=update.chat.id,
            text=f"Привет, {update.new_chat_member.user.full_name}! Добро пожаловать!"
        )
    elif update.new_chat_member.status == "left":
        await update.bot.send_message(
            chat_id=update.chat.id,
            text=f"Пользователь {update.old_chat_member.user.full_name} покинул чат."
        )


