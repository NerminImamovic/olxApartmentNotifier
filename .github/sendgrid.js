#! /usr/bin/env node

const sgMail = require('@sendgrid/mail');
const fs = require('fs')
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

try {
    let body = fs.readFileSync('./body.txt', 'utf8');
    body = body.replace(',', ' ,');
    body = body.split(':').join(':<br />');
    body = body.split('KM').join('KM<br />');

    console.log(body);

    const msg = {
        to: 'nimamovic9@gmail.com',
        from: 'nimamovic9@gmail.com',
        subject: 'OLX Update - Apartments',
        text: body,
        html: body,
    };

    sgMail
        .send(msg)
        .then(() => console.log('Mail sent successfully'))
        .catch(error => console.error(error.toString()));
} catch (err) {
    console.error(err);
}
