from sqlalchemy import Column, String, Integer, Date, Numeric


class TeamStats():
	__tablename__ = 'DAILY_TEAM_STATS'

	id = Column(Integer, primary_key=True)
	team = Column(String)
	opponent = Column(String)
	homeAway = Column(String)
	date = Column(Date)
	pts = Column(Integer)
	fg = Column(Integer)
	fga = Column(Integer)
	fgpercent = Column(Numeric)
	thrp = Column(Integer)
	thrpa = Column(Integer)
	thrppercent = Column(Numeric)
	ft = Column(Integer)
	fta = Column(Integer)
	ftpercent = Column(Numeric)
	orb = Column(Integer)
	drb = Column(Integer)
	trb = Column(Integer)
	ast = Column(Integer)
	stl = Column(Integer)
	blk = Column(Integer)
	tov = Column(Integer)
	pf = Column(Integer)
	tspercent = Column(Numeric)
	efgpercent = Column(Numeric)
	thrpar = Column(Numeric)
	ftr = Column(Numeric)
	astpercent = Column(Numeric)
	stlpercent = Column(Numeric)
	blkpercent = Column(Numeric)
	tovpercent = Column(Numeric)
	ortg = Column(Numeric)
	drtg = Column(Numeric)
	fanduel = Column(Numeric)

	def __init__(self, team, opponent, homeAway, date, pts, fg, fga, fgpercent,
				 thrp, thrpa, thrppercent, ft, fta, ftpercent, orb, drb, trb, ast, stl,
				 blk, tov, pf, tspercent, efgpercent, thrpar, ftr, astpercent,
				 stlpercent, blkpercent, tovpercent, ortg, drtg, fanduel):
		self.team = team
		self.opponent = opponent
		self.homeAway = homeAway
		self.date = date
		self.pts = pts
		self.fg = fg
		self.fga = fga
		self.fgpercent = fgpercent
		self.thrp = thrp
		self.thrpa = thrpa
		self.thrppercent = thrppercent
		self.ft = ft
		self.fta = fta
		self.ftpercent = ftpercent
		self.orb = orb
		self.drb = drb
		self.trb = trb
		self.ast = ast
		self.stl = stl
		self.blk = blk
		self.tov = tov
		self.pf = pf
		self.tspercent = tspercent
		self.efgpercent = efgpercent
		self.thrpar = thrpar
		self.ftr = ftr
		self.astpercent = astpercent
		self.stlpercent = stlpercent
		self.blkpercent = blkpercent
		self.tovpercent = tovpercent
		self.ortg = ortg
		self.drtg = drtg
		self.fanduel = fanduel



