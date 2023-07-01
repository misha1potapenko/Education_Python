text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
             'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
                          'Accusantium alias amet fugit iste neque non odit quiasaepetotamvelit?', ]

text_macarenko = ['В то же время Макаренко хорошо понимал украинский язык (хотя, как отмечал тот же Хиллиг,',
                 ' испытывал определённые трудности, когда Колонию обязали одно время представлять письменные',
                 ' отчёты только на украинском языке) и умело включал отдельные сочные украинизмы в тексты своих',
                 ' произведений. Как свидетельствует один из воспитанников Макаренко по коммуне имени Дзержинского,',
                 ' поляк по происхождению, Леонид Конисевич в своей книге «Нас воспитал Макаренко»,' ,
                 ' Антон Семёнович понимал многие фразы и мог кратко общаться и на польском языке, ',
                 'что выяснилось при приезде польской делегации[8].']


with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text_macarenko))
    f.write('\n')
    for line in text:
        res = f.write(f'{line}\n')
print(f'{res = }\n{len(line) = }')


