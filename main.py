import telebot
import sys, time, random, requests , re
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, parse_qs

TOKEN = '6097544977:AAFk1TU5e6CDV7duwKO-ITLHOZ3VM0pgFZs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Welcome to my bot!')
    bot.send_message(message.chat.id, 'Please send me a URL.')

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.text.startswith('http'):
        url2 = message.text
        bot.send_message(message.chat.id, "بدأ البوت بالعمل ")



        with open('account.txt', 'r') as file:
            for line in file.readlines():
                account, password = line.strip().split(':')

                url = 'https://m.facebook.com'
                xurl = url + '/login.php'

                u1 = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
                u2 = 'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
                u3 = 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko'
                u4 = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'

                def login():
                    user = account
                    pswd = password

                    try:
                        req = requests.Session()
                        req.headers.update({
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language': 'en_US',
                            'cache-control': 'max-age=0',
                            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': random.choice([u1, u2, u3, u4])
                        })

                        with req.get(url) as response_body:
                            inspect = bs(response_body.text, 'html.parser')
                            lsd_key = inspect.find('input', {'name': 'lsd'})['value']
                            jazoest_key = inspect.find('input', {'name': 'jazoest'})['value']
                            m_ts_key = inspect.find('input', {'name': 'm_ts'})['value']
                            li_key = inspect.find('input', {'name': 'li'})['value']
                            try_number_key = inspect.find('input', {'name': 'try_number'})['value']
                            unrecognized_tries_key = inspect.find('input', {'name': 'unrecognized_tries'})['value']
                            bi_xrwh_key = inspect.find('input', {'name': 'bi_xrwh'})['value']

                            data = {
                                'lsd': lsd_key,
                                'jazoest': jazoest_key,
                                'm_ts': m_ts_key,
                                'li': li_key,
                                'try_number': try_number_key,
                                'unrecognized_tries': unrecognized_tries_key,
                                'bi_xrwh': bi_xrwh_key,
                                'email': user,
                                'pass': pswd,
                                'login': "submit"
                            }

                            response_body2 = req.post(xurl, data=data, allow_redirects=True, timeout=300)
                            open("resopnse.html", 'wb').write(response_body2.content)

                            cookie = ";".join([key + "=" + value for key, value in req.cookies.get_dict().items()])

                            if 'checkpoint' in cookie:
                                sys.exit("\033[1;31mAccount terminated by Facebook!\033[0m")
                                bot.send_message(message.chat.id, "Account terminated by Facebook!")
                            elif 'c_user' in cookie:
                                print(f'\n   [\033[38;5;83mSuccessfully Log In!\033[0m] \033[0m\n\n')
                                bot.send_message(message.chat.id, "Successfully Log In")

                                response = requests.get('https://business.facebook.com/business_locations', headers={
                                    'Cookie': cookie,
                                    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
                                }).text
                                token_eaag = re.search('(EAAG\w+)', str(response)).group(1)

                                def extract_post_id_from_url(url2):
                                    parsed_url = urlparse(url2)
                                    query_params = parse_qs(parsed_url.query)

                                    if 'v' in query_params:
                                        post_id = query_params['v'][0]
                                    elif 'story_fbid' in query_params:
                                        post_id = query_params['story_fbid'][0]
                                    else:
                                        post_id = None

                                    return post_id
                                # استخراج ID المنشور من الرابط
                                post_id = extract_post_id_from_url(url2)

                                id_post = post_id

                                text1 = "#نطالب_بالتعين_اسوه_بمعهد_المنصور"
                                text2 = "#خريجي_معاهد_اجهزه_طبيه"
                                text3 = "#وزير_الصحة_د_صالح_الحسناوي"
                                text4 = "#مطلبنا_التعين_اسوه_باقراننا"

                                TX = (text1 + '\n' + text2 + '\n' + text3)
                                TX1 = (text4 + '\n' + text2 + '\n' + text3)
                                delay = 15
                                for i in range(4):
                                    if i / 2 == 0:
                                        GG = TX
                                        comment = GG.split(',')
                                        x, y = 0, 0

                                        time.sleep(delay);
                                        teks = random.choice(comment)
                                        data = {
                                            'message': teks,
                                            'access_token': token_eaag
                                        }
                                        response2 = requests.post(
                                            'https://graph.facebook.com/{}/comments/'.format(id_post), data=data,
                                            cookies={
                                                'Cookie': cookie,
                                            }).json()
                                        if '\'id\':' in str(response2):
                                            x += 1
                                            print(f'\n   [\033[38;5;83mComment : Done\033[0m] \033[0m\n\n')

                                            ee = f'comment Done : {i} '
                                            cou = bot.send_message(message.chat.id, "Comment : Done")
                                            bot.edit_message_text(chat_id=cou.chat.id,message_id=cou.message_id, text=ee)

                                    else:
                                        comment = TX1.split(',')
                                        x, y = 0, 0

                                        time.sleep(delay);
                                        teks = random.choice(comment)
                                        data = {
                                            'message': teks,
                                            'access_token': token_eaag
                                        }
                                        response2 = requests.post(
                                            'https://graph.facebook.com/{}/comments/'.format(id_post), data=data,
                                            cookies={
                                                'Cookie': cookie,
                                            }).json()
                                        if '\'id\':' in str(response2):
                                            x += 1
                                            print(f'\n   [\033[38;5;83mComment : Done\033[0m] \033[0m\n\n')
                                            ee = f'comment Done : {i} '
                                            cou = bot.send_message(message.chat.id, "Comment : Done")
                                            bot.edit_message_text(chat_id=cou.chat.id, message_id=cou.message_id,
                                                                  text=ee)





                            else:
                                sys.exit("\033[38;5;208mIncorrect details\033[0m")
                                bot.send_message(message.chat.id, "Incorrect details")

                            return req

                    except requests.exceptions.ConnectionError:

                        sys.exit('No internet')
                        bot.send_message(message.chat.id, "No internet'")


                login()


bot.polling()