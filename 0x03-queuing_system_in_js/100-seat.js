import express from 'express';
import redis from 'redis';
import util from 'util';
import kue from 'kue';

const client = redis.createClient();
client.on('connect', () => {}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const reserveSeat = util.promisify(client.set).bind(client, 'available_seats');

const getCurrentAvailableSeats = util.promisify(client.get).bind(client, 'available_seats');

const app = express();
const queue = kue.createQueue();

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.json({ status: 'Reservations are blocked' });
  } else {
    const job = queue.create('reserve_seat').save((err) => {
      if (!err) {
        res.json({ status: 'Reservation in process' });
      } else {
        res.json({ status: 'Reservation failed' });
      }
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
    });
  }
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const count = await getCurrentAvailableSeats();
    if (count === '0') {
      reservationEnabled = false;
    } else if (count > 0) {
      await reserveSeat(Number(count) - 1);
    } else {
      return done(new Error('Not enough seats available'));
    }
    done();
  });
});

app.listen(1245);
