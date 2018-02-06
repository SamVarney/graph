//run "npm install socketcluster-client" in terminal before attempting to use
var socketCluster = require('socketcluster-client');

var api_credentials =
    {
        "apiKey": "dc600e0acd16ee7152a5c0691312907e",
        "apiSecret": "2adc5baf89d446c9460a5e6373bfff87"
    }

var options = {
    hostname: "sc-02.coinigy.com",
    port: "443",
    secure: "true"
};

console.log(options);
var SCsocket = socketCluster.connect(options);


SCsocket.on('connect', function (status) {

    console.log(status);

    SCsocket.on('error', function (err) {
        console.log(err);
    });


    SCsocket.emit("auth", api_credentials, function (err, token) {

        if (!err && token) {

            var scChannel = SCsocket.subscribe("TRADE-OK--BTC--CNY");
            console.log(scChannel);
            scChannel.watch(function (data) {
                console.log(data);
            });

            SCsocket.emit("exchanges", null, function (err, data) {
                if (!err) {
                    console.log(data);
                } else {
                    console.log(err)
                }
            });


            SCsocket.emit("channels", "OK", function (err, data) {
                if (!err) {
                    console.log(data);
                } else {
                    console.log(err)
                }
            });
        } else {
            console.log(err)
        }
    });
});




