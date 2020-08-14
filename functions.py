"""Functions for Voice Assistant"""
import xml.etree.ElementTree as ET
import speech_recognition as sr
from selenium import webdriver
from datetime import datetime
from gtts import gTTS
import playsound
import calendar
import random
import pyowm
import time
import os

language = 'ru'

tree = ET.parse('text/configuration.xml')  # Parsing the configuration file
root = tree.getroot()


def xmlParsing():
    """Parses the xml file"""
    tree = ET.parse('text/configuration.xml')  # Parsing the configuration file
    root = tree.getroot()
    return tree, root


def speaking(speaking, printing=True):
    """Says the text"""
    try:
        output = gTTS(text=speaking, lang=language, slow=False)
        output.save('audio/speaking.mp3')
    except:
        noConnection = 'Что-то у меня не выходит подключиться к сети. Попробуйте, пожалуйста, позже.'
        print('Vivian: ', end='')
        print(noConnection)
        playsound.playsound('audio/noConnection.mp3', True)
        exit()
    else:
        if printing:
            print('Vivian: ', end='')
            print(speaking)
            playsound.playsound('audio/speaking.mp3', True)
            os.remove('audio/speaking.mp3')
        else:
            playsound.playsound('audio/speaking.mp3', True)
            os.remove('audio/speaking.mp3')


def firstGreeting(testing=False):
    """The very first greeting, asks the name"""
    firstGreeting = '''Здравствуйте, я Vivian, ваш личный голосовой помощник.'''
    whatsYourName = 'Как мне к вам обращаться?'
    if testing:
        return firstGreeting, whatsYourName
    speaking(firstGreeting)
    speaking(whatsYourName)
    name = getVoice()
    while name == '':
        repeatName = 'Пожалуйста, повторите ваше имя.'
        speaking(repeatName)
        name = getVoice()
    return name


def firstGreeting2(name, testing=False):
    """Continues the first greeting, offers to see 'info''"""
    whatCanYouDo = '''Отлично, ''' + name + '''. Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.'''
    if not testing:
        speaking(whatCanYouDo)
    else:
        return whatCanYouDo


def greeting(name, testing=False):
    """Regular greeting"""
    greeting = 'Здравствуйте, ' + name + '. Чем могу вам помочь?'
    if not testing:
        speaking(greeting)
    else:
        return greeting


def getVoice():
    """Gets the user's text"""
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        playsound.playsound('audio/Speak2.mp3', True)
        audio = rObject.listen(source, phrase_time_limit=6)
    playsound.playsound('audio/Stop2.mp3', True)
    try:
        text = rObject.recognize_google(audio, language='ru')
        print('Вы:    ', text)
        return text
    except sr.UnknownValueError:
        silence = 'Мы что, играем в молчанку?'
        speaking(silence)
        return ''
    except:
        noConnection = 'Что-то у меня не выходит подключиться к сети. Попробуйте, пожалуйста, позже.'
        print('Vivian: ', end='')
        print(noConnection)
        playsound.playsound('audio/noConnection.mp3', True)
        exit()


def info(testing=False, infoTest=False, seeHelpingTest=False):
    """Tells about its opportunities"""
    info = '''Я умею петь и танцевать!
        А если серьезно, то я могу помочь вам с этими задачами:'''
    if testing and infoTest:
        return info
    if not testing:
        print('Vivian: ', end='')
        print(info)
        print('''            - Расскажу о своих возможностях.
            - Помогу разобраться, как со мной работать.
            - Напомню вам ваше имя.
            - Назову текущие дату и время.
            - Покажу вам календарь на месяц или на год.
            - Рассмешу вас шуткой.
            - Скажу, как у меня дела.
            - Узнаю нынешнюю погоду.
            - Подожду вас, если нужно.
            - Очищу экран.
            - Могу повторять за вами.
            - Посчитаю вам легкие примеры.
            - Открою приложение.
            - Запомню и воспроизведу факты о вас.
            - Возьму на себя управление вашеми задачами.
        ! Чтобы посмотреть управление действиями, откройте справку, сказав: "Справка" или "Помощь".''')
        speaking(info, False)
        time.sleep(15)

    seeHelping = 'Хотите посмотреть справку о том, как пользоваться этими функциями?'
    if testing and seeHelpingTest:
        return seeHelping
    speaking(seeHelping)
    answer = getVoice()
    if ('да' in answer.lower()) or ('ага' in answer.lower()):
        ok = 'Хорошо.'
        speaking(ok)
        helping()
    else:
        return


