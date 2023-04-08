import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="analyzer"
)

mycursor=mydb.cursor()

bussiness="CREATE TABLE business( business_id int(11) NOT NULL, business_count int(11) NOT NULL, business_date date NOT NULL) "
mycursor.execute(business)

bussiness_sub="CREATE TABLE business_subcategory (buss_sub_id int(11) NOT NULL,Crypto int(11) NOT NULL,Market int(11) NOT NULL,Money int(11) NOT NULL,Economy int(11) NOT NULL,Industry int(11) NOT NULL,Date date NOT NULL)"
mycursor.execute(business_sub)


entertainment="CREATE TABLE entertainment (entertainment_id int(11) NOT NULL,entertainment_count int(11) NOT NULL,entertainment_date date NOT NULL) "
mycursor.execute(entertainment)

entertainment_sub="CREATE TABLE entertainment_sub_category (ent_sub_id int(11) NOT NULL, bollywood int(11) NOT NULL, hollywood int(11) NOT NULL, tv int(11) NOT NULL, web_series int(11) NOT NULL, Date date NOT NULL) "
mycursor.execute(entertainment_sub)


nation="CREATE TABLE nation (nation_id int(11) NOT NULL,nation_count int(11) NOT NULL,nation_date date NOT NULL)"
mycursor.execute(nation)

nation_sub="CREATE TABLE nation_subcategory (nation_sub_id int(11) NOT NULL,covid int(11) NOT NULL,government int(11) NOT NULL,crime int(11) NOT NULL,court int(11) NOT NULL,Date date NOT NULL)"
mycursor.execute(nation_sub)


sports="REATE TABLE sports (sports_id int(11) NOT NULL,sports_count int(11) NOT NULL,sports_date date NOT NULL) "
mycursor.execute(sports)

sports_sub="CREATE TABLE sports_sub_category (sports_id int(11) NOT NULL,cricket int(11) NOT NULL,football int(11) NOT NULL,tennis int(11) NOT NULL,Date date NOT NULL)"
mycursor.execute(sports_sub)


technology="CREATE TABLE technology (technology_id int(11) NOT NULL,technology_count int(11) NOT NULL,technology_date date NOT NULL) "
mycursor.execute(technology)

technology_sub="CREATE TABLE technology_subcategory (tech_sub_id int(11) NOT NULL,5G int(11) NOT NULL,Mobile int(11) NOT NULL,New_gadgets int(11) NOT NULL,Crypto int(11) NOT NULL,Date date NOT NULL)"
mycursor.execute(technology_sub)


world="CREATE TABLE world (world_id int(11) NOT NULL,world_count int(11) NOT NULL,world_date date NOT NULL)"
mycursor.execute(world)

world_sub="CREATE TABLE world_subcategory (world_sub_id int(11) NOT NULL,Russia int(11) NOT NULL,USA int(11) NOT NULL,UK int(11) NOT NULL,Asia int(11) NOT NULL,Date date NOT NULL)"
mycursor.execute(world_sub)

mydb.commit()
mycursor.close()
mydb.close()
