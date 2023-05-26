import kue from 'kue';

const queue = kue.createQueue();

const job = {
    phoneNumber: 'string',
    message: 'string',
};

const pushCode = queue.create('push_notification_code', job).save((err) => {
        if (!err) console.log(`Notification job created: ${pushCode.id}`);
    }
);

pushCode.on('complete', () => console.log('Notification job completed'));

pushCode.on('failed', () => console.log('Notification job failed'));

pushCode.on('progress', (progress) => console.log(`Notification job ${pushCode.id} ${progress}% complete`));

export default pushCode;
