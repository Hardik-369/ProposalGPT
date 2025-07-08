from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simple in-memory user storage (replace with database in production)
users = {}

class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((u for u in users.values() if u.username == username), None)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if any(u.username == username for u in users.values()):
            flash('Username already exists')
            return render_template('signup.html')
        
        user_id = str(len(users) + 1)
        password_hash = generate_password_hash(password)
        user = User(user_id, username, password_hash)
        users[user_id] = user
        
        login_user(user)
        return redirect(url_for('profile_setup'))
    
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile-setup')
@login_required
def profile_setup():
    return render_template('profile_setup.html')

@app.route('/generate')
@login_required
def generate():
    return render_template('generate.html')

@app.route('/history')
@login_required
def history():
    return render_template('history.html')

@app.route('/test-api')
@login_required
def test_api():
    """Test endpoint to verify API key is loaded"""
    api_key = os.environ.get('OPENROUTER_API_KEY')
    return jsonify({
        'api_key_present': bool(api_key),
        'api_key_length': len(api_key) if api_key else 0,
        'api_key_prefix': api_key[:20] if api_key else 'None'
    })

@app.route('/generate-proposal', methods=['POST'])
@login_required
def generate_proposal():
    try:
        data = request.get_json()
        job_description = data.get('job_description', '')
        tone = data.get('tone', 'Professional')
        user_profile = data.get('user_profile', {})
        
        # Format user profile for the prompt
        profile_text = f"""
Name: {user_profile.get('name', 'N/A')}
Role: {user_profile.get('role', 'N/A')}
Experience: {user_profile.get('experience', 'N/A')}
Skills: {user_profile.get('skills', 'N/A')}
        """.strip()
        
        # Create the prompt for OpenRouter API
        prompt = f"""You are a professional freelancer proposal writer. Create a concise, compelling proposal that is EXACTLY 10-12 lines long.

**STRICT REQUIREMENTS:**
- Write in a {tone.lower()} tone
- Must be exactly 10-12 lines (no more, no less)
- Each line should be a complete sentence or thought
- Include: greeting, project understanding, relevant skills, approach, and closing
- Be direct, impactful, and personalized
- No bullet points or numbered lists - use flowing sentences
- End with a clear call-to-action

**FREELANCER PROFILE:**
{profile_text}

**CLIENT'S JOB POSTING:**
{job_description}

**FORMAT:** Write the proposal as a cohesive 10-12 line message with proper paragraph breaks for readability.

Generate the concise proposal now:"""

        # OpenRouter API configuration
        openrouter_api_key = os.environ.get('OPENROUTER_API_KEY')
        print(f"DEBUG: API Key loaded: {openrouter_api_key[:20] if openrouter_api_key else 'None'}...")
        
        if not openrouter_api_key:
            return jsonify({'error': 'OpenRouter API key not configured'}), 500
        
        # Make request to OpenRouter API using requests library
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openrouter_api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "ProposalGPT",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1:free",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
            })
        )
        
        if response.status_code == 200:
            result = response.json()
            proposal = result['choices'][0]['message']['content']
            
            return jsonify({
                'success': True,
                'proposal': proposal,
                'timestamp': datetime.now().isoformat()
            })
        else:
            error_msg = f"OpenRouter API error: {response.status_code} - {response.text}"
            return jsonify({'error': error_msg}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
