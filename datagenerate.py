# need to create bulk and single folder to store data
#creates all 6 files at a time

import random
import datetime
Names = ['Andrei Eller', 'Sherry Halbert', 'Lib Corkhill', 'Kaylee Rabjohn',
       'Duke De Few', 'Millisent Greenard', 'Nanny Arstall',
       'Larine Tanswell', 'Ericha Ballance', 'Katha Heads',
       'Karee Bentinck', 'Celisse Boniface', 'Lianna Spikings',
       'Darbee Chimienti', 'Matilde Mulcock', 'Artemus Crumb',
       'Raimondo Von Helmholtz', 'Cleo Clementucci', 'Kelbee Layson',
       'Waneta Burder', 'Melly Luckin', "Arly O Hara", 'Trstram Nichols',
       'Ruthi Joysey', 'Lewie Kilrow', 'Maryanna Macklam', 'Thor Tenant',
       'Harmonie Milnes', 'Oralie Coll', 'Cornela Shorie',
       'Karalynn De Micoli', 'Symon Weal', 'Carrol Handaside',
       'Jeramie Botte', 'Kit Magor', 'Bamby Dowglass', 'Clemmie Cinelli',
       'Demetria Quantrill', 'Pegeen Eefting', 'Borg Heminsley',
       'Stella Gailor', 'Charita Sheards', 'Ignaz Wyatt', 'Ralina Lyness',
       'Melitta Annandale', 'Janos Stit', 'Margaretha Lindenblatt',
       'Baxie Downing', 'Cleon Theodoris', 'Diannne Petrazzi',
       'Cooper Donaghy', 'Moyna Josifovic', 'Vania Goalby',
       'Creight Gooding', 'Ricki Grierson', 'Berna Myrie', 'Olia Yearne',
       'Valaria Ligoe', 'Alyosha Bright', 'Winni Brecken',
       'Tammara Sutcliff', 'Ravi Nuzzi', 'Isa Tindley', 'Arlene Slym',
       'Sally Orrin', 'Mead Yetton', 'Nicky Scantlebury', 'Winny Croome',
       'Merrili Pristnor', 'Beaufort Bellard', 'Leonidas Synke',
       'Debi Medmore', 'Karlens Gott', 'Augustin Witt', 'Norry Delacroix',
       'Alvis Clohessy', 'Dmitri Sieve', 'Hayley Northeast',
       'Bernhard MacDonough', 'Allen Espy', 'Nikolaos Rodbourne',
       'Horatia Dwerryhouse', 'Daune McEachern', 'Ailbert Hubbocks',
       'Joscelin Duiguid', 'Tommy Dwelley', 'Isabella Matus',
       'Gilda Staries', 'Luise Braikenridge', 'Cirillo Spellissy',
       'Barthel De Marchi', 'Malina Hellier', 'Dode Hassen',
       'Warner Aloshikin', 'Carmen Lynch', 'Bettina McClaughlin',
       'Celestina Vasnetsov', 'Kerrill Mallison', 'Humfrid Lanfare',
       'Symon Hamlin', 'Ricki Varfolomeev', 'Krystle Tower',
       'Nobie Lohden', 'Sophi Sterley', 'Kinnie Althrop', 'Sky Tonkin',
       'Bunni Tittershill', 'Elfie Menendes', 'Bobbie Vankeev',
       'Ives Huguet', 'Antonella Pain', 'Abdel Fitzhenry',
       'Rafaelia Wornham', 'Amanda Meredyth', 'Shauna Barsam',
       'Umberto Johnsey', 'Tim Minmagh', 'Westleigh Gaskamp',
       'Sharron Pierse', 'Clywd Pinniger', 'Hubie Kinner',
       'Isadora Pitcaithley', 'Roch Sennett', 'Osbourne Goodbanne',
       'Yuma Pengilly', 'Haven Trimnell', 'Olivie Baylie',
       'Clayton Cattlow', 'Theodor Featherstone', 'Neddie Flemyng',
       'Farrell Francescuzzi', 'Hymie Swettenham', 'Kevan Calender',
       'Osgood Forsey', 'Carlynne Edwicke', 'Corey Fairs', 'Denis Vials',
       'Alexina Dumbelton', 'Renae Crimpe', 'Broderick Libri',
       'Winifred Alessandone', 'Vivien Kyncl', 'Clarita Brisard',
       'Durant Englishby', 'Owen Lemmens', 'Mary Wheble', 'Arte Belison',
       'Cliff Adam', 'Rurik Knocker', 'Andy Tefft',
       'Barbara-anne Bradbeer', 'Trisha Vannucci', 'Lida Handrok',
       'Bran Leser', 'Merissa Mawman', 'Linc Gypson', 'Luce Falco',
       'Chrissy Scardefield', 'Tiertza Foy', 'Simonne Kettle',
       'Osmund Hardes', 'Bowie Linklet', 'Silvie McAllen',
       'Doralin Recke', 'Roma Gally', 'Alick Rhule', 'Tibold Tregido',
       'Agathe Scintsbury', 'Doyle Beacroft', 'Sibyl Pitson',
       'Ruddie Brumble', 'Marcus Philpin', 'Bryant Bode',
       'Ernesta Clapperton', 'Scot Hubball', 'Jodi Grutchfield',
       'Monty Eccleston', 'Ryley Curless', 'Hermann Brownsell',
       'Eleni Metschke', 'Justinian Devenport', 'Jania Charlot',
       'Lauraine Lengthorn', 'Gae Buffham', 'Rozele Bradfield',
       'Lola Colebrook', 'Bennett Crome', 'Carolee Schrei',
       'Lelia Trevor', 'Thebault Smiley', 'Reginauld Olyfat',
       'Melosa Kliner', 'Bride Langland', 'Freeman Writer',
       'Meg Walworche', 'Taylor Romushkin', 'Mirabelle Erricker',
       'Fabien Caurah', 'Courtenay Rudram']

