import PySimpleGUI as s
import bot_Commands as b
import botfile as f

layout = [[s.Text("Use /help for Commands",text_color='green')],
          [s.InputText("",key='command'),s.Button("Run")],
          [s.Multiline("",key='data',size=(25,20))]
          ]

window = s.Window("Mr.Bot", layout)

while True:
    event, value = window.Read()
    if(f.com(value["command"]) == '/help'):
        s.Popup("\n/bye \n/meaning <word>\n/synonyms <word>\n/antonyms <word>")

    elif((event == "Run")):
        if(f.com(value["command"]) == "/meaning"):
            a = b.meaning(f.word(value['command']))
            window.Element('data').Update(a)
        elif(f.com(value["command"]) == "/synonym"):
            sy = b.synonyms(f.word(value['command']))
            window.Element('data').Update(sy)

        elif (f.com(value["command"]) == "/antonym"):
            an = b.antonyms(f.word(value['command']))
            window.Element('data').Update(an)

        elif (f.com(value["command"]) == "/bye"):
            s.Popup('Thank you for using Mr.bot Bye folks!')
            break

window.Close()

