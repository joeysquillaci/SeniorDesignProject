answers = [0] * 4

interpretations = [0] * 4

def questions(q1, q2, q3, q4):
  #Display First Prompt
  q1 = input(q1);
  q2 = input(q2);
  q3 = input(q3);
  q4 = input(q4);


  #Logic that saves what the answer to each question was
  if(q1 == "1"):
    answers[0] = True;
  else:
    answers[0] = False;

  if(q2 == "1"):
    answers[1] = True;
  else:
    answers[1] = False;

  if(q3 == "1"):
    answers[2] = True;
  else:
    answers[2] = False;

  if(q4 == "1"):
    answers[3] = True;
  else:
    answers[3] = False;


#Define interpretation function
def configure_questions(q):
  
  print(q)
  configure_q = input("Do you want to change this question?:\n")

  if(configure_q == "1"):
    new_q = input("Please type your new question.\n")
    return new_q
  else:
    return q
  

#Define main function
def main():

  q1 = "Was there TP in stock?";
  q2 = "Was there PT in stock?";
  q3 = "Was there SOAP in stock?";
  q4 = "Was there HS in stock?";


  
  status = True;
  while(status):
    print("Green Button = 1\nRed Button = 2\nNext Button = 3\nPrevious Button = 4\nConfigure = 0\n");
  
    start_survey = input("Press the green button to start the survey.\n");
  
    if(start_survey == "1"):
      questions(q1, q2, q3, q4)
      #Display answers at the end
      print(answers)
      #End the while loop
      status = False;
    elif(start_survey == "0"):

      print("You are limited to four yes or no questions. Format the question so that it can be answered as Yes or No, denoted by the green and red buttons respectively.")
      
      q1 = configure_questions(q1)
      q2 = configure_questions(q2)
      q3 = configure_questions(q3)
      q4 = configure_questions(q4)

      print("\n\n\n\n THIS JUST TO CLEAR CONSOLE \n\n\n\n\n")
      
    else:
      print("Time to loop back to asking the question again")

    print(q1 + "\n")
    print(q2 + "\n")
    print(q3 + "\n")
    print(q4 + "\n")

    
main()