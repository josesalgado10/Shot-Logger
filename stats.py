import datetime
TEAM_DICT={1:'ATL.txt',
2:'CHI.txt',
3:'DAL.txt',
4:'HOU.txt',
5:'LAX.txt',
6:'NYC.txt',
7:'PHI.txt',
8:'SEA.txt'}

Teams={1:'Atlanta',    2:'Chicago',    3:'Dallas',     4:'Houston',
5:'Los Angeles',    6:'New York',     7:'Philadelphia',    8:'Seattle'}

TEAMS='''
1=Atlanta    2=Chicago    3=Dallas     4=Houston
5=Los Angeles    6=New York     7=Philadelphia    8=Seattle
'''


team_player_dict={'Atlanta': ['Cory Boyd', 'Fionn Brown', 'Isom Butler', 'Jacory Hall', 'Jordan Ray', 
                              'Kendrick Summerour', 'Nigel Chaney', 'Xavier Johnson', 'Kern Charles'], 
                'Chicago': ['Antonio Singleton-II', 'Breydon Hargrove', 'Cameren McHenry', 'Harrison Rieger', 
                            'Josiah Pope', 'Lenell Watson', 'Marquis Brown', 'Deon Lyle', 'Montrell Dixson'], 
                'Dallas': ['Cameron Massey', 'Demolia Peterson', 'Nate Morris', 'Martavious Smothers', 
                           'Soleman Zazay', 'Zackery Crockett', 'Luis Silfa', 'Careal Walker'], 
                'Houston': ['Taj Royster', 'Calvin Williams', 'Curtis Hollis', 'DeShawn Washington', 
                            'Jeremiah Allen', 'Jordon Myers', 'Nicholas Lovelace', 'Quan VanPutten', 
                            'Shannon Handy'], 
                'Los Angeles': ['Brandon Phillips', 'Dembo Thimbo', 'Ezekiel Crawford', 'Gregory Floyd', 
                                'Melo Ball', 'Niles Malone', 'Scott-Brandon Harris', 'Taylor Kirkham'], 
                'New York': ['Aron Mata', 'Calvin Brown', 'Chris Lacey', 'Francis Mensah', 'Jameer Killing', 
                             'Jerry Antoine-II', 'Magd Abdelwahab', 'Moises Burgos', 'Morissana Camara'], 
                'Philadelphia': ['Brandon Stacy', 'Devin Haid', 'Jawane Buckner', 'Jaylen Nixon', 
                                 'Marquis Johnson', 'Elijah Hall'], 
                'Seattle': ['Jerell Springer', 'Ishmael Muhamad', 'Jerry Vargas', 'Jamichael Morgan', 
                            'Julius Mischke', 'Melvin Davis', 'Semaj Booker', 'Devin Mitchell']}

_TEAM_FILE=None
while _TEAM_FILE==None:
    try:
        print(TEAMS)
        number=int(input('Choose the number representing the team: '))
        _TEAM_FILE=(Teams[number],team_player_dict[Teams[number]])
    except:
        print('\nPlease input a number between 1-8')
        pass

# for num,line in enumerate(open('players.csv','r'),0):
#     line=line.rstrip().split(',')
#     if num!=0:
#         first=line[0]
#         last=line[1]
#         team=line[7]
#         team_player_dict[team].append(first+' '+last)
# 
# print(dict(team_player_dict))

