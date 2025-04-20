<h1>🤖💬 Social Media Reply Generator</h1>

<p>
This project is a <strong>FastAPI-based application</strong> that generates human-like replies to social media posts using the <code>google/gemma-2b</code> language model. It adjusts tone and sentiment based on the platform (Twitter, LinkedIn, Instagram) and stores all interactions in MongoDB.
</p>

<hr/>

<h2>🚀 Features</h2>
<ul>
  <li><strong>Platform-aware tone:</strong> Witty for Twitter, professional for LinkedIn, friendly for Instagram.</li>
  <li><strong>Sentiment analysis:</strong> Guides the model to align emotionally with the post.</li>
  <li><strong>Prompt chaining:</strong> Detects tone → Analyzes sentiment → Generates reply.</li>
  <li><strong>MongoDB integration:</strong> Stores all interactions.</li>
  <li><strong>GPU-accelerated & quantized:</strong> Efficient inference using quantized Gemma-2B.</li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>
<pre>
post_reply_bot/
├── app/
│   ├── main.py                # FastAPI app entry point
│   ├── generator.py           # Core logic for tone detection, sentiment analysis, and reply generation
│   ├── database.py            # MongoDB connection and interaction
│   └── schemas.py             # Pydantic schemas for request/response models
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables (MongoDB URI, etc.)
</pre>

<hr/>

<h2>🛠️ Setup & Installation</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/shawnalmeida/post_reply_bot.git
cd post_reply_bot
</code></pre>

<h3>2. Create a virtual environment</h3>
<pre><code>python -m venv venv
venv\Scripts\activate   (on Windows)
# or
source venv/bin/activate   (on macOS/Linux)
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Set up environment variables</h3>
<p>Create a <code>.env</code> file:</p>
<pre><code>MONGODB_URI=mongodb+srv://&lt;username&gt;:&lt;password&gt;@&lt;cluster&gt;.mongodb.net/?retryWrites=true&w=majority</code></pre>

<h3>5. Run the FastAPI server</h3>
<pre><code>uvicorn app.main:app --reload</code></pre>

<p>Visit: <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a> for Swagger API docs.</p>

<hr/>

<h2>📬 API Usage</h2>

<h3>Endpoint</h3>
<code>POST /reply </code>

<h4>Supported Platforms:</h4>
<ul>
  <li>Twitter</li>
  <li>LinkedIn</li>
  <li>Instagram</li>
</ul>

<hr/>

<h2>🧠 Human-like Reply Strategy</h2>
<ul>
  <li><strong>Prompt chaining:</strong> Sentiment and tone detected first → reply generated based on them.</li>
  <li><strong>AI-aware design:</strong> Avoids AI giveaways like generic statements or excessive formality.</li>
  <li><strong>Persona simulation:</strong> The assistant responds differently based on platform personas.</li>
</ul>

<hr/>

<h2>⚙️ Architecture Decisions & Trade-offs</h2>
<table border="1" cellpadding="8">
  <tr>
    <th>Decision</th>
    <th>Justification</th>
  </tr>
  <tr>
    <td><strong>Gemma-2B (quantized)</strong></td>
    <td>Runs on mid-range GPUs using 4-bit quantization while maintaining reasonable performance.</td>
  </tr>
  <tr>
    <td><strong>FastAPI</strong></td>
    <td>Minimal, high-performance framework for serving ML models over REST APIs.</td>
  </tr>
  <tr>
    <td><strong>MongoDB Atlas</strong></td>
    <td>Scalable, cloud-hosted NoSQL database for storing user posts and generated replies.</td>
  </tr>
  <tr>
    <td><strong>Prompt chaining</strong></td>
    <td>Enables modular and extensible logic—each step of the chain can evolve independently.</td>
  </tr>
</table>


<h2>🧑‍💻 Author</h2>
<p>Made with ❤️ by <strong>[Your Name]</strong></p>

<hr/>
