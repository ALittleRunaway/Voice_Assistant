"""Unit-tests for functions.py"""
import unittest
import functions
from datetime import datetime


class FirstGreeting2TestCase(unittest.TestCase):
    """Test firstGreeting2 funcrion"""

    def test_different_names(self):
        """Test different names"""
        self.assertEqual(functions.firstGreeting2('Боба', True), '''Отлично, Боба. Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.''')
        self.assertEqual(functions.firstGreeting2('', True), '''Отлично, . Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.''')
        self.assertEqual(functions.firstGreeting2('jndflkagfge', True), '''Отлично, jndflkagfge. Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.''')
        self.assertEqual(functions.firstGreeting2('777', True), '''Отлично, 777. Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.''')
        self.assertEqual(functions.firstGreeting2('М и ж р т', True), '''Отлично, М и ж р т. Я запомнила ваше имя и больше не буду его спрашивать.
        Теперь можете спросить меня, что я умею.''')


class FirstGreetingTestCase(unittest.TestCase):
    """Test firstGreeting finction"""

    def test_first_words(self):
        """Test first words"""
        firstGreeting, whatsYourName = functions.firstGreeting(True)
        self.assertEqual(firstGreeting, 'Здравствуйте, я Vivian, ваш личный голосовой помощник.')
        self.assertEqual(whatsYourName, 'Как мне к вам обращаться?')


class GreetingTestCase(unittest.TestCase):
    """Test greeting finction"""

    def test_different_names(self):
        """Test different names"""
        self.assertEqual(functions.greeting('Стивен', True), 'Здравствуйте, Стивен. Чем могу вам помочь?')
        self.assertEqual(functions.greeting('njk;djafkm;daksf', True), 'Здравствуйте, njk;djafkm;daksf. Чем могу '
                                                                       'вам помочь?')
        self.assertEqual(functions.greeting('', True), 'Здравствуйте, . Чем могу вам помочь?')
        self.assertEqual(functions.greeting('Стивен Хокинг', True), 'Здравствуйте, Стивен Хокинг. Чем могу вам помочь?')
        self.assertEqual(functions.greeting('123', True), 'Здравствуйте, 123. Чем могу вам помочь?')


class InfoTestCase(unittest.TestCase):
    """Test info finction"""

    def test_info(self):
        """Test info """
        self.assertEqual(functions.info(True, True), '''Я умею петь и танцевать!
        А если серьезно, то я могу помочь вам с этими задачами:''')

    def test_seeHelping(self):
        """Test question about helping """
        self.assertEqual(functions.info(True, False, True), 'Хотите посмотреть справку о том, как пользоваться '
                                                            'этими функциями?')


class HelpingTestCase(unittest.TestCase):
    """Test helping finction"""

    def test_helping_wait_question(self):
        """Test this function """
        self.assertEqual(functions.helping(True), 'Эта справка довольно большая. Мне подождать вас пару минут, '
                                                  'пока вы будете её читать?')


class YourNameIsTestCase(unittest.TestCase):
    """Test yourNameIs finction"""

    def test_your_name_is(self):
        """Test different names"""
        self.assertEqual(functions.yourNameIs('Эрик', True), 'Вас зовут Эрик. Вы что, забыли?')
        self.assertEqual(functions.yourNameIs('Эрик Сати', True), 'Вас зовут Эрик Сати. Вы что, забыли?')
        self.assertEqual(functions.yourNameIs('', True), 'Вас зовут . Вы что, забыли?')
        self.assertEqual(functions.yourNameIs('123', True), 'Вас зовут 123. Вы что, забыли?')
        self.assertEqual(functions.yourNameIs('Erick', True), 'Вас зовут Erick. Вы что, забыли?')
        self.assertEqual(functions.yourNameIs('gvhukyfghj', True), 'Вас зовут gvhukyfghj. Вы что, забыли?')


