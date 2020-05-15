## happy path
* greet
  - utter_greet
* mood_great
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
  - utter_prompt_interview
* personal_question
  - utter_greet
* hiring
  - utter_what_kind_of_delevoper

## New Story

* greet
    - utter_greet
* mood_great
    - utter_iamabot
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper

## Story from conversation with bda252544a77499f8def04f267a16f58 on May 15th 2020

* get_started
    - utter_greet
* affirm
    - utter_iamabot
    - utter_prompt_interview

## New Story

* greet
    - utter_greet
* mood_great
    - utter_prompt_interview
* just_chating

## Story from conversation with c1fd95b1b71c49f9ac24d2abc26dffc0 on May 16th 2020

* greet
    - utter_greet
    - utter_prompt_interview
* hiring
    - utter_what_kind_of_delevoper
