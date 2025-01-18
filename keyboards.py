from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


access = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Оплатить 1 ⭐️',pay=True)
]])

buy_chat = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Купить',callback_data='buy')
]])

profile_ru = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Кошелек',callback_data='wallet_ru'),
    InlineKeyboardButton(text='Ваша подписка',callback_data='subscribe_ru')],
    [InlineKeyboardButton(text='Сменить язык',callback_data='change_language_ru'),
    InlineKeyboardButton(text='Настройки',callback_data='settings_ru')]])

profile_us = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Wallet',callback_data='wallet_us'),
    InlineKeyboardButton(text='Your subscribe',callback_data='subscribe_us')],
    [InlineKeyboardButton(text='Change language',callback_data='change_language_us'),
    InlineKeyboardButton(text='Settings',callback_data='settings_us')]])

profile_port = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Carteira',callback_data='wallet_'),
    InlineKeyboardButton(text='Sua assinatura',callback_data='subscribe_')],
    [InlineKeyboardButton(text='Mudar idioma',callback_data='change_language_'),
    InlineKeyboardButton(text='Configurações',callback_data='settings_')]])

profile_kitay = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='钱包',callback_data='wallet_kitay'),
    InlineKeyboardButton(text='您的订阅',callback_data='subscribe_kitay')],
    [InlineKeyboardButton(text='您的订阅',callback_data='change_language_kitay'),
    InlineKeyboardButton(text='设置',callback_data='settings_kitay')]])

profile_germ = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Brieftasche',callback_data='wallet_germ'),
    InlineKeyboardButton(text='Ihr Abonnement',callback_data='subscribe_germ')],
    [InlineKeyboardButton(text='Sprache ändern',callback_data='change_language_germ'),
    InlineKeyboardButton(text='Einstellungen',callback_data='settings_germ')]])

profile_ukr = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Гаманець',callback_data='wallet_ukr'),
    InlineKeyboardButton(text='Ваша підписка',callback_data='subscribe_ukr')],
    [InlineKeyboardButton(text='Змінити мову',callback_data='change_language_ukr'),
    InlineKeyboardButton(text='Налаштування',callback_data='settings_ukr')]])

profile_turk = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Cüzdan',callback_data='wallet_turk'),
    InlineKeyboardButton(text='Aboneliğiniz',callback_data='subscribe_turk')],
    [InlineKeyboardButton(text='Dili değiştir',callback_data='change_language_turk'),
    InlineKeyboardButton(text='Ayarlar',callback_data='settings_turk')]])

profile_isp = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Billetera',callback_data='wallet_isp'),
    InlineKeyboardButton(text='Su suscripción',callback_data='subscribe_isp')],
    [InlineKeyboardButton(text='Cambiar idioma',callback_data='change_language_isp'),
    InlineKeyboardButton(text='Ajustes',callback_data='settings_isp')]])

profile_kore = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='지갑',callback_data='wallet_kore'),
    InlineKeyboardButton(text='구독',callback_data='subscribe_kore')],
    [InlineKeyboardButton(text='언어 변경',callback_data='change_language_kore'),
    InlineKeyboardButton(text='설정',callback_data='settings_kore')]])

profile_uzb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Hamyon',callback_data='wallet_uzb'),
    InlineKeyboardButton(text='Obuna',callback_data='subscribe_uzb')],
    [InlineKeyboardButton(text='Tilni oʻzgartirish',callback_data='change_language_uzb'),
    InlineKeyboardButton(text='Sozlamalar',callback_data='settings_uzb')]])



profile_need = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Portemonnee',callback_data='wallet_need'),
    InlineKeyboardButton(text='Uw abonnement',callback_data='subscribe_need')],
    [InlineKeyboardButton(text='Taal wijzigen',callback_data='change_language_need'),
    InlineKeyboardButton(text='Instellingen',callback_data='settings_need')]])

profile_franc = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Portefeuille',callback_data='wallet_franc'),
    InlineKeyboardButton(text='Votre abonnement',callback_data='subscribe_franc')],
    [InlineKeyboardButton(text='Changer de langue',callback_data='change_language_franc'),
    InlineKeyboardButton(text='Paramètres',callback_data='settings_franc')]])

profile_itali = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Portafoglio',callback_data='wallet_itali'),
    InlineKeyboardButton(text='Il tuo abbonamento',callback_data='subscribe_itali')],
    [InlineKeyboardButton(text='Cambia lingua',callback_data='change_language_itali'),
    InlineKeyboardButton(text='Impostazioni',callback_data='settings_itali')]])

profile_yap = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='財布',callback_data='wallet_yap'),
    InlineKeyboardButton(text='あなたの購読',callback_data='subscribe_yap')],
    [InlineKeyboardButton(text='言語を変更',callback_data='change_language_yap'),
    InlineKeyboardButton(text='設定',callback_data='settings_yap')]])

