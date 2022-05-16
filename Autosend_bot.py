import main_bot,time,math
import telebot as tl
import datetime as dt


path = r"C:\Users\User\Desktop\Timetable\groups.json"
token='5193810359:AAGL-1z8yCuv9n3vVoxaspCvTh_lCtoxwXk'
bot = tl.TeleBot(token, parse_mode=None)
holiday = [6,7]

    
def message_send():
    data = main_bot.get_groups_dict_from(path)
    ids = []

    for id in data["subscribed"]:  # getting all ids of subscribed students except master's degree
        if main_bot.get_student_group(id)[0] != "M":
            ids.append(id)

    counter=0
    for id in ids:
        counter+=1 
        student_group=main_bot.get_student_group(id)
        g="Group "+student_group[-1]
        nLesson = main_bot._next_index(student_group[:-2],g)
        
        try:
            bot.send_message(id,"#"+nLesson.period+" lesson info: \n ~~ "+nLesson.name+" ~~ \nClassroom: "+nLesson.room+"\nTeacher: "+nLesson.teacher_name)
             
        except:
            today = main_bot._today_index(student_group[:-2],g)
            period = int(main_bot.get_lesson_period()) # инт я вписал просто чтобы если там выдаст дробое число оно станет целым
            try:
                indicator = 0 
                for i in range(1,7):
                    if type(today[period+i]) != str:
                        indicator +=1
            except:
                pass
            if indicator > 0: 
                bot.send_message(id,"#"+ str(math.ceil(main_bot.get_lesson_period()))+ " NO LESSON")

        if counter == len(ids):
            time.sleep(60)     
        
    


def loop():
    while(True):
        if not  dt.datetime.today().isoweekday() in holiday:
            now = dt.datetime.now().strftime("%H:%M")
            if now=="09:57" or now=="11:42" or now=="14:12" or now=="15:57" or now=="17:42" or now=="19:27":
                message_send()
        time.sleep(30)
       
        

loop()