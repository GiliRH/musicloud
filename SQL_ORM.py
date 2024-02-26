import sqlite3

import pickle

# https://docs.python.org/2/library/sqlite3.html
# https://www.youtube.com/watch?v=U7nfe4adDw8


__author__ = 'user'


class songs(object):
    def __init__(self, song_name, md5, url, id):
        self.user_name = user_name
        self.password = user_password
        self.first_name = first_Name
        self.last_name = last_Name
        self.address = adress
        self.speed = speed
        self.account_ID = accountID
        self.isCaptain = isCaptain

    def update_max_speed(self, newSpeed):
        self.speed = newSpeed

    def new_pass(self, newPassword):
        self.user_password = newPassword

    def change_manager_status(self):
        self.is_captain = not self.is_captain

    def __str__(self):
        return "user:" + self.user_name + ":" + self.user_password + ":" + self.first_Name + ":" + \
               self.last_Name + ":" + self.adress + ":" + self.speed + ":" + \
               str(self.account_ID) + ":" + self.isCaptain


class playlists(object):
    def __init__(self, id, name, songs, user_id):
        self.id = id
        self.name = name
        self.avg_speed = avgSpeed
        self.coach = coach
        # self.credit_cards=[]

# !!! CHANGE AME TO CORRECT
class users():
    def __init__(self):
        self.conn = None  # will store the DB connection
        self.cursor = None  # will store the DB connection cursor
        self.current = None

    def open_DB(self):
        """
        will open DB file and put value in:
        self.conn (need DB file name)
        and self.cursor
        """
        self.conn = sqlite3.connect('AthleteTeam.db')
        self.current = self.conn.cursor()

    def create_table(self):
        self.open_DB()
        # Create table
        self.current.execute('''CREATE TABLE teams
                     (name, id, avg_speed,coach)''')
        self.current.execute('''CREATE TABLE athletes
                             (id, user_name, password, first_Name, last_Name, address, phone, speed, isCaptain)''')
        self.close_DB()

    def close_DB(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    # All read SQL

    def Get_Athlete(self, username):
        self.open_DB()

        usr = None
        sql = "SELECT SELECT id, user_name, password, first_Name, last_Name, address, phone, speed, isCaptain" \
              " FROM Athletes WHERE user_name = username"
        res = self.current.execute(sql)
        usr = res

        self.close_DB()
        return usr

    def Get_Teams(self):
        self.open_DB()
        teams = []
        sql = "SELECT name, id, avg_speed,coach From teams"
        res = self.current.execute(sql)
        for ans in res:
            teams.append(ans)
        self.close_DB()
        return teams

    def Get_Athletes(self):
        self.open_DB()
        athlt = []
        sql = "SELECT id, user_name, password, first_Name, last_Name, address, speed, isCaptain From Athletes"
        res = self.current.execute(sql)
        for ans in res:
            athlt.append(ans)

        return athlt

    def get_team_avg_speed(self, username):
        self.open_DB()

        sql = "SELECT a.avg_speed FROM Teams a , Athletes b WHERE a.Teamid=b.Teamid and b.Username='" + username + "'"
        res = self.current.execute(sql)
        for ans in res:
            avg_speed = ans[0]
        self.close_DB()
        return avg_speed

    # __________________________________________________________________________________________________________________
    # __________________________________________________________________________________________________________________
    # ______end of read start write ____________________________________________________________________________________
    # __________________________________________________________________________________________________________________
    # __________________________________________________________________________________________________________________
    # __________________________________________________________________________________________________________________

    # All write SQL

    def withdraw_by_username(self, amount, username):
        """
        return true for success and false if failed
        """
        pass

    def deposit_by_username(self, amount, username):
        pass

    def insert_new_user(self, user):
        self.open_DB()
        sql = "SELECT MAX(id) FROM athletes"
        res = self.current.execute(sql)
        ret = self.current.fetchall()
        print("res", ret)
        # id = 1
        # for ans in ret:
        #     if ans[0] is not None:
        #         id = int(ans[0]) + 1
        sql = "INSERT INTO Athletes (id, user_name, password, first_Name, last_Name, address, speed, isCaptain)"
        sql += " VALUES('" + user.user_name + "','" + user.password + "','" + user.first_name + "','" + user.last_name + "',"
        sql += "'" + user.address + "','" + user.phone + "','" + str(user.speed) + "'," + str(
            user.account_ID) + ",'no')"
        res = self.current.execute(sql)
        self.commit()
        self.close_DB()
        print(res)
        return "Ok"

    # def insert_new_account(self,username,password,firstname,lastname,address,phone,email):
    def insert_new_team(self, coach, name):

        self.open_DB()
        sql = "SELECT MAX(Teamid) FROM teams"
        res = self.current.execute(sql)
        id = 0
        for ans in res:
            id = ans[0] + 1
        sql = "INSERT INTO Teams (name, id, avg_speed,coach) VALUES(" + name + ',' + str(id) + ",0,'" + coach + "')"
        res = self.current.execute(sql)
        self.commit()
        self.close_DB()
        print(res)
        return "Ok"

    def update_user(self, user):
        self.open_DB()
        sql = "UPDATE athletes "
        sql += "SET " + user.user_name + "','" + user.password + "','" + \
               user.first_name + "','" + user.last_name + "',""'" + \
               user.address + "','" + str(user.speed) + \
               "'," + str(user.account_ID) + "," + user.isCaptain
        sql += " WHERE user_name='" + user.user_name + "'"
        print(sql)
        res = self.current.execute(sql)
        self.commit()
        self.close_DB()
        print(res)
        return "Ok"
        self.close_DB()
        return True

    def update_user_speed(self, username, speed):
        self.open_DB()
        sql = "UPDATE athletes "
        sql += "SET speed=" + str(speed)
        sql += " WHERE user_name='" + username + "'"
        print(sql)
        res = self.current.execute(sql)
        self.commit()
        self.close_DB()
        print(res)
        return "Ok"
        self.close_DB()
        return True

    def update_account(self, account):
        pass

    def delete_user(self, username):
        self.open_DB()
        sql = "DELETE FROM athletes WHERE user_name='" + username + "'"
        print(sql)
        res = self.current.execute(sql)
        self.commit()
        self.close_DB()
        print(res)
        return "Ok"

    def delete_account(self, accountID):
        pass


def main_test():
    user1 = Athlete("GilRH", "123j23", "Gil", "Reshef", "kfar saba", 358, 1, 'no')
    user2 = Athlete("LM10", "GOAT10", "Leo", "Messi", "Barcelona", 308, 2, 'yes')
    db = AthleteTeamORM()

    # db.create_table()
    # db.insert_new_user(user1)
    # db.insert_new_user(user2)
    db.update_user_speed(user2.user_name, 213)
    users = db.Get_Athletes()
    for u in users:
        print(u)


if __name__ == "__main__":
    main_test()


