var awsIot = require('aws-iot-device-sdk');
// Config
var device = awsIot.device({
   keyPath: "/home/ubuntu/pa6/certs/687e1afefa-private.pem.key",
  certPath: "/home/ubuntu/pa6/certs/687e1afefa-certificate.pem.crt",
    caPath: "/home/ubuntu/pa6/certs/root-ca.crt",
      host: "a3t4q2fjipdbd2-ats.iot.us-east-1.amazonaws.com"
});


// Connect
device
  .on('connect', function() {
    console.log('Connected');
// Subscribe to myTopic
    device.subscribe("mytopic");
// Publish to myTopic
     //device.publish("myTopic", JSON.stringify({message: 'hello'}));  
  device.publish("mytopic", JSON.stringify({
  key1: 'hello1',
  key2: 'hello2',
  key3: 'hello3'
}));

  });
// Receiving a message from any topic that this device is
// subscribed to.
device
  .on('message', function(topic, payload) {
    console.log('message', topic, payload.toString());
  });

// Error
device
  .on('error', function(error) {
    console.log('Error: ', error);
  });