profile_indo = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Dompet',callback_data='wallet_indo'),
    InlineKeyboardButton(text='Langganan Anda',callback_data='subscribe_indo')],
    [InlineKeyboardButton(text='Ubah bahasa',callback_data='change_language_indo'),
    InlineKeyboardButton(text='Pengaturan',callback_data='settings_indo')]])

profile_vet = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Ví',callback_data='wallet_vet'),
    InlineKeyboardButton(text='Đăng ký của bạn',callback_data='subscribe_vet')],
    [InlineKeyboardButton(text='Thay đổi ngôn ngữ',callback_data='change_language_vet'),
    InlineKeyboardButton(text='Cài đặt',callback_data='settings_vet')]])

profile_pol = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Portfel',callback_data='wallet_pol'),
    InlineKeyboardButton(text='Twoja subskrypcja',callback_data='subscribe_pol')],
    [InlineKeyboardButton(text='Zmień język',callback_data='change_language_pol'),
    InlineKeyboardButton(text='Ustawienia',callback_data='settings_pol')]])

profile_venger = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Tárca',callback_data='wallet_venger'),
    InlineKeyboardButton(text='Előfizetése',callback_data='subscribe_venger')],
    [InlineKeyboardButton(text='Nyelvváltás',callback_data='change_language_venger'),
    InlineKeyboardButton(text='Beállítások',callback_data='settings_venger')]])






admin = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Удалить рекламу',callback_data='delete_ad')],
    [InlineKeyboardButton(text='Добавить рекламу',callback_data='add_ad')]])




#!LANGUAGE
#Русский
start_ru = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Добавить в группу',callback_data='group_ru')]])

#Английский
start_us = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Add to a group',callback_data='group_us')]])

#Испания
start_isp = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Añadir al grupo',callback_data='group_isp')]])

#Узбекский 
start_uzb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Guruhga qo'shing",callback_data='group_uzb')]])

#Украина 
start_ukr = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Додати до групи',callback_data='group_ukr')]])

#Корейский
start_kore = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='그룹에 추가',callback_data='group_kore')]])


#Португалия 
start_port = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Adicionar ao grupo',callback_data='group_port')]])

#Китайский
start_kitay = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='添加到组',callback_data='group_kitay')]])

#Германский 
start_germ = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Zur Gruppe hinzufügen',callback_data='group_germ')]])

#Нидерландский
start_need = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Toevoegen aan een groep',callback_data='group_need')]])

#Франция 
start_franc = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Ajouter au groupe',callback_data='group_franc')]])

#Турецкий
start_turk = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Gruba ekle',callback_data='group_turk')]])

#Италянский 
start_itali = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Aggiungi al gruppo',callback_data='group_itali')]])

#Японский
start_yap = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='グループに追加する',callback_data='group_yap')]])

#Индонезия 
start_indo = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Tambahkan ke grup',callback_data='group_indo')]])

#Вьетнамский
start_vet = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Thêm vào một nhóm',callback_data='group_vet')]])

#Польшия 
start_pol = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Thêm vào một nhóm',callback_data='group_pol')]])

#Венгерский 
start_venger = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Hozzáadás egy csoporthoz',callback_data='group_venger')]])






language = InlineKeyboardMarkup(inline_keyboard=[[
    
    InlineKeyboardButton(text='🇷🇺 Русский',callback_data='ru'),
    InlineKeyboardButton(text='🇺🇸 English',callback_data='us')],
    
    [InlineKeyboardButton(text='🇵🇹 Português',callback_data='port'),
    InlineKeyboardButton(text='🇨🇳 中文',callback_data='kitay')],
    
    [InlineKeyboardButton(text='🇩🇪 Deutsch',callback_data='germ'),
    InlineKeyboardButton(text='🇺🇦 Українська',callback_data='ukr')],
    
    [InlineKeyboardButton(text='🇹🇷 Türkçe',callback_data='turk'),
    InlineKeyboardButton(text='🇪🇸 Español',callback_data='isp')],
    
    [InlineKeyboardButton(text='🇰🇷 한국어',callback_data='kore'),
    InlineKeyboardButton(text="🇺🇿 Oʻzbekcha",callback_data='uzb')],
    
    [InlineKeyboardButton(text='🇳🇱 Nederlands',callback_data='need'),
    InlineKeyboardButton(text='🇫🇷 Français',callback_data='franc')],
    
    [InlineKeyboardButton(text='🇮🇹 Italiano',callback_data='itali'),
    InlineKeyboardButton(text='🇯🇵 日本語',callback_data='yap')],
    
    [InlineKeyboardButton(text='🇮🇩 Indonesia',callback_data='indo'),
    InlineKeyboardButton(text='🇻🇳 Tiếng Việt',callback_data='vet')],
    
    [InlineKeyboardButton(text='🇵🇱 Polski',callback_data='pol'),
    InlineKeyboardButton(text='🇭🇺 Magyar',callback_data='venger')]])