def helping(testing=False):
    """Tells how to use it (shows help)"""
    if not testing:
        helping = 'Открываю справку.'
        speaking(helping, False)
        print(root[0].text)
    shouldwait = 'Эта справка довольно большая. Мне подождать вас пару минут, пока вы будете её читать?'
    if testing:
        return shouldwait
    speaking(shouldwait)
    answer = getVoice()
    if ('да' in answer.lower()) or ('ага' in answer.lower()):
        ok = 'Хорошо.'
        speaking(ok)
        time.sleep(150)
    else:
        ok = 'Хорошо.'
        speaking(ok)


def yourNameIs(name, testing=False):
    """Names the user"""
    yourNameIs = 'Вас зовут ' + name + '. Вы что, забыли?'
    if testing:
        return yourNameIs
    speaking(yourNameIs)


def timeNow(hours='', testing=False):
    """Tells current time"""
    now = datetime.now()
    timeNow = now.strftime('%H:%M')

    if not testing:
        hours = int(timeNow[:2])
    else:
        hours = int(hours)

    if 0 <= hours < 4:
        time = 'Сейчас ' + timeNow + '. Это же глубокая ночь! Почему это вы не спите?'
    elif 4 <= hours < 7:
        time = 'Сейчас ' + timeNow + '. Это раннее утро. Я бы на вашем месте еще поспала. Хорошо, что я робот и ' + \
               'мне не нужно спать'
    elif 7 <= hours < 12:
        time = 'Сейчас ' + timeNow + '. С добрым утром! Как спалось?'
    elif 12 <= hours < 17:
        time = 'Сейчас ' + timeNow + '. Середина дня. Отличное время, чтобы заняться делами.'
    elif 17 <= hours < 21:
        time = 'Сейчас ' + timeNow + '. Вечер - моё любимое время суток.'
    elif 21 <= hours <= 23:
        time = 'Сейчас ' + timeNow + '. Уже поздний вечер. Пора готовиться ко сну.'
    if testing:
        return time
    speaking(time)


def dateNow(testing=False):
    """Tells current date"""
    today = datetime.today()
    dateNow = today.strftime("%d/%m/%Y")
    date = 'Сегодня ' + dateNow
    if testing:
        return date
    speaking(date)


def showCalendar(year, mm='', testing=False):
    """Shows year or month calendar"""
    today = str(datetime.today())
    yyyy = today[:4]

    if not testing:
        mm = today[5:7]
        if mm.startswith('0'):
            mm = mm[1:]

    if mm == '1':
        month = 'Январь'
    elif mm == '2':
        month = 'Февраль'
    elif mm == '3':
        month = 'Март'
    elif mm == '4':
        month = 'Апрель'
    elif mm == '5':
        month = 'Май'
    elif mm == '6':
        month = 'Июнь'
    elif mm == '7':
        month = 'Июль'
    elif mm == '8':
        month = 'Август'
    elif mm == '9':
        month = 'Сентябрь'
    elif mm == '10':
        month = 'Октябрь'
    elif mm == '11':
        month = 'Ноябрь'
    elif mm == '12':
        month = 'Декабрь'

    if year:
        calendarYear = 'Открываю календарь на ' + yyyy + ' год.'
        if testing:
            return calendarYear
        print()
        speaking(calendarYear, False)
        print(calendar.calendar(int(yyyy)))
    else:
        calendarMonth = 'Открываю календарь на ' + month
        if testing:
            return calendarMonth
        speaking(calendarMonth, False)
        print()
        print(calendar.month(int(yyyy), int(mm)))


def joke(testing=False):
    """Tells the joke"""
    joke = root[1][random.randint(0, ((len(root[1])) - 1))].text
    if testing:
        return joke
    speaking(joke)