class TimeNowTestCase(unittest.TestCase):
    """Test timeNow finction"""

    def test_(self):
        """Test different time"""
        now = datetime.now()
        timeNow = now.strftime('%H:%M')
        hours = int(timeNow[:2])
        self.assertEqual(functions.timeNow('1', True), 'Сейчас ' + timeNow + '. Это же глубокая ночь! Почему это вы '
                                                                             'не спите?')
        self.assertEqual(functions.timeNow('5', True), 'Сейчас ' + timeNow + '. Это раннее утро. Я бы на вашем месте '
                                                                             'еще поспала. Хорошо, что я '
                                                                             'робот и мне не нужно спать')
        self.assertEqual(functions.timeNow('11', True), 'Сейчас ' + timeNow + '. С добрым утром! Как спалось?')
        self.assertEqual(functions.timeNow('14', True), 'Сейчас ' + timeNow + '. Середина дня. Отличное время, чтобы '
                                                                              'заняться делами.')
        self.assertEqual(functions.timeNow('19', True), 'Сейчас ' + timeNow + '. Вечер - моё любимое время суток.')
        self.assertEqual(functions.timeNow('22', True), 'Сейчас ' + timeNow + '. Уже поздний вечер. Пора готовиться '
                                                                              'ко сну.')


class DateNowTestCase(unittest.TestCase):
    """Test dateNow finction"""

    def test_dateNow(self):
        """Test current date"""
        today = datetime.today()
        dateNow = today.strftime("%d/%m/%Y")
        self.assertEqual(functions.dateNow(True), 'Сегодня ' + dateNow)


class ShowCalendarTestCase(unittest.TestCase):
    """Test showCalendar finction"""

    def test_year_calendar(self):
        """Test current year"""
        today = str(datetime.today())
        yyyy = today[:4]
        self.assertEqual(functions.showCalendar(True, '1', True), 'Открываю календарь на ' + yyyy + ' год.')

    def test_month_calendar(self):
        """Test different months"""
        self.assertEqual(functions.showCalendar(False, '1', True), 'Открываю календарь на Январь')
        self.assertEqual(functions.showCalendar(False, '2', True), 'Открываю календарь на Февраль')
        self.assertEqual(functions.showCalendar(False, '3', True), 'Открываю календарь на Март')
        self.assertEqual(functions.showCalendar(False, '4', True), 'Открываю календарь на Апрель')
        self.assertEqual(functions.showCalendar(False, '5', True), 'Открываю календарь на Май')
        self.assertEqual(functions.showCalendar(False, '6', True), 'Открываю календарь на Июнь')
        self.assertEqual(functions.showCalendar(False, '7', True), 'Открываю календарь на Июль')
        self.assertEqual(functions.showCalendar(False, '8', True), 'Открываю календарь на Август')
        self.assertEqual(functions.showCalendar(False, '9', True), 'Открываю календарь на Сентябрь')
        self.assertEqual(functions.showCalendar(False, '10', True), 'Открываю календарь на Октябрь')
        self.assertEqual(functions.showCalendar(False, '11', True), 'Открываю календарь на Ноябрь')
        self.assertEqual(functions.showCalendar(False, '12', True), 'Открываю календарь на Декабрь')


class JokeTestCase(unittest.TestCase):
    """Test joke finction"""

    def test_joke(self):
        """Test if there is a joke"""
        self.assertTrue(functions.joke(True))


class MoodTestCase(unittest.TestCase):
    """Test mood finction"""

    def test_mood(self):
        """Test if there is a mood"""
        self.assertTrue(functions.mood(False, True))

    def test_mood_answer(self):
        """Test mood answer"""
        self.assertEqual(functions.mood(True, True, 'Хорошо, спасибо, а у вас?', 'хорошо '), 'Это хорошо, '
                                                                                             'что всё хорошо.')
        self.assertEqual(functions.mood(True, True, 'Хорошо, спасибо, а у вас?', 'нормально '),
                         'Главное, что не плохо!')
        self.assertEqual(functions.mood(True, True, 'Хорошо, спасибо, а у вас?', 'плохо '), 'Не расстраивайтесь, '
                                                                                            'по моим подстчетам, уже '
                                                                                            'совсем скоро все наладится.')
        self.assertEqual(functions.mood(True, True, 'Хорошо, спасибо, а у вас?', 'жива '),
                         'Да, ведь и такое случается.')
        self.assertEqual(functions.mood(True, True, 'Что мы все обо мне да обо мне? О себе лучше расскажите - ваши '
                                                    'как дела?', 'хорошо '), 'Это хорошо, что всё хорошо.')
        self.assertEqual(functions.mood(True, True, 'Что мы все обо мне да обо мне? О себе лучше расскажите - ваши '
                                                    'как дела?', 'нормально '), 'Главное, что не плохо!')
        self.assertEqual(functions.mood(True, True, 'Что мы все обо мне да обо мне? О себе лучше расскажите - ваши '
                                                    'как дела?', 'плохо '), 'Не расстраивайтесь, по моим подстчетам, '
                                                                            'уже совсем скоро все наладится.')
        self.assertEqual(functions.mood(True, True, 'Что мы все обо мне да обо мне? О себе лучше расскажите - ваши '
                                                    'как дела?', 'жива '), 'Да, ведь и такое случается.')


