# hiveMentor
Guiding programmers toward better mental well-being.

# Parts of the App

## UserApp
- Contains all basic user functionality
- Is part of Django Admin
- Also contains public facing pages

### Levels
- Admin
    - Enable users access to other levels
- General User
    - Access to general user side of chat
    - Access to log side of app
- Mentor User
    - Access to mentor side of chat
    - Access to log side of app
    - Ability to see if general user has granted provider access (not who provider is just a check box)
- Training User
    - Access to Mentor training
- Duel User
    - Has access to both general user and mentor user side of chat
        - Must have logic for on login they chose the side they wish and can only see those sides.
- Provider User
    - Access to specific user's logs (user grants access to logs they wish to share)
    - Simplified Messaging system between their granted users

### Attributes
- First Name
- Last Name
- Username
- Password
- Level
- Last Logged On Date
- Profile
    - Image
    - Available Logs - Sugar / Sleep / Food

## ChatApp
- Contains the chat portion of the app
    - 2 sides General User and Mentor User
    - Can only see 1 side at a time if a duel user
    - Mentors can flag general users to admin / provider if one is assigned
        - Have some sort of integration to crisis centers?
    - Chats are not saved outside of session unless general user chooses to or chat is flagged. 
- Partially part of Django Admin

## LogApp
- Contains the log or journal side of the app
    - Sleep Tracker
    - Sugar Tracker
    - Mental check in 1-4 scale
    - Notes
- Allow provider access
    - Chose from list
    - Deselect from list
    - Generate printout
    - message between provider and user
    - chose which logs to share
- Provider access
    - Can only see those users that have selected them
    - requires access code to gain provider access
        - Access code granted upon question verification
            - Eventualy needs better verification
    - If alerted regarding a user enables message communication between Mentor and Provider (username based only)

# Styling of app

- Simple colors
- Slight differences between chat vs log as well as mentor vs general vs provider

# Release Stages
## V1
- Basic log side up and running
- User can create logs
- User can generate pdf of logs
- Mentor Training for chat release

## V2
- Chat app release
- Mobile friendly CSS

## V3
- Provider access

## V4
- Alert system from chat to provider/admin


# Backlog ideas
- FAQ's
- Forum / Groups
- Mobile app
- Pagination for logs