def mood(answer=False, testing=False, mood='', text=''):
    """Answers the question: 'How are you?'"""
    if not mood:
        mood = root[2][random.randint(0, ((len(root[2])) - 1))].text

    if testing and not answer:
        return mood
    elif not testing:
        speaking(mood)

    # If she asked you too
    if (mood == 'Хорошо, спасибо, а у вас?') or (
            mood == 'Что мы все обо мне да обо мне? О себе лучше расскажите - ваши как дела?'):
        if not answer:
            text = getVoice()
            text = text + ' '
        if ('хорошо ' in text.lower()) or ('замечательно ' in text.lower()) or ('отлично ' in text.lower()) or (
                'прекрасно ' in text.lower()):
            well = 'Это хорошо, что всё хорошо.'
            if answer:
                return well
            speaking(well)
        elif ('нормально ' in text.lower()) or ('более-менее ' in text.lower()) or ('ну так ' in text.lower()):
            soso = 'Главное, что не плохо!'
            if answer:
                return soso
            speaking(soso)
        elif ('плохо ' in text.lower()) or ('ужасно ' in text.lower()) or ('отвратительно ' in text.lower()):
            bad = 'Не расстраивайтесь, по моим подстчетам, уже совсем скоро все наладится.'
            if answer:
                return bad
            speaking(bad)
        else:
            another = 'Да, ведь и такое случается.'
            if answer:
                return another
            speaking(another)


def whatDoYouDo(testing=False):
    """Answers the question: 'What are you doing?'"""
    whatDoYouDo = 'Наслаждаюсь прекрасной компанией.'
    if testing:
        return whatDoYouDo
    speaking(whatDoYouDo)


def weather(text, testing=False):
    """Tells current weather in a town"""
    try:
        city = text.split()[len(text.split()) - 1]
        if testing:
            return city
        owm = pyowm.OWM('45aead70137433ea2b6608d48aa1afb6', language='RU')
        loc = owm.weather_at_place(city)
        weather = loc.get_weather()
        wind = weather.get_wind()
        humidity = weather.get_humidity()
        temp = weather.get_temperature(unit='celsius')
        preassure = weather.get_pressure()['press'] * 0.75006375541921
        preassure = int(preassure)
    except:
        noWeather = 'Кажется, метеостанция не хочет делиться со мной данными. Пожалуйста, попробуйте еще раз.'
        speaking(noWeather)
    else:
        weather = 'В городе ' + city + ' сейчас:\n\tПогода: ' + str(
            weather.get_detailed_status()) + '.\n\tВетер: ' + str(int(wind['speed'])) + ' км/ч.\n\tВлажность: ' + str(
            humidity) + ' %.\n\tТемпература: ' + str(int(temp['temp'])) + ' °C.\n\tАтм. Давление: ' + str(
            preassure) + ' мм рт. ст.'
        speaking(weather)


def wait():
    """Waits for 10 sec if you ask it to"""
    ok = 'Хорошо.'
    speaking(ok)
    time.sleep(10)
    okstop = 'Надеюсь, вы всё.'
    speaking(okstop)


def repeat(text, testing=False):
    """Repeats the text"""
    text = text.lower().split()
    text.remove('повтори')
    text = (' '.join(text))
    if len(text) == 0:
        silence = 'Повторяю молчание. Слушайте:'
        if testing:
            return silence
        speaking(silence)
        time.sleep(5)
    else:
        text = text[0].upper() + text[1:]
        say = (text + '. Но вообще-то я не попугай.')
        if testing:
            return say
        speaking(say)