class WhatDoYouDoTestCase(unittest.TestCase):
    """Test whatDoYouDo finction"""

    def test_whatDoYouDo(self):
        """Test this function """
        self.assertEqual(functions.whatDoYouDo(True), 'Наслаждаюсь прекрасной компанией.')


class WeatherTestCase(unittest.TestCase):
    """Test weather finction"""

    def test_weather(self):
        """Test different cities"""
        self.assertEqual(functions.weather('погода в городе Москва', True), 'Москва')
        self.assertEqual(functions.weather('Какая сейчас погода в городе Канберра', True), 'Канберра')
        self.assertEqual(functions.weather('погода Осло', True), 'Осло')
        self.assertEqual(functions.weather('Погода сейчас в городе Солт-Лейк-Сити', True), 'Солт-Лейк-Сити')
        self.assertEqual(functions.weather('погода в Минск', True), 'Минск')


class RepeatTestCase(unittest.TestCase):
    """Test repeat finction"""

    def test_repeat_empty(self):
        """Test different expressions to repeat"""
        self.assertEqual(functions.repeat('повтори', True), 'Повторяю молчание. Слушайте:')
        self.assertEqual(functions.repeat('ПОВТОРИ', True), 'Повторяю молчание. Слушайте:')
        self.assertEqual(functions.repeat('Повтори', True), 'Повторяю молчание. Слушайте:')

    def test_repeat_not_empty(self):
        """Test different expressions to repeat"""
        self.assertEqual(functions.repeat('повтори so much depends upon', True), 'So much depends upon. '
                                                                                 'Но вообще-то я не попугай.')
        self.assertEqual(functions.repeat('Повтори пмроанорпмлгп', True), 'Пмроанорпмлгп. Но вообще-то я не попугай.')
        self.assertEqual(functions.repeat('ПОВТОРИ 123', True), '123. Но вообще-то я не попугай.')
        self.assertEqual(functions.repeat('повтори Я лЮбЛю PyThOn', True), 'Я люблю python. Но вообще-то я не попугай.')
        self.assertEqual(functions.repeat('Повтори Gjfnjhb', True), 'Gjfnjhb. Но вообще-то я не попугай.')


