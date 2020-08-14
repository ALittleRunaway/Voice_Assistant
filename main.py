"""The main file for Voice Assistant"""
import functions

tree, root = functions.xmlParsing()
name = root[3].text # Check if there is a name in the file

if name is None:  # If there is no name
    name = functions.firstGreeting() # If there is no connection, 'name' is like flag 'Active' here
    root[3].text = name # Ask for it and write it in the filee
    tree.write('text/configuration.xml', encoding='utf-8')
    functions.firstGreeting2(name)
else:  # If there is
    functions.greeting(name)

while True:  # Send the text to processing
    text = functions.getVoice()
    text = text + ' '

    ########## SERTAIN QUESTION ##########

    #
    if (('что ' in text.lower()) and ('умеешь ' in text.lower())):
        functions.info()
    #
    elif ('помощь ' in text.lower()) or ('справка ' in text.lower()):
        functions.helping()
    #
    elif (('моё ' in text.lower()) and ('имя ' in text.lower())) or (
            ('меня ' in text.lower()) and ('зовут ' in text.lower())):
        functions.yourNameIs(name)
    #
    elif ('время ' in text.lower()) or ('времени ' in text.lower()) or (
            ('который ' in text.lower()) and ('час ' in text.lower())):
        functions.timeNow()
    #
    elif (('сегодня ' in text.lower()) and (
            ('день ' in text.lower()) or ('дата ' in text.lower()) or ('число ' in text.lower()))):
        functions.dateNow()
    #
    elif ('анекдот ' in text.lower()) or ('шутку ' in text.lower()) or (
            ('рассмеши ' in text.lower()) and ('меня ' in text.lower())):
        functions.joke()
    #
    elif (('погода ' in text.lower()) or ('погоду ' in text.lower())):
        functions.weather(text)
    #
    elif ('календарь ' in text.lower()):
        if ('год ' in text.lower()):
            functions.showCalendar(True)
        else:  # Month and everything else
            functions.showCalendar(False)
    #
    elif ('очисти ' in text.lower()) or ('сотри ' in text.lower()) or ('очистить ' in text.lower()):
        functions.os.system('cls')
    #
    elif ('подожди ' in text.lower()):
        functions.wait()
    #
    elif ('настроение ' in text.lower()) or (('как ' in text.lower()) and ('дела ' in text.lower())) or (
            ('как ' in text.lower()) and ('жизнь ' in text.lower())):
        functions.mood()
    #
    elif ('найди ' in text.lower()) or ('загугли ' in text.lower()):
        functions.webSearch(text)
    #
    elif ('задач' in text.lower()):
        functions.taskManager(text)
    #
    elif ('повтори ' in text.lower()):
        functions.repeat(text)
    #
    elif ('открой ' in text.lower()):
        functions.openProgram(text)
    #
    elif ('запомни ' in text.lower()):
        functions.remember(text)
    #
    elif ('посчитай ' in text.lower()) or (('сколько ' in text.lower()) and ('будет ' in text.lower())):
        functions.calculation(text)
    #
    elif (('чем ' in text.lower()) and ('занимаешься ' in text.lower())) or (
            ('что ' in text.lower()) and ('делаешь ' in text.lower())):
        functions.whatDoYouDo()
    #
    elif ('пока ' in text.lower()) or ('прощай ' in text.lower()) or (('мне ' in text.lower())) and (
            ('пора ' in text.lower())):
        functions.bye(name)
        break
    #
    elif text == ' ':
        functions.time.sleep(3)
        continue
    #
    elif ('как' in text.lower()):
        functions.bethink(text)
    #
    else:
        functions.webSearch(text)

    functions.time.sleep(3)
