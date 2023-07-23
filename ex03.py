# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import OrderedDict

text = 'Но все-таки, что же было дальше-то в Москве после того, как в субботний вечер на закате Воланд покинул ' \
       'столицу, исчезнув вместе со своей свитой с Воробьевых гор? О том, что в течение долгого времени по всей ' \
       'столице шел тяжелый гул самых невероятных слухов, очень быстро перекинувшихся и в отдаленные и глухие места ' \
       'провинции, и говорить не приходится, и слухи эти даже тошно повторять. Пишущий эти правдивые строки сам ' \
       'лично, направляясь в Феодосию, слышал в поезде рассказ о том, как в Москве две тысячи человек вышли из театра ' \
       'нагишом в буквальном смысле слова и в таком виде разъехались по домам в таксомоторах. Шепот «Нечистая сила…» ' \
       'слышался в очередях, стоявших у молочных, в трамваях, в магазинах, в квартирах, в кухнях, в поездах, ' \
       'и дачных и дальнего следования, на станциях и полустанках, на дачах и на пляжах. Наиболее развитые и ' \
       'культурные люди в этих рассказах о нечистой силе, навестившей столицу, разумеется, никакого участия не ' \
       'принимали и даже смеялись над ними и пытались рассказчиков образумить. Но факт все-таки, как говорится, ' \
       'остается фактом, и отмахнуться от него без объяснений никак нельзя: кто-то побывал в столице. Уж одни ' \
       'угольки, оставшиеся от Грибоедова, да и многое другое слишком красноречиво это подтверждали. Культурные люди ' \
       'стали на точку зрения следствия: работала шайка гипнотизеров и чревовещателей, великолепно владеющая своим ' \
       'искусством. Меры к ее поимке, как в Москве, так и за пределами ее далеко, были, конечно, приняты немедленные ' \
       'и энергичные, но, к великому сожалению, результатов не дали. Именующий себя Воландом со всеми своими присными ' \
       'исчез и ни в Москву более не возвращался и нигде вообще не появился и ничем себя не проявил. Совершенно ' \
       'естественно, что возникло предположение о том, что он бежал за границу, но и там нигде он не обозначился. ' \
       'Следствие по его делу продолжалось долго. Ведь как-никак, а дело это было чудовищно! Не говоря уже о четырех ' \
       'сожженных домах и о сотнях сведенных с ума людей, были и убитые. О двух это можно сказать точно: о Берлиозе и ' \
       'об этом злосчастном служащем в Бюро по ознакомлению иностранцев с достопримечательностями Москвы, ' \
       'бывшем бароне Майгеле. Ведь они-то были убиты. Обгоревшие кости второго были обнаружены в квартире № 50 по ' \
       'Садовой улице, после того как потушили пожар. Да, были жертвы, и эти жертвы требовали следствия. Но были и ' \
       'еще жертвы, и уже после того, как Воланд покинул столицу, и этими жертвами стали, как это ни грустно, ' \
       'черные коты. Штук сто примерно этих мирных, преданных человеку и полезных ему животных были застрелены или ' \
       'истреблены иными способами в разных местах страны. Десятка полтора котов, иногда в сильно изуродованном виде, ' \
       'были доставлены в отделения милиции в разных городах. Например, в Армавире один из ни в чем не повинных ' \
       'зверей был приведен каким-то гражданином в милицию со связанными передними лапами. Подкараулил этого кота ' \
       'гражданин в тот момент, когда животное с вороватым видом (что же поделаешь, что у котов такой вид? Это не ' \
       'оттого, что они порочны, а оттого, что они боятся, чтобы кто-либо из существ более сильных, чем они,' \
       ' — собаки и люди, — не причинили им какой-нибудь вред или обиду. И то и другое очень нетрудно, но чести в ' \
       'этом, уверяю, нет никакой. Да, нет никакой!), да, так с вороватым видом кот собирался устремиться зачем-то в ' \
       'лопухи. Навалившись на кота и срывая с шеи галстух, чтобы вязать его, гражданин ядовито и угрожающе бормотал: ' \
       '— Ага! Стало быть, теперь к нам, в Армавир, пожаловали, господин гипнотизер? Ну, здесь вас не испугались. Да ' \
       'вы не притворяйтесь немым. Нам уже понятно, что вы за гусь! Вел кота в милицию гражданин, таща бедного зверя ' \
       'за передние лапы, скрученные зеленым галстухом, и добиваясь легкими пинками, чтобы кот непременно шел на ' \
       'задних лапах. — Вы, — кричал гражданин, сопровождаемый свистящими мальчишками, — бросьте, бросьте дурака ' \
       'валять! Не выйдет это! Извольте идти, как все ходят! Черный кот только заводил мученические глаза. Лишенный ' \
       'природой дара слова, он ни в чем не мог оправдаться. Спасением своим бедный зверь обязан в первую очередь — ' \
       'милиции, а, кроме того, своей хозяйке, почтенной старушке-вдове. Лишь только кот был доставлен в отделение, ' \
       'там убедились, что от гражданина сильнейшим образом пахнет спиртом, вследствие чего в показаниях его тотчас ' \
       'же усомнились. А тем временем старушка, узнавшая от соседей, что ее кота замели, кинулась бежать в отделение ' \
       'и поспела вовремя. Она дала самые лестные рекомендации коту, объяснила, что знает его пять лет с тех пор, ' \
       'как он был котенком, ручается за него, как за самое себя, доказала, что он ни в чем плохом не замечен и ' \
       'никогда не ездил в Москву. Как он родился в Армавире, так в нем и вырос и учился ловить мышей. Кот был ' \
       'развязан и возвращен владелице, хлебнув, правда, горя, узнав на практике, что такое ошибка и клевета. Кроме ' \
       'котов, некоторые незначительные неприятности постигли кое-кого из людей. Произошло несколько арестов. В числе ' \
       'других задержанными на короткое время оказались: в Ленинграде — граждане Вольман и Вольпер, в Саратове, ' \
       'Киеве и Харькове — трое Володиных, в Казани — Волох, а в Пензе, и уж совершенно неизвестно почему, — кандидат ' \
       'химических наук Ветчинкевич… Правда, тот был огромного роста, очень смуглый брюнет. Попались в разных местах, ' \
       'кроме того, девять Коровиных, четыре Коровкина и двое Караваевых. Некоего гражданина сняли с севастопольского ' \
       'поезда связанным на станции Белгород. Гражданин этот вздумал развлечь едущих с ним пассажиров карточными ' \
       'фокусами. В Ярославле, как раз в обеденную пору, в ресторан явился гражданин с примусом в руках, который он ' \
       'только что взял из починки. Двое швейцаров, лишь только увидели его, бросили свои посты в раздевалке и ' \
       'бежали, а за ними бежали из ресторана все посетители и служащие. При этом у кассирши непонятным образом ' \
       'пропала вся выручка. Было еще многое, всего не вспомнишь. Было большое брожение умов. Еще и еще раз нужно ' \
       'отдать справедливость следствию. Все было сделано не только для того, чтобы поймать преступников, ' \
       'но и для того, чтобы объяснить все то, что они натворили. И все это было объяснено, и объяснения эти нельзя ' \
       'не признать и толковыми и неопровержимыми. Представители следствия и опытные психиатры установили, ' \
       'что члены преступной шайки или, может быть, один из них (преимущественно подозрение в этом падало на ' \
       'Коровьева) являлись невиданной силы гипнотизерами, могущими показывать себя не в том месте, где они на самом ' \
       'деле находились, а на позициях мнимых, смещенных. Помимо этого, они свободно внушали столкнувшимся с ними, ' \
       'что некие вещи или люди находятся там, где на самом деле их не было, и наоборот, удаляли из поля зрения те ' \
       'вещи или людей, которые действительно в этом поле зрения имелись. В свете таких объяснений решительно все ' \
       'понятно, и даже наиболее волновавшая граждан, ничем, казалось бы не объяснимая неуязвимость кота, ' \
       'обстрелянного в квартире № 50, при попытках взять его под стражу. Никакого кота на люстре, натурально, ' \
       'не было, никто и не думал отстреливаться, стреляли по пустому месту, в то время как Коровьев, внушивший, ' \
       'что кот безобразничает на люстре, мог свободно находиться за спиной стрелявших, кривляясь и наслаждаясь своею ' \
       'громадной, но преступно использованной способностью внушать. Он же, конечно, и поджег квартиру, ' \
       'разлив бензин. Ни в какую Ялту, конечно, Степа Лиходеев не улетал (такая штука не под силу даже Коровьеву) и ' \
       'телеграмм оттуда не посылал. После того, как он упал в обморок в ювелиршиной квартире, испуганный фокусом ' \
       'Коровьева, показавшего ему кота с маринованным грибом на вилке, он пролежал в ней до тех пор, пока Коровьев, ' \
       'издеваясь над ним, не напялил на него войлочную шляпу и не отправил его на московский аэродром, ' \
       'внушив предварительно встречавшим Степу представителям угрозыска, что Степа вылезет из аэроплана, ' \
       'прилетевшего из Севастополя. Правда, угрозыск Ялты утверждал, что он принимал босого Степу и телеграммы ' \
       'насчет Степы в Москву слал, но ни одной копии этих телеграмм в делах никак не обнаружилось, из чего был ' \
       'сделан печальный, но совершенно несокрушимый вывод, что гипнотизерская банда обладает способностью ' \
       'гипнотизировать на громадном расстоянии, и притом не только отдельных лиц, но и целые группы их. При этих ' \
       'условиях преступники могли свести с ума людей с самой стойкой психической организацией. Что там говорить о ' \
       'таких пустяках, как колода карт в чужом кармане в партере, или исчезнувшие дамские платья, или мяукающий ' \
       'берет и прочее в этом же роде! Такие штуки может отколоть любой профессионал-гипнотизер средней силы на любой ' \
       'сцене, в том числе и нехитрый фокус с оторванием головы у конферансье. Говорящий кот — тоже сущий вздор. Для ' \
       'того чтобы предъявить людям такого кота, достаточно владеть первыми основами чревовещания, а вряд ли ' \
       'кто-нибудь усомнится в том, что искусство Коровьева шло значительно дальше этих основ. Да, дело тут вовсе не ' \
       'в колодах, фальшивых письмах в портфеле Никанора Ивановича. Это все пустяки. Это он, Коровьев, погнал под ' \
       'трамвай Берлиоза на верную смерть. Это он свел с ума бедного поэта Ивана Бездомного, он заставлял его грезить ' \
       'и видеть в мучительных снах древний Ершалаим и сожженную солнцем безводную Лысую Гору с тремя повешенными на ' \
       'столбах. Это он и его шайка заставили исчезнуть из Москвы Маргариту Николаевну и ее домработницу Наташу. ' \
       'Кстати: этим делом следствие занималось особенно внимательно. Требовалось выяснить, были ли похищены эти ' \
       'женщины шайкой убийц и поджигателей или же бежали вместе с преступной компанией добровольно? Основываясь на ' \
       'нелепых и путаных показаниях Николая Ивановича и приняв во внимание странную и безумную записку Маргариты ' \
       'Николаевны, оставленную мужу, записку, в которой она пишет, что уходит в ведьмы, учтя то обстоятельство, ' \
       'что Наташа исчезла, оставив все свои носильные вещи на месте, — следствие пришло к заключению, что и хозяйка ' \
       'и домработница были загипнотизированы, подобно многим другим, и в таком виде похищены бандой. Возникла и, ' \
       'вероятно, совершенно правильная мысль, что преступников привлекла красота обеих женщин. Но вот что осталось ' \
       'совершенно неясным для следствия — это побуждение, заставившее шайку похитить душевнобольного, именующего ' \
       'себя мастером, из психиатрической клиники. Этого установить не удалось, как не удалось добыть и фамилию ' \
       'похищенного больного. Так и сгинул он навсегда под мертвой кличкой: «Номер сто восемнадцатый из первого ' \
       'корпуса». Итак, почти все объяснилось, и кончилось следствие, как вообще все кончается. Прошло несколько лет, ' \
       'и граждане стали забывать и Воланда, и Коровьева, и прочих. Произошли многие изменения в жизни тех, ' \
       'кто пострадал от Воланда и его присных, и как бы ни были мелки и незначительны эти изменения, все же следует ' \
       'их отметить. Жорж, например, Бенгальский, проведя в лечебнице три месяца, поправился и вышел, но службу в ' \
       'Варьете вынужден был покинуть, и в самое горячее время, когда публика валом шла за билетами — память о черной ' \
       'магии и ее разоблачениях оказалась очень живуча. Бросил Бенгальский Варьете, ибо понимал, что представать ' \
       'ежевечерне перед двумя тысячами человек, быть неизбежно узнаваемым и бесконечно подвергаться глумливым ' \
       'вопросам о том, как ему лучше: с головой или без головы? — слишком мучительно. Да, кроме того, ' \
       'утратил конферансье значительную дозу своей веселости, которая столь необходима при его профессии. Осталась у ' \
       'него неприятная, тягостная привычка каждую весну в полнолуние впадать в тревожное состояние, ' \
       'внезапно хвататься за шею, испуганно оглядываться и плакать. Припадки эти проходили, но все же при наличности ' \
       'их прежним делом нельзя было заниматься, и конферансье ушел на покой и начал жить на свои сбережения, ' \
       'которых, по его скромному подсчету, должно было хватить ему на пятнадцать лет. Он ушел и никогда больше не ' \
       'встречался с Варенухой, приобревшим всеобщую популярность и любовь за свою невероятную, даже среди ' \
       'театральных администраторов, отзывчивость и вежливость. Контрамарочники, например, его иначе не называли, ' \
       'как отец-благодетель. В какое бы время, кто бы ни позвонил в Варьете, всегда слышался в трубке мягкий, ' \
       'но грустный голос: «Я вас слушаю», — а на просьбу позвать к телефону Варенуху, тот же голос поспешно отвечал: ' \
       '«Я к вашим услугам». Но зато и страдал же Иван Савельевич от своей вежливости! Степе Лиходееву больше не ' \
       'приходится разговаривать по телефону в Варьете. Немедленно после выхода из клиники, в которой Степа провел ' \
       'восемь дней, его перебросили в Ростов, где он получил назначение на должность заведующего большим ' \
       'гастрономическим магазином. Ходят слухи, что он совершенно перестал пить портвейн и пьет только водку, ' \
       'настоянную на смородиновых почках, отчего очень поздоровел. Говорят, что стал молчалив и сторонится женщин. ' \
       'Удаление Степана Богдановича из Варьете не доставило Римскому той радости, о которой он так жадно мечтал в ' \
       'продолжение нескольких лет. После клиники и Кисловодска старенький-престаренький, с трясущейся головой, ' \
       'финдиректор подал заявление об уходе из Варьете. Интересно то, что это заявление привезла в Варьете супруга ' \
       'Римского. Сам Григорий Данилович не нашел в себе силы даже днем побывать в том здании, где видел он залитое ' \
       'луной треснувшее стекло в окне и длинную руку, пробирающуюся к нижней задвижке. Уволившись из Верьете, ' \
       'финдиректор поступил в театр детских кукол в Замоскворечье. В этом театре ему уже не пришлось сталкиваться по ' \
       'делам акустики с почтеннейшим Аркадием Аполлоновичем Семплеяровым. Того в два счета перебросили в Брянск и ' \
       'назначили заведующим грибнозаготовочным пунктом. Едят теперь москвичи соленые рыжики и маринованные белые и ' \
       'не нахвалятся ими и до чрезвычайности радуются этой переброске. Дело прошлое, и можно сказать, ' \
       'что не клеились у Аркадия Аполлоновича дела с акустикой, и сколько ни старался он улучшить ее, ' \
       'она какая была, такая и осталась. К числу лиц, порвавших с театром, помимо Аркадия Аполлоновича, ' \
       'надлежит отнести и Никанора Ивановича Босого, хоть тот и не был ничем связан с театрами, кроме любви к ' \
       'даровым билетам. Никанор Иванович не только не ходит ни в какой театр ни за деньги, ни даром, ' \
       'но даже меняется в лице при всяком театральном разговоре. В не меньшей, а в большей степени возненавидел он, ' \
       'помимо театра, поэта Пушкина и талантливого артиста Савву Потаповича Куролесова. Того — до такой степени, ' \
       'что в прошлом году, увидев в газете окаймленное черным объявление о том, что Савву Потаповича в самый расцвет ' \
       'его карьеры хватил удар, — Никанор Иванович побагровел до того, что сам чуть не отправился вслед за Саввой ' \
       'Потаповичем, и взревел: «Так ему и надо!» Более того, в тот же вечер Никанор Иванович, на которого смерть ' \
       'популярного артиста навеяла массу тягостных воспоминаний, один, в компании только с полной луной, освещающей ' \
       'Садовую, напился до ужаса. И с каждой рюмкой удлинялась перед ним проклятая цепь ненавистных фигур, ' \
       'и были в этой цепи и Дунчиль Сергей Герардович, и красотка Ида Геркулановна, и тот рыжий владелец бойцовых ' \
       'гусей, и откровенный Канавкин Николай. Ну, а с теми-то что же случилось? Помилуйте! Ровно ничего с ними не ' \
       'случилось, да и случиться не может, ибо никогда в действительности не было их, как не было и симпатичного ' \
       'артиста-конферансье, и самого театра, и старой сквалыги Пороховниковой тетки, гноящей валюту в погребе, и уж, ' \
       'конечно, золотых труб не было и наглых поваров. Все это только снилось Никанору Ивановичу под влиянием ' \
       'поганца Коровьева. Единственный живой, влетевший в этот сон, именно и был Савва Потапович — артист, ' \
       'и ввязался он в это только потому, что врезался в память Никанору Ивановичу благодаря своим частым ' \
       'выступлениям по радио. Он был, а остальных не было. Так, может быть, не было и Алоизия Могарыча? О, ' \
       'нет! Этот не только был, но и сейчас существует, и именно в той должности, от которой отказался Римский, ' \
       'то есть в должности финдиректора Варьете. Опомнившись, примерно через сутки после визита к Воланду, в поезде, ' \
       'где-то под Вяткой, Алоизий убедился в том, что, уехав в помрачении ума зачем-то из Москвы, он забыл надеть ' \
       'брюки, но зато непонятно для чего украл совсем ненужную ему домовую книгу застройщика. Уплатив колоссальные ' \
       'деньги проводнику, Алоизий приобрел у него старую и засаленную пару штанов и из Вятки повернул обратно. Но ' \
       'домика застройщика он, увы, уже не нашел. Ветхое барахло начисто слизнуло огнем. Но Алоизий был человеком ' \
       'чрезвычайно предприимчивым, через две недели он уже жил в прекрасной комнате в Брюсовском переулке, ' \
       'а через несколько месяцев уже сидел в кабинете Римского. И как раньше Римский страдал из-за Степы, ' \
       'так теперь Варенуха мучился из-за Алоизия. Мечтает теперь Иван Савельевич только об одном, чтобы этого ' \
       'Алоизия убрали из Варьете куда-нибудь с глаз долой, потому что, как шепчет иногда Варенуха в интимной ' \
       'компании, «такой сволочи, как этот Алоизий, он будто бы никогда не встречал в жизни и что будто бы от этого ' \
       'Алоизия он ждет всего, чего угодно». Впрочем, может быть, администратор и пристрастен. Никаких темных дел за ' \
       'Алоизием не замечено, как и вообще никаких дел, если не считать, конечно, назначения на место буфетчика ' \
       'Сокова какого-то другого. Андрей же Фокич умер от рака печени в клинике Первого МГУ месяцев через девять ' \
       'после появления Воланда в Москве…'

cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
words = cleaned_text.split()
print(f'В тексте всего {len(words)} слов')
word_counts = {}
for i in words:
    if i not in word_counts:
        word_counts[i] = words.count(i)

sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)
print(f'10 самых часто встречающихся слов: {sorted_words[:10:]}')