class CalculationTestCase(unittest.TestCase):
    """Test calculation finction"""

    def test_calculation_plus(self):
        """Test different plus actions"""
        self.assertEqual(functions.calculation('сколько будет 5 + 7', True), '5 + 7 = 12')
        self.assertEqual(functions.calculation('Сколько будет 555 + 111', True), '555 + 111 = 666')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 123 + 321', True), '123 + 321 = 444')
        self.assertEqual(functions.calculation('сколько будет 44+66', True), '44 + 66 = 110')
        self.assertEqual(functions.calculation('Сколько будет1022+1028', True), '1022 + 1028 = 2050')

        self.assertEqual(functions.calculation('Сколько будет 25 плюс 5', True), '25 + 5 = 30')
        self.assertEqual(functions.calculation('Сколько будет111 плюс 55', True), '111 + 55 = 166')
        self.assertEqual(functions.calculation('Сколько будет100плюс50', True), '100 + 50 = 150')
        self.assertEqual(functions.calculation('Сколько будет123ПЛЮС77', True), '123 + 77 = 200')

        self.assertEqual(functions.calculation('Сколько будет 25 прибавить 5', True), '25 + 5 = 30')
        self.assertEqual(functions.calculation('Сколько будет111 прибавить 55', True), '111 + 55 = 166')
        self.assertEqual(functions.calculation('Сколько будет100прибавить50', True), '100 + 50 = 150')
        self.assertEqual(functions.calculation('Сколько будет123ПРИБАВИТЬ77', True), '123 + 77 = 200')

    def test_calculation_minus(self):
        """Test different minus actions"""
        self.assertEqual(functions.calculation('сколько будет 1 - 1', True), '1 - 1 = 0')
        self.assertEqual(functions.calculation('Сколько будет 22 - 74', True), '22 - 74 = -52')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 555 - 38', True), '555 - 38 = 517')
        self.assertEqual(functions.calculation('сколько будет 56-76', True), '56 - 76 = -20')
        self.assertEqual(functions.calculation('Сколько будет2067-1846', True), '2067 - 1846 = 221')

        self.assertEqual(functions.calculation('Сколько будет 55 минус 62', True), '55 - 62 = -7')
        self.assertEqual(functions.calculation('Сколько будет4 минус 2', True), '4 - 2 = 2')
        self.assertEqual(functions.calculation('Сколько будет487минус329', True), '487 - 329 = 158')
        self.assertEqual(functions.calculation('Сколько будет1349МИНУС4894', True), '1349 - 4894 = -3545')

        self.assertEqual(functions.calculation('Сколько будет 1 отнять 2', True), '1 - 2 = -1')
        self.assertEqual(functions.calculation('Сколько будет77 отнять 55', True), '77 - 55 = 22')
        self.assertEqual(functions.calculation('Сколько будет422отнять321', True), '422 - 321 = 101')
        self.assertEqual(functions.calculation('Сколько будет5098ОтНяТь5098', True), '5098 - 5098 = 0')

    def test_calculation_multiplication(self):
        """Test different multiplication actions"""
        self.assertEqual(functions.calculation('сколько будет 2 х 4', True), '2 х 4 = 8')
        self.assertEqual(functions.calculation('сколько будет 38 х 94', True), '38 х 94 = 3572')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ67 х 33', True), '67 х 33 = 2211')
        self.assertEqual(functions.calculation('Сколько будет 200х1111', True), '200 х 1111 = 222200')
        self.assertEqual(functions.calculation('Сколько будет2867х8568', True), '2867 х 8568 = 24564456')

        self.assertEqual(functions.calculation('Сколько будет 2 умножить на 2', True), '2 х 2 = 4')
        self.assertEqual(functions.calculation('Сколько будет23 умножить на 45', True), '23 х 45 = 1035')
        self.assertEqual(functions.calculation('Сколько будет768умножить на869', True), '768 х 869 = 667392')
        self.assertEqual(functions.calculation('Сколько будет9463УмнОжитЬ нА4802', True), '9463 х 4802 = 45441326')

    def test_calculation_division(self):
        """Test different division actions"""
        self.assertEqual(functions.calculation('сколько будет 5 / 5', True), '5 / 5 = 1')
        self.assertEqual(functions.calculation('Сколько будет 25 / 5', True), '25 / 5 = 5')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 100 / 333', True), '100 / 333 = 0,3')
        self.assertEqual(functions.calculation('сколько будет 72/9', True), '72 / 9 = 8')
        self.assertEqual(functions.calculation('Сколько будет144/12', True), '144 / 12 = 12')

        self.assertEqual(functions.calculation('Сколько будет 6 разделить на 2', True), '6 / 2 = 3')
        self.assertEqual(functions.calculation('Сколько будет20 разделить на 44', True), '20 / 44 = 0,45')
        self.assertEqual(functions.calculation('Сколько будет745разделить на99', True), '745 / 99 = 7,53')
        self.assertEqual(functions.calculation('Сколько будет6666РаЗдЕлИтЬ На1111', True), '6666 / 1111 = 6')

        self.assertEqual(functions.calculation('Сколько будет 10 делить на 5', True), '10 / 5 = 2')
        self.assertEqual(functions.calculation('Сколько будет90 делить на 21', True), '90 / 21 = 4,29')
        self.assertEqual(functions.calculation('Сколько будет534делить на978', True), '534 / 978 = 0,55')
        self.assertEqual(functions.calculation('Сколько будет5709дЕлИтЬ На2546', True), '5709 / 2546 = 2,24')

        self.assertEqual(functions.calculation('Сколько будет 55 поделить на 5', True), '55 / 5 = 11')
        self.assertEqual(functions.calculation('Сколько будет73 поделить на 65', True), '73 / 65 = 1,12')
        self.assertEqual(functions.calculation('Сколько будет123поделить на321', True), '123 / 321 = 0,38')
        self.assertEqual(functions.calculation('Сколько будет8463ПодЕлитЬ нА16926', True), '8463 / 16926 = 0,5')

        self.assertEqual(functions.calculation('сколько будет 5 / 0', True), 'На ноль делить нельзя.')
        self.assertEqual(functions.calculation('Сколько будет 6 разделить на 0', True), 'На ноль делить нельзя.')
        self.assertEqual(functions.calculation('Сколько будет 10 делить на 0', True), 'На ноль делить нельзя.')
        self.assertEqual(functions.calculation('Сколько будет 55 поделить на 0', True), 'На ноль делить нельзя.')

    def test_strange_calculation(self):
        """Test strange calculation actions"""
        self.assertEqual(functions.calculation('сколько будет ', True), 'Безусловно, очень хороший пример.')
        self.assertEqual(functions.calculation('Сколько будет', True), 'Безусловно, очень хороший пример.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 123+', True), 'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ +321', True), 'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 123 + ', True),
                         'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ 123 +', True),
                         'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ + 321', True),
                         'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ +321 ', True),
                         'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ123+', True), 'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ123 +', True), 'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ+ 321', True), 'Мне кажется, что вы недоговорили условие.')
        self.assertEqual(functions.calculation('СКОЛЬКО БУДЕТ+321 ', True), 'Мне кажется, что вы недоговорили условие.')