Stadiums = ['Seattle Stadium', 'Gangkoujie Stadium', 'Mounlapamôk Stadium',
       'Luoxiong Stadium', 'Ugljan Stadium', 'Goteborg Stadium',
       'Chiang Yuen Stadium', 'Popayán Stadium', 'Martinlongo Stadium',
       'Kangān Stadium', 'Bolshoy Karay Stadium', 'Jadowniki Stadium',
       'Donglinxi Stadium', 'Rēzekne Stadium', 'Riti Stadium',
       'Lappajärvi Stadium', 'Ōtsuki Stadium',
       "Les Sables-d Olonne Stadium", 'Arkalyk Stadium',
       'Rakičan Stadium', 'Pākpattan Stadium', 'Krajan Stadium',
       'Karangbayat Stadium', 'Foros de Salvaterra Stadium',
       'Smyshlyayevka Stadium', 'Ô Môn Stadium', 'Ōzu Stadium',
       'Tafí del Valle Stadium', 'Brckovljani Stadium', 'Tacheng Stadium',
       'Alae Stadium', 'Tlogosadang Stadium', 'Yiyang Stadium',
       'Bảo Lộc Stadium', 'Quankou Stadium', 'Kamen’-na-Obi Stadium',
       'La Caya Stadium', 'Reims Stadium', 'Fulin Stadium',
       'Gueset Stadium', 'Bressuire Stadium', 'Pagnag Stadium',
       'Yingjiang Stadium', 'Aix-les-Bains Stadium',
       'Novorossiysk Stadium', 'Nisí Stadium', 'Banyue Stadium',
       'Iwakura Stadium', 'Nardaran Stadium', 'Mönhbulag Stadium',
       'Tinaco Stadium', 'Jiexiu Stadium', 'Kondrovo Stadium',
       'Baihe Stadium', 'Singa Stadium', 'Zhangjiang Stadium',
       'Usarin Stadium', 'Lipinki Łużyckie Stadium', 'Besteiros Stadium',
       'Frýdek-Místek Stadium', 'Yanchi Stadium', 'San Andres Stadium',
       'Huangkeng Stadium', 'Lopatinskiy Stadium', 'Doubrava Stadium',
       'Jagodnjak Stadium', 'Krzepice Stadium', 'Gogaran Stadium',
       'Pugeran Stadium', 'Bayt Ūr at Taḩtā Stadium', 'Aso Stadium',
       'Kota Kinabalu Stadium', 'Providence Stadium', 'Balai Stadium',
       'Pandean Stadium', 'Jinxiang Stadium', 'Martil Stadium',
       'Tambong Stadium', 'Áno Kastrítsion Stadium', 'Kurba Stadium',
       'Hetian Stadium', 'Peñarrubia Stadium', 'Xiaozhi Stadium',
       'Wanareja Stadium', 'Tres Arroyos Stadium', 'Dali Stadium',
       'Volgo-Kaspiyskiy Stadium', 'Xiabao Stadium', 'Yumbel Stadium',
       'Cikujang Stadium', 'Plumtree Stadium', 'Bugembe Stadium',
       'San Jose Stadium', 'Vairão Stadium', 'Kushovë Stadium',
       'Lalauigan Stadium', 'Harstad Stadium', 'Sibiti Stadium',
       'Severo-Yeniseyskiy Stadium', 'Lyambir’ Stadium',
       'Embalse Stadium', 'Hopetown Stadium', 'Huangbei Stadium',
       'Tyoply Stan Stadium', 'Reguengos de Monsaraz Stadium',
       'Сарај Stadium', 'Ayorou Stadium', 'Nieying Stadium',
       'KwaMbonambi Stadium', 'Portland Stadium', 'Fradelos Stadium',
       'Acacías Stadium', 'Semikarakorsk Stadium', 'Huayuan Stadium',
       'Madrid Stadium', 'Quinarayan Stadium', 'Sangzhen Stadium',
       'Menuma Stadium', 'Peterhof Stadium', 'Zhongshan Donglu Stadium',
       'Palcamayo Stadium', 'Muff Stadium', 'San Rafael Stadium',
       'Moppo Stadium', 'Íasmos Stadium', 'Monção Stadium',
       'Taesal-li Stadium', 'Nanyulinxi Stadium', 'Alikalia Stadium',
       'Mojoroto Stadium', 'Staraya Toropa Stadium',
       'Burhānuddin Stadium', 'Leworook Stadium', 'Seaton Stadium',
       'Pácora Stadium', 'Kasina Wielka Stadium', 'Novaya Igirma Stadium',
       'Qi’an Stadium', 'Karlskrona Stadium', 'Ginowan Stadium',
       'Portelândia Stadium', 'Banī an Nahārī Stadium',
       'Saint-Quentin Stadium', 'Bantal Stadium', 'Germiston Stadium',
       'Stuttgart Stadium', 'Catache Stadium', 'Belén Stadium',
       'Panorama Stadium', 'Kainantu Stadium', 'Jönköping Stadium',
       'Choros Stadium', 'Ivanovskoye Stadium', 'Esperanza Stadium',
       'Nambalan Stadium', 'Kieta Stadium', 'Youxi Chengguanzhen Stadium',
       'Raofeng Stadium', 'Kefang Stadium', 'Zrenjanin Stadium',
       'Sivers’k Stadium', 'Lagny-sur-Marne Stadium', 'Ar Ruţbah Stadium',
       'Yaroslavskiy Stadium', 'Yangshan Stadium', 'Rahayu Dua Stadium',
       'Holboo Stadium', 'Gugut Stadium', 'Dayu Stadium',
       'Lawepakam Stadium', 'Zhanghuban Stadium', 'Sibreh Stadium',
       'Mangas Stadium', 'Bagalangit Stadium', 'Bogorame Stadium',
       'Padre Las Casas Stadium', 'Las Vegas Stadium', 'Shaxi Stadium',
       'Pakenjeng Stadium', 'Caen Stadium', 'Houndé Stadium',
       'Bánov Stadium', 'Villejuif Stadium', 'Dehui Stadium',
       'Sudoměřice Stadium', 'Nubl Stadium', 'Arivonimamo Stadium',
       'Zhangcun Stadium', 'Murça Stadium', 'Ramon’ Stadium',
       'Hoorn Stadium', 'María la Baja Stadium', 'Nansan Stadium',
       'Shadrinsk Stadium', 'Xiekou Stadium', 'Calinaoan Malasin Stadium',
       'Xinyang Stadium', 'La Libertad Stadium', 'Paungde Stadium',
       'Besançon Stadium']

