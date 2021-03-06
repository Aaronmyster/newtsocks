import sys
from models import Company
from models import NewsSource
from models import News
from models import Price
from models import OpinionAPI
from models import OpinionAPIResponse

# 
# Creates the database, and populates initial data
# 

# Main entry point
def main():
	createDB()
	addCompanies()
	addNewsSources()
	print "Done!"

# Creates the db file and schema
def createDB():
	print "Creating the initial db"
	Company.create_table()
	NewsSource.create_table()
	News.create_table()
	Price.create_table()
	OpinionAPI.create_table()
	OpinionAPIResponse.create_table()

# Adds News Sources
def addNewsSources():
	print "Adding News Sources"
	NewsSource.create(name="Reuters", url="http://www.reuters.com")

# Adds Companies
def addCompanies():
	print "Adding companies..."
	Company.create(name="Sprint", ticker="S")
	Company.create(name="Bank of America", ticker="BAC")
	Company.create(name="Pfizer", ticker="PFE")
	Company.create(name="Advanced Micro Devices", ticker="AMD")
	Company.create(name="General Electric", ticker="GE")
	Company.create(name="Ambev ADS", ticker="ABEV")
	Company.create(name="Walgreen", ticker="WAG")
	Company.create(name="Ford Motor", ticker="F")
	Company.create(name="Rite Aid", ticker="RAD")
	Company.create(name="Taiwan Semiconductor Manufacturing ADS", ticker="TSM")
	Company.create(name="Petroleo Brasileiro ADS", ticker="PBR")
	Company.create(name="AT&T", ticker="T")
	Company.create(name="Verizon Communications", ticker="VZ")
	Company.create(name="Boston Scientific", ticker="BSX")
	Company.create(name="Twitter", ticker="TWTR")
	Company.create(name="SandRidge Energy", ticker="SD")
	Company.create(name="Wells Fargo", ticker="WFC")
	Company.create(name="Delta Air Lines", ticker="DAL")
	Company.create(name="Alcoa", ticker="AA")
	Company.create(name="Coca-Cola", ticker="KO")
	Company.create(name="Regions Financial", ticker="RF")
	Company.create(name="AbbVie", ticker="ABBV")
	Company.create(name="Post Holdings", ticker="POST")
	Company.create(name="JPMorgan Chase", ticker="JPM")
	Company.create(name="Coach Inc.", ticker="COH")
	Company.create(name="Western Union", ticker="WU")
	Company.create(name="CBS Cl B", ticker="CBS")
	Company.create(name="Citigroup", ticker="C")
	Company.create(name="Molycorp", ticker="MCP")
	Company.create(name="J.C. Penney", ticker="JCP")
	Company.create(name="Vale ADS", ticker="VALE")
	Company.create(name="EMC", ticker="EMC")
	Company.create(name="Exxon Mobil", ticker="XOM")
	Company.create(name="Nokia ADS", ticker="NOK")
	Company.create(name="BP ADS", ticker="BP")
	Company.create(name="Kinross Gold", ticker="KGC")
	Company.create(name="Medtronic", ticker="MDT")
	Company.create(name="General Motors", ticker="GM")
	Company.create(name="SunEdison", ticker="SUNE")
	Company.create(name="MGIC Investment", ticker="MTG")
	Company.create(name="T-Mobile US", ticker="TMUS")
	Company.create(name="Oracle", ticker="ORCL")
	Company.create(name="Alpha Natural Resources", ticker="ANR")
	Company.create(name="Talisman Energy", ticker="TLM")
	Company.create(name="Barrick Gold", ticker="ABX")
	Company.create(name="Morgan Stanley", ticker="MS")
	Company.create(name="Petroleo Brasileiro ADS A", ticker="PBRA")
	Company.create(name="Itau Unibanco Holding ADS", ticker="ITUB")
	Company.create(name="Bank of New York Mellon", ticker="BK")
	Company.create(name="KeyCorp", ticker="KEY")
	Company.create(name="American International Group", ticker="AIG")
	Company.create(name="Gap", ticker="GPS")
	Company.create(name="Time Warner", ticker="TWX")
	Company.create(name="D.R. Horton", ticker="DHI")
	Company.create(name="Dow Chemical", ticker="DOW")
	Company.create(name="Banco Santander ADS", ticker="SAN")
	Company.create(name="Paragon Offshore", ticker="PGN")
	Company.create(name="Las Vegas Sands", ticker="LVS")
	Company.create(name="Quicksilver Resources", ticker="KWK")
	Company.create(name="Lowe's", ticker="LOW")
	Company.create(name="Covidien", ticker="COV")
	Company.create(name="PPL", ticker="PPL")
	Company.create(name="Home Depot", ticker="HD")
	Company.create(name="Gafisa ADS", ticker="GFA")
	Company.create(name="Merck&Co", ticker="MRK")
	Company.create(name="Marathon Oil", ticker="MRO")
	Company.create(name="International Game Technology", ticker="IGT")
	Company.create(name="United Continental Holdings", ticker="UAL")
	Company.create(name="Ryerson Holding", ticker="RYI")
	Company.create(name="Magnum Hunter Resources", ticker="MHR")
	Company.create(name="Chesapeake Energy", ticker="CHK")
	Company.create(name="McDonald's", ticker="MCD")
	Company.create(name="NRG Energy", ticker="NRG")
	Company.create(name="Genworth Financial Cl A", ticker="GNW")
	Company.create(name="MGM Resorts International", ticker="MGM")
	Company.create(name="Walt Disney", ticker="DIS")
	Company.create(name="SouFun Holdings", ticker="SFUN")
	Company.create(name="Youku Tudou ADS", ticker="YOKU")
	Company.create(name="Dollar General", ticker="DG")
	Company.create(name="Procter&Gamble", ticker="PG")
	Company.create(name="U.S. Bancorp", ticker="USB")
	Company.create(name="Xerox", ticker="XRX")
	Company.create(name="Corning", ticker="GLW")
	Company.create(name="Exelon", ticker="EXC")
	Company.create(name="Yamana Gold", ticker="AUY")
	Company.create(name="Cemex ADS", ticker="CX")
	Company.create(name="Charles Schwab", ticker="SCHW")
	Company.create(name="Millennial Media", ticker="MM")
	Company.create(name="Freeport-McMoRan", ticker="FCX")
	Company.create(name="Interpublic Group", ticker="IPG")
	Company.create(name="Halliburton", ticker="HAL")
	Company.create(name="Hewlett-Packard", ticker="HPQ")
	Company.create(name="Transocean", ticker="RIG")
	Company.create(name="Johnson&Johnson", ticker="JNJ")
	Company.create(name="United States Steel", ticker="X")
	Company.create(name="Halcon Resources", ticker="HK")
	Company.create(name="Hertz Global Holdings", ticker="HTZ")
	Company.create(name="Hartford Financial Services Group", ticker="HIG")
	Company.create(name="Office Depot", ticker="ODP")
	Company.create(name="Annaly Capital Management", ticker="NLY")


if __name__ == '__main__':
	sys.exit(main())