def calculation(text, testing=False):
    """Calculates simple things"""
    text = text.lower()
    # Get rid of letters if they are in text
    if 'плюс' in text:
        text = text.replace('плюс', '+')
    if 'прибавить' in text:
        text = text.replace('прибавить', '+')
    if 'минус' in text:
        text = text.replace('минус', '-')
    if 'отнять' in text:
        text = text.replace('отнять', '-')
    if 'умножить на' in text:
        text = text.replace('умножить на', 'х')
    if 'разделить на' in text:
        text = text.replace('разделить на', '/')
    if 'поделить на' in text:
        text = text.replace('поделить на', '/')
    if 'делить на' in text:
        text = text.replace('делить на', '/')
    mathIndex = ''
    for i in range(len(text)): # We find where the digits start
        if text[i] in '0123456789':
            mathIndex = i
            break
    # If there is nothing to calculate
    if mathIndex == '':
        nothingToCalc = 'Безусловно, очень хороший пример.'
        if testing:
            return nothingToCalc
        speaking(nothingToCalc)
    # If there is
    else:
        mathPhrase = text[i:]
        mathPhrase = mathPhrase.split()
        result = ''
        go = False
        # And digits are not separated: '123+321'
        if (len(mathPhrase) == 1) and (('+' in mathPhrase[0]) or ('-' in mathPhrase[0]) or ('х' in mathPhrase[0]) or ('/' in mathPhrase[0])):
            mathPhrase = mathPhrase[0]
            for i in range(len(mathPhrase)):
                if (mathPhrase[i] == '+') or (mathPhrase[i] == '-') or (mathPhrase[i] == 'х') or (mathPhrase[i] == '/'):
                    n1 = int(mathPhrase[:i])
                    # For situations like: '123+'
                    try:
                        n2 = int(mathPhrase[i+1:])
                    except:
                        nothingToCalc = 'Мне кажется, что вы недоговорили условие.'
                        if testing:
                            return nothingToCalc
                        speaking(nothingToCalc)
                        return
                    else:
                        s = mathPhrase[i]
                        go = True

        if len(mathPhrase) == 3:
            n1 = int(mathPhrase[0])
            n2 = int(mathPhrase[2])
            s = mathPhrase[1]
        # If there is not enough data
        elif not go:
            nothingToCalc = 'Мне кажется, что вы недоговорили условие.'
            if testing:
                return nothingToCalc
            speaking(nothingToCalc)
            return

        # We make this list because later we will join it together so we can say  it
        mathPhrase = [str(n1), '', str(n2)]
        if s == '+':
            s = ' + '
            result = n1 + n2
            mathPhrase[1] = 'плюс'
        elif s == '-':
            s = ' - '
            result = n1 - n2
            mathPhrase[1] = 'минус'
        elif s == 'х' or s == 'X' or s == 'x': # This are different X'es
            s = ' х '
            result = n1 * n2
            mathPhrase[1] = 'умножить на'
        elif s == '/':
            s = ' / '
            try:
                result = n1 / n2
            except ZeroDivisionError:
                noZeroDivision = 'На ноль делить нельзя.'
                if testing:
                    return noZeroDivision
                speaking(noZeroDivision)
                return
            else:
                mathPhrase[1] = 'разделить на'
                result = float(format(result, '.2f'))
                result = str(result)
                for i in range(len(result)):
                    if result[i] == '.':
                        dot = i
                if result[dot + 1] == '0':
                    result = result[:-2]
                else:
                    result = result.replace('.', ',')
        mathPhrase = ' '.join(mathPhrase)
        answerSay = mathPhrase + ' = ' + str(result)
        answerPrint = str(n1) + s + str(n2) + ' = ' + str(result)
        if testing:
            return answerPrint
        print('Vivian: ', end='')
        print(answerPrint)
        speaking(answerSay, False)


