#! /usr/bin/env node

const sgMail = require('@sendgrid/mail');
const fs = require('fs')
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

let body;

try {
    body = fs.readFileSync('./body.txt', 'utf8')
    console.log(body)
} catch (err) {
    console.error(err)
}

const msg = {
    to: 'nimamovic9@gmail.com',
    from: 'nimamovic9@gmail.com',
    subject: 'Hello world',
    text: body,
};

sgMail
    .send(msg)
    .then(() => console.log('Mail sent successfully'))
    .catch(error => console.error(error.toString()));
