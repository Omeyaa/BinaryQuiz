import random
import time
import sqlite3

conn = sqlite3. connect( 'profile.db' )
c = conn.cursor()

def banner():
    a = print("""|---------------------------------------|
|                                       |
|                                       |
|              *BINARY QUIZ*            |
|                ~OMEYAA~               |
|                                       |
|---------------------------------------|

    [ 1 ] Login
    [ 2 ] Create Account
    [ 3 ] Leaderboard
    [ 4 ] Exit
    """)

banner()
while True:
    time.sleep(2)
    pick = input("Enter Number : ")
    if pick == '1':
        def login():
            time.sleep(1)
            while True:
                print("""\n|-----------------------------------------|
|                                         |
|                 LOGIN                   |
|                                         |
|-----------------------------------------|
                                """)
                uname = input("\nEnter Username : ")
                passw = input("Enter Password : ")

                log = "SELECT * FROM info WHERE username = ? and password = ?"
                c.execute(log,(uname,passw))
                if c.fetchall():
                    while True:
                        time.sleep(1)
                        print("""\n|-----------------------------------------|
|                                         |
|                                         |
|           [ 1 ] Play                    |
|           [ 2 ] Profile                 |
|           [ 3 ] Exit                    |
|                                         |
|                                         |
|-----------------------------------------|
                    """)
                        pick1 = input("Enter Number : ")
                        if pick1 == '1':
                            class easy:
                                time.sleep(1)
                                def easyq():
                                    e_randint_list = [random.randint(0,20),random.randint(21,40),random.randint(41,60),random.randint(61,80),random.randint(81,100)]
                                    e_randint_bin_list = [bin(random.randint(0,20)),bin(random.randint(21,40)),bin(random.randint(41,60)),bin(random.randint(61,80)),bin(random.randint(81,100))]
                                    score = 0
                                    eloop = 0
                                    print("""\n|-----------------------------------------|
|                                         |
|               EASY MODE                 |
|                                         |
|-----------------------------------------|
                                """)
                                    while eloop <= 4:
                                        time.sleep(2)
                                        e_rand_display_list = ['\n[ {} ] Convert {} into Binary'.format(eloop+1,e_randint_list[eloop]),'\n[ {} ] Convert {} into Decimal'.format(eloop+1,e_randint_bin_list[eloop])]
                                        e_rand_que = random.choice(e_rand_display_list)

                                        print(e_rand_que)
                                        eanswer = input("[ * ] Enter Answer : ")
                                        if e_rand_que == e_rand_display_list[0]:
                                            str_eans = str(eanswer)
                                            e_int_bin = bin(e_randint_list[eloop])
                                            if str_eans == e_int_bin:
                                                print("[ + ] Correct")
                                                score+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(bin(e_randint_list[eloop])))
                                        else:
                                            int_eans = int(eanswer)
                                            if e_randint_bin_list[eloop] == bin(int_eans):
                                                print("[ + ] Correct")
                                                score+=1
                                            else:
                                                c_str = int(e_randint_bin_list[eloop],2)
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(str(c_str)))
                                        eloop+=1
                                    time.sleep(1)
                                    print("\n [ *EASY* ] Your Score in Easy Mode : {}/5".format(score))
                                    f = c.execute(log,(uname,passw))
                                    for i in f:
                                        add_score = int(i[3]) + int(score)
                                        score_update = "UPDATE info set easy = ? WHERE username = ?"
                                        c.execute(score_update,(add_score,uname))

                            class medium:
                                time.sleep(1)
                                def mediumq():
                                    m_rand_numbers1 = [random.randint(1,10),random.randint(11,20),random.randint(21,30),random.randint(31,40),random.randint(41,50)]
                                    m_rand_numbers2 = [random.randint(51,60),random.randint(61,70),random.randint(71,80),random.randint(81,90),random.randint(91,100)]
                                    mscore = 0
                                    mloop = 0
                                    print("""\n|-----------------------------------------|
|                                         |
|               MEDUIM MODE               |
|                                         |
|-----------------------------------------|
                                """)
                                    while mloop <= 4:
                                        time.sleep(2)
                                        moperation = ['+','-','*','/']
                                        m_operation_rand = random.choice(moperation)
                                        print("\n")
                                        show = (" [ {0} ] {1} {2} {3} = 0b?".format(mloop+1,m_rand_numbers2[mloop],m_operation_rand,m_rand_numbers1[mloop]))
                                        print(show)
                                        if '+' in show:
                                            ans = int(m_rand_numbers2[mloop] + m_rand_numbers1[mloop])
                                            input_ans = str(input(" [ * ]Enter Answer : "))
                                            if str(input_ans) == str(bin(ans)):
                                                print(" [ + ] Correct")
                                                mscore+=1
                                            else:
                                                print(" [ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(bin(m_rand_numbers2[mloop]+m_rand_numbers1[mloop])))
                                        elif '-' in show:
                                            ans = int(m_rand_numbers2[mloop] - m_rand_numbers1[mloop])
                                            input_ans = str(input(" [ * ] Enter Answer : "))
                                            if str(input_ans) == str(bin(ans)):
                                                print(" [ + ] Correct")
                                                mscore+=1
                                            else:
                                                print(" [ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(bin(m_rand_numbers2[mloop] - m_rand_numbers1[mloop])))
                                        elif '*' in show:
                                            ans = int(m_rand_numbers2[mloop] * m_rand_numbers1[mloop])
                                            input_ans = str(input(" [ * ] Enter Answer : "))
                                            if str(input_ans) == str(bin(ans)):
                                                print(" [ + ] Correct")
                                                mscore+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(bin(m_rand_numbers2[mloop] * m_rand_numbers1[mloop])))
                                        elif '/' in show:
                                            ans = int(m_rand_numbers2[mloop] / m_rand_numbers1[mloop])
                                            input_ans = str(input(" [ * ] Enter Answer : "))
                                            if str(input_ans) == str(bin(ans)):
                                                print(" [ + ] Correct")
                                                mscore+=1
                                            else:
                                                print(" [ - ] Wrong")
                                                print("\n[ ANSWER ] {}".format(bin(int(m_rand_numbers2[mloop] / m_rand_numbers1[mloop]))))

                                        mloop+=1
                                    print("\n [ *MEDIUM* ] Your Score in Medium Mode : {}/5".format(mscore))
                                    f = c.execute(log,(uname,passw))
                                    for i in f:
                                        add_score = int(i[3]) + int(mscore)
                                        score_update = "UPDATE info set medium = ? WHERE username = ?"
                                        c.execute(score_update,(add_score,uname))
                                    
                            class hard:
                                time.sleep(1)
                                def hardq():
                                    hscore = 0
                                    hloop = 0
                                    num1 = [random.randint(0,10),random.randint(11,20),random.randint(21,30),random.randint(31,40),random.randint(41,50)]
                                    num2 = [random.randint(51,60),random.randint(61,70),random.randint(71,80),random.randint(81,90),random.randint(91,100)]
                                    operation1 = random.choice(['+','-','*','/'])
                                    print("""\n|-----------------------------------------|
|                                         |
|               HARD MODE                 |
|                                         |
|-----------------------------------------|
                                """)
                                    while hloop <= 4:
                                        time.sleep(2)
                                        que = "\n[ {0} ] {1} {2} {3} = 0b?".format(hloop+1,bin(num2[hloop]),bin(ord(operation1)),bin(num1[hloop]))
                                        print(que)
                                        ans = input("[ * ] Answer : ")
                                        if bin(ord('+')) in que:
                                            bin_ans = bin(num2[hloop]+num1[hloop])
                                            if bin_ans == ans:
                                                print("[ + ] Correct")
                                                hscore+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {0} + {1} = {2}".format(str(num2[hloop]),str(num1[hloop]),str(num2[hloop]+num1[hloop])))
                                                print("[ {} ] = {}".format(str(num2[hloop]+num1[hloop]),str(bin(num2[hloop]+num1[hloop]))))
                                        elif bin(ord('-')) in que:
                                            bin_ans = bin(num2[hloop]-num1[hloop])
                                            if bin_ans == ans:
                                                print("[ + ] Correct")
                                                hscore+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {0} - {1} = {2}".format(str(num2[hloop]),str(num1[hloop]),str(num2[hloop]-num1[hloop])))
                                                print("[ {} ] = {}".format(str(num2[hloop]-num1[hloop]),str(bin(num2[hloop]-num1[hloop]))))
                                        elif bin(ord('*')) in que:
                                            bin_ans = bin(num2[hloop]*num1[hloop])
                                            if bin_ans == ans:
                                                print("[ + ] Correct")
                                                hscore+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {0} * {1} = {2}".format(str(num2[hloop]),str(num1[hloop]),str(num2[hloop]*num1[hloop])))
                                                print("[ {} ] = {}".format(str(num2[hloop]*num1[hloop]),str(bin(num2[hloop]*num1[hloop]))))
                                        elif bin(ord('/')) in que:
                                            answer1 =int(num2[hloop] / num1[hloop])
                                            bin_ans = bin(answer1)
                                            if bin_ans == ans:
                                                print("[ + ] Correct")
                                                hscore+=1
                                            else:
                                                print("[ - ] Wrong")
                                                print("\n[ ANSWER ] {0} / {1} = {2}".format(str(num2[hloop]),str(num1[hloop]),str(int(num2[hloop]/num1[hloop]))))
                                                print("[ {} ] = {}".format(str(int(num2[hloop]/num1[hloop]),str(bin(num2[hloop]/num1[hloop])))))
                                        hloop+=1
                                    print("\n [ *HARD* ] Your Score in HARD Mode : {}/5".format(hscore))
                                    f = c.execute(log,(uname,passw))
                                    for i in f:
                                        add_score = int(i[3]) + int(hscore)
                                        score_update = "UPDATE info set hard = ? WHERE username = ?"
                                        c.execute(score_update,(add_score,uname))
                                        

                                    

                            easy.easyq()
                            medium.mediumq()
                            hard.hardq()
                            conn.commit()
                        elif pick1 == '2':
                            time.sleep(1)
                            pro_sql = "SELECT * FROM info WHERE username = ? and password = ?"
                            c.execute(pro_sql,(uname,passw))
                            f = c.execute(pro_sql,(uname,passw))
                            for i in f:
                                time.sleep(1)
                                print("""|-----------------------------------------------------------|
|ID : {0}                                                   
|-----------------------------------------------------------
|Username : {1}                                             
|-----------------------------------------------------------
|Password : {2}                                             
|-----------------------------------------------------------|
|  EASY  |   MEDIUM   |   HARD                              |                        
|-----------------------------------------------------------|
|   {3}    |    {4}       |   {5}                                 |
|-----------------------------------------------------------|
                """.format(str(i[0]),i[1],i[2],str(i[3]),str(i[4]),str(i[5])))
                            continue

                        elif pick1 == '3':
                            print("""\n|-----------------------------------------|
|                                         |
|               EXIT IN 3s                |
|                                         |
|-----------------------------------------|
                                """)
                            time.sleep(3)
                            banner()
                            break
                    break
                else:
                    time.sleep(1)
                    print("""\n|-----------------------------------------|
|                                         |
|            YOU DON'T HAVE               |
|              AN ACCOUNT                 |
|                                         |
|-----------------------------------------|
                                """)
        login()

    elif pick == '2':
        time.sleep(1)
        def create_acc():
            
            print("""\n|-----------------------------------------|
|                                         |
|            CREATE ACCOUNT               |
|                                         |
|-----------------------------------------|
                                """)
            c_uname = input("Enter Username : ")
            c_passw = input("Enter Password : ")
            if len(c_passw) >= 8:
                find_same = "SELECT * FROM info WHERE username = ? AND password = ?"
                c.execute(find_same,(c_uname,c_passw))
                if c.fetchall():
                    time.sleep(1)
                    print("""\n|-----------------------------------------|
|                                         |
|  YOUR USERNAME AND PASSWORD ARE TAKEN   |
|                                         |
|-----------------------------------------|
                                """)
                else:
                    time.sleep(1)
                    insert = "INSERT INTO info(username,password,easy,medium,hard)VALUES(?,?,?,?,?)"
                    c.execute(insert,(c_uname,c_passw,0,0,0))
                    print("""\n|-----------------------------------------|
|                                         |
|  YOUR ACCOUNT WAS SUCCESSFULLY CREATED  |
|                                         |
|-----------------------------------------|
                                """)
                    conn.commit()
        create_acc()
        banner()
        continue
        
    elif pick == '3':
        while True:
            time.sleep(1)
            print("""\n|-----------------------------------------|
|                                         |
|                SCORES                   |
|                                         |
|-----------------------------------------|

     [ 1 ] EASY MODE
     [ 2 ] MEDIUM MODE
     [ 3 ] HARD MODE
     [ 4 ] EXIT
                                """)

            pick3 = int(input("Enter Number : "))
            if pick3 == 1:
                print("""\n|-----------------------------------------|
|                                         |
|               EASY MODE                 |
|                                         |
|-----------------------------------------|
                                """)
                e_sql = "SELECT * FROM info"
                exe = c.execute(e_sql)
                a_name_sets = []
                for exes in exe:
                    name_set = (exes[1],exes[3])
                    a_name_sets.append(name_set)

                a_name_sets.sort(key=lambda names:names[1],reverse=True)
                print("RANK\t NAME\tSCORE")
                rank1 = 1
                for rank in a_name_sets:
                    time.sleep(1)
                    print(" "+str(rank1)+"\t"+rank[0]+"\t "+str(rank[1]))
                    rank1+=1

            elif pick3 == 2:
                time.sleep(1)
                print("""\n|-----------------------------------------|
            }
|                                         |
|             MEDIUM MODE                 |
|                                         |
|-----------------------------------------|
                                """)
                e_sql = "SELECT * FROM info"
                exe = c.execute(e_sql)
                a_name_sets = []
                for exes in exe:
                    name_set = (exes[1],exes[4])
                    a_name_sets.append(name_set)

                a_name_sets.sort(key=lambda names:names[1],reverse=True)
                print("RANK\t NAME\tSCORE")
                rank1 = 1
                for rank in a_name_sets:
                    time.sleep(1)
                    print(" "+str(rank1)+"\t"+rank[0]+"\t "+str(rank[1]))
                    rank1+=1
            elif pick3 == 3:
                time.sleep(1)
                print("""\n|-----------------------------------------|
|                                         |
|               HARD MODE                 |
|                                         |
|-----------------------------------------|
                                """)
                e_sql = "SELECT * FROM info"
                exe = c.execute(e_sql)
                a_name_sets = []
                for exes in exe:
                    name_set = (exes[1],exes[5])
                    a_name_sets.append(name_set)
                    
                a_name_sets.sort(key=lambda names:names[1],reverse=True)
                print("RANK\t NAME\tSCORE")
                rank1 = 1
                for rank in a_name_sets:
                    time.sleep(1)
                    print(" "+str(rank1)+"\t"+rank[0]+"\t "+str(rank[1]))
                    rank1+=1
            elif pick3 == 4:
                print("""\n|-----------------------------------------|
|                                         |
|             EXIT IN 3s                  |
|                                         |
|-----------------------------------------|
                                """)
                time.sleep(3)
                banner()
                break
    elif pick == '4':
        print("""\n|-----------------------------------------|
|                                         |
|             EXIT IN 3s                  |
|                                         |
|-----------------------------------------|
                                """)
        time.sleep(3)
        exit()
    else:
        print("""\n|-----------------------------------------|
|                                         |
|     PLEASE ENTER A CORRECT NUMBER       |
|                                         |
|-----------------------------------------|
                                """)
        continue