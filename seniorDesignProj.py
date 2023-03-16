### NOTE ###
# Green button is input 1, Red button is input 0. For the values in array "answers", true means it is in stock, false means its not in stock. Rating 1 means it was a positive experience, rating 0 means it was a negative experience.


#Array that saves the answers to be used for later interpretations/sending to faculty
answers = [0] * 4;
rating = "";

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

  #Asking user if they want to change the current question
  print(q)
  configure_q = input("Do you want to change this question?:\n")

  #Logic branch; will set new question if user inputs 1
  if(configure_q == "1"):
    new_q = input("Please type your new question.\n")
    return new_q
  #Return old question if user chooses not to configure current, shown question
  else:
    return q
  

#Define main function
def main():

  #Define default questions
  q1 = "Was there TP in stock?";
  q2 = "Was there PT in stock?";
  q3 = "Was there SOAP in stock?";
  q4 = "Was there HS in stock?";

  #Set status to True to enter while loop
  status = True;
  while(status):
    #Print prompts to initiate interaction
    print("\nNEW SESSION\n\n");
    print("Green Button = 1\nRed Button = 2\nNext Button = 3\nPrevious Button = 4\nConfigure = 0\n");

    #Take input to see if user is ready to start survey
    start_survey = input("Press the green button to start the survey, or press 0 to configure questions.\n");

    #Check input to determine whether we're taking survey,   configuring questions, or need to prompt user again if they are ready to take survey
    if(start_survey == "1"):
      print("If there's an issue, type 1, otherwise type 0.");
      issue = input("Was there an issue with the restroom?\n");
      #Check if user said there is an issue
      if(issue == "1"):
        #Call questions() function to prompt user with questions, then print out the answers that we'll use later to send to faculty
        questions(q1, q2, q3, q4)
        rating = input("Was this a positive or negative visit?")
        print("")
      else: 
        rating = input("Was this a positive or negative visit?")
      #Print thank you message to end interaction
      print(answers)
      print("Rating: " + rating)
      print("Thank you for taking the survey!")

    #Logic branch for configuring questions
    elif(start_survey == "0"):

      print("You are limited to four yes or no questions. Format the question so that it can be answered as Yes or No, denoted by the green and red buttons respectively.")

      #Reset/configure questions using configure_questions() function
      q1 = configure_questions(q1)
      q2 = configure_questions(q2)
      q3 = configure_questions(q3)
      q4 = configure_questions(q4)

      #Placeholder text to help separate printed text
      print("\n\n\n\n THIS JUST TO CLEAR CONSOLE \n\n\n\n\n")

    #Error handler; if user inputs an invalid input then they will be prompted to take the survey again
    else:
      print("INVALID INPUT - SURVEY PROMPT AGAIN\n")

#Call main() function
main()