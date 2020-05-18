## happy path 2
* greet
  - utter_greet
* introduction{"name":"any"}
  - utter_introduction
> introduced
 
## Re_introduced
> introduced
* greet
 - utter_greet_again

## mood great  
> introduced
* mood_great
  - utter_bot_mood
  - utter_prompt_interview
* hiring OR affirm
  - utter_what_kind_of_delevoper
> type


## type_js
> type
* type_developer{"type_dev":"js"}
  - utter_js_front
* question_js
  - utter_anwser_js

## sad path 1
> introduced
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
> introduced
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  - action_session_start

## happy question
> introduced
* personal_question
  - utter_personal_interests
* hiring OR affirm
  - utter_what_kind_of_delevoper


