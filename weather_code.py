from datadog import initialize, statsd
import time
import random

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

while True:

  temperature = random.randint(70,75)
  humidity = random.randint(30,35)
  pressure = random.randint(800,1000)
 
  #Count
  statsd.increment('temperature.count.increment', temperature, tags=["environment:dev"])
  statsd.decrement('temperature.count.decrement', temperature, tags=["environment:dev"])  
  statsd.increment('humidity.count.increment', humidity, tags=["environment:dev"])
  statsd.decrement('humidity.count.decrement', humidity, tags=["environment:dev"])  
  statsd.increment('pressuse.count.increment', pressure, tags=["environment:dev"])
  statsd.decrement('pressure.count.decrement', pressure, tags=["environment:dev"]) 
 
  #Gauge
  statsd.gauge('temperature.gauge', temperature,tags=["environment:dev"])
  statsd.gauge('humidity.gauge',humidity, tags=["environment:dev"])
  statsd.gauge('pressure.gauge',pressure, tags=["environment:dev"])
 
  #Histogram (.avg, .median, .count, .max, .95percentile)
  statsd.histogram('temperature.histogram', temperature, tags=["environment"])
  statsd.histogram('humidity.histogram', humidity, tags=["environment"])
  statsd.histogram('pressure.histogram', pressure, tags=["environment"])
  
  #Distribution (avg, count, max, min)
  statsd.distribution('temperature.distribution', temperature, tags=["environment"])
  statsd.distribution('humidity.distribution', humidity, tags=["environment"])
  statsd.distribution('pressure.distribution', pressure, tags=["environment"])


  time.sleep(10)