class OpenProgramTestCase(unittest.TestCase):
    """Test openProgram finction"""

    def test_openProgram(self):
        """Test different programs"""
        self.assertEqual(functions.openProgram('Пожалуйста открой Google Chrome', True), 'Открываю Google Chrome.')
        self.assertEqual(functions.openProgram('открой visual studio', True), 'Открываю Visual Studio.')
        self.assertEqual(functions.openProgram('Открой steam', True), 'Открываю Steam.')
        self.assertEqual(functions.openProgram('открой Пожалуйста access', True), 'Открываю Access.')
        self.assertEqual(functions.openProgram('Открой почту', True), 'Открываю Почту.')

    def test_no_program(self):
        """Test if there is no (such) program"""
        self.assertEqual(functions.openProgram('Пожалуйста открой ', True, True), 'Я умею много чего, но пустоту пока '
                                                                                  'открывать не научилась.')
        self.assertEqual(functions.openProgram('открой', True, True), 'Я умею много чего, но пустоту пока открывать '
                                                                      'не научилась.')
        self.assertEqual(functions.openProgram('Открой Kazam', True, True), 'К сожалению, я не знаю такого приложения.')
        self.assertEqual(functions.openProgram('открой Пожалуйста crunch', True, True), 'К сожалению, я не знаю такого '
                                                                                        'приложения.')
        self.assertEqual(functions.openProgram('Открой Nmap', True, True), 'К сожалению, я не знаю такого приложения.')


class FormattingTextTestCase(unittest.TestCase):
    """Test formattingText finction"""

    def test_formattingText(self):
        """Test text formattion """
        self.assertEqual(functions.formattingText('Привет Вивиан как дела?', True), 'Привет как дела?')
        self.assertEqual(functions.formattingText('Пожалуйста скажи Скажи мне какая столица штата Юта?', True), 'какая столица штата Юта?')
        self.assertEqual(functions.formattingText('viper Kevin vivian Vivern', True), '')
        self.assertEqual(functions.formattingText('Vivian Вивиан вивиан Виверн виверн пожалуйста манго', True), 'манго')
        self.assertEqual(functions.formattingText('Viper vivern Viber viber Мне ирис Kevin kevin', True), 'ирис')
        self.assertEqual(functions.formattingText('', True), '')


