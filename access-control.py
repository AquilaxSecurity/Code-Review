from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class UserProfileService:
    def get_user_profile(self, username):
        pass

    def update_user_profile(self, user_profile):
        pass

user_profile_service = UserProfileService()

@app.route('/edit-profile', methods=['POST'])
def edit_profile():
    if not is_authenticated():
        return redirect(url_for('login'))
        
    username = request.form.get('username')
    user_profile = user_profile_service.get_user_profile(username)

    if user_profile.get_username() == username:
        user_profile_service.update_user_profile(user_profile)
        
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
