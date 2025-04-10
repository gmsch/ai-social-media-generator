# AI-Powered Social Media Post Generator

An AI-powered Python application designed to streamline social media engagement. The app fetches interesting news articles based on user-specific topics and generates compelling, platform-specific posts for X/Twitter, Facebook, and LinkedIn, adjusting tone and style to match each social media platform.

---

## 🚀 Features:

- **News Sourcing**: Automatically identifies relevant news items based on provided topics.
- **AI-backed Generation**: Uses Generative AI technology (OpenAI GPT or similar) to create engaging, provocative posts optimized for:
  - **X/Twitter**: Concise, to-the-point, provocative & hashtag-driven.
  - **Facebook**: Conversational, friendly, personable.
  - **LinkedIn**: Professional, insightful, thought-provoking with business context.
- **Simplified Web UI**: A straightforward interface for inputting topics and reviewing & approving generated posts per platform.
- **Modular Architecture**: Easy scalability and maintainability, with clear module separation for news fetching, AI generation, platform-specific logic, and web UI.

---

## ⚙️ Technology Stack:

| Component            | Technology / Library                     |
|----------------------|------------------------------------------|
| Programming Language | Python (3.8+)                            |
| AI Language Model    | OpenAI API (GPT-3.5/GPT-4 recommended)   |
| Web Framework        | Flask or Streamlit                       |
| News API             | NewsAPI.org                              |
| UI Framework (optional)   | Bootstrap, Tailwind CSS, Streamlit       |

---

## 📁 Recommended Repository Structure:

```
ai-social-post-gen/
│
├── ai_model/
│   ├── __init__.py
│   └── generator.py      # AI-generated content logic
│
├── news_scraper/
│   ├── __init__.py
│   └── news_fetcher.py   # Fetch news from APIs
│
├── platform_adapters/
│   ├── __init__.py
│   ├── twitter.py        # Twitter/X post formatting logic
│   ├── facebook.py       # Facebook post formatting logic
│   └── linkedin.py       # LinkedIn post formatting logic
│
├── web_ui/
│   ├── templates/
│   │    └── index.html
│   ├── static/
│   │    └── css/
│   └── app.py            # Flask web UI app
│
├── config/
│   └── config.yaml       # Stores API keys / credentials
│
├── tests/
│   └── test_ai.py        # Initial testing skeleton
│
├── .gitignore
├── README.md
└── requirements.txt      
```

---

## 🛠️ Setup Instructions:

### ⚠️ Prerequisites:

- Python 3.8+
- A valid API key from [OpenAI](https://platform.openai.com/api-keys) and [NewsAPI](https://newsapi.org/)

### 🔧 Installation:

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ai-social-post-gen.git
cd ai-social-post-gen
```

2. **Set Up a Virtual Environment:**

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

3. **Install requirements:**

```bash
pip install -r requirements.txt
```

4. **Configure your API keys:**
Create `config/config.yaml` with your OpenAI and NewsAPI keys:

```yaml
openai_api_key: "your-openai-api-key"
newsapi_key: "your-newsapi-key"
```

### 🖥️ Run the Application:

- Navigate to `web_ui` directory and run:

```bash
cd web_ui
python app.py
```

- Visit `http://localhost:5000` in your browser.

---

## 🎯 Usage Workflow:

1. Enter the topics of interest through the web UI.
2. Confirm generated news snippets and evaluate social media posts produced for each platform.
3. Approve or regenerate content explicitly for:
   - X/Twitter (concise, hashtags, provocative)
   - Facebook (friendly, engaging conversational)
   - LinkedIn (professional, insightful, thought-leadership oriented)
4. Copy generated posts to respective social platforms.

---

## 🧪 Testing:

Run automated tests (PyTest or unittest supported):

```bash
python -m unittest tests/test_ai.py 
```

---

## 📌 Roadmap (Future Improvements):

- Automated posting directly to social platforms via API integrations.
- Advanced scheduler for automatic post-timing.
- Analytics dashboard integration.
- Expanded UI for monitoring news trends and user history.

---

## 🤝 Contributing:

Please open an issue or create a Pull Request. Contributions, feature requests, and bug reports are welcome.

---

## 📜 License:

Distributed under the MIT license. See `LICENSE` file for more information.

---

## 🙋 Contact:

Your Name - [youremail@example.com](mailto:youremail@example.com) or [GitHub](https://github.com/your-username)

--- 

Enjoy crafting engaging, AI-powered social media posts effortlessly! 🌟🚀
