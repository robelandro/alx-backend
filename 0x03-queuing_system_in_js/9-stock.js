import express from 'express';
import redis from 'redis';
import util from 'util';

const client = redis.createClient();
client.on('connect', () => {}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const list = [
  {
    itemId: '1',
    itemName: 'Suitcase 250',
    price: '50',
    initialAvailableQuantity: 4,
  },
  {
    itemId: '2',
    itemName: 'Suitcase 450',
    price: '100',
    initialAvailableQuantity: 10,
  },
  {
    itemId: '3',
    itemName: 'Suitcase 650',
    price: '350',
    initialAvailableQuantity: 2,
  },
  {
    itemId: '4',
    itemName: 'Suitcase 1050',
    price: '550',
    initialAvailableQuantity: 5,
  },
];

const getItemById = (itemId) => list.find(item => item.itemId === itemId);

const reserveStockById = (itemId, stock) => {
  client.hset('item', itemId, stock);
};

const getCurrentReservedStockById = util.promisify(client.hget).bind(client, 'item');

const app = express();

app.get('/list_products', (req, res) => {
  res.json(list);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);
  if (product) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    product.currentQuantity = currentQuantity;
    res.json(product);
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);
  if (product) {
    if (product.initialAvailableQuantity > 0) {
      reserveStockById(itemId, product.initialAvailableQuantity);
      product.initialAvailableQuantity--;
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'Not enough stock available', itemId });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.listen(1245);
