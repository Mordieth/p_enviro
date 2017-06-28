const express = require('express')
const moment = require('moment')
const fs = require('fs')

const app = express()

const TS_TIMEFORMAT = 'YYYY.MM.DD HH:mm:ss:SSS'

app.all('*', function (req, res) {
    console.log('new req', req.query)
    let raw = round(req.query.temperature, 2)
    let calc = calcTemp(req.query.temperature)

    fs.appendFile('temp_log.csv', csv(moment().format(TS_TIMEFORMAT), raw, calc), () => { })

    res.send()
})

app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
})

//22 = 28
//21 = 26.8
//20 = 25.35
//24 = 28.58

function csv(...str) {
    if (!str) { return; }

    if (str.length === 1 && Array.isArray(str[0])) {
        str = str[0];
    }

    let ret = '';
    for (let i = 0, iEnd = str.length; i < iEnd; i++) {
        ret += str[i];
        if ((i + 1) < iEnd) {
            ret += ';';
        }
    }
    ret += '\r\n';

    return ret;
}

function calcTemp(n) {
    const b = 0.896119
    const a = 0.7524846

    return round(n * a + b, 2)
}

function round(value, decimals) {
    return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
}