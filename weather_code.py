while True:
  
  temperature = random.randint(70,75)
  humidity = random.randint(30,35)
  pressure = random.randint(800,1000)
 
  #Count
  
  #Rate

  #Gauge
  statsd.gauge('current.temperature.gauge', temperature,tags=["environment:dev"])
  statsd.gauge('current.humidity.gauge',humidity, tags=["environment:dev"])
  statsd.gauge('current.pressure.gauge',pressure, tags=["environment:dev"])
 
  #Histogram (.avg, .median, .count)

  #Distribution (avg, count, max, min)
 
  time.sleep(10)