class Player:
    def __init__(self, first, last, team):
        self._first = first
        self._last = last
        self._team = team
        self._made = 0
        self._att = 0
        self._twoptmade = 0
        self._twoptatt = 0
        self._threeptmade = 0
        self._threeptatt = 0
        self.shotspots = []
        self.player_status=''
        
    def percentage(self):
        if self._att == 0:
            print('{} - Shot percentage: 0 %'.format(self._first + ' ' + self._last))
        else:
            print('{} \n  Shot percentage: {:3.1f} %\n  Two pt. shot percentage: {:3.1f} %\n  Three pt. shot percentage: {:3.1f} %'.format(self._first + ' ' + self._last,
                                                           (self._made / self._att) * 100,
                                                           self.twoptperc(),
                                                           self.threeptperc()))
    def twoptperc(self):
        if self._twoptatt == 0:
            #print('{} - Two pt. shot percentage: 0 %'.format(self._first + ' ' + self._last))
            return 0.0
        else:
            #print('{} - Two pt. shot percentage: {} %'.format(self._first + ' ' + self._last, (self._twoptmade / self._twoptatt) * 100))
            return (self._twoptmade / self._twoptatt) * 100
    
    def threeptperc(self):
        if self._threeptatt == 0:
            #print('{} - Three pt. shot percentage: 0 %'.format(self._first + ' ' + self._last))
            return 0.0
        else:
            #print('{} - Three pt. shot percentage: {} %'.format(self._first + ' ' + self._last, (self._threeptmade / self._threeptatt) * 100))
            return (self._threeptmade / self._threeptatt) * 100
            
    def handle(self, key):
        if key == '2+':
            self.twoscore()
        elif key == '2-':
            self.twomiss()
        elif key == '3+':
            self.threescore()
        elif key == '3-':
            self.threemiss()
        elif key == 'Show %':
            self.percentage()
            
    def twoscore(self):
        self._made += 1
        self._att += 1
        self._twoptmade += 1
        self._twoptatt += 1
        self.player_status = 'Two made for: {}'.format(self._first + ' ' + self._last)
        print('Two made for: {}'.format(self._first + ' ' + self._last))
        
    def twomiss(self):
        self._att += 1
        self._twoptatt += 1
        self.player_status = 'Two miss for {}'.format(self._first + ' ' + self._last)
        print('Two miss for {}'.format(self._first + ' ' + self._last))
        
    def threescore(self):
        self._made += 1
        self._att += 1
        self._threeptmade += 1
        self._threeptatt += 1
        self.player_status = 'Three made for: {}'.format(self._first + ' ' + self._last)
        print('Three made for: {}'.format(self._first + ' ' + self._last))
        
    def threemiss(self):
        self._att += 1
        self._threeptatt += 1
        self.player_status = 'Three miss for: {}'.format(self._first + ' ' + self._last)
        print('Three miss for: {}'.format(self._first + ' ' + self._last))
        
    def store(self):
        try:
            file_name=_TEAM_FILE[0]+'_'+datetime.datetime.today().strftime('%Y-%m-%d')
            file = open(file_name, 'a+')
            if self._att == 0:
                file.write('{} - Shot percentage: 0 % \n\n'.format(self._first + ' ' + self._last))
            else:
                file.write('{} \n  Shot percentage: {:3.1f} %\n  Two pt. shot percentage: {:3.1f} %\n  Three pt. shot percentage: {:3.1f} % \n\n'.format(self._first + ' ' + self._last,
                                                               (self._made / self._att) * 100,
                                                               self.twoptperc(),
                                                               self.threeptperc()))
        except TypeError:
            pass
            

def select_team(file):
    team=[]
    for person in _TEAM_FILE[1]:
        person=person.split(' ')
        team.append(Player(person[0],person[1],_TEAM_FILE[0]))
    return team
#     try:
#         team = []
#         for line in open(file):
#             line = line.rstrip().split(',')
#             team.append(Player(line[0], line[1], line[2].rstrip()))
#         return team
#     except IndexError:
#         print("Already took stats for {}".format(str(file)))

TEAM = select_team(_TEAM_FILE)

def select_player(name):
    for player in TEAM:
        fl = name.split()
        if player._first == fl[0] and player._last == fl[1]:
            return player
        
def store_all(team):
    for player in team:
        player.store()
    file_name=_TEAM_FILE[0]+'_'+datetime.datetime.today().strftime('%Y-%m-%d')
    file = open(file_name, 'a+')
    file.write('\n----------------------------------------------------------------------------------------\n')


    










    
