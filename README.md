# dogstatsd-weather-sim-app
Dogstatsd Excercise
<h1><i>1. Install Agent on Ubuntu Sandbox</i><h1>
<h1><i>2. Enable Dogstatsd Paramters:</i></h1>
  <h1>3.(Choose your option)</h1>
<h1>Run 'eval' command:</h1>
<pre>eval "$(curl https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_script.sh)"</pre>
<h2>Or</h2>
<h1>Run 'curl' command</h1>
<pre>curl https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_script.sh</pre>
<h3>Run the script:</h3>
<pre>weather_script.sh</pre>
  <h1>4. Run Python program:</h1>
  <pre>python3 weather_code.py &</pre>
  <h3>*Note* using '&' symbol will run program in background</h3>
  <h1>5. Go to your Datadg account and you should be able to search list of custom created 'weather_code.py' Dogstatsd metrics:</h1>
  <pre>
  <li>temp</li>
    <li>humi</li>
  