class RememberTestCase(unittest.TestCase):
    """Test remember finction"""

    def test_remember(self):
        """Test different """
        adj, rememb = functions.remember('Запомни моя любимая группа Pink Floyd', True)
        self.assertEqual(adj, 'моя')
        self.assertEqual(rememb, 'любимая группа Pink Floyd')
        adj, rememb = functions.remember('запомни мой любимый альбом The Wall', True)
        self.assertEqual(adj, 'мой')
        self.assertEqual(rememb, 'любимый альбом The Wall')
        adj, rememb = functions.remember('Запомни мое любимое произведение Time', True)
        self.assertEqual(adj, 'мое')
        self.assertEqual(rememb, 'любимое произведение Time')

    def test_remember_empty(self):
        """Test empty fact"""
        self.assertEqual(functions.remember('Запомни', True), 'Ничего - мой любимый объект для запоминания.')
        self.assertEqual(functions.remember('запомни ', True), 'Ничего - мой любимый объект для запоминания.')


class BethinkTestCase(unittest.TestCase):
    """Test bethink finction"""

    def test_bethink(self):
        """Test different """
        self.assertEqual(functions.bethink('Как зовут моего кота', True), 'Вашего кота зовут Макс')
        self.assertEqual(functions.bethink('какая моя любимая книга', True), 'Ваша любимая книга Python Crash Course')
        self.assertEqual(functions.bethink('Какая моя любимая группа', True), 'Ваша любимая группа Pink Floyd')
        self.assertEqual(functions.bethink('какой мой любимый сериал', True), 'Ваш любимый сериал Мистер Робот')


class TaskManagerTestCase(unittest.TestCase):
    """Test taskManager finction"""

    def test_tasks(self):
        """Test if there are tasks"""
        self.assertTrue(functions.taskManager('', True, True))

    def test_delitingTask(self):
        """Test delitingTask finction"""
        self.assertEqual(functions.taskManager('удали задачу полить цветы', True), 'полить цветы')
        self.assertEqual(functions.taskManager('удали задачу покормить кота', True), 'покормить кота')
        self.assertEqual(functions.taskManager('удали задачу застелить кровать', True), 'застелить кровать')
        self.assertEqual(functions.taskManager('удали задачу приготовить ужин', True), 'У вас нет такой '
                                                                                       'задачи.')
        self.assertEqual(functions.taskManager('удали задачу сходить в магазин', True), 'У вас нет такой '
                                                                                        'задачи.')


class WebSearchTestCase(unittest.TestCase):
    """Test webSearch finction"""

    def test_webSearch(self):
        """Test different webSearches"""
        self.assertEqual(functions.webSearch('Скажи вивиан почему снег белый', True), 'Почему снег белый')
        self.assertEqual(functions.webSearch('загугли столица ЮАР', True), 'Столица ЮАР')
        self.assertEqual(functions.webSearch('найди годы жизни Бетховена', True), 'Годы жизни Бетховена')
        self.assertEqual(functions.webSearch('Vivian назови семь чудес света', True), 'Семь чудес света')
        self.assertEqual(functions.webSearch('Расскажи новости в сфере Data Sciense', True), 'Новости '
                                                                                             'в сфере Data Sciense')


class ByeTestCase(unittest.TestCase):
    """Test bye finction"""

    def test_bye_different_names(self):
        """Test different names"""
        self.assertEqual(functions.bye('Эндрю', True), 'Уже уходите, Эндрю? Ну что ж, буду с нетерпением вас ждать!')
        self.assertEqual(functions.bye('Эндрю Траск', True), 'Уже уходите, Эндрю Траск? Ну что ж, буду с нетерпением '
                                                             'вас ждать!')
        self.assertEqual(functions.bye('123', True), 'Уже уходите, 123? Ну что ж, буду с нетерпением вас ждать!')
        self.assertEqual(functions.bye('', True), 'Уже уходите, ? Ну что ж, буду с нетерпением вас ждать!')
        self.assertEqual(functions.bye('ghujthjiujh', True), 'Уже уходите, ghujthjiujh? Ну что ж, буду с нетерпением '
                                                             'вас ждать!')


if __name__ == '__main__':
    unittest.main()
