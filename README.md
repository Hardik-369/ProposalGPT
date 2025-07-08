# ProposalGPT

**Generate Winning Freelance Proposals with AI**

ProposalGPT is a modern, sleek web application that helps freelancers and agencies create high-quality, AI-powered proposals for job listings. Using advanced AI models via OpenRouter API, it generates personalized, professional proposals that stand out from the competition.

## ✨ Key Features

- **🤖 AI-Powered Generation**: Advanced AI analyzes job requirements and generates tailored proposals
- **👤 User Authentication**: Secure sign-up/login system with Flask-Login
- **📝 Freelancer Profiles**: Comprehensive profile setup with skills, experience, and tone preferences
- **📊 Proposal Management**: Save, edit, delete, and organize your proposals
- **📄 PDF Export**: Export proposals as professional PDF documents
- **💾 Client-Side Storage**: All data stored securely in your browser using localStorage
- **📱 Modern UI**: Sleek black and white design with responsive layout
- **⚡ Fast Generation**: Get professional proposals in 10-12 lines within seconds

## 🎨 Design Philosophy

- **Modern & Professional**: Clean black and white color scheme
- **User-Friendly**: Intuitive interface with smooth transitions
- **Mobile-First**: Responsive design that works on all devices
- **Performance-Focused**: Fast loading and efficient AI processing

## 🛠 Tech Stack

- **Backend**: Python 3.13 + Flask 2.3.3
- **Frontend**: HTML5 + Tailwind CSS 3.x (via CDN)
- **Authentication**: Flask-Login 0.6.3 (session-based)
- **AI Engine**: DeepSeek R1 via OpenRouter API
- **HTTP Client**: Requests 2.31.0
- **Storage**: Browser localStorage (client-side only)
- **PDF Export**: html2pdf.js
- **Icons**: Font Awesome 6.0
- **Typography**: Inter font family

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd proposalgpt
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
SECRET_KEY=your_secret_key_here
```

**Getting an OpenRouter API Key:**
1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Create a free account
3. Navigate to the API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

### 4. Launch the Application
```bash
python app.py
```

The application will be available at:
- **Local**: http://127.0.0.1:5000
- **Network**: http://[your-ip]:5000

## 📝 Usage Guide

### 1. Sign Up or Login
- Easily create an account or log in with existing credentials
- Secure authentication with Flask-Login

### 2. Complete Your Profile
- Add essential details like your role, skills, and experience
- Choose your tone: Professional, Friendly, or Persuasive
- Information is securely stored on the client-side

### 3. Generate Proposals
- Paste job descriptions, select the tone, and watch the magic happen
- Full proposals are generated in 10-12 lines
- Professionally tailored to win clients

### 4. Manage Your Proposals
- Save, edit, and organize all your proposals
- Export proposals as PDF for sharing
- Proposals are stored directly in your browser

### 3. Generate Proposals
- Paste job descriptions from platforms like Upwork, LinkedIn, or Clutch
- Optionally add a job link for reference
- Select your preferred tone
- Click "Generate Proposal" to create an AI-powered proposal

### 4. Manage Proposals
- Save generated proposals to your browser storage
- View proposal history with edit, delete, and PDF export options
- Edit proposals directly in the browser
- Download proposals as PDF files

## Project Structure

```
proposalgpt/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # Environment variables (create this)
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── login.html        # Login page
    ├── signup.html       # Sign-up page
    ├── dashboard.html    # Main dashboard
    ├── profile_setup.html # Profile configuration
    ├── generate.html     # Proposal generation
    └── history.html      # Proposal history management
```

## API Integration

The application uses the OpenRouter API to access DeepSeek models:
- **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Model**: `deepseek/deepseek-r1:free`
- **Authentication**: Bearer token via OpenRouter API key

## Storage

- **User Authentication**: In-memory storage (for demo purposes)
- **User Profiles**: Browser localStorage
- **Proposals**: Browser localStorage
- **No Backend Database**: All data is stored client-side

## Security Notes

- Change the `SECRET_KEY` in production
- For production use, implement proper user database storage
- Consider implementing rate limiting for API calls
- Validate and sanitize all user inputs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open-source and available under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.