def openProgram(text, testing=False, empty=False):
    """Opens an app"""
    text = text.lower().split()
    text.remove('открой')
    if ('пожалуйста' in text):
        text.remove('пожалуйста')
    for i in range(len(text)):
        text[i] = text[i][0].upper() + text[i][1:]
    app = (' '.join(text))
    openingApp = ('Открываю ' + app + '.')
    if testing and not empty:
        return openingApp

    noSuchApp = 'К сожалению, я не могу найти это приложение'
    if ('chrome' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        except:
            speaking(noSuchApp)
    elif ('word' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Word')
        except:
            speaking(noSuchApp)
    elif ('excel' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Excel')
        except:
            speaking(noSuchApp)
    elif ('access' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Access')
        except:
            speaking(noSuchApp)
    elif (('power point' in app.lower()) or ('powerpoint' in app.lower())):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\PowerPoint')
        except:
            speaking(noSuchApp)
    elif (('calculator' in app.lower()) or ('калькулятор' in app.lower())):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Калькулятор')
        except:
            speaking(noSuchApp)
    elif ('paint' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Paint 3D')
        except:
            speaking(noSuchApp)
    elif ('visual' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Visual Studio 2019 (2)')
        except:
            speaking(noSuchApp)
    elif ('steam' in app.lower()):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Steam (2)')
        except:
            speaking(noSuchApp)
    elif (('почта' in app.lower()) or ('почту' in app.lower())):
        try:
            speaking(openingApp)
            os.startfile('C:\ALL\links\Почта')
        except:
            speaking(noSuchApp)
    elif len(app) == 0:
        notOpeningApp = ('Я умею много чего, но пустоту пока открывать не научилась.')
        if testing and empty:
            return notOpeningApp
        speaking(notOpeningApp)
    else:
        notOpeningApp = ('К сожалению, я не знаю такого приложения.')
        if testing and empty:
            return notOpeningApp
        speaking(notOpeningApp)

def formattingText(text, testing=False):
    """Cleans the text"""
    # I don't do text.lower(), because there can be names, I don't want to spoil
    if testing:
        text = text.split()
    if 'Вивиан' in text:
        text.remove('Вивиан')
    if 'вивиан' in text:
        text.remove('вивиан')
    if 'Виверн' in text:
        text.remove('Виверн')
    if 'виверн' in text:
        text.remove('виверн')
    if ('Пожалуйста' in text):
        text.remove('Пожалуйста')
    if ('пожалуйста' in text):
        text.remove('пожалуйста')
    if ('Viper' in text):
        text.remove('Viper')
    if ('viper' in text):
        text.remove('viper')
    if ('Vivern' in text):
        text.remove('Vivern')
    if ('vivern' in text):
        text.remove('vivern')
    if ('Vivian' in text):
        text.remove('Vivian')
    if ('vivian' in text):
        text.remove('vivian')
    if ('Viber' in text):
        text.remove('Viber')
    if ('viber' in text):
        text.remove('viber')
    if ('Мне' in text):
        text.remove('Мне')
    if ('мне' in text):
        text.remove('мне')
    if ('Kevin' in text):
        text.remove('Kevin')
    if ('kevin' in text):
        text.remove('kevin')
    if ('Скажи' in text):
        text.remove('Скажи')
    if ('скажи' in text):
        text.remove('скажи')
    if testing:
        text = (' '.join(text))
        text = text.strip()
    return text


def remember(text, testing=False):
    """Remember facts about you"""
    text = text.split()
    if 'Запомни' in text:
        text.remove('Запомни')
    else:
        text.remove('запомни')
    text = formattingText(text)

    if len(text) == 0:
        notRemember = ('Ничего - мой любимый объект для запоминания.')
        if testing:
            return notRemember
        speaking(notRemember)
    else:
        adj = text[0]
        rememb = text[1:]
        rememb = (' '.join(rememb))
        if testing:
            return adj, rememb
        parent = root.find('remember')
        child = ET.SubElement(parent, 'fact', {'adj': adj}).text = rememb
        tree.write('text/configuration.xml', encoding='utf-8')
        Remember = ('Хорошо, я запомнила это.')
        speaking(Remember)


def bethink(text, testing=False):
    """Recalls previous information"""
    searchText = text[:-1]
    text = text.split()
    # Get rid of the first word 'Какой', e.g.
    text = text[1:]
    if 'Вспомни' in text:
        text.remove('Вспомни')
    if 'вспомни' in text:
        text.remove('вспомни')
    text = formattingText(text)

    facts = {}
    k = 0
    # Make a dictionarywith facts: {'Fact': 'Adjective', ...}
    for parent in root.findall('remember/fact'):
        adj = parent.get('adj')
        fact = parent.text
        facts[fact] = adj
    # Find the needed fact
    for key, value in facts.items():
        for word in text:
            if word.lower() in key.lower():
                k += 1
        if k >= 2:
            answerKey = key
            break
        k = 0
    # Change the adjective
    if k >= 2:
        answerAdj = facts[answerKey]
        if answerAdj == 'Мой' or answerAdj == 'мой':
            answerAdj = 'Ваш'
        elif answerAdj == 'Моя' or answerAdj == 'моя':
            answerAdj = 'Ваша'
        elif answerAdj == 'Моё' or answerAdj == 'моё':
            answerAdj = 'Ваше'
        elif answerAdj == 'Мои' or answerAdj == 'мои':
            answerAdj = 'Ваши'
        elif answerAdj == 'Моего' or answerAdj == 'моего':
            answerAdj = 'Вашего'
        elif answerAdj == 'Мою' or answerAdj == 'мою':
            answerAdj = 'Вашу'

        answer = answerAdj + ' ' + answerKey
        if testing:
            return answer
        speaking(answer)
    else:
        text = ' '.join(text)
        if ('мо' in text.lower()):
            answer = 'Боюсь, вы мне об этом не говорили.'
            speaking(answer)
        else:
            webSearch(searchText)


def taskManager(text, testing=False, alltasks=False):
    """Task manager"""

    def listOfTasks(text):
        """Shows the list of tasks in the form of a table"""
        taskList = 'Открываю ваш список задач.)'
        speaking(taskList, False)

        print('Vivian: ', end='-' * 55)
        print('\n\t{0: <22}'.format('Название'), end='')
        print('{0: <11}'.format('Сфера'), end='')
        print('{0: <12}'.format('Приоритет'), end='')
        print('{0: <10}\n'.format('Дата'))
        # If there is no tasks
        if len(tasks) == 0:
            print('\t{0: <22}'.format('Пусто'), end='')
            print('{0: <11}'.format('Пусто'), end='')
            print('{0: <12}'.format('Пусто'), end='')
            print('{0: <10}'.format('Пусто'))
            print('\t' + ('-' * 55))

            noTasks = 'Кажется, у вас нет задач. Вы можете добавить несколько, сказав "Добавь задачу".'
            speaking(noTasks)
        # If there are tasks after all
        else:
            for key, value in tasks.items():
                print('\t{0: <22}'.format(key), end='')
                print('{0: <11}'.format(value[0]), end='')
                print('{0: <12}'.format(value[1]), end='')
                print('{0: <10}'.format(value[2]))
            print('\t' + ('-' * 55))

    def addingTask(text, n):
        """Adds a task"""
        text = text.lower().split()
        if 'добавь' in text:
            text.remove('добавь')
        if 'добавить' in text:
            text.remove('добавить')
        if 'задачу' in text:
            text.remove('задачу')
        if 'пожалуйста' in text:
            text.remove('пожалуйста')
        text = formattingText(text)
        newTask = (' '.join(text))
        # If there is already this task
        if newTask in tasks:
            while newTask in tasks:
                if n < 2:
                    newTask = newTask + ' ' + str(n)
                    n += 1
                else:
                    newTask = newTask[:-2]
                    newTask = newTask + ' ' + str(n)
                    n += 1

        if len(newTask) == 0:
            newTask = 'Какую?'
            speaking(newTask, False)
            newTask = getVoice().lower() ############
            if newTask in tasks:
                while newTask in tasks:
                    if n < 2:
                        newTask = newTask + ' ' + str(n)
                        n += 1
                    else:
                        newTask = newTask[:-2]
                        newTask = newTask + ' ' + str(n)
                        n += 1

        sphere = 'Из какой она сферы? (Работа, учеба и т.д.)'
        speaking(sphere, False)
        sphere = getVoice()
        if ('нет' in sphere) or (sphere == ''):
            sphere = '-'

        priorety = 'Какой у нее приоритет? (высокий / средний / низкий)'
        speaking(priorety, False)
        priorety = getVoice()
        if 'нет' in priorety or (priorety == ''):
            priorety = '-'

        date = 'На какую дату записать эту задачу (назовите числа)'
        speaking(date, False)
        b = True
        while b:
            date = getVoice()
            if 'нет' in date or (date == ''):
                date = '-'
            date = date.replace('.', '/')
            date = date.replace(' ', '/')
            date = date.replace('-', '/')
            dmy = date.split('/')
            if len(dmy) != 3:
                # If there is no dmy
                repeatDate = 'Пожалуйста, повторите дату.'
                speaking(repeatDate, False)
                pass
            else:
                # If there is no y
                if len(dmy[2]) != 4:
                    today = datetime.today()
                    dateNow = today.strftime("%Y")
                    dmy[2] = dateNow
                dm = date[:-5]
                dm = dm.split('/')
                if len(dm) == 1:
                    dm = [dm[:len(dm[0])//2], dm[len(dm[0])//2:]]
                if len(dm[0]) == 1:
                    dm[0] = '0' + dm[0]
                if len(dm[1]) == 1:
                    dm[1] = '0' + dm[1]
                date = dm[0] + '/' + dm[1] + '/' + dmy[2]
                b = False

        tasks[newTask] = [sphere, priorety, date]

        parent = root.find('tasks')
        child = ET.SubElement(parent, 'task', {'name': newTask})
        ET.SubElement(child, 'sphere').text = sphere
        ET.SubElement(child, 'priorety').text = priorety
        ET.SubElement(child, 'date').text = date
        tree.write('text/configuration.xml', encoding='utf-8')

        ok = 'Задача "' + newTask + '" добавлена.'
        speaking(ok)
        return n

    def delitingTask(text, testing=False):
        """Delites a task"""
        text = text.lower().split()
        if 'удали' in text:
            text.remove('удали')
        if 'удалить' in text:
            text.remove('удалить')
        if 'задачу' in text:
            text.remove('задачу')
        if 'пожалуйста' in text:
            text.remove('пожалуйста')
        text = formattingText(text)

        # If the task name was sad
        if len(text) == 0:
            taskToDel = 'Какую?'
            speaking(taskToDel, False)
            taskToDel = getVoice().lower() ##############
            # If the task exists
            if taskToDel in tasks:
                parent = root.find('tasks')
                for child in parent:
                    if taskToDel in child.attrib['name'].lower():
                        parent.remove(child)
                tree.write('text/configuration.xml', encoding='utf-8')
            # If it doesn't
            else:
                noSuchTask = 'У вас нет такой задачи.'
                speaking(noSuchTask)
                return
        # If the task name wasnt sad
        else:
            taskToDel = (' '.join(text))
            # If the task exists
            if taskToDel in tasks:
                if testing:
                    return taskToDel
                parent = root.find('tasks')
                for child in parent:
                    if taskToDel in child.attrib['name'].lower():
                        parent.remove(child)
                tree.write('text/configuration.xml', encoding='utf-8')
            # If it doesn't
            else:
                noSuchTask = 'У вас нет такой задачи.'
                if testing:
                    return noSuchTask
                speaking(noSuchTask)
                return

        done = 'Удалено.'
        speaking(done)

    ### The Code ###

    # Build a dictionary with tasks: {'Task': ['sphere', 'priorety', 'date'], ...}
    n = 1
    tasks = {}
    for parent in root.findall('tasks/task'):
        task = parent.get('name')
        sphere = parent.find('sphere').text
        priorety = parent.find('priorety').text
        date = parent.find('date').text
        tasks[task] = [sphere, priorety, date]
    if testing and alltasks:
        return tasks

    ### List Of Tasks ###
    if ('список ' in text.lower()):
        listOfTasks(text)

    ### Adding A Task ###
    elif ('добав' in text.lower()):
        addingTask(text, n)

    ### Deliting A Task ###
    elif ('удали' in text.lower()):
        if not testing:
            delitingTask(text)
        else:
            return delitingTask(text, testing)

    else:
        didntGet = 'Я не совсем поняла вас. Пожалуйста, повторите снова или обратитесь к справке.'
        speaking(didntGet)


def webSearch(text, testing=False):
    """Searcher in browser for something"""
    text = text.split()
    if ('Найди' in text):
        text.remove('Найди')
    if ('найди' in text):
        text.remove('найди')
    if ('Узнай' in text):
        text.remove('Узнай')
    if ('узнай' in text):
        text.remove('узнай')
    if ('Ответь' in text):
        text.remove('Ответь')
    if ('ответь' in text):
        text.remove('ответь')
    if ('Поведай' in text):
        text.remove('Поведай')
    if ('поведай' in text):
        text.remove('поведай')
    if ('Расскажи' in text):
        text.remove('Расскажи')
    if ('расскажи' in text):
        text.remove('расскажи')
    if ('Загугли' in text):
        text.remove('Загугли')
    if ('загугли' in text):
        text.remove('загугли')
    if ('Погугли' in text):
        text.remove('Погугли')
    if ('погугли' in text):
        text.remove('погугли')
    if ('Прошу' in text):
        text.remove('Прошу')
    if ('прошу' in text):
        text.remove('прошу')
    if ('Назови' in text):
        text.remove('Назови')
    if ('назови' in text):
        text.remove('назови')
    text = formattingText(text)
    text = ' '.join(text)
    text = text[0].upper() + text[1:]
    if testing:
        return text
    shouldShow = 'Хотите, чтобы я нашла информацию в интернете по запросу "' + text + '"?'
    speaking(shouldShow)
    show = getVoice()
    if ('да' in show.lower()) or ('ага' in show.lower()):
        searching = 'Вот, что мне удалось найти по запросу "' + text + '".'
        speaking(searching)
        try:
            driver = webdriver.Chrome('web/chromedriver.exe')
            driver.get('https://www.google.com/')
            search = driver.find_element_by_name('q')
            search.send_keys(text)
            time.sleep(3)
            button = driver.find_element_by_name('btnK')
            button.click()
            time.sleep(10)
            os.system('cls')
        except:
            noServices = 'Что-то сервисы Google не выходят на связь. Попробуйте, пожалуйста снова.'
            speaking(noServices)
    else:
        ok = 'Хорошо.'
        speaking(ok)


def bye(name, testing=False):
    """Says goodbye"""
    bye = 'Уже уходите, ' + name + '? Ну что ж, буду с нетерпением вас ждать!'
    if not testing:
        speaking(bye)
    else:
        return bye