Teamname = ['Twinte', 'Jaxnation', 'Abata', 'Bubbletube', 'Kazu', 'Feednation',
       'Eire', 'Wordpedia', 'Skaboo', 'Jamia', 'Photospace', 'Skiba',
       'Minyx', 'Topicshots', 'Brainsphere', 'Aivee', 'Tanoodle',
       'Bubblebox', 'Zoombox', 'Trilia', 'Lazzy', 'Viva', 'Trunyx',
       'Mita', 'Topiczoom', 'Wordware', 'Fadeo', 'Mudo', 'Linktype',
       'Chatterbridge', 'Linkbuzz', 'Dablist', 'Skiba', 'Janyx', 'Twinte',
       'Kare', 'Aimbo', 'Lazzy', 'Avavee', 'Kimia', 'Fliptune', 'Voonder',
       'Tavu', 'Yodel', 'Tagcat', 'Kazio', 'Roomm', 'Avamm', 'Jamia',
       'Brightdog', 'Feedbug', 'Roombo', 'Mymm', 'Twinte', 'Muxo',
       'Jabberstorm', 'Zoomdog', 'Vipe', 'Wordify', 'Jatri', 'Yotz',
       'Youopia', 'Riffpedia', 'Browsecat', 'Vitz', 'Latz',
       'Thoughtbridge', 'Blogspan', 'Kimia', 'Bluezoom', 'Photolist',
       'Centimia', 'Skyble', 'Jatri', 'Yata', 'Browsetype', 'Edgetag',
       'Eire', 'Photobug', 'Skidoo', 'Topicware', 'Agivu', 'Youtags',
       'Edgetag', 'Teklist', 'Vimbo', 'Thoughtbeat', 'Twinte', 'Viva',
       'Tekfly', 'Jetwire', 'Skinte', 'Wikizz', 'Abata', 'Centimia',
       'Zooxo', 'Babbleopia', 'Brainverse', 'Browseblab', 'Voonte',
       'Meevee', 'Tagpad', 'Pixonyx', 'Skalith', 'Divanoodle', 'Dynava',
       'Fliptune', 'Yakidoo', 'Meevee', 'Centidel', 'Tambee', 'Eimbee',
       'Divanoodle', 'Lazz', 'Realmix', 'Eare', 'Twiyo', 'Topicstorm',
       'Devshare', 'Wordify', 'Mudo', 'Midel', 'Youspan', 'Agivu',
       'Thoughtbeat', 'Browsezoom', 'Twinder', 'Linkbuzz', 'Mynte',
       'Zoomzone', 'Zoonder', 'Realblab', 'Fadeo', 'Trilia',
       'Thoughtstorm', 'Eamia', 'Eamia', 'Blognation', 'Topicware',
       'Browsedrive', 'Skivee', 'Dabshots', 'Leenti', 'Jabbersphere',
       'Agimba', 'Linkbuzz', 'Bubblebox', 'Mymm', 'Eare', 'Gabcube',
       'Photobug', 'Realmix', 'Pixonyx', 'Mynte', 'Ntags', 'Wordware',
       'Feedbug', 'Quimba', 'Dabjam', 'Twitterwire', 'Gabvine',
       'Youbridge', 'Yata', 'Centimia', 'Realpoint', 'Oodoo', 'Quinu',
       'Browsezoom', 'Zoozzy', 'Zooxo', 'Quatz', 'Tagopia', 'Topicshots',
       'Zoomdog', 'Jabbertype', 'Nlounge', 'Jabbertype', 'Kwilith',
       'Skipfire', 'Mydeo', 'Plajo', 'Thoughtsphere', 'Kimia',
       'Shuffletag', 'Kazio', 'Tavu', 'Kimia', 'Geba', 'Skyvu',
       'Flashset', 'Yoveo', 'Zooxo', 'Zazio', 'Trudeo', 'Podcat',
       'Kayveo', 'Vidoo', 'Jayo', 'InnoZ', 'Photofeed']

