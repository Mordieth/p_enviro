var app = require('http').createServer(handler)
var io = require('socket.io')(app)

app.listen(3000)

function handler(req, res) {
    res.writeHead(200)
    res.end(data)
}

io.on('connection', function (socket) {
    socket.on('*', function (data) {
        console.log(data)
    });
});