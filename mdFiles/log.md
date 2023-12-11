# LogApp
- Contains the log or journal side of the app
- Provider access / ability
- Not in Django Admin

Not all of the following will be released at the same time.  See bottom of approx Version for release

## Parts of Logs
- Sleep Tracker - Enabled by user
- Sugar Tracker - Enabled by user
- Mental check in 1-4 scale
- Notes
- Provider Center
- Message Center - Enabled when Provider is added
- Generate PDF

## Provider Center
- Chose from list - User
- Deselect from list - User
- Generate printout - User
- Message Center between provider and user
- chose which logs to share - User
    - Generate PDF of selected logs and save to chosen provider
        - Check boxes to chose provider and desired logs
        - Logs will have checkbox as well to say avail to share
- Alerts for certain events - 
    - 7 days and 15 days extra alerts (if alert not cleared these trigger)
- User alerts
    - When a new provider is added to system (in case they are waiting on one they can go check)
    - Message read by provider
    - Message received by provider
    - Log downloaded by provider
    - 7 and 15 days post message sent w/o read/reply
- Provider alerts
    - When User adds or removes them
    - When new PDF is avail
    - When User reads messages
    - When provider receives message
    - 7 and 15 days post message sent w/o read/reply
    - Mentor flagged user

## Provider Access Parts
- Can only see those users that have selected them
- requires access code to gain provider access
    - Access code granted upon verification
        - Question based?
        - How to get code to provider
- If alerted regarding a user enables message communication between Mentor and Provider (username based only)