Position = ['WR','RB','QB']
Touchdowns = [i for i in range(50,300,5)]
Totalyards =[i for i in range(300,1000,25)]
Salary = [i*1000 for i in range(50,400,10)]
Result = ['W','L','T']
Attendance =[i for i in range(500,4000)]
start = datetime.datetime.strptime("2014-01-20", "%Y-%m-%d")
end = datetime.datetime.strptime("2018-12-25", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dates =[]
for date in date_generated:
    dates.append(date.strftime("%Y-%m-%d"))
TicketRevenue =[i for i in range(50000,4000000,10000)]
#input number of tuble and file extension number
size = int(input("enter number of tuples: "))
ext = input("enter extension for file: ")
filename = 'bulk/games'+ext+'.txt'
with open(filename,"w") as file:
    for i in range(1,size+1):
        file.write(str(i)+",")
        file.write(str(random.choice(dates))+",")
        file.write(random.choice(Stadiums)+",")
        file.write(random.choice(Result)+",")
        file.write(str(random.choice(Attendance))+",")
        file.write(str(random.choice(TicketRevenue)))
        file.write("\r\n")

filename1 ='single/games'+ext+'.txt'
with open(filename1,"w") as file:
    for i in range(1,size+1):
        file.write(str(i)+",")
        file.write("'"+random.choice(dates)+"',")
        file.write("'"+random.choice(Stadiums)+"',")
        file.write("'"+random.choice(Result)+"',")
        file.write(str(random.choice(Attendance))+",")
        file.write(str(random.choice(TicketRevenue)))
        file.write("\r\n")


filename = 'single/players'+ext+'.txt'
with open(filename,"w") as file:
    for i in range(1,size+1):
        file.write("'"+random.choice(Names)+"',")
        file.write(str(i+800000000)+",")
        file.write("'"+random.choice(Teamname)+"',")
        file.write("'"+random.choice(Position)+"',")
        file.write(str(random.choice(Touchdowns))+",")
        file.write(str(random.choice(Totalyards))+",")
        file.write(str(random.choice(Salary)))
        file.write("\r\n")

filename1 = 'bulk/players'+ext+'.txt'
with open(filename1,"w") as file:
    for i in range(1,size+1):
        file.write(random.choice(Names)+",")
        file.write(str(i+800000000)+",")
        file.write(random.choice(Teamname)+",")
        file.write(random.choice(Position)+",")
        file.write(str(random.choice(Touchdowns))+",")
        file.write(str(random.choice(Totalyards))+",")
        file.write(str(random.choice(Salary)))
        file.write("\r\n")

filename = 'single/play'+ext+'.txt'
with open(filename,"w") as file:
    for i in range(1,size+1):
        if(i>size//2):
            file.write(str(random.randint(800000001,800000000+size+1))+",")
            file.write(str(i))
        else :
            file.write(str(i+800000000)+",")
            file.write(str(random.randint(1,size+1)))
        file.write("\r\n")

filename1 = 'bulk/play'+ext+'.txt'
with open(filename1, "w") as f2:
    for i in range(1,size+1):
        if(i>size//2):
            f2.write(str(random.randint(800000001,800000000+size+1))+",")
            f2.write(str(i))
        else :
            f2.write(str(i+800000000)+",")
            f2.write(str(random.randint(1,size+1)))
        f2.write("\r\n")
