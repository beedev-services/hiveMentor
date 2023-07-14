# hiveMentor
Guiding programmers toward better mental well-being.

Users have 2 options when they 1st log in.  Chat and Health

Chat gives the user a save space to talk to a mentor.  Mentors can not diagnose users they are there to allow the user a save place to vent and offer moral support.  General advice is allowed but it is just that advice or suggestions.  Mentors are there as a shoulder to listen

Also on the chat side will be groups.  Places where like users can post topic specific questions and be connected to others with similar interests.  These are not live interactions but more forum based

Health side gives the user a place to keep track of different things (they can opt into some extras) as well as keep a journal of sorts.  They can grant access to their provider if they have an account (they can also give their provider the link)  They can alternatively print out their desired logs as a pdf to give to their provider

Mentors have the ability to talk to general users, they must be approved after some training on how to listen.  They will have the ability to alert the user's provider (if one was granted by the user) if they see certain concerning items.  If  not provider is present for the user the alert goes to a SuperAdmin The alert system is for safety of the user

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
- User can generate pdf of logs
- Mentor Training for chat release

## V2
- Chat app release
- Mobile friendly CSS

## V3
- Provider access

## V4
- Alert system from chat to provider/admin

## V5
- Live chat


# Backlog ideas
- FAQ's
- Forum / Groups
- Mobile app
- Pagination for logs


# Branches (as of 7/14/23)
Officially switched to branches dev and publicPages