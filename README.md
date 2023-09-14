# hiveMentor
# !!!!! New Name / New URL !!!!!
# BeeMindful-Buzz / beemindful-buzz.com
Guiding programmers toward better mental well-being.

Users have 2 options when they 1st log in.  Chat and Health

Chat gives the user a save space to talk to a mentor.  Mentors can not diagnose users they are there to allow the user a save place to vent and offer moral support.  General advice is allowed but it is just that advice or suggestions.  Mentors are there as a shoulder to listen

Also on the chat side will be groups.  Places where like users can post topic specific questions and be connected to others with similar interests.  These are not live interactions but more forum based

Health side gives the user a place to keep track of different things (they can opt into some extras) as well as keep a journal of sorts.  They can grant access to their provider if they have an account (they can also give their provider the link)  They can alternatively print out their desired logs as a pdf to give to their provider

Mentors have the ability to talk to general users, they must be approved after some training on how to listen.  They will have the ability to alert the user's provider (if one was granted by the user) if they see certain concerning items.  If  not provider is present for the user the alert goes to a SuperAdmin The alert system is for safety of the user

# Links and Release Dates/Version Live

## Links
- [Main site](https://hivementor.beedev-services.com)
- [Dev site](https://dev.thehive-services.com)
- Both sites access the same database but current version updates are on Dev till released

## Current Version Released
- Main Site - Version 1.0 - Launched 8/7/2023
    - Log side only with limited logs
        - Water Count
        - Mood Symptoms
        - Medication
- Dev Site - Version 1.1 - Updated 8/17/2023
    - Same as Main and Log sites - Plus
        - CSS updates
        - Food completed
        - Weather completed
        - Dev page updated
    - This will remain in Dev only for testing 
- Under development - Version 1.2 - Updated 8/17/2023
    - Same as Main and Log sites - Plus
        - CSS updates
        - Food completed
        - Weather completed
        - Dev page updated




# Parts of the App

## UserApp
- Contains all basic user functionality
- Is viewable in Django Admin
- Also contains public facing pages

## ChatApp
- Contains the chat portion of the app
- Possibly viewable in Django Admin
- Initial chat will not be live chat but message based for quicker release

## LogApp
- Contains the log or journal side of the app
- Provider access / ability
- Not in Django Admin

# Styling of app

- Simple colors
- Slight differences between chat vs log as well as mentor vs general vs provider

# Release Stages
## V1
- Basic log side up and running
- User can create logs

## V2
- Chat app release - Live chat
    Groups and DM avail. 
- User can generate pdf of logs

## V3
- Provider access - log side only
- Mentor Training for chat release - when user gets upgraded to mentor/trainer username in chat will become Trainer - username and Mentor - username

## V4
- Mobile friendly CSS
- Messaging between provider and patient... 


## V5
- Alert system from chat to provider/admin
- Email alerts

## V6 (potential final)
- Mobile App


# Backlog ideas
- FAQ's
- Forum / Groups
- Mobile app
- Pagination for logs - added for V1 release


# Branches (as of 7/14/23)
Officially switched to branches dev and publicPages

## PublicPages branch
- will contain the updates for the public pages... index, about, contact