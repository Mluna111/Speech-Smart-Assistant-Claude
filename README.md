<h1>Speech Recognition and Text-to-Speech Conversion</h1>

<h2>Description</h2>
<p>This Python script demonstrates speech recognition and text-to-speech conversion functionalities using various libraries. It captures audio input from the microphone, recognizes speech using Google's Speech Recognition API, processes the input using the Anthropics API, and converts the response to speech using gTTS (Google Text-to-Speech).</p>

<h2>Libraries Used</h2>
<ul>
    <li><b>speech_recognition</b>: For capturing and recognizing speech from audio input.</li>
    <li><b>anthropic</b>: Integrates with Anthropics API for processing input and generating responses.</li>
    <li><b>gtts</b>: Converts text responses into speech audio files.</li>
    <li><b>dotenv</b>: Loads environment variables, including API keys.</li>
</ul>

<h2>Environment Setup</h2>
<p>Ensure you have the required Python libraries installed:</p>
<pre><code>pip install speech_recognition gtts python-dotenv anthropic
</code></pre>

<h2>How to Run</h2>
<ol>
    <li><b>Environment Variables</b>:
        <ul>
            <li>Create a <code>.env</code> file in the project directory and set <code>ANTHROPIC_API</code> with your API key.</li>
        </ul>
    </li>
    <li><b>Run the Script</b>:
        <pre><code>python your_script_name.py</code></pre>
        <ul>
            <li>Follow the prompt to speak into the microphone.</li>
        </ul>
    </li>
</ol>

<h2>Output</h2>
<p>The script will recognize speech, send it to the Anthropics API for processing, receive a response, convert the response into an audio file (<code>welcome.mp3</code>), and play it using <code>mpg321</code>.</p>

<h2>Dependencies</h2>
<p>Ensure the system has <code>mpg321</code> installed to play the audio file.</p>

<h2>Example Run</h2>
<p>Sample interaction:</p>
<pre><code>Say something...
You said: Hello, how are you?
Answer the questions in 90 words or less: Hello, how are you?
[Anthropic Response]
</code></pre>

<h2>Files in the Project</h2>
<ul>
    <li><b><code>.env</code></b>: Contains environment variables, including <code>ANTHROPIC_API</code> key.</li>
    <li><b><code>your_script_name.py</code></b>: Main Python script implementing speech recognition and text-to-speech conversion.</li>
</ul>

<h2>Note</h2>
<ul>
    <li>Make sure your microphone is properly configured and accessible by the script.</li>
    <li>Adjust parameters such as <code>model</code>, <code>max_tokens</code>, and <code>temperature</code> in the Anthropics API call for different responses.</li>
</ul>
