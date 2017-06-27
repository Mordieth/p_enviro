var app = require('http').createServer(handler)
var io = require('socket.io')(app)

app.listen(3000)

function handler(req, res) {
    console.log('request!')
    res.writeHead(200)
    res.end(data)
}

app.on('connection', (socket) => {
    console.log('connection!', socket)
})

io.on('connection', function (socket) {
    console.log('connection!')
    socket.on('*', function (data) {
        console.log(data)
    });
});