# 🔍 Product Research Agent

**AI-powered product research agent using Google Gemini 2.0 Flash and Tavily Search API**

Get comprehensive product analysis, price comparisons, reviews summary, and personalized recommendations - all powered by AI.

---

## ✨ Features

🎯 **Smart Product Analysis** - AI understands your specific needs and budget  
⭐ **Review Aggregation** - Summarizes reviews from multiple sources  
💰 **Price Comparison** - Finds best deals across retailers  
📊 **Comparison Charts** - Easy-to-read decision matrices  
🤖 **Personalized Recommendations** - Tailored to your use case  
💡 **Alternative Suggestions** - Discovers similar products you might prefer  

---

## 🚀 Quick Start

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Get API Keys
- **Google Gemini API**: Get free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Tavily Search API**: Get free API key from [Tavily](https://app.tavily.com/)

### 3️⃣ Setup Environment
```bash
# Copy the template
cp .env.example .env

# Edit .env and add your API keys
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4️⃣ Run the Agent

**Option A: Command Line Interface**
```bash
python ui/cli.py
```

**Option B: Web Interface (Recommended)**
```bash
streamlit run ui/web.py
```

---

## 📱 Usage Examples

### Command Line
```bash
# Start CLI
python ui/cli.py

# Enter your query when prompted
> Best wireless headphones for working from home under $200
```

### Web Interface
1. Run: `streamlit run ui/web.py`
2. Open browser (usually http://localhost:8501)
3. Enter your product query
4. Get comprehensive analysis in seconds!

### Example Queries
- "Best laptop for programming under $1000"
- "Wireless earbuds for running with good bass"
- "Coffee maker for small office under $300"
- "Gaming chair with lumbar support"
- "4K monitor for graphic design work"

---

## 📁 Project Structure

```
product-research-agent/
├── 📁 app/
│   ├── agent.py          # 🤖 Main AI agent logic
│   ├── tools.py          # 🔍 Search and analysis tools
│   └── config.py         # ⚙️ Configuration settings
├── 📁 ui/
│   ├── cli.py            # 💻 Command line interface
│   └── web.py            # 🌐 Streamlit web interface
├── 📁 data/
│   └── results/          # 📊 Research results storage
├── .env                  # 🔑 Your API keys (keep private!)
├── .env.example          # 📝 Template for API keys
├── .gitignore           # 🚫 Git ignore rules
├── README.md            # 📖 This documentation
└── requirements.txt     # 📦 Python dependencies
```

---

## 🔧 Installation Guide

### Prerequisites
- Python 3.8 or higher
- Internet connection for API calls

### Detailed Setup

1. **Clone/Download the project**
   ```bash
   git clone <repository-url>
   cd product-research-agent
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux  
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file:
   ```env
   GEMINI_API_KEY=your_actual_gemini_key
   TAVILY_API_KEY=your_actual_tavily_key
   ```

5. **Test the installation**
   ```bash
   python ui/cli.py
   ```

---

## 🔑 Getting API Keys

### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key to your `.env` file

### Tavily Search API Key  
1. Go to [Tavily](https://app.tavily.com/)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key to your `.env` file

**Note:** Both services offer free tiers that are sufficient for personal use.

---

## 💡 How It Works

### Research Process
1. **Query Understanding** - AI analyzes your requirements, budget, and use case
2. **Review Search** - Searches for authentic user reviews and ratings
3. **Price Discovery** - Finds current prices across multiple retailers  
4. **AI Analysis** - Gemini 2.0 processes all data for insights
5. **Recommendations** - Generates personalized buying advice
6. **Comparison Chart** - Creates easy decision matrix

### Technologies Used
- **Google Gemini 2.0 Flash** - Advanced AI for analysis and recommendations
- **Tavily Search API** - Real-time web search for reviews and prices
- **Streamlit** - Interactive web interface
- **Python** - Core application logic

---

## 📊 Sample Output

```
🎯 PRODUCT: Sony WH-1000XM4 Wireless Headphones

👤 USER NEEDS:
• Product: Wireless headphones for working from home
• Budget: Under $200
• Use Case: Video calls and music

📋 RESEARCH SUMMARY:
## 🏆 Overall Verdict
**Recommendation**: Buy - Excellent choice for your needs
**Overall Score**: 9/10
**Best For**: Professional work-from-home setup

## 💯 Quick Scores  
- **Value for Money**: ⭐⭐⭐⭐⭐ (5/5)
- **Quality**: ⭐⭐⭐⭐⭐ (5/5)
- **User Satisfaction**: ⭐⭐⭐⭐⭐ (4/5)
- **Features**: ⭐⭐⭐⭐⭐ (5/5)

## ✅ Top Pros
- Excellent noise cancellation for calls
- 30-hour battery life
- Superior comfort for long sessions

## ❌ Main Cons  
- Slightly above budget at $248
- Can be bulky for travel

## 💰 Price Insight
**Expected Range**: $220 - $280
**Best Value**: Amazon ($248) or Best Buy ($259)

## 🎯 Bottom Line
Perfect for your work-from-home needs, worth the small budget stretch.
```

---

## 🎛️ Configuration Options

Edit `app/config.py` to customize:

```python
class Config:
    # Search settings
    MAX_SEARCH_RESULTS = 5
    SEARCH_TIMEOUT = 30
    
    # AI model settings  
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    TEMPERATURE = 0.3
    
    # Output settings
    SAVE_RESULTS = True
    OUTPUT_FORMAT = "json"
```

---

## 🐛 Troubleshooting

### Common Issues

**❌ "API key not found" error**
- Check if `.env` file exists in project root
- Verify API keys are correctly added to `.env`
- Make sure no extra spaces around the `=` sign

**❌ "Module not found" error**  
- Run `pip install -r requirements.txt`
- Make sure you're in the correct directory
- Check if virtual environment is activated

**❌ "Streamlit command not found"**
- Install streamlit: `pip install streamlit`
- Or run: `python -m streamlit run ui/web.py`

**❌ Search results empty**
- Check internet connection
- Verify Tavily API key is correct
- Try a simpler product query

**❌ Gemini API errors**
- Check if you have API quota remaining
- Verify API key is active
- Try again after a few minutes

### Debug Mode
Run with debug info:
```bash
python ui/cli.py --debug
```

---

## 📈 Tips for Best Results

### Query Writing Tips
✅ **Be specific**: "Gaming laptop under $800" vs "laptop"  
✅ **Include use case**: "for video editing", "for students"  
✅ **Mention budget**: "under $200", "around $500"  
✅ **Add constraints**: "lightweight", "wireless", "with warranty"  

### Examples of Great Queries
- "Best noise-cancelling headphones for open office under $300"
- "Ergonomic office chair for tall person under $400"
- "4K webcam for streaming with good low-light performance"
- "Portable SSD 1TB for video editing under $150"

---

## 🔄 Updates and Maintenance

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Clearing Cache
```bash
# Remove old results
rm data/results/*.json
```

### Backup Results
```bash
# Copy results to backup folder
cp -r data/results data/backup_$(date +%Y%m%d)
```

---

## 🤝 Contributing

Found a bug or want to improve something?

1. Fork the repository
2. Create a feature branch
3. Make your changes  
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🆘 Support

Having trouble? Here's how to get help:

1. **Check this README** - Most questions are answered here
2. **Review error messages** - They usually point to the solution
3. **Test API keys** - Many issues are authentication related
4. **Check internet connection** - Required for API calls
5. **Create an issue** - For bugs or feature requests

---

## 🎉 What's Next?

After getting familiar with the basic usage, you can:

- Customize the analysis prompts in `app/agent.py`
- Add new search sources in `app/tools.py`
- Modify the web interface in `ui/web.py`
- Integrate with other APIs
- Add export to PDF/Excel features
- Create scheduled research reports

---

**🚀 Ready to start researching? Run `python ui/cli.py` or `streamlit run ui/web.py`**

*Happy researching! 🔍✨*
