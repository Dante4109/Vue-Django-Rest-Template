Bullet points for video:

- Brief introduction of what the webapp is. 
- Explain the front page and what technologies were used to make this app. 
  - Vue3 and Vuetify3 
  - Django Rest Framework latest
  - Postgresql
  - Heroku which is also using Amazon RDMS for postgresql 
  - AWS S3 for blob storage, Route 53 for domain. 
  - Gunmail
- Attempt to log in with a non existent account. 
  - Explain error message that appears
  - Demonstrate validation checking in forms
- Create an account. Explain validation checking in sign up page. 
  - Mention third party ways to create accounts such as Okta, OpenAuth, Active Directory.
- Go to verification email. 
  - Explain how the reroute works using rzeller.net
- Show jwt token in session storage.
  - Explain session storage as a whole. 
- Demonstrate reset password function. 
- Go to password reset email. 
- Enter new password. 
- Show new password working. Point out this is not secure. 
  - Explain we could set the password to not be the same as previous ones. 
  - We could reinforce stronger password rules. 
  - We could use other means than JWT such as Session, Cookie, Token, and Basic. 

- Demonstrate the photo gallery
  - Show the photos currently uploaded. 
  - Open the image manager. 
  - Upload a photo. 
  - Rename the photo. 
  - Change folder and comment on the change in real time. 
  - Go to developer tools and show the profile image collection data as json. 

- Demonstrate account management
  - Show changing profile picture          
  - Show changing account text such as username
  - Show password change option

- Briefly click on the coming soon features and then plug the github repo. 
- Mention your links are below on the footer
