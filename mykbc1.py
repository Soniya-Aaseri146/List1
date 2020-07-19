
question=["Which of these Hindi phrases is used to denote high inflation?",
    "The traditional attire 'pheta' is worn on which part of the body ?",
    "Which of the following was once a lifeline on the TV show 'Kaun Banega Crorepati'?",
    "what time corresponds to 23:23 hours ?",
    "Where is girl's campus Navgurukul?",
    "which repo are you coding in .........?"]
_question="question."
options1_list=["Gali","Tridev","Lawn Tennis","11.11PM","Shimla","Chikungunya",]
options2_list=["Dil","Triguni","Table Tennis","7:23PM","Bangalore","Typhoid",]
options3_list=["Kholi","Trimurti","Badminton","Amar Akbar Anthony","jaipur","Dengue",]
options4_list=["Baju","Squash","9.11PM","11:23PM","Kolkata","Rail Coaches"]
question_key=[1,2,3,4,5,6]
answer_key=[1,1,2,4,2,2]
prize=[16000,320000,640000,120000,1000000,10000000]
RightAnswer=True
for index in range(6):
    if RightAnswer:
        print("---------------------------------")
        print("apka question"+str(question_key[index]) +". yeh hai ")
        print(_question + " " +question[index])
        print("(a) " + options1_list[index])
        print("(b) " + options2_list[index])
        print("(c) " + options3_list[index])
        print("(d) " + options4_list[index])
        answer= input("Enter your answer\n")
        if answer == "Quit":
            print ("aapne game quit kar di hai")
            print ("aap yaha se",prize[index -1],"jeet kar  jaa rahe hai")
        elif int(answer) == answer_key[index]:
            print ("aapka jawab sahi hai")
            print ("aap",prize[index],"jeet chuke hain")
        else:
            print ("aapka jawab galat hai")
            while True:
                RightAnswer=False
                Lifeline=input("Life line 50-50?\n Yes/No\n")
                if Lifeline == "yes" :
                    print("Aapko dubara se chance diya jaa rha h")
                if int(answer) == answer_key[index]:
                    print("You answer is right")
                    print("Congrats aap",prize[index],"jeet chuke hain")
                    break
                else:
                    print("Your answer is wrong")
                    print("Aap yha se",prize[index-1],"jeet kar nhi jaa rhe hain")
                    break