library(RSQLite)

#Make a connection to the database
drv <-dbDriver("SQLite")
con <- dbConnect(drv,"~/newtsocks/newtsocks.db")

#Get the date distribution
res <- dbSendQuery(con, "SELECT date from news")
data <- fetch(res, n=-1)
data$date <- as.Date(data$date, "%Y-%m-%d")
hist(data$date,"month")

#Get the company distribution
res <- dbSendQuery(con, "SELECT company_id from news")
data <- fetch(res, n=-1)
hist(data$company_id)

#Get the score distribution
res <- dbSendQuery(con, "SELECT score from OpinionAPIResponse")
data <- fetch(res, n=-1)
hist(data$score)
