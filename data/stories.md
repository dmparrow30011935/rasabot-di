## happy path 2
* get_started
  - utter_greet
* mood_great
  - utter_bot_mood
  - utter_prompt_interview
* hiring
  - utter_what_kind_of_delevoper

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  - action_session_start

## bot challenge
* bot_challenge
  - utter_iamabot

## happy question
* greet
  - utter_greet
* personal_question
  - utter_personal_interests
* hiring
  - utter_what_kind_of_delevoper

## Story from conversation with c1fd95b1b71c49f9ac24d2abc26dffc0 on May 16th 2020

* greet
    - utter_greet
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper

## Story from conversation with 8a4f928d231f4886ac243703b9db0434 on May 16th 2020

* greet
    - utter_greet
* mood_great
    - utter_bot_mood
    - utter_prompt_interview
* affirm
    - utter_what_kind_of_delevoper
* javascript_developer
    - utter_js_front

## Story from conversation with eaaa8d170b1e4b809d9de7415398c42f on May 16th 2020

* greet
    - utter_greet
* mood_great
    - utter_bot_mood
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper
* javascript_developer
    - utter_js_front

## New Story

* greet
    - utter_greet
* mood_great
    - utter_bot_mood
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper
* javascript_developer
    - utter_js_front
* question_js
    - utter_anwser_js

## New Story

* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper
* javascript_developer
    - utter_js_front
* question_js
    - utter_anwser_js
* request_education
    - utter_my_education
* question_education
    - utter_i_enjoy_edu
* js_knowledge
    - utter_js_lvl
