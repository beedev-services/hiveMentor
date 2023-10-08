## ChatApp
- Contains the chat portion of the app
- Possibly viewable in Django Admin
- Initial chat will not be live chat but message based for quicker release

### 
- 2 sides General User and Mentor User
- Can only see 1 side at a time if a duel user
- Mentors can flag general users to admin / provider if one is assigned
    - Have some sort of integration to crisis centers?
- Chats are not saved outside of session unless general user chooses to or chat is flagged. 
- Messages will need to be saved to DB
    - If both read and 15 days + or just 15 days + messages will be removed when sender logs back on ( or Admin ) to help keep DB use lower
- Chat can be saved as pdf - will be avail to both sides
    - If chat was flagged by Mentor a button to save to pdf will appear so Mentor can generate it at any point.  
    - List of saved chats (general only sees the ones they saved?)