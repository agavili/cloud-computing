var awsIot = require('aws-iot-device-sdk');
// Config
var device = awsIot.device({
   keyPath: "/home/ubuntu/pa6/configs-pa6/4a642e2d47-private.pem.key",
  certPath: "/home/ubuntu/pa6/configs-pa6/4a642e2d47-certificate.pem.crt",
    caPath: "/home/ubuntu/pa6/configs-pa6/root-ca.crt",
      host: "a3t4q2fjipdbd2-ats.iot.us-east-1.amazonaws.com"
});


// Connect
device
  .on('connect', function() {
    console.log('Connected');
// Subscribe to myTopic
	  //
    device.subscribe("myTopic");
// Publish to myTopic
    device.publish("myTopic", JSON.stringify({message: 'OPEN'}));  
    
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
