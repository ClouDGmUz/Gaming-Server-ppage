from django.shortcuts import render

def home(request):
    """
    Renders the main Discord server homepage with MEGA TEAM branding
    and gaming information for CS2 and DOTA 2 in Uzbek language.
    """
    context = {
        'server_name': 'MEGA TEAM',
        'main_games': ['CS2', 'DOTA 2'],
        'discord_invite': 'https://discord.gg/g8UBrgm8',  # Replace with actual Discord invite link
        'page_title': 'MEGA TEAM - Discord Serveri',
        'hero_subtitle': 'CS2 va DOTA2 o\'yinchilari',
        'hero_description': 'Jamodosh toping, O\'ynang, Yuting',
        'join_discord': 'Discordga Qo\'shilish',
        'our_games': 'Bizning O\'yinlarimiz',
        'featured_games': 'Asosiy O\'yinlar',
        'cs2_description': 'Taktik FPS mukammalligi. Bizning jamoalarimizga qo\'shiling va birgalikda reytingni ko\'taring.',
        'dota2_description': 'Strategik MOBA mahorati. Afsonaviy jamoalar tuzing va jang maydonida hukmronlik qiling.',
        'active_players': 'Faol O\'yinchilar',
        'servers': 'Serverlar',
        'tournaments': 'Turnirlar',
        'daily': 'Kunlik',
        'competitive_matches': 'Raqobatli O\'yinlar',
        'training_sessions': 'Mashg\'ulot Sesiyalari',
        'team_formation': 'Jamoa Tuzish',
        'ranked_parties': 'Reytingli Partiyalar',
        'strategy_coaching': 'Strategiya Murabbiylik',
        'tournament_play': 'Turnir O\'yini',
        'why_choose': 'Nega MEGA TEAM ni tanlash kerak?',
        'active_community': 'Faol Jamiyat',
        'active_community_desc': 'Bizning serverimizda boshqa o\'yinchilar bilan birgalikda o\'ynang',
        'competitive_play': 'Raqobatli O\'yin',
        'competitive_play_desc': 'Muntazam turnirlarda qatnashing va reytinglar jadvalini ko\'taring',
        'support_24_7': '24/7 Yordam',
        'support_24_7_desc': 'Bizning maxsus xodimlar jamoamiz har doim yordam berish va moderatsiya qilish uchun shu yerda',
        'skill_development': 'Mahorat Rivojlantirish',
        'skill_development_desc': 'Murabbiylik sesiylari va strategiya qo\'llanmalari bilan professionallardan o\'rganing',
        'members': 'A\'zolar',
        'hours_active': 'Soat Faol',
        'uptime': 'Ishlash Vaqti',
        'ready_to_join': 'Elitaga qo\'shilishga tayyormisiz?',
        'connect_gamers': 'O\'xshash fikrli o\'yinchilar bilan bog\'laning va mahoratingizni keyingi bosqichga olib chiqing',
        'join_mega_team': 'MEGA TEAM ga Hoziroq Qo\'shiling',
    }
    return render(request, 'discord_server/home.html', context)
